"""z64 EQUIV: which odd n admit 4/n - 1 as the orbifold Euler characteristic of a closed orientable
2-orbifold S^2(m_1..m_r) with r = 4 or 5 cone points (m_i >= 2), other than via the (2,2,a,b) family
(which is the two-term equation 4/n = 1/a + 1/b)?  Exact rational enumeration (Fractions).
r=4: 1/m1+1/m2+1/m3+1/m4 = 1 + 4/n ; r=5: sum_5 1/m_i = 2 + 4/n.  Prints sporadic n (not via (2,2,.,.)).
Usage: python z64_equiv_orbifold.py NMAX"""
import sys
from fractions import Fraction as F
from math import gcd
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
spor4 = {}
# r = 4, m1<=m2<=m3<=m4, (m1,m2) != (2,2).  Sum > 1 forces m1<=3, and 1/m1+3/m2>1.
for m1 in (2, 3):
    for m2 in range(m1, 12):
        if F(1, m1) + F(3, m2) <= 1: continue
        if (m1, m2) == (2, 2): continue
        for m3 in range(m2, 10**4):
            rest = F(1, m1) + F(1, m2) + F(1, m3)
            if rest + F(1, m3) <= 1: break
            # 1/m4 = 1 + 4/n - rest, m4 >= m3  -> 4/n = 1/m4 + rest - 1
            for m4 in range(m3, 10**5):
                s = rest + F(1, m4) - 1
                if s <= 0: break
                if s.numerator == 4 or (4 % s.numerator == 0):
                    n = F(4) / s
                    if n.denominator == 1 and n.numerator % 2 == 1 and n.numerator <= NMAX:
                        spor4.setdefault(int(n), []).append((m1, m2, m3, m4))
spor5 = {}
for m1 in (2,):
    for m2 in (2,):
        for m3 in (2,):
            for m4 in range(2, 7):
                for m5 in range(m4, 10**5):
                    s = F(3, 2) + F(1, m4) + F(1, m5) - 2
                    if s <= 0: break
                    n = F(4) / s
                    if n.denominator == 1 and n.numerator % 2 == 1 and n.numerator <= NMAX:
                        spor5.setdefault(int(n), []).append((2, 2, 2, m4, m5))
for m3 in range(2, 4):  # (2,2,m3,m4,m5) with m3>=3 handled: sum<=1+1/3*3=2 -> need care
    pass
# general r=5 brute force small: m_i>=2, sum_5 > 2 forces at least two 2's; enumerate fully
for m1 in (2,):
    for m2 in (2, 3):
        for m3 in range(m2, 7):
            for m4 in range(m3, 13):
                base = F(1, m1) + F(1, m2) + F(1, m3) + F(1, m4)
                if base + F(1, m4) <= 2: continue
                for m5 in range(m4, 10**5):
                    s = base + F(1, m5) - 2
                    if s <= 0: break
                    n = F(4) / s
                    if n.denominator == 1 and n.numerator % 2 == 1 and n.numerator <= NMAX:
                        t = (m1, m2, m3, m4, m5)
                        if t not in spor5.get(int(n), []):
                            spor5.setdefault(int(n), []).append(t)
print("r=4 sporadic odd n (not (2,2,a,b)):", sorted(spor4))
for n in sorted(spor4): print(" ", n, spor4[n][:4])
print("r=5 odd n:", sorted(spor5))
for n in sorted(spor5): print(" ", n, spor5[n][:4])
