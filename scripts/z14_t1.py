# z14_t1.py — T1 control for the z14 leaf families: odd squares n = m^2 never satisfy the II2 / I3 divisor conditions
# (ET Prop 1.6).  Exhaustive over 4ad, 4cd <= A and all divisors f of n + 4a^2 d (resp. n^2 + 4c^2 d).
# Usage: PYTHONPATH=scripts uv run python scripts/z14_t1.py MMAX A
import sys
from math import gcd
from sympy import divisors
MM, A = int(sys.argv[1]), int(sys.argv[2])
bad = 0; tests = 0
for m in range(1, MM + 1, 2):
    n = m * m
    for a in range(1, A // 4 + 1):
        for d in range(1, A // (4 * a) + 1):
            for f in divisors(n + 4 * a * a * d):
                tests += 1
                if (f + 1) % (4 * a * d) == 0: bad += 1; print('II2 hit', m, a, d, f)
    for c in range(1, A // 4 + 1):
        for d in range(1, A // (4 * c) + 1):
            for f in divisors(n * n + 4 * c * c * d):
                tests += 1
                if f > 1 and gcd(f, 4 * c * d) == 1 and (n + f) % (4 * c * d) == 0: bad += 1; print('I3 hit', m, c, d, f)
print('T1 control: odd m <=', MM, 'A =', A, 'tests', tests, 'hits', bad)
