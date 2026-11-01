# Core of scripts/z52d_p2_NC3_mgo.py (MGO q-rationals), importable without side effects.
# Z2783: Morier-Genoud–Ovsienko q-rationals [a1,...,an]_q of the regular CF of A/p (or p/A), evaluated at q = i and
# q = e^{i pi/4}; sanity q->1 gives the rational. Test: phase / sign pattern vs Legendre (A/p) on words (p = 1 (8), p<=300).
import sys, cmath, math
from fractions import Fraction
def qint(a, q):
    return sum(q**k for k in range(a))
def mgo(seq, q):
    # [a1,...,an]_q = [a1]_q + q^{a1} / ( [a2]_{q^-1} + q^{-a2} / ( [a3]_q + ... ) )
    def rec(i, qq):
        if i == len(seq) - 1:
            return qint(seq[i], qq)
        return qint(seq[i], qq) + qq**seq[i] / rec(i+1, 1/qq)
    return rec(0, q)
def regcf(p, a):
    out = []; x, y = p, a
    while y:
        out.append(x // y); x, y = y, x % y
    return out
