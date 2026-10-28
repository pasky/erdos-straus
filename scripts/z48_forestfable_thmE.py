#!/usr/bin/env python3
"""z48 forestfable — direct check of Theorem E (independent of the forest scan):
for odd m ≤ M and v ≤ V with v ≡ 7 (mod 8) or 4 | v and gcd(v, m) = 1, the integer m² + v has no divisor A ≡ −1 (mod v), A > 1.
Also checks the numerator version: A ≡ 7 (mod 8), A | m² + u, A ≡ −1 (mod u) never happens (u ≤ V)."""
import sys
from math import gcd
from sympy import divisors
M = int(sys.argv[1]) if len(sys.argv) > 1 else 301
V = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
bad = 0; checked = 0; bad2 = 0; checked2 = 0
for m in range(3, M + 1, 2):
    for v in range(4, V + 1):
        if not (v % 8 == 7 or v % 4 == 0) or gcd(v, m) != 1:
            continue
        checked += 1
        for A in divisors(m * m + v):
            if A > 1 and A % v == v - 1:
                bad += 1; print("THM E COUNTEREXAMPLE", m, v, A)
    for u in range(1, V + 1):
        if gcd(u, m) != 1:
            continue
        checked2 += 1
        for A in divisors(m * m + u):
            if A % 8 == 7 and A % u == (u - 1) % u:
                bad2 += 1; print("NUMERATOR-7 COUNTEREXAMPLE", m, u, A)
print(f"Theorem E: {checked} pairs (m,v) checked, {bad} counterexamples; numerator class 7 (8): {checked2} pairs (m,u), {bad2} counterexamples")
