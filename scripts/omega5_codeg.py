#!/usr/bin/env python3
"""POINTWISE_OMEGA5 (EVIDENCE): pair codegrees split by the Pi-part m, against hub height.

For free primes l1<l2 (q=l1*l2, both > y) and every class c mod q:
  Delta(c) = sum over DISTINCT events e=(r, class mod r) strictly containing
             the pair (l1,c mod l1),(l2,c mod l2) of 1/phi(r/q),
events from atoms (M,D): M<=T, M=3 (4), q || M, m = y-smooth part of M,
r = M/m (all primes > y, r != q, q exactly divides r), D | A^2 (A=(M+1)/4),
survival m | 4D+1, class -4D mod M.  (The quarantine set B is ignored: Pi=Pi_0.)
Each event is tagged with m (merged events keep the least m).
Height: h(c) = min over the three hub families (O3 Def 2.3) of the level at
which c is a hub, computed by enumerating hub rationals up to HCAP.
Output: for X in powers of 2, max Delta(c) over classes with h(c) > X, split
into the m=1 part and the m>1 part, next to X^(-1/3).

usage: omega5_codeg.py T y l1 l2 [HCAP]
"""
import sys
from math import gcd, isqrt
from sympy import factorint, primerange


def heights(q, cap):
    """dict kappa mod q -> least hub level, kappa = -c."""
    h = {}
    def put(k, lev):
        if lev < h.get(k, 1 << 62):
            h[k] = lev
    for u in range(1, cap + 1):
        for v in range(1, cap // u + 1):
            if gcd(u, v) == 1 and gcd(u * v, q) == 1:
                put(u * pow(v, -1, q) % q, u * v)          # c = -u/v
    sqf = [True] * (cap + 1)
    for p in range(2, isqrt(cap) + 1):
        for j in range(p * p, cap + 1, p * p):
            sqf[j] = False
    for s in range(1, cap + 1):
        if not sqf[s]:
            continue
        for a in range(1, cap // s + 1):
            E = 4 * s * a * a
            if gcd(E, q) == 1:
                put(E % q, s * a)                           # c = -4sa^2
                put(pow(E, -1, q), s * a)                   # c = -1/(4sb^2)
    return h


def main():
    T, y, l1, l2 = (int(x) for x in sys.argv[1:5])
    cap = int(sys.argv[5]) if len(sys.argv) > 5 else 4096
    q = l1 * l2
    assert l1 > y and l2 > y
    ev = {}                       # (c, r, cls) -> least m
    for N in range(1, T // q + 1):
        M = q * N
        if M % 4 != 3 or N % l1 == 0 or N % l2 == 0:
            continue
        fa = factorint(M)
        m = 1
        for p, e in fa.items():
            if p <= y:
                m *= p ** e
        r = M // m
        if r == q:
            continue
        A = (M + 1) // 4
        fA = factorint(A)
        ds = [1]
        for p, e in fA.items():
            ds = [d * p ** j for d in ds for j in range(2 * e + 1)]
        for D in ds:
            if (4 * D + 1) % m:
                continue
            cls = (-4 * D) % r
            key = (cls % q, r, cls)
            if m < ev.get(key, 1 << 62):
                ev[key] = m
    tot, one = {}, {}
    for (c, r, cls), m in ev.items():
        n1 = r // q
        phi = 1
        for p, e in factorint(n1).items():
            phi *= (p - 1) * p ** (e - 1)
        w = 1.0 / phi
        tot[c] = tot.get(c, 0.0) + w
        if m == 1:
            one[c] = one.get(c, 0.0) + w
    h = heights(q, cap)
    print(f"T={T} y={y} q={l1}*{l2}={q} events={len(ev)} classes={len(tot)} HCAP={cap}")
    print(" X     max_tot(h>X)  max_m1(h>X)  max_m>1(h>X)   X^-1/3   argmax_tot(c,h)")
    X = 1
    while X <= cap // 2:
        best = (0.0, None)
        b1 = bm = 0.0
        for c, v in tot.items():
            hc = h.get((-c) % q, cap + 1)
            if hc > X:
                v1 = one.get(c, 0.0)
                b1, bm = max(b1, v1), max(bm, v - v1)
                if v > best[0]:
                    best = (v, (c, hc))
        print(f"{X:5d}  {best[0]:11.5f}  {b1:11.5f}  {bm:11.5f}  {X ** (-1/3):8.4f}   {best[1]}")
        X *= 2
    top = sorted(tot.items(), key=lambda t: -(t[1] - one.get(t[0], 0.0)))[:8]
    print("heaviest m>1 parts: (c, h, total, m>1 part)")
    for c, v in top:
        print(f"  {c:9d}  h={h.get((-c) % q, cap + 1):6d}  {v:.5f}  {v - one.get(c, 0.0):.5f}")


if __name__ == "__main__":
    main()
