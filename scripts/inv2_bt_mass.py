"""O162 Prop 7.1: certified upper bound for the Brun–Titchmarsh mass of {t=u} on p = 1 (24).
mu = sum over odd a >= 3 with a = 15, 23 (mod 24) of phi(gcd(24,a^2-1))/phi(a^2-1).
(Compatibility: the class -a mod (a^2-1) meets 1 mod 24 iff -a = 1 mod gcd(24,a^2-1) iff a = 15, 23 mod 24.)
Partial sum a <= AMAX in Decimal with ROUND_CEILING (each quotient and each addition rounded up);
tail a > AMAX via phi(n) >= 0.375 n^0.9 (> n^0.9/3; the minimum of prod_p min_k p^{0.1k}(1-1/p) is over p<=5)
and phi(gcd) <= 8:  tail <= sum_{a>AMAX, a in 2 classes mod 24} 24/(a^2-1)^0.9
                          <= 24 * (2/24) * (1 + 24/AMAX) * int_{AMAX-24}^inf (x^2-1)^-0.9 dx  (monotone terms)
                          <= 2 * 1.01 * (AMAX-25)^-0.8 / 0.8 * 1.01   (crude, (x^2-1)^-0.9 <= 1.01 x^-1.8 for x>=AMAX-24)
Also prints the empirical covered fraction. Usage: uv run python scripts/inv2_bt_mass.py [AMAX] [PMAX]"""
import sys
from math import gcd
from decimal import Decimal, getcontext, ROUND_CEILING
from sympy import totient, isprime
AMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2 * 10**6
getcontext().prec = 40
getcontext().rounding = ROUND_CEILING
mass = Decimal(0)
for a in range(3, AMAX + 1, 2):
    m = a * a - 1
    g = gcd(24, m)
    if (-a - 1) % g:
        continue
    assert a % 24 in (15, 23)
    mass += Decimal(int(totient(g))) / Decimal(int(totient(m)))
tail = Decimal(2) * Decimal("1.01") * Decimal("1.01") / Decimal("0.8") * (Decimal(AMAX - 25) ** Decimal("-0.8"))
mu = mass + tail
print(f"partial mass (a<={AMAX}, rounded up) = {mass:.12f}; tail <= {tail:.3e}; mu <= {mu:.9f}; 1-2mu >= {1-2*mu:.6f}")
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
