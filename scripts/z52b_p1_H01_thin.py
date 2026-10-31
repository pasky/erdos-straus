"""z52b pass1 H01 (Z0253): do (*)-hard primes cluster on values of low-degree polynomials (thin-set test)?
Input: "p R" lines (scripts/z52b_p1_H01_rzeros.c). Hard = R(p) <= RMAX (p = 1 mod 8, p > 10^5).
Statistic: |p - nearest square| <= K (i.e. p = m^2 + k, |k| <= K: values of the quadratics m^2 + k), compared with all
p = 1 (8) in the same range, by size bins. Usage: thin.py file RMAX"""
import sys, math
import numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64)
RMAX = int(sys.argv[2])
P, R = d[:, 0], d[:, 1]
sel = (P % 8 == 1) & (P > 10**5)
P, R = P[sel], R[sel]
m = np.sqrt(P.astype(float)).round().astype(np.int64)
dist = np.abs(P - m * m)
L = np.log(P.astype(float))
hard = R <= RMAX
print('p=1(8), 1e5<p<=%d: %d primes, hard (R<=%d): %d' % (P.max(), len(P), RMAX, hard.sum()))
for K in (16, 64, 256, 1024):
    base = (dist <= K)
    # size-adjusted expectation: P(dist<=K) ~ (2K+1)/(2 sqrt p) for a prime-like random p (parity aside)
    # size-matched expectation: base rate in the hard prime's log-size bin (bins of width 0.1 in log p)
    b = np.floor(L * 10).astype(int)
    rate = {k: base[b == k].mean() for k in np.unique(b)}
    exp = sum(rate[k] for k in b[hard])
    print('K=%5d: hard count %d, size-matched expected %.1f, ratio %.2f (all-range frac %.4f)' % (
          K, base[hard].sum(), exp, base[hard].sum() / exp, base.mean()))
# also: R/L^2 vs dist bucket
for lo, hi in ((0, 16), (17, 64), (65, 256), (257, 10**9)):
    s = (dist >= lo) & (dist <= hi)
    print('dist in [%d,%d]: n=%d mean R/L^2 %.4f  frac R<=%d %.4f' % (lo, hi, s.sum(), (R[s] / L[s] ** 2).mean(), RMAX,
                                                                  (R[s] <= RMAX).mean()))
