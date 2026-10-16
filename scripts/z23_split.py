"""O251 repair (reviewer FATAL): for the primes with empty d = 1 meeting locus, which Type II solutions have a
SPLIT slice (a slice g = 4acd - 1 or D = 4bcd - 1 with -p a square mod g), i.e. a lattice reading in Z[sqrt(-p)]?
Enumerates all Type II solutions with ET d <= DM (all a <= bound, all divisors g), checks roots with sympy sqrt_mod.
Usage: z23_split.py P DM
"""
import sys
import numpy as np
from fractions import Fraction as F
from math import isqrt
from sympy import primerange
from sympy.ntheory.residue_ntheory import sqrt_mod
from z23_meet import quick, meet_points


def sols_d(p, d):
    A = (1 + isqrt(4 * d * p + 1)) // (4 * d) + 2
    for a in range(1, A + 1):
        N = p + 4 * a * a * d
        J = (N + 1) // (4 * a * d)
        g = 4 * a * d * np.arange(1, J + 1, dtype=np.int64) - 1
        for gg in g[N % g == 0].tolist():
            m = N // gg
            b = (p + m) // (4 * a * d)
            c = (a + b) // m
            assert F(4, p) == F(1, a * b * d) + F(1, a * c * d * p) + F(1, b * c * d * p)
            yield (a, b, c, d, 4 * a * c * d - 1, 4 * b * c * d - 1)


def split(p, g):
    return sqrt_mod((-p) % g, g) is not None


P, DM = int(sys.argv[1]), int(sys.argv[2])
first_split, nosplit = {}, []
for p in primerange(5, P + 1):
    if p % 4 != 1 or quick(p) or meet_points(p, True):
        continue
    best = None
    for d in range(2, DM + 1):
        for s in sols_d(p, d):
            if split(p, s[4]) or split(p, s[5]):
                best = s
                break
        if best:
            break
    if best:
        first_split[p] = best
    else:
        nosplit.append(p)
hist = {}
for s in first_split.values():
    hist[s[3]] = hist.get(s[3], 0) + 1
print('empty-d1 primes with a split-slice Type II solution (d <=', DM, '):', len(first_split), 'least-d hist', sorted(hist.items()))
print('no split-slice solution with d <=', DM, ':', nosplit)

# independent brute force for the primes without a split-slice solution: ALL Type II solutions via
# x in (p/4, p/2], m = 4x - p, delta | x^2, delta = -x (mod m); slices 4y' - 1, 4z' - 1.
from sympy import divisors
for p in nosplit:
    sols = set()
    for x in range(p // 4 + 1, p // 2 + 1):
        m = 4 * x - p
        for de in divisors(x * x):
            if (x + de) % m == 0:
                y1, z1 = (x + de) // m, (x + x * x // de) // m
                assert F(4, p) == F(1, x) + F(1, p * y1) + F(1, p * z1)
                sols.add((x,) + tuple(sorted((y1, z1))))
    vis = [s for s in sols if split(p, 4 * s[1] - 1) or split(p, 4 * s[2] - 1)]
    print('brute force p =', p, ': Type II solutions', sorted(sols), ' with a split slice:', vis)
