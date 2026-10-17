"""R264 from-scratch check of FORCED_WINDOW Thm 4.3 mechanics at y = 7 (S = {3,5,7}, P = 105).
For p ≡ 1 (8) prime ≤ PMAX (optionally only Mordell-hard classes mod 840), every prime q ≤ QMAX with q ≡ 3 (8),
q ≡ -p (mod 105), (q/p) = -1: compute L_min(q) (cube covering of U_q by s^2, s ∈ S), then the Lemma-1.1 certificate
using ONLY s ∈ S (j_s = 0 elsewhere) hitting t = -c, with sides j_s ≤ L_min; check its cap ≤ L_min - 1, and rebuild the
ES^{(y,e)} solution with exact rationals.
Usage: python review_r264_thm43.py PMAX QMAX hardonly(0/1)
"""
import sys
from fractions import Fraction
from itertools import product
from math import isqrt

PMAX, QMAX, HARD = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
S = [3, 5, 7]
PP = 105


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def leg(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


Lmin_cache = {}


def Lmin(q):
    if q in Lmin_cache:
        return Lmin_cache[q]
    n = (q - 1) // 2
    L = 0
    while True:
        W = {1}
        for s in S:
            g = s * s % q
            W = {w * pow(g, j, q) % q for w in W for j in range(L + 1)}
        if len(W) == n:
            Lmin_cache[q] = L
            return L
        L += 1
        if L > n:
            Lmin_cache[q] = None
            return None


qs = [q for q in range(3, QMAX + 1, 8) if isprime(q) and PP % q]
npairs = 0
maxcap = 0
for p in range(9, PMAX + 1, 8):
    if not isprime(p):
        continue
    if HARD and p % 840 not in (1, 121, 169, 289, 361, 529):
        continue
    for q in qs:
        if (q + p) % PP or leg(q, p) != -1:
            continue
        L = Lmin(q)
        if L is None:
            continue
        K = (p + q) // 4
        f = factor(K)
        assert K % 2 == 1 and all(K % s == 0 for s in S)
        O = [s for s in f if f[s] % 2]
        c = 1
        for s in O:
            c *= s
        t = (-c) % q
        hit = None
        for j in product(range(L + 1), repeat=3):
            v = 1
            for s, jj in zip(S, j):
                v = v * pow(s, 2 * jj, q) % q
            if v == t:
                hit = j
                break
        assert hit is not None, (p, q, L)
        jd = dict(zip(S, hit))
        delta = {s: -(1 if s in O else 0) + 2 * jd.get(s, 0) for s in f}
        cap = 0
        for s in f:
            b, ds = f[s], delta[s]
            if ds > b:
                assert (ds - b) % 2 == 0
                cap = max(cap, (ds - b) // 2)
            else:
                assert ds >= -b
        assert cap <= L - 1 or (L == 0 and cap == 0), (p, q, L, cap)
        d = Fraction(K)
        for s in f:
            d *= Fraction(s) ** delta[s]
        d = int(d)
        assert (K + d) % q == 0
        A = (K + d) // q
        z = Fraction(p * K * A, d)
        assert Fraction(4, p) == Fraction(1, K) + Fraction(1, p * A) + 1 / z
        r = isqrt(z.denominator)
        assert r * r == z.denominator and r % 2 == 1
        npairs += 1
        maxcap = max(maxcap, cap)
print(f"Thm 4.3 mechanics (y=7): {npairs} (p, q) pairs, p ≤ {PMAX}{' hard' if HARD else ''}, q ≤ {QMAX}; all certificates "
      f"have cap ≤ L_min(q) - 1 and exact ES rebuild; max cap {maxcap}")
