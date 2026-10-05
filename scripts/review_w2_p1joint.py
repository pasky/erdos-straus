#!/usr/bin/env python3
"""R29: joint sieve data |A_{d1,d2}| (d1|n3 bad-3, d2|n7 bad-7) for classes (p/3),(p/7) with
p≡1 (8), p≡1 (5), p≤X.  Checks the proposed M1 repair ((+,+) vs (+,-) identical)."""
import sys
from sympy import primerange
X = int(float(sys.argv[1]))
L = lambda a, q: 1 if pow(a % q, (q - 1) // 2, q) == 1 else -1
cls = {}
for p in primerange(11, X):
    if p % 8 == 1 and p % 5 == 1:
        cls.setdefault((L(p, 3), L(p, 7)), []).append(p)
D = [(1, 1), (1, 3), (11, 1), (1, 5), (1, 13), (11, 13), (17, 3), (23, 17), (1, 19), (29, 31)]
print("class N", *[f"{a}|{b}" for a, b in D])
for k in sorted(cls):
    l = cls[k]
    print(k, len(l), *[sum(1 for p in l if ((p + 3) // 4) % a == 0 and ((p + 7) // 4) % b == 0) for a, b in D])
