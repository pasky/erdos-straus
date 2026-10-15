# review_r254_small.py -- R254: independent ES search for small members + which certificate leaf covers squares.
import sys
from math import gcd, isqrt
from sympy import divisors
from fractions import Fraction as Fr

def es(n, X=50):
    # greedy-free search: x from ceil(n/4) up, then y from ceil range, z determined
    for x in range(n // 4 + 1, n // 4 + X):
        r = Fr(4, n) - Fr(1, x)
        if r <= 0: continue
        p, q = r.numerator, r.denominator
        # (p y - q)(p z - q) = q^2 ; enumerate divisors D <= q of q^2 by trial division of q^2 (small n only)
        Q = q * q
        for D in divisors(Q):
            if D > q: break
            if (D + q) % p == 0 and (Q // D + q) % p == 0:
                return x, (D + q) // p, (Q // D + q) // p
    return None

for name, f, R in (('7*4^s+9', lambda s: 7 * 4**s + 9, range(0, 12)), ('3*2^m+1', lambda m: 3 * 2**m + 1, range(0, 31))):
    for s in R:
        n = f(s); sol = es(n)
        sq = isqrt(n) ** 2 == n
        assert sol and Fr(4, n) == sum(Fr(1, v) for v in sol), (name, s)
        print(name, s, n, 'SQUARE' if sq else '', sol, flush=True)
