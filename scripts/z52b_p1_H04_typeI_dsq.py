#!/usr/bin/env python3
"""Z1482 sanity check: Type I slice f | p^2+4c^2 d, f ≡ -p (mod 4cd) is EMPTY for p ≡ 1 (4) prime when d is a square
(p^2+(2c s)^2 is a sum of two coprime squares -> all divisors ≡ 1 mod 4, but -p ≡ 3 mod 4). Brute force confirmation."""
from sympy import divisors, primerange
bad = 0; tested = 0
for p in primerange(5, 3000):
    if p % 4 != 1: continue
    for c in range(1, 40):
        for s in (1, 2, 3):
            d = s*s; m = 4*c*d; N = p*p + 4*c*c*d
            tested += 1
            if any((f + p) % m == 0 for f in divisors(N)): bad += 1; print("HIT", p, c, d)
print("tested", tested, "hits", bad)
# contrast: non-square d gives hits
hits = sum(1 for p in primerange(5, 3000) if p % 4 == 1 and any(any((f + p) % (4*c*d) == 0 for f in divisors(p*p + 4*c*c*d)) for c in range(1, 40) for d in (2, 3, 5, 6, 7)))
print("primes 1 mod 4 < 3000 with a hit for d in {2,3,5,6,7}, c<40:", hits)
