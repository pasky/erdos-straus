"""Prop 3.2(b) check: for Mordell-hard primes p (p mod 840 in {1,121,169,289,361,529}), p <= LIM:
an interior word with endpoint u = 3 (t >= 3, v >= 3) exists  <=>  M = (p+3)/4 is composite."""
import sys
from sympy import primerange, divisors, isprime
LIM = int(sys.argv[1])
H = {1, 121, 169, 289, 361, 529}
n = agree = 0; cert = 0
for p in primerange(5, LIM):
    if p % 840 not in H: continue
    n += 1
    M = (p + 3) // 4
    ex = False; ex_cert = False
    for A in divisors(p + 3):
        if A % 3 == 2:
            t, v = (A + 1) // 3, (p + 3) // A
            if t >= 3 and v >= 3:
                assert t * 3 * v - 3 - v == p
                ex = True
                if any(c % 4 == 0 or (c + p) % 8 == 0 for c in (t, 3, v)): ex_cert = True
    agree += (ex == (not isprime(M)))
    cert += ex_cert
print(f'Mordell-hard primes <= {LIM}: {n}; equivalence holds for {agree}; with a certifying u=3 interior word: {cert}')
