"""R180: spot-check bsG_lens_dinv formula 12 s(q,n) = (q+q*)/n + sum(b_i - 3), n/q = [[b1..br]] (negative CF), q q* = 1 mod n."""
from fractions import Fraction as F
from math import gcd, floor
def saw(x):
    return F(0) if x.denominator == 1 else x - floor(x) - F(1, 2)
def ded(q, n):
    return sum(saw(F(k, n)) * saw(F(q * k, n)) for k in range(1, n))
def hj(n, q):
    b = []
    while q:
        c = -(-n // q); b.append(c); n, q = q, c * q - n
    return b
bad = tot = 0
for n in range(2, 80):
    for q in range(1, n):
        if gcd(q, n) != 1: continue
        b = hj(n, q); qs = pow(q, -1, n); tot += 1
        if 12 * ded(q, n) != F(q + qs, n) + sum(x - 3 for x in b): bad += 1
print("pairs", tot, "failures", bad)
