"""control for z22_dickson_check: p = L t + 1 prime but R_m NOT all prime: how many windows m <= M are alive?"""
import sys
from math import lcm, prod
from sympy import isprime, primerange, factorint
from sympy.ntheory import reduced_totient
from z22_common import best_cap
M, NP = int(sys.argv[1]), int(sys.argv[2])
Lam = 1
for k in range(1, M + 2):
    Lam = lcm(Lam, k)
L = 16 * Lam * prod(primerange(2, M + 2)); wins = list(range(3, M + 1, 4))
n = alive_any = 0; t = 0
while n < NP:
    t += 1; p = L * t + 1
    if not isprime(p) or all(isprime(L // (m + 1) * t + 1) for m in wins):
        continue
    n += 1
    alive = sum(best_cap(p, m, int(reduced_totient(m)) + 2, fK=factorint((p + m) // 4)) is not None for m in wins)
    alive_any += alive > 0
print('M', M, 'control primes', n, 'with some live window <= M:', alive_any)
