"""Independent brute force for ES_Q1 counts at Gaussian primes a+bi (0<a<b), N <= LIM: loop over x (least norm coordinate)
and y (middle), z from the equation; exact rational complex arithmetic."""
import sys
from fractions import Fraction as Fr
from sympy import isprime
def inv(zr, zi):
    n = zr * zr + zi * zi; return (Fr(zr) / n, Fr(-zi) / n)
def key(z): return (z[0]*z[0]+z[1]*z[1], z[0], z[1])
def count(a, b):
    N = a * a + b * b; wr, wi = Fr(4 * a, N), Fr(-4 * b, N)
    R = int((9 * N / 16) ** 0.5) + 2; c = 0
    for xr in range(R + 1):
        for xi in range(R + 1):
            nx = xr * xr + xi * xi
            if nx == 0 or 16 * nx > 9 * N: continue
            ur, ui = inv(xr, xi); rr, ri = wr - ur, wi - ui
            nr = rr * rr + ri * ri
            if nr == 0: continue
            Ymax = int(4 / nr) + 1
            Ry = int(Ymax ** 0.5) + 1
            for yr in range(Ry + 1):
                for yi in range(Ry + 1):
                    ny = yr * yr + yi * yi
                    if ny == 0 or ny > Ymax or key((yr, yi)) < key((xr, xi)): continue
                    vr, vi = inv(yr, yi); sr, si = rr - vr, ri - vi
                    if sr == 0 and si == 0: continue
                    zr, zi = inv(sr, si)  # 1/(s) with rational parts
                    if zr.denominator != 1 or zi.denominator != 1: continue
                    z = (int(zr), int(zi))
                    if z[0] < 0 or z[1] < 0: continue
                    if key(z) < key((yr, yi)): continue
                    c += 1
    return c
LIM = int(sys.argv[1])
for a in range(1, 40):
    for b in range(a + 1, 40):
        N = a * a + b * b
        if N <= LIM and isprime(N): print(a, b, N, count(a, b))
