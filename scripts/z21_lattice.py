"""O249 (ASTRA_BRIDGE Thm 3.4, lattice picture): for primes p = 1 (4) <= P, moduli g = 3 (4) <= GM with a root
rho^2 = -p (mod g), every k | h = (g+1)/4 and every Y in 1..YM with Y = 2k rho (mod g), gcd(Y, 2k) = 1,
gcd(hY/k, p) = 1: build the shot (Q, g) with Q = (h/k) Y via EXPONENT_CAP §1 and check exactly
 4/p = 1/x + 1/y + 1/z, y = p h, den z = Y^2 (overflow = Y), and ES <=> Y = 1.
Also the Astra source (m, 1): m = rho^{-1} (mod g), m <= YM: identity exact.
Usage: z21_lattice.py P GM YM
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import primerange, divisors

P, GM, YM = (int(a) for a in sys.argv[1:4])
st = dict(shots=0, es=0, src=0)
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for g in range(3, GM + 1, 4):
        if g % p == 0:
            continue
        roots = [r for r in range(g) if (r * r + p) % g == 0]
        h = (g + 1) // 4
        for rho in roots:
            for k in divisors(h):
                y0 = (2 * k * rho) % g
                for Y in range(y0 if y0 else g, YM + 1, g):
                    if gcd(Y, 2 * k) != 1 or gcd(h * Y // k, p) != 1:
                        continue
                    Q = (h // k) * Y
                    assert (p + 4 * Q * Q) % g == 0
                    m = (p + 4 * Q * Q) // g
                    assert (p + m) % 4 == 0
                    x, y = (p + m) // 4, p * (g + 1) // 4
                    z = F(p * x * (g + 1), 4 * Q * Q)
                    assert F(4, p) == F(1, x) + F(1, y) + 1 / z and y == p * h
                    assert z.denominator == Y * Y, (p, g, k, Y, z)
                    st['shots'] += 1
                    st['es'] += (Y == 1)
            if gcd(rho, g) == 1:
                m0 = pow(rho, -1, g)
                for m in range(m0 if m0 else g, YM + 1, g):
                    assert (p * m * m + 1) % g == 0
                    s = (p * m * m + 1) // g
                    N = p * m * m
                    assert F(4, N) == F(1, s * h) + F(1, N * s * h) + F(1, N * h)
                    st['src'] += 1
print(st)
