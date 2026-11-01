#!/usr/bin/env python3
"""Z1177: integer-only vs mixed (BV divisibility + Int) SMT encodings of one divisor family.

Family (same as Z1183): p = 1 mod 4 prime, x >= ceil(p/4), r = 4x-p, M = p x.
A solution with this x is y,z >= 1 integers with  r*y*z = M*(y+z).
  (I)  integer-only: Int variables y, z, nonlinear constraint r*y*z == M*(y+z), bounds 1..(M^2+M)/r+1.
  (II) mixed: divisor variable e in BV64 with explicit bit-vector divisibility:
         bvurem(M^2, e) == 0, e != 0, f = bvudiv(M^2, e),
         bvurem(e + M, r) == 0 (so y = (e+M)/r is an integer), bvurem(f + M, r) == 0,
         plus y = (e+M)/r, z = (f+M)/r in Int-free BV form, bounded e <= M^2.
Both are asked for the same (p,x). Verdicts are checked against ground truth (divisor
enumeration of M^2, exact). Time limit per query 5 s. Output: agreement, sat/unsat/unknown
counts and wall time per formulation.
"""
import sys, time, json
import z3

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors_of_square(M):
    f = factor(M)
    ds = [1]
    for q, a in f.items():
        ds = [d * q ** i for d in ds for i in range(2 * a + 1)]
    return ds

def ground_truth(p, x):
    r = 4 * x - p; M = p * x
    for e in divisors_of_square(M):
        if (e + M) % r == 0 and ((M * M // e) + M) % r == 0:
            return True
    return False

def solve_int(p, x, timeout_ms=5000):
    r = 4 * x - p; M = p * x
    y, z = z3.Ints('y z')
    s = z3.Solver(); s.set("timeout", timeout_ms)
    # exact a-priori bound: e = r*y - M divides M^2 and e > 0, so y <= (M^2 + M)/r  (same for z)
    Ymax = (M * M + M) // r + 1
    s.add(y >= 1, z >= 1, y <= Ymax, z <= Ymax)
    s.add(r * y * z == M * (y + z))
    t = time.time(); res = s.check(); dt = time.time() - t
    return str(res), dt

def solve_bv(p, x, timeout_ms=5000):
    r = 4 * x - p; M = p * x; M2 = M * M
    assert M2 < 2 ** 63
    W = 64
    e = z3.BitVec('e', W)
    Mb = z3.BitVecVal(M, W); M2b = z3.BitVecVal(M2, W); rb = z3.BitVecVal(r, W)
    f = z3.UDiv(M2b, e)
    s = z3.Solver(); s.set("timeout", timeout_ms)
    s.add(e != 0)
    s.add(z3.URem(M2b, e) == 0)                       # e | M^2 (bit-vector divisibility)
    s.add(z3.URem(e + Mb, rb) == 0)                   # r | e + M  -> y integer
    s.add(z3.URem(f + Mb, rb) == 0)                   # r | f + M  -> z integer
    s.add(z3.UGT(e + Mb, 0))
    t = time.time(); res = s.check(); dt = time.time() - t
    model_ok = None
    if res == z3.sat:
        ev = s.model()[e].as_long()
        Mv = M; rv = r
        model_ok = ((ev + Mv) % rv == 0) and ((M2 // ev + Mv) % rv == 0) and (M2 % ev == 0)
    return str(res), dt, model_ok

def main(pmax=800, K=4):
    primes = [q for q in range(5, pmax) if all(q % d for d in range(2, int(q ** 0.5) + 1)) and q % 4 == 1]
    rows = []
    agg = dict(queries=0, int_sat=0, int_unsat=0, int_unknown=0, bv_sat=0, bv_unsat=0, bv_unknown=0,
               disagree=0, bv_model_bad=0, int_time=0.0, bv_time=0.0, gt_true=0)
    t0 = time.time()
    for p in primes:
        x0 = -(-p // 4)
        for x in range(x0, x0 + K):
            gt = ground_truth(p, x)
            ri, ti = solve_int(p, x)
            rb, tb, mok = solve_bv(p, x)
            agg["queries"] += 1
            agg["gt_true"] += int(gt)
            agg["int_time"] += ti; agg["bv_time"] += tb
            for tag, res in (("int", ri), ("bv", rb)):
                key = {"sat": "sat", "unsat": "unsat", "unknown": "unknown"}[res]
                agg[f"{tag}_{key}"] += 1
            if mok is False:
                agg["bv_model_bad"] += 1
            if (ri == "sat") != gt and ri != "unknown":
                agg["disagree"] += 1
            if (rb == "sat") != gt and rb != "unknown":
                agg["disagree"] += 1
            rows.append((p, x, gt, ri, round(ti, 4), rb, round(tb, 4)))
    agg["seconds"] = round(time.time() - t0, 1)
    agg["primes"] = len(primes)
    agg["K"] = K
    agg["int_time"] = round(agg["int_time"], 2); agg["bv_time"] = round(agg["bv_time"], 2)
    return agg, rows

if __name__ == "__main__":
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    agg, rows = main(pmax, K)
    print(json.dumps(agg, indent=1))
    slow = sorted(rows, key=lambda r: -(r[4] + r[6]))[:5]
    print("slowest (p,x,gt,int,t_int,bv,t_bv):", slow)
    json.dump({"agg": agg, "rows": rows}, open(f"data/z52b/pass2/NC0/sub/Z1177_smt_{pmax}_{K}.json", "w"))
