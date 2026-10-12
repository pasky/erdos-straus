"""O162 §7: Brun–Titchmarsh mass of the cylinder {t=u} on p = 1 (24).
mass = sum over odd a>=3 with class -a mod (a^2-1) compatible with 1 mod 24 of phi(gcd(24,a^2-1))/phi(a^2-1),
plus a rigorous tail bound; and the empirical covered fraction.
Usage: uv run python scripts/inv2_bt_mass.py [AMAX] [PMAX]"""
import sys
from math import gcd
from sympy import totient, isprime
AMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2 * 10**6
mass = 0.0
for a in range(3, AMAX + 1, 2):
    m = a * a - 1
    g = gcd(24, m)
    if (-a - 1) % g:  # class -a mod m incompatible with p = 1 mod 24
        continue
    mass += float(totient(g)) / float(totient(m))
# tail a > AMAX: phi(g) <= 8 and Rosser–Schoenfeld phi(m) > m/(e^g loglog m + 3/loglog m); crude numeric bound
# phi(m) >= m / (2 log log m + 3) for m >= 10^12 (crude, Rosser-Schoenfeld gives 1.79 loglog + 2.5/loglog)
import math
L = 2 * math.log(math.log(AMAX**2)) + 3
tail = 8 * L * sum(1.0 / (a * a - 1) for a in range(AMAX + 1, 50 * AMAX, 2)) + 8 * L / (2 * 50 * AMAX) * 1.01 * 2
print(f"BT mass of {{t=u}} on p=1(24): sum_(a<= {AMAX}) = {mass:.6f}, tail <= {tail:.2e}; 2*mass = {2*mass:.6f}")
cov = tot = 0
for p in range(25, PMAX, 24):
    if not isprime(p):
        continue
    tot += 1
    a = 3
    hit = False
    while a * a - 1 <= p + a:
        if (p + a) % (a * a - 1) == 0:
            hit = True
            break
        a += 2
    cov += hit
print(f"empirical: primes p=1(24) < {PMAX}: {tot}, with E(p)∩{{t=u}}≠∅: {cov} ({cov/tot:.4f})")
