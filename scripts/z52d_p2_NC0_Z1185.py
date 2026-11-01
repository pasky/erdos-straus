#!/usr/bin/env python3
"""Z1185: proof size of bounded-box UNSAT for two encodings of 4/p = 1/x+1/y+1/z.

Box: 1 <= x <= y <= z <= B. For each prime p = 1 mod 4 we compute B*(p) = min over all
solutions of z (exact enumeration), then test the deliberately too-small box B = B*-1 (UNSAT)
and the exact box B = B* (SAT, sanity).

Encodings (both bit-vector, bit-blasted by z3 tactic simplify;bit-blast;tseitin-cnf):
  DIRECT: x,y,z in BV32 with 4xyz == p(xy+yz+zx) in BV64 (no overflow for B < 2^12).
  FACTOR: x in BV32 with r = 4x - p > 0, M = p x, a divisor e (BV64) of M^2 with
          e + M = r*y, f = M^2/e, f + M = r*z (bit-vector divisibility), and the box.
Measures: CNF vars/clauses, CaDiCaL 1.9.5 (pysat) time, DRAT proof size in bytes (UNSAT only),
and conflicts. Proof checking with drat-trim is not done (not installed).
"""
import sys, time, json
import z3
from pysat.solvers import Solver
from pysat.formula import CNF

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def all_solutions_sorted(p):
    """all (x,y,z) with x<=y<=z, 4/p = 1/x+1/y+1/z (exact)"""
    sols = []
    for x in range(p // 4 + 1, 3 * p // 4 + 2):
        r = 4 * x - p
        if r <= 0: continue
        M = p * x
        f = factor(M * M)
        ds = [1]
        for q, a in f.items():
            ds = [d * q ** i for d in ds for i in range(a + 1)]
        for e in ds:
            if (e + M) % r: continue
            y = (e + M) // r
            ff = M * M // e
            if (ff + M) % r: continue
            z = (ff + M) // r
            if x <= y <= z:
                sols.append((x, y, z))
    return sols

def bvsize_check(B):
    assert B < 2 ** 12

def direct_goal(p, B):
    x, y, z = z3.BitVecs('x y z', 32)
    g = z3.Goal()
    for v in (x, y, z):
        g.add(z3.UGE(v, 1), z3.ULE(v, B))
    g.add(z3.ULE(x, y), z3.ULE(y, z))
    X, Y, Z = (z3.ZeroExt(32, v) for v in (x, y, z))
    P = z3.BitVecVal(p, 64)
    g.add(4 * X * Y * Z == P * (X * Y + Y * Z + Z * X))
    return g

def factor_goal(p, B):
    x = z3.BitVec('x', 32); e = z3.BitVec('e', 64)
    g = z3.Goal()
    X = z3.ZeroExt(32, x)
    P = z3.BitVecVal(p, 64)
    Mv = P * X
    R = 4 * X - P
    M2 = Mv * Mv
    g.add(z3.UGE(x, 1), z3.ULE(x, B))
    g.add(z3.UGT(R, 0))
    g.add(z3.UGE(e, 1))
    g.add(z3.URem(M2, e) == 0)                  # e | M^2
    f = z3.UDiv(M2, e)
    g.add(z3.URem(e + Mv, R) == 0)              # r | e + M  -> y integer
    g.add(z3.URem(f + Mv, R) == 0)              # r | f + M  -> z integer
    Y = z3.UDiv(e + Mv, R); Z = z3.UDiv(f + Mv, R)
    g.add(z3.UGE(Y, X), z3.ULE(Y, Z), z3.ULE(Z, B))
    g.add(z3.UGE(Y, 1))
    return g

def cnf_from_goal(g):
    t = z3.Then('simplify', 'bit-blast', 'tseitin-cnf')
    sub = t(g)
    assert len(sub) == 1
    dimacs = sub[0].dimacs(include_names=False)
    cnf = CNF(from_string=dimacs)
    return cnf

def solve_cnf(cnf, want_proof):
    s = Solver(name='cd19', with_proof=want_proof, bootstrap_with=cnf.clauses)
    t = time.time()
    res = s.solve()
    dt = time.time() - t
    proof_bytes = None
    if want_proof and not res:
        pr = s.get_proof()
        proof_bytes = sum(len(line) + 1 for line in pr)
        proof_lines = len(pr)
    else:
        proof_lines = None
    stats = s.accum_stats() if hasattr(s, 'accum_stats') else {}
    s.delete()
    return res, dt, proof_bytes, proof_lines, stats

def main(pmax):
    primes = [q for q in range(5, pmax) if q % 4 == 1 and all(q % d for d in range(2, int(q ** 0.5) + 1))]
    rows = []
    for p in primes:
        sols = all_solutions_sorted(p)
        if not sols:
            rows.append({"p": p, "error": "no solution"}); continue
        Bstar = min(z for x, y, z in sols)
        for B, expect in ((Bstar - 1, False), (Bstar, True)):
            row = {"p": p, "B": B, "expect_sat": expect}
            for name, mk in (("direct", direct_goal), ("factor", factor_goal)):
                g = mk(p, B)
                t0 = time.time()
                cnf = cnf_from_goal(g)
                tenc = time.time() - t0
                res, dt, pb, pl, st = solve_cnf(cnf, want_proof=not expect)
                row[name] = {"sat": bool(res), "clauses": len(cnf.clauses), "vars": cnf.nv,
                             "enc_s": round(tenc, 3), "solve_s": round(dt, 3),
                             "drat_bytes": pb, "drat_lines": pl,
                             "conflicts": st.get("conflicts") if isinstance(st, dict) else None}
                if bool(res) != expect:
                    row[name]["MISMATCH"] = True
            rows.append(row)
        print(p, Bstar, [(r["B"], r.get("direct", {}).get("drat_bytes"), r.get("factor", {}).get("drat_bytes"),
                          r.get("direct", {}).get("clauses"), r.get("factor", {}).get("clauses")) for r in rows[-2:]], flush=True)
    return rows

if __name__ == "__main__":
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    rows = main(pmax)
    json.dump(rows, open(f"data/z52b/pass2/NC0/sub/Z1185_proof_{pmax}.json", "w"), indent=0)
    mism = [r for r in rows if any(isinstance(r.get(k), dict) and r[k].get("MISMATCH") for k in ("direct", "factor"))]
    print("rows", len(rows), "mismatches", len(mism))
