"""R245 from-scratch: forced windows for nu/a^2 (a odd, gcd(a,nu)=1): m = nu*K - a^2 in (0, MW], K odd,
every prime q of m is 3 mod 4 with (K/q) = -1, gcd(m, a) = 1. Count squares having one, per nu."""
import sys
from sympy import factorint, legendre_symbol
from math import gcd
A, MW = int(sys.argv[1]), int(sys.argv[2])
for nu in range(1, 25):
    hit = tot = 0
    for a in range(3, A, 2):
        if gcd(a, nu) != 1: continue
        tot += 1; n = a * a
        K0 = n // nu + 1
        found = False
        for K in range(K0, (n + MW) // nu + 1):
            m = nu * K - n
            if m <= 0 or K % 2 == 0 or gcd(m, n) != 1: continue
            f = factorint(m)
            if all(q % 4 == 3 and legendre_symbol(K % q, q) == -1 for q in f):
                found = True; break
        hit += found
    print(f'nu={nu:2d} (mod4={nu%4}) squares with forced window: {hit}/{tot}')
