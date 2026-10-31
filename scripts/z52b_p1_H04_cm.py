#!/usr/bin/env python3
"""Z1553: check #E(F_q) = q+1 for E: y^2 = x^3 - x at primes q ≡ 3 (4) (so q ≡ -1 mod 4C <=> 4C | #E(F_q))."""
from sympy import primerange, legendre_symbol
bad = 0
for q in primerange(3, 3000):
    if q % 4 != 3: continue
    cnt = 1 + sum(1 + legendre_symbol((x**3 - x) % q, q) if (x**3 - x) % q else 1 for x in range(q))
    bad += cnt != q + 1
print("q≡3 (4) < 3000 with #E != q+1:", bad)
