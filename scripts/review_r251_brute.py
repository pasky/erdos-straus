"""R251: independent ES search for n = 3*2^s + 1, small s (no rules used).
For x near n/4 (a few hundred candidates), remainder p/q = 4/n - 1/x; 1/y + 1/z = p/q  <=>
(p y - q)(p z - q) = q^2; enumerate divisors D of q^2 with D = -q mod p."""
import sys
from math import gcd
from sympy import factorint, divisors
from fractions import Fraction as F

def es(n, xspan=400):
    x0 = n // 4 + 1
    for x in range(x0, x0 + xspan):
        p, q = 4*x - n, n*x
        g = gcd(p, q); p //= g; q //= g
        fq = factorint(q)
        f2 = {k: 2*v for k, v in fq.items()}
        # iterate divisors of q^2 up to q
        divs = [1]
        for pr, e in f2.items():
            divs = [d*pr**i for d in divs for i in range(e+1)]
            if len(divs) > 2_000_000: break
        for D in divs:
            if D <= q and (D + q) % p == 0:
                y = (D + q)//p; z = (q*q//D + q)//p
                assert F(1, x) + F(1, y) + F(1, z) == F(4, n)
                return x, y, z
    return None

S = int(sys.argv[1]) if len(sys.argv) > 1 else 40
for s in range(0, S + 1):
    n = 3*2**s + 1
    sol = es(n) if n > 4 else (2, 3, 6)
    print(s, n, sol)
    assert sol
