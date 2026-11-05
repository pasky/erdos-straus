#!/usr/bin/env python3
"""Local data of the 38 G*-zero primes: p mod 8, Legendre symbols at small primes, least ODD prime QNR (primes from 3)."""
from sympy import legendre_symbol, primerange, isprime
zeros = [int(x) for x in open('data/z57/bff/gstar_zeros_le1e8.txt')] + [564661441]
smalls = list(primerange(3, 60))
print('p', 'p%8', 'p%840', ' '.join(f'({q})' for q in smalls), 'leastOddQNR')
for p in zeros:
    assert isprime(p) and p % 4 == 1
    syms = [legendre_symbol(p, q) for q in smalls]
    lq = next(q for q in primerange(3, 10**6) if legendre_symbol(p, q) == -1)
    print(p, p % 8, p % 840, ' '.join('+' if s == 1 else '-' for s in syms), lq)
