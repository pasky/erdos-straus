"""R32: independent a_min census for the POINTWISE_XWIN §1.3 table.
a_min(p) = min{a≡3 (4): p∤x_a, Rat_a(x_a) ∩ {−1,−p} ≠ ∅}, x_a=(p+a)/4, primes p≡1 (24), p<X.
Rat_a(x)={u/v mod a: uv|x, gcd(u,v)=1} by full enumeration.  Prints T(X,Z) and the
normalisation T/(X/(log X)^{1+J/2})."""
import sys
from math import log
import numpy as np

ZS = (3, 7, 11, 15, 19, 23)

def spf_table(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx.astype(np.int32)
    return spf

def factor(x, spf):
    f = {}
    while x > 1:
        r = int(spf[x])
        e = 0
        while x % r == 0:
            x //= r; e += 1
        f[r] = e
    return f

def rat(fx, a):
    vals = {1 % a}
    for r, e in fx.items():
        rm = r % a
        ri = pow(rm, -1, a)
        mults = [1] + [pow(rm, i, a) for i in range(1, e + 1)] + [pow(ri, i, a) for i in range(1, e + 1)]
        vals = {v * m % a for v in vals for m in mults}
    return vals

def main(X):
    amax_guess = 400
    spf = spf_table((X + amax_guess) // 4 + 10)
    isprime = np.ones(X + 1, dtype=bool); isprime[:2] = False
    for i in range(2, int(X ** 0.5) + 1):
        if isprime[i]:
            isprime[i * i::i] = False
    T = {Z: 0 for Z in ZS}
    for p in range(25, X, 24):
        if not isprime[p]:
            continue
        a = 3
        while True:
            x = (p + a) // 4
            assert x < len(spf), (p, a)
            if x % p != 0:
                R = rat(factor(x, spf), a)
                if (a - 1) in R or (-p) % a in R:
                    break
            a += 4
        for Z in ZS:
            if a > Z:
                T[Z] += 1
    L = log(X)
    print(X, " ".join("Z=%d:%d(%.3f)" % (Z, T[Z], T[Z] / (X / L ** (1 + ((Z + 1) // 4) / 2))) for Z in ZS))

if __name__ == "__main__":
    for X in map(int, sys.argv[1:]):
        main(X)
