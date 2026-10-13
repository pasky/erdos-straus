#!/usr/bin/env python3
"""R185: from-scratch check of §4.3 (k=9, X2 neighbourhood of mu=5). On X2, nu_q = 289 if v2(ord_q 2) <= 2,
nu_q = -287 if v2(ord_q 2) = 3 (claimed). List primes q with v2(ord)=3 and (-287/q) = -1 (where X2 is NOT a unit square)."""
from sympy import primerange, n_order
from sympy.functions.combinatorial.numbers import legendre_symbol as leg
def v2(x):
    c = 0
    while x % 2 == 0: x//=2; c+=1
    return c
bad3 = []; bad_low = []
for q in primerange(3, 5000):
    o = n_order(2, q); v = v2(o)
    if v <= 2 and (289 % q == 0 or leg(289 % q, q) != 1): bad_low.append(q)
    if v == 3 and (287 % q == 0 or leg((-287) % q, q) != 1): bad3.append((q, q % 16, o))
print('v2<=2 primes where 289 is not a unit square:', bad_low)
print('v2=3 primes with (-287/q) != 1 (q, q mod 16, ord):', bad3[:15])
print('of these, q not 1 mod 16:', [x for x in bad3 if x[1] != 1][:10])
