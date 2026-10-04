#!/usr/bin/env python3
"""POINTWISE_OMEGA6 (EVIDENCE): the m>1 atoms split into corner / non-corner.

For free primes l1<l2 (q=l1*l2, both > y) enumerate all atoms (s,a,b),
s squarefree, M=4sab-1<=T, q || M, Pi-part m = y-smooth part of M/q,
n'=M/(qm)>1 (so n'>y), survival m | a+b.  Class kappa = a/b mod q.
Weight 2/n' (the upper bound used in O5/O6).
Corner atom (O6 Def 1.3): first element of its (s,a,m)-, (s,b,m)- and
(a,b,m)-fibres, and 4sa,4sb,4ab > y.  "First" means: stepping the free
variable down by qm leaves the range (<=0) or gives n'_m < y.
Output: for hub levels X, max over classes with height > X of
  tot = sum over m>1 atoms of 2/n',   K = corner part,
and the overall counts.  usage: omega6_corner.py T y l1 l2 [HCAP]
"""
import sys
from sympy import factorint, divisors
from omega5_codeg import heights


def sqfree(n):
    return all(e == 1 for e in factorint(n).values())


def main():
    T, y, l1, l2 = (int(x) for x in sys.argv[1:5])
    cap = int(sys.argv[5]) if len(sys.argv) > 5 else 2048
    q = l1 * l2
    tot, cor = {}, {}
    natoms = ncor = 0
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
        L = (M + 1) // 4
        Q = q * m
        for s in divisors(L):
            if not sqfree(s):
                continue
            for a in divisors(L // s):
                b = L // (s * a)
                if (a + b) % m:
                    continue
                kap = a * pow(b, -1, q) % q
                n1 = N // m
                w = 2.0 / n1
                natoms += 1
                tot[kap] = tot.get(kap, 0.0) + w
                first = True
                for (u, v, x) in ((s, a, b), (s, b, a), (a, b, s)):
                    # free variable x, fixed product 4uv; step in n' is 4uv
                    if 4 * u * v <= y:
                        first = False
                        break
                    if x - Q >= 1 and n1 - 4 * u * v >= y:
                        first = False
                        break
                if first:
                    ncor += 1
                    cor[kap] = cor.get(kap, 0.0) + w
    h = heights(q, cap)
    print(f"T={T} y={y} q={l1}*{l2}={q} m>1 atoms={natoms} corner atoms={ncor} "
          f"classes={len(tot)} HCAP={cap}")
    print(" X    max_tot(h>X)  max_K(h>X)   X^-1/4")
    X = 1
    while X <= cap // 2:
        bt = max([v for c, v in tot.items() if h.get(c, cap + 1) > X], default=0.0)
        bk = max([v for c, v in cor.items() if h.get(c, cap + 1) > X], default=0.0)
        print(f"{X:5d}  {bt:11.5f}  {bk:11.5f}  {X ** -0.25:8.4f}")
        X *= 2
    top = sorted(cor.items(), key=lambda t: -t[1])[:6]
    print("heaviest corner sums: (kappa, height, K, tot)")
    for c, v in top:
        print(f"  {c:9d}  h={h.get(c, cap + 1):6d}  {v:.5f}  {tot[c]:.5f}")


if __name__ == "__main__":
    main()
