"""O200: overflow rigidity in the shot family r | n+4Q^2.
For every odd n<=NMAX, odd Q<=QMAX with gcd(Q,n)=1, every divisor g = 3 mod 4 of n+4Q^2:
Q0=gcd(Q,(g+1)/4), Q1=Q/Q0, k=(g+1)/(4 Q0), m=(n+4Q^2)/g, j=(m+n)/Q0, D=k j - Q1^2.
Checks: j integer, D>0, 4 Q0 D = 4kn+j, D g = 4k^2 n + Q1^2, den(z)=Q1^2 (exact Fraction check),
and records max g relative to n, Q1.  usage: xc_rigidity.py NMAX QMAX"""
import sys
from math import gcd
from fractions import Fraction as F
from sympy import divisors

NMAX, QMAX = int(sys.argv[1]), int(sys.argv[2])
worst = {}  # Q1 -> (max g/(n^2), args)
cnt = 0; best_ratio = (0, None)
for n in range(3, NMAX + 1, 2):
    for Q in range(1, QMAX + 1, 2):
        if gcd(Q, n) != 1: continue
        a = n + 4 * Q * Q
        for g in divisors(a):
            if g % 4 != 3: continue
            Q0 = gcd(Q, (g + 1) // 4); Q1 = Q // Q0
            k = (g + 1) // (4 * Q0); m = a // g
            assert (m + n) % Q0 == 0
            j = (m + n) // Q0; D = k * j - Q1 * Q1
            assert D > 0 and 4 * Q0 * D == 4 * k * n + j and D * g == 4 * k * k * n + Q1 * Q1
            e = a // g; x = (n + e) // 4; y = n * (g + 1) // 4; z = F(n * x * (g + 1), 4 * Q * Q)
            assert F(4, n) == F(1, x) + F(1, y) + 1 / z and z.denominator == Q1 * Q1
            cnt += 1
            # bound candidate: g <= n + 4 Q1^2 * Q0^2 ; record g / (n*(n+Q1^2)*Q1^2)
            r = g / (n * Q1 * Q1 * (n + Q1 * Q1))
            if r > best_ratio[0]: best_ratio = (r, (n, Q, g, Q0, Q1, k, j, D))
            w = worst.get(Q1)
            if w is None or g / n**2 > w[0]: worst[Q1] = (g / n**2, (n, Q, g, k, j, D))
print("shots checked", cnt)
print("max g/(n Q1^2 (n+Q1^2)) =", best_ratio)
for Q1 in sorted(worst)[:12]:
    print("Q1", Q1, "max g/n^2 %.3f" % worst[Q1][0], worst[Q1][1])
