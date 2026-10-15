"""O221 (NEAR_SQUARE §4): does the T1-type word fraction phi = NT/N predict N-/N beyond the adelic cell?
Input: output of ns_census; optional 2nd arg RMAX (cell = p mod 8, (r/p) for odd r <= RMAX, lnr capped).
Reports: within-cell regression of N-/N on phi; and of N-/(N-NT) on phi (does the effect go beyond the forced words?)."""
import sys
import numpy as np
from sympy import legendre_symbol
rows = np.loadtxt(sys.argv[1], dtype=np.int64)
RS = [r for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) if r <= (int(sys.argv[2]) if len(sys.argv) > 2 else 13)]
QCAP = max(RS) + 4
p, N, Nm, NT, NTm, q, minK, Ncl, Nclm, Nu = rows.T
cells = {}
for i, pp in enumerate(p):
    key = (int(pp % 8),) + tuple(legendre_symbol(r, int(pp)) for r in RS) + (min(int(q[i]), QCAP),)
    cells.setdefault(key, []).append(i)
y = Nm / N; phi = NT / N; y2 = Nm / (N - NT); y3 = Nm / (N - Ncl); y4 = Nm / (N - Nu); phicl = Ncl / N
lp = np.log(p)
def within(v):
    out = np.empty_like(v, dtype=float)
    for idx in cells.values():
        idx = np.array(idx); out[idx] = v[idx] - v[idx].mean()
    return out
print("words: all", N.sum(), "on T1-type levels", NT.sum(), "on clean levels", Ncl.sum(), "chi=-1 on clean", Nclm.sum(), "chi=-1 on T1-type", NTm.sum())
for name, yy in (("N-/N", y), ("N-/(N-NT)", y2), ("N-/(N-Ncl)", y3)):
    ry, rphi, rlp = within(yy), within(phi), within(lp)
    X = np.vstack([rphi, rlp]).T
    beta, res, *_ = np.linalg.lstsq(X, ry, rcond=None)
    pred = X @ beta; r2 = 1 - ((ry - pred) ** 2).sum() / (ry ** 2).sum()
    c = np.corrcoef(rphi, ry)[0, 1]
    print(f"{name}: within-cell corr(phi, y) = {c:+.3f}; slope on phi = {beta[0]:+.3f}, on log p = {beta[1]:+.4f}; R2 = {r2:.3f}; cells = {len(cells)}; primes = {len(p)}")
# near-square strata: minK small
for lo, hi in ((1, 30), (30, 300), (300, 3000), (3000, 10**9)):
    sel = (minK >= lo) & (minK < hi)
    if sel.sum(): print(f"minK in [{lo},{hi}): {sel.sum()} primes, mean within-cell residual of N-/N {within(y)[sel].mean():+.4f}, of N-/(N-NT) {within(y2)[sel].mean():+.4f}, of N-/(N-Ncl) {within(y3)[sel].mean():+.4f} (SE {within(y3)[sel].std()/np.sqrt(sel.sum()):.4f}), mean phi {phi[sel].mean():.3f}, phi_clean {phicl[sel].mean():.3f}")
rc, ry = within(phicl), within(y)
print("within-cell corr(phi_clean, N-/N) = %+.3f" % np.corrcoef(rc, ry)[0, 1])
X = np.vstack([rc, within(phi)]).T; beta, *_ = np.linalg.lstsq(X, ry, rcond=None); print("N-/N on (phi_clean, phi_T1): slopes", beta)
# archimedean proximity independent of the words: K0 = p - floor(sqrt p)^2
from math import isqrt
K0 = np.array([int(x) - isqrt(int(x)) ** 2 for x in p])
r1, r3, r4 = within(y), within(y3), within(y4)
for lo, hi in ((1, 2), (2, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10**9)):
    sel = (K0 >= lo) & (K0 < hi)
    if sel.sum(): print(f"K0 = p - floor(sqrt p)^2 in [{lo},{hi}): {sel.sum():5d} primes; residual N-/N {r1[sel].mean():+.4f}, N-/(N-Ncl) {r3[sel].mean():+.4f} (SE {r3[sel].std() / np.sqrt(sel.sum()):.4f}), N-/(N-Nu) {r4[sel].mean():+.4f}, phi_clean {phicl[sel].mean():.3f}")
for k in (1, 4, 9, 16, 24, 25, 36):
    sel = K0 == k
    if sel.sum(): print(f"K0 = {k:2d}: {sel.sum():4d} primes; residual N-/N {r1[sel].mean():+.4f}, N-/(N-Ncl) {r3[sel].mean():+.4f} (SE {r3[sel].std() / np.sqrt(sel.sum()):.4f})")
