#!/usr/bin/env python3
"""R185 from-scratch checks of numerical side claims of EXPONENT_COVERING.md."""
import sympy as sp
from sympy.ntheory import legendre_symbol as leg, n_order
# primes in 27*2^m+1
print('27*2^m+1 prime for m in', [m for m in range(0, 80) if sp.isprime(27*2**m+1)])
# k=27 character table Q={5,7,13}, L=12
for m in range(12, 24):
    N = 27*2**m+1
    ch = {q: (0 if N % q == 0 else leg(N % q, q)) for q in (3, 5, 7, 13)}
    print('m mod 12 =', m % 12, ch, 'N mod 840 =', N % 840, 'N mod 7 =', N % 7, 'N mod 13 =', N % 13)
print('315*8 =', 315*8, '15015*8 =', 15015*8, 'ord_7(2), ord_5, ord_13:', n_order(2,7), n_order(2,5), n_order(2,13))
