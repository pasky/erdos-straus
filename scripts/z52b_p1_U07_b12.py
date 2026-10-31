#!/usr/bin/env python3
"""U07 Z0291: reverse greedy: choose z = p·d for d | D0 (D0 = lcm(1..12)), then solve 4/p − 1/z = 1/x + 1/y (2-term)
by divisor method. Records the fraction of primes p ≡ 1 (mod 4), p ≤ 3000, solved this way and the smallest d needed."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
import math
from fractions import Fraction as F
from sympy import primerange, divisors
def two_term(r):
    # solutions of 1/x+1/y = r (r Fraction > 0); returns one (x,y) or None
    a, b = r.numerator, r.denominator
    for d in divisors(b * b):
        if (b + d) % a: continue
        x = (b + d) // a
        e = b * b // d
        if (b + e) % a: continue
        y = (b + e) // a
        if x >= 1 and y >= 1: return (x, y)
    return None
D = [d for d in range(1, 13) if d]
solved = 0; total = 0; need = {}
for p in primerange(5, 3001):
    if p % 4 != 1: continue
    total += 1
    found = None
    for d in D:
        z = p * d
        r = F(4, p) - F(1, z)
        if r <= 0: continue
        sol = two_term(r)
        if sol: found = d; break
    if found: solved += 1; need[found] = need.get(found, 0) + 1
print("p≡1(4), p≤3000:", total, " solved with z=p·d, d≤12:", solved, " d-distribution:", sorted(need.items()))
