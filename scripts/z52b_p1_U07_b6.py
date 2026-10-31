#!/usr/bin/env python3
"""U07 Z1990: 4-term solutions 4/p = 1/a+1/b+1/c+1/d (a<=b<=c<=d), primes p<=40; count solutions in which some pair of
terms merges into a single unit fraction (1/c+1/d = 1/e). Capped (p<=40, loops bounded by 4/p)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from fractions import Fraction as F
from sympy import primerange
def unit(q):  # q a Fraction; is it 1/e ?
    return q.numerator == 1
tot = 0; merge = 0
for p in primerange(5, 41):
    sols = []
    for a in range(p // 4 + 1, 2 * p + 1):
        ra = F(4, p) - F(1, a)
        if ra <= 0: continue
        for b in range(a, int(3 / ra) + 2):
            rb = ra - F(1, b)
            if rb <= 0: continue
            for c in range(b, int(2 / rb) + 2):
                rc = rb - F(1, c)
                if rc <= 0: continue
                if rc.numerator == 1 and rc.denominator >= c: sols.append((a, b, c, rc.denominator))
    for s in sols:
        tot += 1
        a, b, c, d = s
        pairs = [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)]
        if any(unit(F(1, x) + F(1, y)) for x, y in pairs): merge += 1
print("4-term solutions (p<=40):", tot, " with a mergeable pair (two terms sum to a unit fraction):", merge)
