"""R82: check that the MN3 atom coordinates obey ElsholtzTao's Type I bounds (Lemma 2.8, 4 -> m),
so that ET's 3/5 device applies to R(N):  c <= 2aN/3 (m>=4),  e*f*(cd)^2*(ac) <= (10/3) N^3,
hence min(e, f, cd, ac) <= ((10/3)N^3)^{1/5}. Also verifies m/N = 1/(abdN)+1/(acd)+1/(bcd).
Enumeration via (a,d,f|P,c) as in review_mn3_rn.py, all N <= X.
Usage: review_mn3_et35.py m X
"""
import sys
from math import gcd
from fractions import Fraction
import sympy

m, X = int(sys.argv[1]), int(sys.argv[2])
sqf = lambda n: all(k == 1 for k in sympy.factorint(n).values())
worst = 0.0; worst_min = 0.0; cnt = 0; bad = 0
for a in range(1, X + 1):
    for d in range(1, X // a + 1):
        if not sqf(d): continue
        P = m * a * a * d + 1
        divs = sympy.divisors(P)
        for c in range(1, X // (a * d) + 1):
            for f in divs:
                N = m * a * c * d - f
                if N < a * c * d or N > X: continue
                e = P // f; b = c * e - a
                if b < a or gcd(e * N, P) != e: continue
                cnt += 1
                if 3 * c > 2 * a * N: bad += 1
                if Fraction(m, N) != Fraction(1, a*b*d*N) + Fraction(1, a*c*d) + Fraction(1, b*c*d): bad += 1
                prod = e * f * (c * d) ** 2 * a * c
                worst = max(worst, prod / N ** 3)
                worst_min = max(worst_min, min(e, f, c * d, a * c) / N ** 0.6)
print(f"m={m} X={X}: atoms={cnt}, violations={bad}, max e f (cd)^2 ac / N^3 = {worst:.4f} (<= 10/3), "
      f"max min(e,f,cd,ac)/N^0.6 = {worst_min:.4f}")
