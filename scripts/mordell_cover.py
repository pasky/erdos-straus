"""Level-wise covering search for Sigma_r by ES polynomial classes (task O80).

usage: mordell_cover.py r variant Mmax stages
  variant: 'main' (p=1 mod 24, square mod 5 and 7, non-residue mod r)
           'np'   (additionally a non-zero square mod every prime 5<=l<r)
  stages:  comma list of prime powers multiplied into L one by one, e.g. 2,3,11,17,13,5,7
Base L0 = 8*3*5*7*r (and the primes <r for 'np').  At each stage the uncovered
unit residues mod L are filtered by every class modulus M | L, M <= Mmax.
Prints the number and Haar fraction of uncovered residues after each stage.
"""
import sys
import numpy as np
from math import gcd
from mordell_lib import residue_table, divisors

def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** .5) + 1))]

def is_sq(x, l):
    return pow(x % l, (l - 1) // 2, l) == 1

def base(r, variant):
    mods = [8, 3, 5, 7, r]
    if variant == 'np':
        mods = [8, 3] + [l for l in primes_upto(r) if l >= 5]
    L = 1
    for m in mods:
        L *= m
    X = []
    for x in range(1, L, 2):
        if x % 8 != 1 or x % 3 != 1:
            continue
        ok = True
        for l in mods[2:]:
            if l == r:
                ok = ok and x % r != 0 and not is_sq(x, r)
            elif l in (5, 7) or variant == 'np':
                ok = ok and x % l != 0 and is_sq(x, l)
        if ok:
            X.append(x)
    return L, np.array(X, dtype=np.int64)

TABLE = {}
def table(M):
    if M not in TABLE:
        w = residue_table(M)
        a = np.zeros(M, dtype=bool)
        if w:
            a[list(w)] = True
        TABLE[M] = (a, w)
    return TABLE[M]

def filt(X, L, Lprev, Mmax):
    for M in divisors(L):
        if M > Mmax or Lprev % M == 0 or M < 3:
            continue
        a, w = table(M)
        if not w:
            continue
        X = X[~a[X % M]]
        if len(X) == 0:
            break
    return X

def refine(X, L, q):
    """multiply modulus by q (prime power); keep only lifts that are units mod q's prime."""
    p = min(d for d in range(2, q + 1) if q % d == 0)
    L2 = L * q // gcd(L, q) if L % p else L * p
    t = np.arange(L2 // L, dtype=np.int64)
    Y = (X[:, None] + L * t[None, :]).ravel()
    Y = Y[Y % p != 0]
    return Y, L2

def main():
    r = int(sys.argv[1]); variant = sys.argv[2]; Mmax = int(sys.argv[3])
    stages = [int(s) for s in sys.argv[4].split(',')] if len(sys.argv) > 4 and sys.argv[4] else []
    L, X = base(r, variant)
    n0 = len(X); L0 = L
    X = filt(X, L, 1, Mmax)
    print(f"L={L} uncovered {len(X)}/{n0} frac={len(X)/n0:.5f}", flush=True)
    for q in stages:
        Lprev = L
        X, L = refine(X, L, q)
        # Haar normalisation: fraction of Sigma uncovered
        X = filt(X, L, Lprev, Mmax)
        p = min(d for d in range(2, q + 1) if q % d == 0)
        # count of lifts of a Sigma-residue mod L0 to mod L
        lifts = 1
        for l, e in [(l, 0) for l in []]:
            pass
        print(f"+{p}: L={L} uncovered {len(X)}", flush=True)
        if len(X) == 0:
            print("COVERED"); break
    if len(X):
        print("sample uncovered:", X[:10].tolist())
        fac = [l for l in (16, 9, 25, 49, 121, 169, 11, 13, 17, 19, 23, 29, 31, 37) if L % l == 0 and not (l in (11,13) and L % (l*l) == 0)]
        from collections import Counter
        pats = Counter(tuple(int(x % l) for l in fac) for x in X)
        print("moduli", fac)
        for pat, c in sorted(pats.items())[:60]:
            print(c, pat)

if __name__ == '__main__':
    main()
