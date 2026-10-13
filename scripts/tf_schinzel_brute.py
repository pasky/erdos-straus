"""O194: independent brute-force check (no divisor enumeration) of m/p = 1/x+1/y+1/z, 0 < x <= y <= z:
x in (p/m, 3p/m], y in [x, 2/r] with r = m/p - 1/x, z = 1/(r - 1/y) tested with Fractions.  usage: m p [p ...]"""
import sys
from fractions import Fraction as F
m = int(sys.argv[1])
for p in map(int, sys.argv[2:]):
    c = 0
    for x in range(1, 3 * p // m + 1):
        r = F(m, p) - F(1, x)
        if r <= 0:
            continue
        for y in range(x, int(2 / r) + 1):
            s = r - F(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                c += 1
    print(f"m = {m}, p = {p}: {c} solutions (x <= y <= z)")
