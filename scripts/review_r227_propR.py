"""R227 check of the input to Prop R: chi(w) = (-A/n) is a function of (w mod 8, sign vector) over ALL odd n tested
(signed words included), n ranging over primes and composites, and n mod 8 is determined by w mod 8.
Also checks the stronger statement used in the review: the 2-adic Gram matrix of Q_w mod 8 (hence its Z_2-class) is a
function of w mod 8 (trivial: Gram = [[v,-1,0],[-1,t,-1],[0,-1,u]]).
usage: uv run --with sympy python scripts/review_r227_propR.py
"""
from math import gcd
from sympy import jacobi_symbol as J

table = {}
clash = 0
nw = 0
for n in range(3, 400, 2):
    for u in range(-60, 61):
        if u == 0:
            continue
        for t in range(-60, 61):
            if t == 0:
                continue
            A = t * u - 1
            if A == 0 or (n + u) % A:
                continue
            v = (n + u) // A
            if v == 0:
                continue
            assert t * u * v - u - v == n
            if gcd(A, n) != 1:
                continue  # chi = 0 words excluded (Prop R is stated for primes)
            chi = J(-A % n, n)
            key = (t % 8, u % 8, v % 8, t > 0, u > 0, v > 0)
            nw += 1
            if key in table and table[key][0] != chi:
                clash += 1
            table.setdefault(key, (chi, n))
print("signed words", nw, "cells", len(table), "clashes", clash)
