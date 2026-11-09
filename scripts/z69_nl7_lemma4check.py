"""Numerical sanity check of Lemma 4 (collapse at a fixed letter) of Z69_NL7.md.
For odd n, letter L, N = n+L (cases x,z) or N = L n + 1 (case y) with N = c*q, q prime > c:
if n is an odd square modulo 8cL then n has no U7 word with that letter in that position.
Also the control: when n is NOT a square mod 8cL such words do occur (so the test is not vacuous).
"""
import sys, random
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import factorint, isprime

def is_odd_square_mod(n, M):
    # n odd; M = 8cL. square of a unit mod every prime power of M (and ≡ 1 mod 8)
    if gcd(n, M) != 1:
        return False
    for ell, e in factorint(M).items():
        if ell == 2:
            if n % 8 != 1:
                return False
        else:
            if pow(n, (ell - 1) // 2, ell) != 1:
                return False
    return True

random.seed(7)
stats = {'x': [0, 0, 0, 0], 'z': [0, 0, 0, 0], 'y': [0, 0, 0, 0]}  # [sq cases, sq with word, nonsq cases, nonsq with word]
for n in range(3, 400000, 2):
    for L in (1, 2, 3, 4, 5, 6, 7, 8, 12, 15, 24):
        for pos in ('x', 'z', 'y'):
            N = n + L if pos in 'xz' else L * n + 1
            fac = factorint(N, limit=200)
            q = max(fac)
            if fac[q] != 1 or not isprime(q):
                continue
            c = N // q
            if q <= c or c > 200:
                continue
            sq = is_odd_square_mod(n, 8 * c * L)
            if pos == 'x':
                w = words_with_x(n, L)
            elif pos == 'z':
                w = words_with_z(n, L)
            else:
                w = words_with_y(n, L)
            s = stats[pos]
            if sq:
                s[0] += 1
                if w:
                    s[1] += 1
                    print("COUNTEREXAMPLE to Lemma 4:", n, L, pos, w[:2])
            else:
                s[2] += 1
                if w:
                    s[3] += 1
for pos in 'xzy':
    s = stats[pos]
    print(f"position {pos}: square-class cases {s[0]}, with a word {s[1]} (Lemma 4 predicts 0); non-square-class cases {s[2]}, with a word {s[3]}")
