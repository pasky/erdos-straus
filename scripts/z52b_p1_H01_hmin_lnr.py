"""z52b pass1 H01 (Z0379/Z0230): least Type II modulus h_min(p) (as in scripts/s3_min_scale.py) versus the least
prime quadratic non-residue l(p), primes p = 1 (mod 4) below N. Prints h_min statistics per l(p) bucket and the best
fit exponent kappa for max h_min <= c * l^kappa. Usage: z52b_p1_H01_hmin_lnr.py N"""
import sys
import numpy as np
from sympy import primerange, divisors
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
P = np.array([p for p in primerange(5, N) if p % 4 == 1], dtype=np.int64)
hmin = np.zeros(len(P), dtype=np.int64)
left = np.arange(len(P))
h = 3
while len(left) and h < 4 * N:
    k = (h + 1) // 4
    pairs = [(c, d) for c in divisors(k) for d in divisors(k // c)]
    pl = P[left]
    hit = np.zeros(len(left), dtype=bool)
    for c, d in pairs:
        hit |= ((pl + 4 * c * c * d) % h) == 0
    hmin[left[hit]] = h
    left = left[~hit]
    h += 4
assert len(left) == 0
# least prime non-residue via Euler criterion, vectorised
lnr = np.zeros(len(P), dtype=np.int64)
und = np.arange(len(P))
for q in primerange(2, 2000):
    pl = P[und]
    if q == 2:
        nr = (pl % 8 == 3) | (pl % 8 == 5)
    else:
        e = [pow(int(q), int((p - 1) // 2), int(p)) for p in pl]
        nr = np.array([x == p - 1 for x, p in zip(e, pl)], dtype=bool)
    lnr[und[nr]] = q
    und = und[~nr]
    if not len(und):
        break
assert len(und) == 0
lp = np.log(P.astype(float))
print('N=%d  #p=%d' % (N, len(P)))
print('lnr  #p   min_hmin mean_hmin  median  p99  max  (max/log^3p)')
for q in sorted(set(lnr.tolist())):
    m = lnr == q
    a = hmin[m]
    print('%4d %6d %6d %8.1f %6d %6d %6d %.3f' % (q, m.sum(), a.min(), a.mean(), np.median(a), np.percentile(a, 99), a.max(),
                                            (a / lp[m] ** 3).max()))
m8 = lnr >= 3
print('p=1 mod 8 only: frac hmin>=lnr = %.4f; corr(log hmin, log lnr) = %.3f' % ((hmin[m8] >= lnr[m8]).mean(), np.corrcoef(np.log(hmin[m8]), np.log(lnr[m8]))[0, 1]))
r8 = hmin[m8] / lnr[m8].astype(float)
print('p=1 mod 8: max hmin/lnr = %.1f, max hmin/lnr^2 = %.2f' % (r8.max(), (hmin[m8] / lnr[m8].astype(float) ** 2).max()))
print('corr(log hmin, log lnr) = %.3f' % np.corrcoef(np.log(hmin), np.log(lnr))[0, 1])
for kap in (1, 2, 3):
    r = hmin / lnr.astype(float) ** kap
    print('kappa=%d: max hmin/lnr^k = %.2f at p=%d (hmin=%d lnr=%d)' % (kap, r.max(), P[r.argmax()], hmin[r.argmax()],
                                                                     lnr[r.argmax()]))
np.savez_compressed('data/z52b/pass1/H01/hmin_lnr_%d.npz' % N, P=P, hmin=hmin, lnr=lnr)
