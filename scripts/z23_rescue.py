"""O251 (LATTICE_MEETING §1.4): for the primes with empty d = 1 meeting locus (z23_meet), find the least ET parameter
d with a Type II solution: g | p + 4 a^2 d, g = -1 (mod 4ad) (EXP_OPEN row II-ad; Thm 1.4), exhaustive in a by
min(a, b) <= (1 + sqrt(4dp+1))/(4d).  Report least d, its squarefree part d0 (the field Q(sqrt(-d0 p))), and
check the solution exactly.  Usage: z23_rescue.py P DMAX
"""
import sys
import numpy as np
from fractions import Fraction as F
from math import isqrt
from sympy import primerange, factorint
sys.path.insert(0, '.')
from z23_meet import quick, meet_points


def sqfree(n):
    r = 1
    for q, e in factorint(n).items():
        if e % 2:
            r *= q
    return r


def typeII_d(p, d):
    A = (1 + isqrt(4 * d * p + 1)) // (4 * d) + 2
    for a in range(1, A + 1):
        N = p + 4 * a * a * d
        J = (N + 1) // (4 * a * d)
        g = 4 * a * d * np.arange(1, J + 1, dtype=np.int64) - 1
        for gg in g[N % g == 0].tolist():
            m = N // gg
            b = (p + m) // (4 * a * d)
            assert (p + m) % (4 * a * d) == 0 and (a + b) % m == 0
            c = (a + b) // m
            assert F(4, p) == F(1, a * b * d) + F(1, a * c * d * p) + F(1, b * c * d * p)
            return (a, b, c, d)
    return None


P, DM = int(sys.argv[1]), int(sys.argv[2])
hist = {}
for p in primerange(5, P + 1):
    if p % 4 != 1 or quick(p) or meet_points(p, True):
        continue
    for d in range(2, DM + 1):
        s = typeII_d(p, d)
        if s:
            hist[sqfree(d)] = hist.get(sqfree(d), 0) + 1
            print(p, 'least d =', d, 'd0 =', sqfree(d), 'sol (a,b,c,d) =', s)
            break
    else:
        print(p, 'no Type II with d <=', DM)
print('least-d0 histogram:', sorted(hist.items()))
