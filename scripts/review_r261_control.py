"""R261: least forced window for the Dickson examples + from-scratch control (p = Lt+1 prime, some R_m composite)."""
import sys
from math import lcm, prod
from sympy import isprime, primerange, jacobi_symbol
from review_r261_windows import least_cap
def least_forced(p):
    for q in primerange(3, 10**4):
        if q % 4 == 3 and jacobi_symbol(q, p) == -1:
            return q
for p in [807330585601, 1482496646401, 2412770976001, 4714845095999745907201, 11787094675874034316801]:
    print(p, 'least forced window', least_forced(p))
M, NP = int(sys.argv[1]), int(sys.argv[2])
L = 16 * lcm(*range(1, M + 2)) * prod(primerange(2, M + 2))
ms = list(range(3, M + 1, 4))
cnt = live = 0; t = 0; deadcomp = 0
while cnt < NP:
    t += 1; p = L * t + 1
    if not isprime(p): continue
    Rs = [L // (m + 1) * t + 1 for m in ms]
    if all(isprime(R) for R in Rs): continue
    cnt += 1
    if any(least_cap(p, m, 20) for m in ms): live += 1
print('L', L, 'control primes', cnt, 'with a live window <=', M, ':', live)
