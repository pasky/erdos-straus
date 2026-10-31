#!/usr/bin/env python3
"""U07 Z2790: for 1/p(1,A) the canonical class is (up to sign and convention, from memory: K ↔ −(1+A) in Z/p) so test the
square class of (1+A) mod p against (A/p) over all A, primes p ≤ 300, p ≠ 2. Counts agreements and the joint table."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (500_000_000, 500_000_000))
from sympy import primerange, legendre_symbol
tab = {}
for p in primerange(3, 301):
    for A in range(1, p):
        if (1 + A) % p == 0: continue
        key = (legendre_symbol(A, p), legendre_symbol((1 + A) % p, p))
        tab[key] = tab.get(key, 0) + 1
print("joint counts (χ(A), χ(1+A)):", sorted(tab.items()))
agree = sum(v for (a, b), v in tab.items() if a == b); tot = sum(tab.values())
print("agreement fraction:", round(agree / tot, 4))
