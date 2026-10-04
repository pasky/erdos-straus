#!/usr/bin/env python3
"""Review checks for POINTWISE_OMEGA6 (hostile review, not part of O6).

usage: review_omega6_check.py T y l1 l2 [kappa ...]
Enumerates m>1 atoms exactly as scripts/omega6_corner.py and checks
  * Lemma 1.4: corner atoms have s,a,b <= 2qm and n' < y+4 min(sa,sb,ab);
  * Thm 3.2 identity: for a corner atom, n' = nu(s,a,m) (least nu>=y,
    q m nu = -1 mod 4sa);
  * Lemma 3.3(2): each class mod X=4sa holds <= 2 divisors of 4sa^2+1
    (checked for all (s,a) occurring in corner atoms);
  * Thm 1.5: Sigma^{>1} <= (1+L/2)(D_ab+D_sa+D_sb) + K, with the D's
    restricted to pairs that actually carry an m>1 atom (lower bound
    for the true D's, so a failure would be a real counterexample);
and decomposes the corner mass of the listed classes by plane/pair.
"""
import sys
import math
from collections import defaultdict
from sympy import factorint, divisors


def sqfree(n):
    return all(e == 1 for e in factorint(n).values())


def main():
    T, y, l1, l2 = (int(x) for x in sys.argv[1:5])
    watch = {int(x) for x in sys.argv[5:]}
    q = l1 * l2
    L_ = math.log(T)
    sigma = K = 0.0
    bad14 = badnu = 0
    ncor = 0
    pairs_sa = set()
    pairs_sb = set()
    pairs_ab = set()
    decomp = defaultdict(float)
    for N in range(1, T // q + 1):
        M = q * N
        if M % 4 != 3 or N % l1 == 0 or N % l2 == 0:
            continue
        m = 1
        for p, e in factorint(N).items():
            if p <= y:
                m *= p ** e
        if m == 1 or N == m:
            continue
        Lh = (M + 1) // 4
        Q = q * m
        for s in divisors(Lh):
            if not sqfree(s):
                continue
            for a in divisors(Lh // s):
                b = Lh // (s * a)
                if (a + b) % m:
                    continue
                kap = a * pow(b, -1, q) % q
                n1 = N // m
                w = 2.0 / n1
                sigma += w
                pairs_sa.add((s, a))
                pairs_sb.add((s, b))
                pairs_ab.add((a, b))
                first = True
                for (u, v, x) in ((s, a, b), (s, b, a), (a, b, s)):
                    if 4 * u * v <= y or (x - Q >= 1 and n1 - 4 * u * v >= y):
                        first = False
                        break
                if not first:
                    continue
                ncor += 1
                K += w
                if max(s, a, b) > 2 * Q or n1 >= y + 4 * min(s * a, s * b, a * b):
                    bad14 += 1
                X = 4 * s * a
                nu = (-pow(Q, -1, X)) % X
                while nu < y:
                    nu += X
                if nu != n1:
                    badnu += 1
                if kap in watch:
                    decomp[(kap, s, a, b, m)] += w
    # Lemma 3.3(2) on all corner (s,a) pairs
    bad33 = 0
    for (s, a) in pairs_sa:
        X = 4 * s * a
        F = 4 * s * a * a + 1
        cnt = defaultdict(int)
        for d in divisors(F):
            cnt[d % X] += 1
        if max(cnt.values()) > 2:
            bad33 += 1

    def tau(n):
        r = 1
        for e in factorint(n).values():
            r *= e + 1
        return r
    Dsa = sum(tau(4 * s * a * a + 1) / (s * a) for s, a in pairs_sa)
    Dsb = sum(tau(4 * s * b * b + 1) / (s * b) for s, b in pairs_sb)
    Dab = sum(tau(a + b) / (a * b) for a, b in pairs_ab)
    rhs = (1 + L_ / 2) * (Dab + Dsa + Dsb) + K
    print(f"T={T} q={q} corner={ncor} Lemma1.4 violations={bad14} "
          f"n'!=nu violations={badnu} Lemma3.3(2) violations={bad33}")
    print(f"Sigma^>1={sigma:.5f}  K={K:.5f}  D_ab*={Dab:.4f} D_sa*={Dsa:.4f} "
          f"D_sb*={Dsb:.4f}  RHS(Thm1.5, restricted D)={rhs:.4f}")
    for key in sorted(decomp, key=lambda t: -decomp[t]):
        kap, s, a, b, m = key
        print(f"  kappa={kap} (s,a,b)=({s},{a},{b}) m={m} w={decomp[key]:.5f}")


if __name__ == "__main__":
    main()
