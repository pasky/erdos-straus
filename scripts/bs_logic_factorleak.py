"""O141(c): does an ES-solution oracle leak factors of n = p*q?
For semiprimes n (both factors >= 5, n = 1 mod 24) enumerate ALL solutions 4/n = 1/x+1/y+1/z (x<=y<=z) and
count those where no denominator has 1 < gcd(den, n) < n ("non-revealing").
Usage: bs_logic_factorleak.py NMAX
"""
import sys
from math import gcd
from sympy import factorint, primerange
NMAX = int(sys.argv[1])
def divs_of_square(fac):
    ds = [1]
    for pr, e in fac.items():
        ds = [d * pr**k for d in ds for k in range(2 * e + 1)]
    return ds
def solutions(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r, s = 4 * x - n, n * x
        g = gcd(r, s); r //= g; s //= g
        fac = factorint(s)
        for d in divs_of_square(fac):
            if d > s or (s + d) % r: continue
            y = (s + d) // r; z = (s + s * s // d) // r
            if (s + s * s // d) % r == 0 and y >= x:
                out.append((x, y, z))
    return out
primes = list(primerange(5, NMAX // 5 + 1))
tot = 0; noleak_zero = []
for i, p in enumerate(primes):
    for q in primes[i:]:
        n = p * q
        if n > NMAX: break
        if n % 24 != 1: continue
        sols = solutions(n)
        nr = sum(1 for sol in sols if all(gcd(v, n) in (1, n) for v in sol))
        tot += 1
        if nr == 0: noleak_zero.append(n)
        if tot <= 12 or nr == 0:
            print(f"n={n}={p}*{q} n%840={n%840} solutions={len(sols)} non-revealing={nr}", flush=True)
print("semiprimes tested:", tot, " with NO non-revealing solution:", noleak_zero)
