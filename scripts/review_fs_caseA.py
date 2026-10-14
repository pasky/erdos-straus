#!/usr/bin/env python3
"""R217 from-scratch Case A mass for (Sigma) (FF_STERILE_PUSH Lemma 2.2), q = 3^r, k = 2, exact rationals.
Datum (a1', b1, K, F) monic (a1', b1 prime to T; T | K); pattern (alpha; lam, beta, kap), f = alpha - beta - kap >= 0,
kap >= 1, zeta = max(beta, f) - lam >= 1. Relative mass per datum q^{-alpha}. Route bounds (re-derived in the review):
  (i) a1', b1, K          (ii) a1', K, F -> b1      (iii) b1, K; E | T^a + b1^2 K, E = -1 mod b1 K   [L1.4 / L1.5]
  (iv) a1', b1; E | T^a a1' + b1, E = -1 mod T a1' b1  [L1.4 / L1.5]   (v) z, ordered (b1, K, F) | T^a + z
  (vi) a1', z, K; quadratic.
Unlike fs_caseA.py, the class count here also allows Lemma 1.5 (E-version only), so it can only be smaller; we print both
the Lemma-1.4-only value and the 1.4+1.5 value. Tail alpha > AMAX: DEPTH_ASPECT Lemma 2.4 majorant
(alpha+1)^3 4 2^alpha 3^alpha q^{floor((alpha-1)/2) - alpha}, summed by a geometric series with exact rational ratio bound.
usage: review_fs_caseA.py r[,r..] [AMAX=40]"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial

def jcop(n, d, rho, JMAX=60):
    X = d - rho
    if X < 0: return 1
    if n * X >= d * d: return 0
    for j in range(1, JMAX + 1):
        for m in range(1, j + 1):
            if n * m * (m + 1) + X * j * (j + 1) < 2 * (j + 1) * m * d:
                return j
    return 0

def cls(n, d, rho, cop):
    if d < rho or n - d < rho: return 1
    c = 2 if 3 * rho > n else 0
    if cop:
        j = jcop(n, d, rho)
        if j and (not c or j < c): c = j
    b = comb(n, d)
    return min(b, c) if c else b

def mass(r, AMAX, cop):
    q = 3**r
    Ns = lambda d: 1 if d == 0 else q**d - q**(d - 1)
    tot = Fr(0)
    for al in range(1, AMAX + 1):
        acc = 0
        for be in range(0, al + 1):
            for ka in range(1, al - be + 1):
                f = al - be - ka
                for la in range(0, al + 1):
                    ze = max(be, f) - la
                    if ze < 1: continue
                    n3 = max(al, 2 * be + ka)
                    acc += min(Ns(la) * Ns(be) * q**(ka - 1),
                               Ns(la) * q**(ka - 1) * q**f,
                               Ns(be) * q**(ka - 1) * cls(n3, la + be + ka, be + ka, cop),
                               Ns(la) * Ns(be) * cls(al + la, la + be + ka, la + be + 1, cop),
                               q**ze * factorial(al) // (factorial(be) * factorial(ka) * factorial(f)),
                               2 * Ns(la) * q**ze * q**(ka - 1))
        tot += Fr(acc, q**al)
    # tail: term(al) <= (al+1)^3 * 4 * 6^al * q^{-(al+1)/2}; ratio <= ((a0+2)/(a0+1))^3 * 6 / sqrt(q), bound sqrt(q) below
    a0 = AMAX + 1
    sq = 3**(r // 2)                     # <= sqrt(q)
    ratio = Fr(a0 + 2, a0 + 1)**3 * Fr(6, sq)
    assert ratio < 1
    first = Fr((a0 + 1)**3 * 4 * 6**a0) / Fr(sq)**(a0 + 1)
    tail = first / (1 - ratio)
    return tot, tail

if __name__ == '__main__':
    AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    for r in [int(x) for x in sys.argv[1].split(',')]:
        t14, tail = mass(r, AMAX, False)
        t15, _ = mass(r, AMAX, True)
        print(f'r={r} AMAX={AMAX} caseA(L1.4 only)={float(t14):.10e} caseA(L1.4+1.5)={float(t15):.10e} tail<={float(tail):.4e} '
              f'total(L1.4 only)<={float(t14 + tail) * (1 + 1e-12):.10e}', flush=True)
