"""O230 s5_gcd_sides: check gcd(tp+1, p+u) = tu-1 = A on every word, and ES-five <=> some (t,u) with gcd = tu-1 psi-odd,
for primes p = 1 (4), p < PMAX.  Brute force over (t,u) with tu - 1 | p + u."""
import sys
from math import gcd
from sympy import primerange, legendre_symbol, jacobi_symbol
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
bad = nw = 0
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    found = False
    for u in range(1, p + 2):
        for t in range(1, (p + u) // u + 2):
            A = t * u - 1
            if A < 1 or (p + u) % A: continue
            v = (p + u) // A
            if (t * v - 1) * A != t * p + 1: bad += 1
            nw += 1
            if gcd(t * p + 1, p + u) != A: bad += 1
            if jacobi_symbol(A, p) == -1: found = True
    if not found: print("no psi-odd gcd at", p)
print("words", nw, "violations", bad)
