"""y6_verify.py — independent exact re-verification of the certificates found by y6_cover.py (saved in /tmp/y6_best.npy):
for every prime 3 <= p <= N rebuild (a, B, c) from (g, B, c), the shot Q = c^2 a B^3 / 4, and check with exact rationals
4/p = 1/x + 1/y + 1/z, den z = q^2 with q = c B^2, rad q | y, v_l(q) <= 2, q odd prime to p (EXPONENT_CAP Def 1.1).
Usage: y6_verify.py N"""
import sys, numpy as np
from fractions import Fraction
from math import gcd
from sympy import primerange, factorint
N = int(sys.argv[1]); best, bB, bc = np.load('/tmp/y6_best.npy')
cnt = 0; cap2 = 0
for p in primerange(3, N+1):
    g, B, c = int(best[p]), int(bB[p]), int(bc[p]); assert g > 0, p
    assert (g+1) % (c*B) == 0; a = (g+1)//(c*B); assert a % 4 == 0
    Q = c*c*a*B**3//4; assert gcd(Q, p) == 1 and (p + 4*Q*Q) % g == 0
    m = (p + 4*Q*Q)//g; x = Fraction(p+m, 4); y = p*(g+1)//4; assert x.denominator == 1
    z = Fraction(p*int(x)*(g+1), 4*Q*Q); assert Fraction(4, p) == 1/x + Fraction(1, y) + 1/z
    q2 = z.denominator; q = c*B*B; assert q2 == q*q and q % 2 == 1 and gcd(q, p) == 1
    for l, v in factorint(q).items(): assert v <= 2 and y % l == 0
    cnt += 1; cap2 += (B > 1)
print(f"verified {cnt} primes 3 <= p <= {N}; certificates with exponent exactly 2 (B > 1): {cap2}")
