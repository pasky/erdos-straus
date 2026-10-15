"""O231 UNFORCED_WORDS §3: check Prop F / F' family by family.  For primes p = 1 (8) < HI and s = 1..8, families
t = s (side s p + 1) and u = s (side p + s): count primes where (side unclean) != (family has a certificate) and where
(family has an unforced word) != (family has a certificate).  Prop F (s = 1, 2) and F' (s = 3, 4) predict 0 mismatches.
usage: z7_propF.py HI"""
import sys
from math import isqrt
HI = int(sys.argv[1]); S = 8
M = S * HI + S + 10
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def leg(a, p): return pow(a % p, (p - 1) // 2, p) == 1
def primes_of(x):
    s = set(); d = 2
    while x > M:
        if x % d == 0:
            s.add(d)
            while x % d == 0: x //= d
        d += 1
        if d * d > x:
            if x > 1: s.add(x)
            return s
    while x > 1: s.add(spf[x]); x //= spf[x]
    return s
def divisors(x):
    ds = [1]
    while x > 1:
        r = spf[x]; e = 0
        while x % r == 0: x //= r; e += 1
        ds = [d * r ** k for d in ds for k in range(e + 1)]
    return ds
def clean(x, p): return all(leg(r, p) for r in primes_of(x))
mis = {}
for p in range(17, HI):
    if p % 8 != 1 or spf[p] != p: continue
    for s in range(1, S + 1):
        for kind, N in (('t', s * p + 1), ('u', p + s)):
            words = []
            for D in divisors(N):
                if (D + 1) % s: continue
                if kind == 't': t, u, v = s, (D + 1) // s, (N // D + 1) // s
                else: t, u, v = (D + 1) // s, s, N // D
                words.append((t, u, v))
            cert = any(not leg(t * u - 1, p) for t, u, v in words)
            unf = any(not clean(t * p + 1, p) and not clean(p + u, p) and not clean(p + v, p) for t, u, v in words)
            unc = not clean(N, p)
            k = (kind, s); m = mis.setdefault(k, [0, 0, 0])
            m[0] += (unc != cert); m[1] += (unf != cert); m[2] += unc
for k in sorted(mis): print(k, 'unclean!=cert:', mis[k][0], ' unforced!=cert:', mis[k][1], ' #unclean:', mis[k][2])
