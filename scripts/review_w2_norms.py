#!/usr/bin/env python3
"""R29: brute-force check of Lemma 1.2 (POINTWISE_WINDOW2 §1) for n<=N:
 for 3∤n: n has no prime factor ≡2 (3)  <=>  n = a²+ab+b² with gcd(a,b)=1;
 for 7∤n: n has no prime factor r with (r/7)=-1  <=>  n = c²+cd+2d², gcd(c,d)=1.
"""
import sys
from math import gcd, isqrt
from sympy import factorint, legendre_symbol as L

N = int(float(sys.argv[1]))
rep3 = bytearray(N + 1); rep7 = bytearray(N + 1)
B = isqrt(4 * N) + 2
for a in range(-B, B + 1):
    for b in range(0, B + 1):
        if gcd(a, b) != 1:
            continue
        v = a * a + a * b + b * b
        if 0 < v <= N: rep3[v] = 1
        v = a * a + a * b + 2 * b * b
        if 0 < v <= N: rep7[v] = 1
bad = 0
for n in range(1, N + 1):
    f = factorint(n)
    if n % 3:
        c = all(r % 3 != 2 for r in f)
        bad += c != bool(rep3[n])
    if n % 7:
        c = all(r == 7 or L(r % 7, 7) != -1 for r in f)
        bad += c != bool(rep7[n])
print(f"N={N}: mismatches={bad}")
