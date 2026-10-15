# R225 independent re-analysis of NEAR_SQUARE §5 from census rows (p N Nm NT NTm q minK Ncl Nclm Nu).
# Within-cell residuals (cell = p mod 8, Legendre (r/p) for odd primes r <= RMAX, least non-residue q capped),
# K0 = p - isqrt(p)^2 bins; sensitivity to RMAX; permutation-free SE via cell-cluster bootstrap.
import sys, numpy as np
from math import isqrt
rows = np.loadtxt(sys.argv[1], dtype=np.int64)
p, N, Nm, NT, NTm, q, minK, Ncl, Nclm, Nu = rows.T
PR = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def leg(a, pp): return 1 if pow(int(a), (int(pp) - 1) // 2, int(pp)) == 1 else -1
LEG = np.array([[leg(r, pp) for r in PR] for pp in p])
K0 = np.array([int(x) - isqrt(int(x)) ** 2 for x in p])
y1 = Nm / N; y3 = Nm / (N - Ncl); phicl = Ncl / N; phit = NT / N
def resid(v, rmax):
    k = sum(1 for r in PR if r <= rmax); qcap = max(r for r in PR if r <= rmax) + 4
    keys = [(int(pp % 8),) + tuple(LEG[i, :k]) + (min(int(q[i]), qcap),) for i, pp in enumerate(p)]
    idx = {}
    for i, key in enumerate(keys): idx.setdefault(key, []).append(i)
    out = np.empty(len(v)); ncell = 0
    for ii in idx.values():
        ii = np.array(ii); out[ii] = v[ii] - v[ii].mean(); ncell += 1
    return out, ncell, idx
bins = [(1, 2), (2, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10**9)]
for rmax in (13, 23, 31, 47):
    r1, nc, idx = resid(y1, rmax); r3, _, _ = resid(y3, rmax); rc, _, _ = resid(phicl, rmax); rt, _, _ = resid(phit, rmax)
    sing = sum(1 for ii in idx.values() if len(ii) == 1)
    print(f'RMAX {rmax}: cells {nc} (singletons {sing}); corr(phi_cl, N-/N) = {np.corrcoef(rc, r1)[0,1]:+.3f}; '
          f'slopes N-/N ~ (phi_cl, phi_T1) = {np.linalg.lstsq(np.vstack([rc, rt]).T, r1, rcond=None)[0].round(3)}')
    for lo, hi in bins:
        s = (K0 >= lo) & (K0 < hi)
        print(f'   K0 [{lo},{hi}) n={s.sum():5d}  res N-/N {r1[s].mean():+.4f}   res N-/(N-Ncl) {r3[s].mean():+.4f} ± {r3[s].std()/np.sqrt(s.sum()):.4f}')
    for kk in (1, 4, 9, 16, 24, 25, 36):
        s = K0 == kk
        print(f'   K0 = {kk:2d} n={s.sum():3d} res N-/N {r1[s].mean():+.4f}  res N-/(N-Ncl) {r3[s].mean():+.4f} ± {r3[s].std()/np.sqrt(s.sum()):.4f}')
