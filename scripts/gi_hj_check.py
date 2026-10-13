"""O170 §5 item 4: check 12 s(m,n) = sum(a_i - 3) + (m + m*)/n (HJ expansion of n/m, m m* = 1 mod n)
and Riemenschneider: sum(a_i - 1) = sum(b_j - 1) = r + s - 1 for n/m, n/(n-m)."""
from fractions import Fraction as F
from math import gcd, floor
def hj(n, m):
    out = []
    while m:
        a = -(-n // m); out.append(a); n, m = m, a * m - n
    return out
def ded(m, n):
    def saw(x):
        return 0 if x.denominator == 1 else x - floor(x) - F(1, 2)
    return sum(saw(F(k, n)) * saw(F(k * m, n)) for k in range(1, n))
bad = 0
for n in range(2, 120):
    for m in range(1, n):
        if gcd(m, n) != 1: continue
        a = hj(n, m); ms = pow(m, -1, n) if n > 1 else 0
        if 12 * ded(m, n) != sum(x - 3 for x in a) + F(m + ms, n): bad += 1
        b = hj(n, n - m)
        if not (sum(x - 1 for x in a) == sum(x - 1 for x in b) == len(a) + len(b) - 1): bad += 1
print("violations", bad)
