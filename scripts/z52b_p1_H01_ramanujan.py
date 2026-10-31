"""z52b pass1 H01 (Z0389): compare (*) zeros/counts R(p) with Ramanujan's form Q = x^2+y^2+10z^2 at primes p = 7 (mod 8)
(and p = 3 mod 8).  r_Q(n) by theta convolution; R(p) from scripts/z52b_p1_H01_rzeros.c-style pair sieve (all odd n).
Usage: ramanujan.py N   (needs /tmp/rall_N.txt = "n R" for odd n, produced by the --all mode below)"""
import sys, math
import numpy as np
from sympy import primerange
from scipy.stats import spearmanr, hypergeom
N = int(sys.argv[1])
# r_2(n) for x^2+y^2 (ordered, signed)
th = np.zeros(N + 1, dtype=np.int64)
for x in range(-math.isqrt(N), math.isqrt(N) + 1):
    th[x * x] += 1
r2 = np.zeros(N + 1, dtype=np.int64)
for x in range(-math.isqrt(N), math.isqrt(N) + 1):
    r2[x * x:] += th[:N + 1 - x * x]
rQ = np.zeros(N + 1, dtype=np.int64)
for z in range(-math.isqrt(N // 10), math.isqrt(N // 10) + 1):
    rQ[10 * z * z:] += r2[:N + 1 - 10 * z * z]
R = np.loadtxt('/tmp/rall_%d.txt' % N, dtype=np.int64)
Rv = np.zeros(N + 1, dtype=np.int64); Rv[R[:, 0]] = R[:, 1]
for res in (7, 3):
    P = np.array([p for p in primerange(3, N) if p % 8 == res])
    z1 = set(P[rQ[P] == 0].tolist()); z2 = set(P[Rv[P] == 0].tolist())
    print('p=%d (8), p<%d: #p=%d, Q-zeros %s, R-zeros %s, both %s' % (res, N, len(P), sorted(z1), sorted(z2), sorted(z1 & z2)))
    small = P[P < 3000]
    k1 = sum(1 for p in small if p in z1); k2 = sum(1 for p in small if p in z2); kb = sum(1 for p in small if p in z1 & z2)
    if k1 and k2:
        print('  p<3000: %d primes, |Q0|=%d |R0|=%d |both|=%d, hypergeom P(>=both)=%.2e' % (
            len(small), k1, k2, kb, hypergeom.sf(kb - 1, len(small), k1, k2)))
    for lo in (10**3, 10**4):
        s = P[P > lo]
        a = rQ[s] / np.sqrt(s); b = Rv[s] / np.log(s) ** 2
        print('  p>%d: spearman(rQ/sqrt p, R/log^2 p) = %.3f (n=%d)' % (lo, spearmanr(a, b)[0], len(s)))
