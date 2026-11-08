#!/usr/bin/env python3
"""z65 LIFT §5.4: Hernandez (arXiv:1112.2425 Thm 3.1) F-pure threshold of x^a+y^b+z^c in char p,
evaluated for a=b=c=(p+1)/2; claim fpt = 4/p for every prime p >= 5. Exact rational arithmetic."""
from fractions import Fraction as F

def digits(alpha, p, n):
    """first n digits of the NON-terminating base-p expansion of alpha in (0,1]."""
    out = []
    x = alpha
    for _ in range(n):
        d = (x * p).__ceil__() - 1   # non-terminating convention: largest digit with remainder > 0
        out.append(d)
        x = x * p - d
    return out

def fpt(ds, p, n=60):
    digs = [digits(F(1, d), p, n) for d in ds]
    L = None
    for e in range(n):
        if sum(dg[e] for dg in digs) > p - 1:
            L = e  # digits 1..e add without carry, digit e+1 carries
            break
    if L is None:
        return sum(F(1, d) for d in ds)
    return sum(sum(F(dg[i], p ** (i + 1)) for i in range(L)) for dg in digs) + F(1, p ** L)

def primes(n):
    return [q for q in range(5, n) if all(q % r for r in range(2, int(q ** .5) + 1))]

bad = [p for p in primes(2000) if fpt([(p + 1) // 2] * 3, p) != F(4, p)]
print("primes 5..2000 with fpt_p(x^d+y^d+z^d) != 4/p for d=(p+1)/2:", bad)
print("examples:", [(p, fpt([(p + 1) // 2] * 3, p)) for p in (5, 13, 409)])
