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

# Exact evaluation at q = ζ₈ in ℤ[ζ]/(ζ⁴+1) with projective (num:den) recursion (triage fix: float poles).
def _mul(a, b):
    r = [0]*4
    for i in range(4):
        for j in range(4):
            k = i + j
            if k < 4: r[k] += a[i]*b[j]
            else: r[k-4] -= a[i]*b[j]
    return r
def _add(a, b): return [x+y for x, y in zip(a, b)]
def _zpow(e):  # ζ^e, e any int
    e %= 8; r = [0]*4
    if e < 4: r[e] = 1
    else: r[e-4] = -1
    return r
def _qint(a, s):  # [a]_{ζ^s} = Σ_{k<a} ζ^{sk}
    r = [0]*4
    for k in range(a): r = _add(r, _zpow(s*k))
    return r
def mgo_zeta8_exact(seq):
    """Returns complex value of [seq]_{ζ₈}, or raises ZeroDivisionError at an exact pole."""
    n = len(seq); s = 1 if (n - 1) % 2 == 0 else -1   # q-orientation of the last level
    num, den = _qint(seq[-1], s), [1, 0, 0, 0]
    for i in range(n - 2, -1, -1):
        s = 1 if i % 2 == 0 else -1
        num, den = _add(_mul(_qint(seq[i], s), num), _mul(_zpow(s*seq[i]), den)), num
    if not any(den): raise ZeroDivisionError
    z = cmath.exp(1j*math.pi/4)
    ev = lambda v: sum(c*z**k for k, c in enumerate(v))
    return ev(num)/ev(den)
