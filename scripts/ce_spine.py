"""Cor 3.3 check: for p = 1 mod 8 < N, t=1 certificate (divisor a | p+1 with (a/p) = -1) <=> p+1 has a prime factor 3 mod 4."""
import sys
from sympy import primerange, factorint, divisors
N = int(sys.argv[1])
bad = tot = miss = 0
for p in primerange(9, N):
    if p % 8 != 1:
        continue
    tot += 1
    f = factorint(p + 1)
    crit = any(q % 4 == 3 for q in f)
    if N <= 200000:
        direct = any(pow(a, (p - 1) // 2, p) == p - 1 for a in divisors(p + 1))
        bad += direct != crit
    miss += not crit
print('p=1 mod 8 <', N, ':', tot, 'primes; no t=1 certificate:', miss, '; criterion mismatches:', bad)
