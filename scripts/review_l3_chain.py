"""R205 from-scratch census for LENGTH_THREE §7.6 (Farey-chain slice).

A solution {x,y,z} of 4/p = 1/x+1/y+1/z is a "chain" if for some ordering (X,Y,Z) there are positive integers, gcd(b0, b1) = 1 (needed for a
Farey chain a0/b0 < .. < a3/b3 of unimodular neighbours) and X = b0 b1, Y = b1 b2, Z = b2 b3, b1 | b0 + b2, b2 | b1 + b3.
Usage: uv run --with sympy python scripts/review_l3_chain.py PMAX
"""
import sys
from fractions import Fraction as F
from math import gcd
from itertools import permutations
from sympy import primerange, divisors


def es_solutions(p):
    sols = set()
    for x in range(p // 4 + 1, 3 * p // 4 + 2):
        r = F(4, p) - F(1, x)
        if r <= 0:
            continue
        a, b = r.numerator, r.denominator
        # 1/y + 1/z = a/b, y <= z, y >= x:  (a y - b)(a z - b) = b^2
        for d in divisors(b * b):
            if (d + b) % a:
                continue
            y = (d + b) // a
            e = b * b // d
            if (e + b) % a:
                continue
            z = (e + b) // a
            if x <= y <= z:
                sols.add((x, y, z))
    return sols


def is_chain(t):
    for X, Y, Z in set(permutations(t)):
        for b1 in divisors(X):
            if Y % b1:
                continue
            b0, b2 = X // b1, Y // b1
            if Z % b2:
                continue
            b3 = Z // b2
            if (b0 + b2) % b1 == 0 and (b1 + b3) % b2 == 0 and gcd(b0, b1) == 1:
                return True
    return False


def main():
    PMAX = int(sys.argv[1])
    tot = {1: 0, 2: 0}; ch = {1: 0, 2: 0}; none = []
    for p in primerange(5, PMAX):
        S = es_solutions(p)
        for t in S:
            assert F(4, p) == sum(F(1, v) for v in t)
        anyc = False
        for t in S:
            typ = sum(1 for v in t if v % p == 0)
            tot[typ] += 1
            if is_chain(t):
                ch[typ] += 1; anyc = True
        if not anyc:
            none.append(p)
    print(f"primes < {PMAX}: Type I chains {ch[1]}/{tot[1]}, Type II chains {ch[2]}/{tot[2]}; primes with no chain: {none}")


if __name__ == "__main__":
    main()
