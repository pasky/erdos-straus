"""Numerical sanity check of Lemma 4 (collapse at a fixed letter) of Z69_NL7.md.
For odd n, letter L, N = n+L (cases x,z) or N = L n + 1 (case y) with N = c*q, q prime > c:
if n is congruent to an odd square modulo 8cL (units or not) then n has no U7 word with that letter in that position.
Also the control: in the complementary cases such words do occur (so the test is not vacuous).  All odd n >= 1.
"""
import sys, random
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import factorint, isprime

def is_odd_square_mod(n, M):
    """n odd, M = 8cL.  True iff some odd m has m^2 ≡ n (mod M).
    2-part (2^a | M, a >= 3): n ≡ 1 (mod 8).  Odd l^a || M: either v_l(n) >= a, or v_l(n) is even and the unit part
    n / l^v is a quadratic residue mod l.  (Non-units are allowed: e.g. n = 9, M = 144.)  The first version of this
    script wrongly rejected every n with gcd(n, M) > 1 (cross-model review, fix 2)."""
    for ell, a in factorint(M).items():
        if ell == 2:
            if n % 8 != 1:
                return False
        else:
            v, u = 0, n
            while u % ell == 0 and v < a:
                u //= ell; v += 1
            if v >= a:
                continue
            if v % 2 == 1 or pow(u, (ell - 1) // 2, ell) != 1:
                return False
    return True

def is_unit_square_mod(n, M):
    return gcd(n, M) == 1 and is_odd_square_mod(n, M)

random.seed(7)
stats = {'x': [0, 0, 0, 0, 0], 'z': [0, 0, 0, 0, 0], 'y': [0, 0, 0, 0, 0]}  # [sq cases, sq with word, nonsq cases, nonsq with word, unit-square cases]
for n in range(1, 400000, 2):
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
                if is_unit_square_mod(n, 8 * c * L):
                    s[4] += 1
                if w:
                    s[1] += 1
                    print("COUNTEREXAMPLE to Lemma 4:", n, L, pos, w[:2])
            else:
                s[2] += 1
                if w:
                    s[3] += 1
for pos in 'xzy':
    s = stats[pos]
    print(f"position {pos}: odd n in [1, 4e5): square-class cases {s[0]} (of which unit-square classes {s[4]}), with a word {s[1]} (Lemma 4 predicts 0); complementary cases {s[2]}, with a word {s[3]}")
