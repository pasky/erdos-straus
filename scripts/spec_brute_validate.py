"""O123: brute-force validation of spec_typecount.c for small primes.
Counts Type I / Type II solutions (x,y,z) of 4/n = 1/x+1/y+1/z with y <= z
(Type I: n|x, n∤y, n∤z; Type II: n∤x, n|y, n|z)."""
import sys, numpy as np
from fractions import Fraction
from sympy import isprime

def sols(n):
    out = set()
    for u in range(n // 4 + 1, 3 * n // 4 + 2):
        r1 = Fraction(4, n) - Fraction(1, u)
        if r1 <= 0: continue
        vlo = max(u, int(1 / r1))
        for v in range(vlo, int(2 / r1) + 2):
            r2 = r1 - Fraction(1, v)
            if r2 <= 0: continue
            if r2.numerator == 1 and r2.denominator >= v:
                out.add((u, v, r2.denominator))
    return out

def counts(n):
    I = set(); II = set()
    for t in sols(n):
        for i in range(3):
            x = t[i]; y, z = sorted(t[:i] + t[i+1:])
            if x % n == 0 and y % n and z % n: I.add((x, y, z))
            if x % n and y % n == 0 and z % n == 0: II.add((x, y, z))
    return len(I), len(II)

N = int(sys.argv[1]); pre = sys.argv[2]
FI = np.fromfile(pre + ".FI.bin", dtype=np.uint32)
FII = np.fromfile(pre + ".FII.bin", dtype=np.uint32)
bad = 0
for p in range(3, N + 1):
    if not isprime(p): continue
    cI, cII = counts(p)
    if (cI, cII) != (FI[p], FII[p]):
        bad += 1; print("MISMATCH", p, cI, cII, FI[p], FII[p])
print("checked primes <=", N, "mismatches", bad)
