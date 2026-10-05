"""R32: check beta_tot(Z) ~ Z^2/(4 pi^2) and the optimum c of Thm 1.5 (from scratch)."""
from math import gcd, pi, log

def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r

def omega(n):
    c, p = 0, 2
    while p * p <= n:
        if n % p == 0:
            c += 1
            while n % p == 0:
                n //= p
        p += 1
    return c + (n > 1)

for Z in (100, 1000, 5000):
    bt = sum((phi(a) - 2 ** omega(a)) // 4 + 2 ** (omega(a) - 1) - 1 for a in range(3, Z + 1, 4))
    print(Z, bt, bt / (Z * Z / (4 * pi * pi)))
# exponent f(k)= -(k/8) + (log2/(4pi^2)) k^2  per L^2, with Z=kL, J~Z/4
k = pi ** 2 / (4 * log(2))
print("k*=%.3f  c=%.4f" % (k, k / 8 - log(2) / (4 * pi * pi) * k * k))
