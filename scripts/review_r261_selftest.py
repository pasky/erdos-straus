"""R261 self-test: least_cap (review_r261_windows) vs a direct enumeration of D1 = prod s^{c_s}
(all c_s in [0, 2b_s + 2E], c_p in [0, 2], c_2 in [0, 2 b_2 + 2]) checked against Def 1.1 by exact rationals.
Usage: PMAX MMAX E"""
import sys
from itertools import product
from fractions import Fraction
from math import gcd
from sympy import primerange, factorint
from review_r261_windows import least_cap, check_def11

PMAX, MMAX, E = map(int, sys.argv[1:4])
bad = n = 0
for p in primerange(5, PMAX):
    if p % 4 != 1:
        continue
    for m in range(3, MMAX + 1, 4):
        if gcd(m, p) != 1:
            continue
        x = (p + m) // 4
        N = p * x
        fac = factorint(N * 2)
        primes = sorted(fac)
        rng = []
        for s in primes:
            b = factorint(N).get(s, 0)
            rng.append(range(0, 2 * b + 2 * E + 3))
        best = None
        for cs in product(*rng):
            D1 = 1
            for s, c in zip(primes, cs):
                D1 *= s ** c
            if (N + D1) % m:
                continue
            y = (N + D1) // m
            z = Fraction(N * y, D1)
            for e in range(0, E + 1):
                if best is not None and e >= best:
                    break
                if check_def11(p, x, y, z, e):
                    best = e
                    break
        r = least_cap(p, m, E)
        mine = r[0] if r else None
        n += 1
        if mine != best:
            bad += 1
            print('MISMATCH', p, m, best, mine)
print('pairs', n, 'mismatches', bad)
