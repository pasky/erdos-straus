#!/usr/bin/env python3
"""R29 from-scratch brute-force check of Thm P1 (POINTWISE_WINDOW2 §2).

A^± = {p<=X: p≡1(8), p≡1(35), (p/3)=±1}; n3=(p+3)/4.
 1. A^-: n3 never 'clean' (clean = no prime factor ≡2 mod 3).
 2. (-1)^{Omega_3^-(n3)} = (p/3) for all p≡1(8) (Omega with multiplicity).
 3. sieve data |A^±_d| for odd squarefree d made of primes ≡2(3): compare.
 4. joint version: classes ((p/3),(p/7)) with p≡1(8), p≡1(5); window-7 bad
    primes r with (r/7)=-1; check whether joint data |A_{d1 d2}| coincide,
    in particular for d2 divisible by 3.
Usage: review_w2_p1.py X
"""
import sys
from sympy import factorint, primerange, legendre_symbol as L

X = int(float(sys.argv[1]))
P = list(primerange(3, X))
def bad3(r): return r % 3 == 2
def bad7(r): return r != 7 and L(r % 7, 7) == -1

cnt = {}
viol1 = viol2 = 0
Am, Ap = [], []
for p in P:
    if p % 8 != 1:
        continue
    n3 = (p + 3) // 4
    f = factorint(n3)
    om = sum(e for r, e in f.items() if bad3(r))
    if (-1) ** om != (1 if p % 3 == 1 else -1):
        viol2 += 1
    if p % 35 == 1:
        if p % 3 == 2:
            Am.append(p)
            if om == 0:
                viol1 += 1
        else:
            Ap.append(p)
print(f"X={X}: |A+|={len(Ap)} |A-|={len(Am)}; A- clean violations={viol1}; parity-identity violations={viol2}")
cleanp = sum(1 for p in Ap if all(not bad3(r) for r in factorint((p + 3) // 4)))
print(f"A+ with n3 clean: {cleanp}")
ds = [1, 5, 11, 17, 23, 29, 5 * 11, 11 * 17, 11 * 23, 17 * 23, 41, 47, 53]
for dd in ds:
    a = sum(1 for p in Ap if ((p + 3) // 4) % dd == 0)
    b = sum(1 for p in Am if ((p + 3) // 4) % dd == 0)
    print(f"  d={dd:4d}: |A+_d|={a:6d} |A-_d|={b:6d}")

# joint version
print("joint classes (p≡1 mod 8, p≡1 mod 5):")
cls = {}
for p in P:
    if p % 8 != 1 or p % 5 != 1 or p in (3, 7):
        continue
    key = (L(p % 3, 3), L(p % 7, 7))
    cls.setdefault(key, []).append(p)
for key, lst in sorted(cls.items()):
    both = 0; d3n7 = 0; viol = 0
    for p in lst:
        n3, n7 = (p + 3) // 4, (p + 7) // 4
        c3 = all(not bad3(r) for r in factorint(n3))
        f7 = factorint(n7)
        c7 = all(not bad7(r) for r in f7)
        om7 = sum(e for r, e in f7.items() if bad7(r))
        if (-1) ** om7 != key[1]:
            viol += 1
        both += c3 and c7
        d3n7 += (n7 % 3 == 0)
    print(f"  {key}: N={len(lst)} both-clean={both} 3|n7: {d3n7}  window-7 parity-identity violations={viol}")
