"""z52b pass1 H01 (Z0389): is the positive correlation between r_Q(p)/sqrt p (Q = x^2+y^2+10z^2) and R(p)/log^2 p at
p = 7 (8) explained by small-prime Legendre symbols? Regress both on the symbols (q/p), q <= QMAX (one-hot), correlate residuals.
Usage: ramanujan_partial.py N QMAX  (needs /tmp/rall_N.txt as in z52b_p1_H01_ramanujan.py)"""
import sys, math
import numpy as np
from sympy import primerange, legendre_symbol
from scipy.stats import spearmanr, pearsonr
N, QMAX = int(sys.argv[1]), int(sys.argv[2])
th = np.zeros(N + 1, dtype=np.int64)
for x in range(-math.isqrt(N), math.isqrt(N) + 1): th[x * x] += 1
r2 = np.zeros(N + 1, dtype=np.int64)
for x in range(-math.isqrt(N), math.isqrt(N) + 1): r2[x * x:] += th[:N + 1 - x * x]
rQ = np.zeros(N + 1, dtype=np.int64)
for z in range(-math.isqrt(N // 10), math.isqrt(N // 10) + 1): rQ[10 * z * z:] += r2[:N + 1 - 10 * z * z]
R = np.loadtxt('/tmp/rall_%d.txt' % N, dtype=np.int64); Rv = np.zeros(N + 1, dtype=np.int64); Rv[R[:, 0]] = R[:, 1]
for res in (7, 3):
    P = np.array([p for p in primerange(10**4, N) if p % 8 == res])
    a = rQ[P] / np.sqrt(P); b = Rv[P] / np.log(P) ** 2
    X = np.array([[legendre_symbol(q, int(p)) for q in primerange(3, QMAX + 1)] + [1] for p in P], dtype=float)
    ra = a - X @ np.linalg.lstsq(X, a, rcond=None)[0]; rb = b - X @ np.linalg.lstsq(X, b, rcond=None)[0]
    R2a = 1 - ra.var() / a.var(); R2b = 1 - rb.var() / b.var()
    print('p=%d(8) n=%d: raw pearson %.3f spearman %.3f | symbols q<=%d explain R2(rQ)=%.2f R2(R)=%.2f | residual pearson %.3f spearman %.3f' % (
        res, len(P), pearsonr(a, b)[0], spearmanr(a, b)[0], QMAX, R2a, R2b, pearsonr(ra, rb)[0], spearmanr(ra, rb)[0]))
