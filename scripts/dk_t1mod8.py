"""O169 §3: T1 for the HJ-length-3 slices via Rademacher's mod-8 congruence.
(R) for odd c, gcd(a,c)=1: 12 c s(a,c) = c + 1 - 2 (a/c)  (mod 8)   [checked numerically below]
On a certificate n/A=[[v,t,u]]: 12 n s(A,n) = n(t+u+v-9) + A + A*  (Hirzebruch-Zagier, §2).
Finite check over (t,u,v) mod 8: if n = tuv-u-v = 1 (mod 4) and [4 | tu-1  or  4 | t],
then n+1 - (n(t+u+v-9) + (tu-1) + (tv-1)) = -2 (mod 8), i.e. Jacobi (A/n) = -1.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/dk_t1mod8.py
"""
from fractions import Fraction
from sympy import jacobi_symbol
from dk_dict import dedekind

bad = 0
for c in range(3, 400, 2):
    for a in range(1, c):
        from math import gcd
        if gcd(a, c) == 1:
            v = 12 * c * dedekind(a, c)
            assert v.denominator == 1
            if (v - (c + 1 - 2 * jacobi_symbol(a, c))) % 8:
                bad += 1
print("(R) failures for odd c<400:", bad)
cases = {"I(4|A)": 0, "II(4|t)": 0}
for t in range(8):
    for u in range(8):
        for v in range(8):
            n = t * u * v - u - v
            if n % 4 != 1:
                continue
            rhs = n + 1 - (n * (t + u + v - 9) + (t * u - 1) + (t * v - 1))
            for name, cond in (("I(4|A)", (t * u - 1) % 4 == 0), ("II(4|t)", t % 4 == 0)):
                if cond:
                    cases[name] += 1
                    if (rhs + 2) % 8:
                        bad += 1; print("fail", name, t, u, v)
print("residue triples checked:", cases, "failures:", bad)
