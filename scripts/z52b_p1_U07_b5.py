#!/usr/bin/env python3
"""U07 Z1705: for L_p={(x,y): y≡ i x (mod p)} (p≡1 mod 4 ≤ 2000), lambda1^2/p (Gauss-reduced) vs Minkowski bound (sqrt(4/pi)),
and fraction of primes with lambda1^2 <= p/4 (product-bound side). Capped at p<=2000."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from sympy import primerange, sqrt_mod
import math
def gauss(u, v):
    while True:
        if u[0]**2+u[1]**2 > v[0]**2+v[1]**2: u, v = v, u
        m = round((u[0]*v[0]+u[1]*v[1]) / (u[0]**2+u[1]**2))
        if m == 0: return u, v
        v = (v[0]-m*u[0], v[1]-m*u[1])
ratios = []; small = 0; n = 0
for p in primerange(5, 2001):
    if p % 4 != 1: continue
    i = sqrt_mod(-1, p); u, v = gauss((1, i), (0, p)); n += 1
    l1 = u[0]**2 + u[1]**2
    ratios.append(l1 / p)
    if l1 <= p / 4: small += 1
print("primes", n, "min lambda1^2/p", round(min(ratios), 5), "max", round(max(ratios), 5), "mean", round(sum(ratios)/n, 4))
print("primes with lambda1^2 <= p/4:", small, "(Minkowski/Hermite: lambda1^2 <= 2p/sqrt3 ~ 1.155p always)")
