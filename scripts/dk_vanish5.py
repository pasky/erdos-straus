"""O169 §9: vanishing set of the five X/e-slices (+ boundary 4.2) over ALL odd n = 1 (4), n <= N.
Lists non-square n with no hit, with factorisations; flags those having a prime factor = 3 (mod 4).
Usage: uv run python scripts/dk_vanish5.py N
"""
import sys
from math import isqrt
N = int(sys.argv[1])
hit = bytearray(N + 1)
t = 2
while 4*t - 4 <= N:
    u = 2
    while 2*(t*u-1) - u <= N:
        A = t*u - 1; v = 2
        while (n := v*A - u) <= N:
            if not hit[n] and (A % 4 == 0 or (t*v-1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0):
                hit[n] = 1
            v += 1
        u += 1
    t += 1
def fac(m):
    f, q = [], 2
    while q*q <= m:
        while m % q == 0: f.append(q); m //= q
        q += 1
    if m > 1: f.append(m)
    return f
ex = []
for n in range(5, N+1, 4):
    if isqrt(n)**2 == n:
        assert not hit[n]; continue
    if hit[n] or any(q % 4 == 3 for q in fac((n+1)//2)): continue
    ex.append(n)
print(f"N={N}: non-square n=1(4) with no five-slice/boundary hit: {len(ex)}")
for n in ex: print(n, fac(n), "has q=3(4)" if any(q % 4 == 3 for q in fac(n)) else "")
