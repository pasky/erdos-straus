#!/usr/bin/env python3
"""U07 Z2718/Z2719: for primes p ≡ 1 (mod 8), p ≤ 500, and every nonresidue A mod p: m(A) = min{|x·y| : (x,y) ∈ Λ_A, xy ≠ 0}
with Λ_A = {(x,y) ∈ Z²: y ≡ A x (mod p)}, restricted to |x|,|y| ≤ p (brute force; capped). Report min over A of m(A)/p,
and the Hurwitz-type constant comparison (1/√5 ≈ 0.447 is the Markov bound for the best lattices)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from sympy import primerange, legendre_symbol
import math
worst = []; total = 0; below = 0
for p in primerange(5, 501):
    if p % 8 != 1: continue
    for A in range(2, p):
        if legendre_symbol(A, p) != -1: continue
        best = None
        for x in range(1, p):
            r = (A * x) % p
            for y in (r, r - p):          # y ≡ A x, nearest representatives
                if y == 0: continue
                v = x * abs(y)
                if best is None or v < best: best = v
        total += 1
        ratio = best / p
        if ratio < 1/math.sqrt(5) + 1e-9: below += 1
        worst.append((ratio, p, A))
worst.sort()
print("nonresidue A tested:", total, " with m(A)/p <= 1/sqrt5:", below)
print("smallest m(A)/p:", [(round(r, 4), p, A) for r, p, A in worst[:5]])
print("largest m(A)/p (min over A of m is the relevant quantity per p):", round(max(worst)[0], 4))
