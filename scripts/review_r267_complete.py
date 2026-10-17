"""R267 from-scratch check of the complete-level dictionary (NONCONG_LIFTS §2.4).

L (k | L) is complete if every non-square unit class r mod L lies in a witness class of some slice (θ, a, b, c)
with H = k*a*b | L:  II: r ≡ -e (mod H);  I: r*e ≡ -1 (mod H);  e = (a+b)/c.
Also asserts T1 (no square unit class is ever covered).
Usage: review_r267_complete.py k Lmax [smooth7only]
"""
import sys
from math import gcd
import numpy as np


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return sorted(ds)


_cache = {}


def covered_mod_H(k, H):
    """residues mod H (as frozenset) covered by slices with k*a*b == H exactly."""
    if (k, H) in _cache:
        return _cache[(k, H)]
    S = set()
    if H % k == 0:
        ab = H // k
        for a in divisors(ab):
            b = ab // a
            s = a + b
            for c in divisors(s):
                e = s // c
                S.add((-e) % H)
                if gcd(e, H) == 1:
                    S.add((-pow(e, -1, H)) % H)
    _cache[(k, H)] = S
    return S


def analyse(k, L):
    r = np.arange(L)
    unit = np.gcd(r, L) == 1
    sq = np.zeros(L, bool)
    sq[(r[unit] * r[unit]) % L] = True
    cov = np.zeros(L, bool)
    for H in divisors(L):
        S = covered_mod_H(k, H)
        if S:
            cov |= np.isin(r % H, np.fromiter(S, int))
    bad_sq = int((cov & sq & unit).sum())
    deficit = int((unit & ~sq & ~cov).sum())
    return deficit, bad_sq


def smooth7(n):
    for p in (2, 3, 5, 7):
        while n % p == 0:
            n //= p
    return n == 1


def rule(L):
    return (L % 3 != 0 or L % 8 == 0) and (L % 7 != 0 or L % 24 == 0)


if __name__ == "__main__":
    k = int(sys.argv[1]); Lmax = int(sys.argv[2]); only7 = len(sys.argv) > 3
    complete = []
    totbad = 0
    for L in range(k, Lmax + 1, k):
        if only7 and not smooth7(L):
            continue
        d, b = analyse(k, L)
        totbad += b
        if d == 0:
            complete.append(L)
        if k == 4 and smooth7(L) and (d == 0) != rule(L):
            print("RULE VIOLATION", L, d)
    print(f"k={k} Lmax={Lmax} only7={only7} T1-violations={totbad}")
    print("complete:", complete)
    print("non-7-smooth complete:", [L for L in complete if not smooth7(L)])
