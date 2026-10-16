"""R262 from-scratch check of Thm 1.4 (slice criterion), INCLUDING non-split slices.

For p = 1 (4) prime <= P, slices g = 3 (4), gcd(g, p) = 1, g <= G, h = (g+1)/4:
brute force: all Type II solutions with y = p*h: 1/x + 1/(pZ) = g/(ph), p ∤ x.  x ranges over
(ph/g, ph/(g-h)] (since 1/(pZ) <= 1/p).  Z = hx/(gx - ph) must be a positive integer.
criterion image: k | h, d = (-4k^2 p) mod g, 1 <= d | k  ->  a = h/k, c = k/d, m = (p+4a^2 d)/g, b = (p+m)/(4ad),
solution (x, Z) = (abd, bcd).  Compare sets.  Also records non-injectivity instances.
"""
import sys
import math
import numpy as np
from sympy import primerange, divisors

P, G = int(sys.argv[1]), int(sys.argv[2])
mism = nsl = nsplit_es = nnonsplit_es = noninj = 0
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for g in range(3, G + 1, 4):
        if g % p == 0:
            continue
        nsl += 1
        h = (g + 1) // 4
        lo, hi = p * h // g + 1, (p * h) // (g - h)
        x = np.arange(lo, hi + 1, dtype=np.int64)
        den = g * x - p * h
        ok = (den > 0) & ((h * x) % np.where(den > 0, den, 1) == 0) & (x % p != 0)
        brute = {(int(xx), int(h * xx // (g * xx - p * h))) for xx in x[ok]}
        img, seen = set(), {}
        for k in divisors(h):
            d = (-4 * k * k * p) % g
            if d >= 1 and k % d == 0:
                a, c = h // k, k // d
                m, r = divmod(p + 4 * a * a * d, g)
                assert r == 0
                b, r2 = divmod(p + m, 4 * a * d)
                assert r2 == 0 and c * p + a + b == 4 * a * b * c * d
                sol = (a * b * d, b * c * d)
                if sol in seen:
                    noninj += 1
                seen[sol] = k
                img.add(sol)
        if img != brute:
            mism += 1
            print("MISMATCH", p, g, sorted(img), sorted(brute))
        if brute:
            split = all(pow((-p) % l, (l - 1) // 2, l) == 1 for l in set(__import__('sympy').primefactors(g)))
            if split:
                nsplit_es += 1
            else:
                nnonsplit_es += 1
print(f"slices {nsl}, mismatches {mism}, ES slices split {nsplit_es} / non-split {nnonsplit_es}, non-injective hits {noninj}")
