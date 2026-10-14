#!/usr/bin/env python3
"""R217: exact-integer evaluation of the Lemma 1.6 route bounds for one pattern (for spot checks against the C codes),
and exact finite sums for small S (fractions). Independent of scripts/fs_sum_check.py.
usage: review_fs_exact.py pattern r s a z y t      -> prints every route value (exact integer)
       review_fs_exact.py sum r S                    -> exact rational finite sum, s <= S
"""
import sys
from fractions import Fraction
from math import comb, factorial

def Ns(q, d): return 1 if d == 0 else q**d - q**(d - 1)
def Som(q, e): return 1 if e == 0 else q**e * 2 + q**(e - 1) * (e - 1) * (q - 1)  # q^e(2 + (e-1)(1-1/q))

def jcop(n, d, rho, JMAX=400):
    X = d - rho
    if X < 0: return 1
    for j in range(1, JMAX + 1):
        for m in range(1, j + 1):
            # Delta(m, k) with k = j - m, literal form of (C)
            k = j - m
            D2 = n * m * (m + 1) + X * (m * (m + 1) + 2 * k * m + k * (k + 1))   # = 2 Delta(m,k)
            if D2 < 2 * (m + k + 1) * m * d:
                return j
    return 0

def cls(n, d, rho, cof):
    best = comb(n, d)
    if d < rho or (cof and n - d < rho): return 1
    c = 0
    if 3 * rho > n: c = 2
    j = jcop(n, d, rho)
    if j and (not c or j < c): c = j
    if cof:
        j = jcop(n, n - d, rho)
        if j and (not c or j < c): c = j
    return min(best, c) if c else best

def routes(q, s, a, z, y, t):
    b = y + t
    M, G, W, C, V = Ns(q, z), Ns(q, y), Ns(q, a - 1), Ns(q, b - 1), Ns(q, t - 2)
    mult = factorial(s - 2) // (factorial(z) * factorial(a - 1) * factorial(b - 1))
    R = {
        'T0': M * G * W, "R4'": M * W * V, 'X1': 2 * M * G * V, 'X2': G * V * W, 'R1': V * mult,
        'R2': M * G * cls(s + 2 * y + z, a + y + z, 1 + y + z, 1),
        'R3': W * G * cls(s - 1 + y, a + y + z, a + y, 0),
        'R4': M * W * cls(s - 2, a + y + z, a + z, 1),
        'R3C': C * G * cls(s - 1 + y, b + y + z, b + y, 0),
        'R4C': M * C * cls(z + 2 * b - 2, b + y + z, b + z, 1),
        'R5a': V * W * cls(s - 1 - a, b - 1, t - 1, 1),
        'R5b': V * C * cls(s - 1 - b, a - 1, t - 1, 1),
        'R6a': V * comb(s - 2, a - 1) * cls(s - 1 - a, b - 1, t - 1, 1),
        'R6b': V * comb(s - 2, b - 1) * cls(s - 1 - b, a - 1, t - 1, 1),
        'R8a': G * V * comb(s - 2, a - 1), 'R8b': G * V * comb(s - 2, b - 1),
        'R9a': M * V * comb(a + b - 2, a - 1),
        'R10a': M * 2 * Som(q, t - 2) * cls(a + b - 2, a - 1, t - 1, 1),
        'R10b': 2 * Som(q, t - 2) * comb(s - 2, z) * cls(a + b - 2, a - 1, t - 1, 1),
    }
    return R

def main():
    if sys.argv[1] == 'pattern':
        r, s, a, z, y, t = map(int, sys.argv[2:8]); q = 3**r
        R = routes(q, s, a, z, y, t)
        import math
        for k, v in sorted(R.items(), key=lambda kv: kv[1]):
            print(f'{k:5s} {v}  log={math.log(v):.6f}')
    else:
        r, S = int(sys.argv[2]), int(sys.argv[3]); q = 3**r
        tot = Fraction(0)
        for s in range(3, S + 1):
            term = 0
            for a in range(1, s + 1):
                for z in range(0, s - a + 1):
                    for y in range(0, s - a - z + 1):
                        t = s - a - z - y; b = y + t
                        if t < 2 or b < a: continue
                        term += (2 if a < b else 1) * min(routes(q, s, a, z, y, t).values())
            tot += Fraction(term, q**((s + 1) // 2 - 1))
            print(f's={s} term={float(Fraction(term, q**((s + 1) // 2 - 1))):.12e} cum={float(tot):.12e}', flush=True)
        print(f'EXACT r={r} S={S} total={tot.numerator}/{tot.denominator} ~ {float(tot):.15e}')

if __name__ == '__main__':
    main()
