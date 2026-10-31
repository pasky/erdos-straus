"""U01 Z1944: 4-term rescue. For prime p<=PMAX, minimal max(x,y,z) over x<=y<=z with 4/p-1/x-1/y-1/z = 1/w, w<=p^3,
compared with R(p) = minimal max denominator of a 3-term ES solution (from allsols data)."""
import sys, os, gzip, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from z52b_p1_U01_common import primes_upto, REPO
def spf_sieve(N):
    s = np.zeros(N+1, dtype=np.int64)
    for i in range(2, int(N**0.5)+1):
        if s[i] == 0:
            idx = np.arange(i*i, N+1, i); m = s[idx] == 0; s[idx[m]] = i
    ar = np.arange(N+1); z = s == 0; s[z] = ar[z]
    return s
def factor(n, spf):
    f = {}; d = 2
    if n < len(spf):
        while n > 1:
            q = int(spf[n]); e = 0
            while n % q == 0: n //= q; e += 1
            f[q] = e
        return f
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def all_two_term(A, B, spf):
    f = factor(B, spf); ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(2*e+1)]
    out = []
    for d in ds:
        if (d + B) % A == 0:
            a = (d + B)//A; e2 = B*B//d
            if (e2 + B) % A == 0:
                b = (e2 + B)//A
                if 0 < a <= b: out.append((a, b))
    return out
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300
spf = spf_sieve(int(PMAX*PMAX*2)+10)
R = {}
for line in gzip.open(os.path.join(REPO, "data/z52b/pass1/U01/allsols_5000.txt.gz"), "rt"):
    if line.startswith("#"): continue
    t = line.split()
    if int(t[1]) > 0: R[int(t[0])] = float(t[2])*int(t[0])
res = []
for p in primes_upto(PMAX):
    if p < 5: continue
    best = None
    for x in range(-(-p//4), p+1):
        r1 = Fr(4, p) - Fr(1, x)
        if r1 <= 0: continue
        for y in range(x, 4*p+1):
            r2 = r1 - Fr(1, y)
            if r2 <= 0: continue
            if best is not None and y >= best: break
            # need 1/z + 1/w = r2 with z>=y, w<=p^3, and z = max? (x,y,z) max is z
            A, B = r2.numerator, r2.denominator
            for z, w in all_two_term(A, B, spf):
                if z >= y and w <= p**3:
                    cand = z
                    if best is None or cand < best: best = cand
                    break
    res.append((p, best, R.get(p)))
print("p, min max(x,y,z) for 4-term rescue (w<=p^3), R(p) min-max 3-term:")
for r in res[:15]: print(r)
ratio = [(r[1]/r[2]) for r in res if r[1] and r[2]]
print("n=%d, median ratio rescue/R(p) = %.3f, max = %.2f" % (len(ratio), sorted(ratio)[len(ratio)//2], max(ratio)))
