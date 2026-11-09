#!/usr/bin/env python3
"""z69 IDEAB sanity check for ideas I1/I18 (uniform covering in the 'pseudosquare corridor').
For n == 1 (mod 840) and n == r (mod q) (r a non-residue mod q): least modulus of an identity class
(K1: -e mod 4ab, e|a+b;  K2: -4a^2 d mod 4k-1, ad|k;  K3: -f mod 4ad, f|4a^2d+1) containing n.
UC for the class predicts: bounded, independent of the range of n.
usage: corridor.py q T MMAX"""
import sys, math
import numpy as np
from collections import defaultdict
q = int(sys.argv[1]); T = int(sys.argv[2]); MMAX = int(sys.argv[3])
cls = defaultdict(set)
def divs(n): return [d for d in range(1, n + 1) if n % d == 0]
for a in range(1, MMAX // 4 + 1):                       # K1
    for b in range(a, MMAX // (4 * a) + 1):
        for e in divs(a + b):
            if e % 4 == 3: cls[4 * a * b].add((-e) % (4 * a * b))
for k in range(1, (MMAX + 1) // 4 + 1):                 # K2
    u = 4 * k - 1
    for a in divs(k):
        for d in divs(k // a): cls[u].add((-4 * a * a * d) % u)
for a in range(1, MMAX // 4 + 1):                       # K3
    for d in range(1, MMAX // (4 * a) + 1):
        N = 4 * a * a * d + 1; M = 4 * a * d
        f = 3
        # divisors f == 3 mod 4 of N
        for f in range(3, int(math.isqrt(N)) + 1, 2):
            if N % f == 0:
                for g in (f, N // f):
                    if g % 4 == 3: cls[M].add((-g) % M)
mods = sorted(cls)
print(f"q={q} T={T} MMAX={MMAX}: {len(mods)} moduli, {sum(len(v) for v in cls.values())} classes")
nr = [r for r in range(1, q) if pow(r, (q - 1) // 2, q) == q - 1]
def crt(r):  # n == 1 mod 840, n == r mod q
    for t in range(q):
        if (1 + 840 * t) % q == r: return 1 + 840 * t
for r in nr + [1]:
    n0 = crt(r); n = n0 + 840 * q * np.arange(0, T, dtype=np.int64)
    if r == 1:   # control: square class; drop perfect squares
        s = np.rint(np.sqrt(n.astype(np.float64))).astype(np.int64); n = n[s * s != n]
    n = n[n > 1]
    best = np.zeros(len(n), dtype=np.int64); idx = np.arange(len(n))
    for M in mods:
        if len(idx) == 0: break
        hit = np.isin(n[idx] % M, np.fromiter(cls[M], dtype=np.int64))
        best[idx[hit]] = M; idx = idx[~hit]
    out = []
    for cut in (10**2, 10**3, 10**4, 10**5, 10**6):
        if cut <= len(n) * 10:
            b = best[:cut]; un = int((b == 0).sum()); mx = int(b.max())
            out.append(f"first {min(cut,len(n))}: max={mx} unresolved={un}")
    vals, cnts = np.unique(best, return_counts=True)
    top = sorted(zip(cnts, vals), reverse=True)[:6]
    print(f" r={r}{' (control, square class)' if r==1 else ''}: " + " | ".join(out))
    print("     most frequent least moduli (count,mod):", [(int(c), int(v)) for c, v in top], " #distinct:", len(vals))
