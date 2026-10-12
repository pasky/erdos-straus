"""Mordell-type covering test for the F_q[t] ES analogue (BRAINSTORM/ff_erdos_straus.md §4).

Families with FIXED data give ES_q(A,P) for all P (deg P large) in a congruence class:
  Type II  (a,b | X):   E | a+b, lc(E) = lc(a+b);          P ≡ -E (mod A·lcm(a,b)).
  Type I   (a = P·a1):  E monic, E | W;                    P ≡ -E (mod A·lcm(a1,b)), P ≡ -b/a1 (mod E).
We take W = A·∏S (S = list of monic irreducibles coprime to A, squarefree) and report which unit
classes mod W are covered.
usage: bs_ff_cover.py q A_digits maxdegS
"""
import sys, itertools
import bs_ff_es as F


def inv_mod(x, m):
    # extended Euclid over F_q[t]
    r0, r1, s0, s1 = m, F.divmod_(x, m)[1], (), (1,)
    while r1:
        qt, rr = F.divmod_(r0, r1)
        r0, r1 = r1, rr
        s0, s1 = s1, F.sub(s0, F.mul(qt, s1))
    if len(r0) != 1:
        return None
    c = pow(r0[0], F.Q - 2, F.Q)
    return F.divmod_(F.mul(s0, (c,)), m)[1]


def main():
    F.Q = int(sys.argv[1])
    A = tuple(int(c) for c in reversed(sys.argv[2]))
    dS = int(sys.argv[3])
    S = [p for d in range(1, dS + 1) for p in F.irreducibles(d) if F.divmod_(A, p)[1]]
    assert len(F.factor(A)) == 1 and list(F.factor(A).values()) == [1], "A must be irreducible here"
    mods = [A] + S
    unit_sets = [[r for r in itertools.chain.from_iterable(
        F.monics(dd) if False else [] for dd in [])]]  # placeholder
    def residues(m):
        d = len(m) - 1
        out = []
        for low in itertools.product(range(F.Q), repeat=d):
            r = F.trim(low)
            if r:
                out.append(r)
        return out
    allres = [residues(m) for m in mods]
    total = 1
    for r in allres:
        total *= len(r)
    # a condition is a dict index->residue; covered classes = union of product sets
    conds = set()
    subsets = []
    for r in range(len(S) + 1):
        for comb in itertools.combinations(range(len(S)), r):
            prod = (1,)
            for i in comb:
                prod = F.mul(prod, S[i])
            subsets.append((comb, prod))
    # Type II
    for (ca, a), (cb, b) in itertools.product(subsets, repeat=2):
        s = F.add(a, b)
        if not s:
            continue
        lcs = s[-1]
        f = F.factor(F.mul(s, (pow(lcs, F.Q - 2, F.Q),)))
        idx = sorted(set(ca) | set(cb))
        for kap in F.divisors_from(f):
            E = F.divmod_(s, kap)[0]  # lc(E) = lc(s)
            cond = []
            ok = True
            for j, m in [(0, A)] + [(i + 1, S[i]) for i in idx]:
                rr = F.divmod_(F.neg(E), m)[1]
                if not rr:
                    ok = False
                    break
                cond.append((j, rr))
            if ok:
                conds.add(tuple(cond))
    nII = len(conds)
    # Type I: E monic squarefree product of S-primes disjoint from lcm(a1,b)
    for (ca, a1), (cb, b) in itertools.product(subsets, repeat=2):
        used = set(ca) | set(cb)
        for (ce, E) in subsets:
            if not ce or used & set(ce):
                continue
            cond = []
            ok = True
            for j, m in [(0, A)] + [(i + 1, S[i]) for i in sorted(used)]:
                rr = F.divmod_(F.neg(E), m)[1]
                if not rr:
                    ok = False
                    break
                cond.append((j, rr))
            if not ok:
                continue
            for i in ce:
                ia = inv_mod(a1, S[i])
                rr = F.divmod_(F.neg(F.mul(b, ia)), S[i])[1]
                if not rr:
                    ok = False
                    break
                cond.append((i + 1, rr))
            if ok:
                conds.add(tuple(sorted(cond)))
    # count covered unit classes by brute enumeration
    covered = 0
    unc = []
    condlist = [dict(c) for c in conds]
    for cls in itertools.product(*allres):
        if any(all(cls[j] == r for j, r in c.items()) for c in condlist):
            covered += 1
        else:
            unc.append(cls)
    print(f"q={F.Q} A={sys.argv[2]} S=irreducibles deg<={dS} (#{len(S)}): families II={nII} total={len(conds)};"
          f" covered {covered}/{total} unit classes mod W")
    from collections import Counter
    def chi(r, m):  # quadratic character of residue r mod irreducible m
        e = (F.Q ** (len(m) - 1) - 1) // 2
        x, acc = r, (1,)
        while e:
            if e & 1: acc = F.divmod_(F.mul(acc, x), m)[1]
            x = F.divmod_(F.mul(x, x), m)[1]; e >>= 1
        return 1 if acc == (1,) else -1
    pat = Counter((F.poly_str(c[0]),) + tuple(chi(r, m) for r, m in zip(c[1:], S)) for c in unc)
    print("  uncovered by (P mod A, chi_s(P) for s in S):")
    for k, v in sorted(pat.items()): print("   ", k, v)
    full = Counter((F.poly_str(c[0]),) + tuple(chi(r, m) for r, m in zip(c[1:], S)) for c in itertools.product(*allres))
    print("  pattern sizes:", sorted(set(full.values())))


if __name__ == "__main__":
    main()
