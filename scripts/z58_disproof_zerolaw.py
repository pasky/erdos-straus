# z58 DISPROOF §6: zero law P(count = 0 | cell) = exp(-a * mu^beta), mu = cell mean of the count, fitted by binomial ML
# on cells of scripts/z58_disproof_cells.c (cell = p mod 840 x 5 Legendre bits x half-octave).  Fits for R8 (the
# C-even sibling with ~1.4e3 zeros) and R (12 zeros in the range), cross-prediction, and pooled fits.
# Run: uv run --with numpy --with scipy python scripts/z58_disproof_zerolaw.py data/z58/disproof/cells_2e8.txt [pmin]
import sys, math
import numpy as np
from scipy.optimize import minimize
fn = sys.argv[1]; pmin = float(sys.argv[2]) if len(sys.argv) > 2 else 1e5
rows = np.array([[float(x) for x in l.split()] for l in open(fn) if not l.startswith('#')])
a840, bits, hb, n, sR, sR2, s8, s82, zR, z8, l2R, l28 = rows.T
keep = (2 ** (hb / 2) >= pmin)
# smoothed cell means: mu_hat = kappa[class,bits] * t[bin] * L_bin^2, kappa from bins >= 1e7, t per bin (pooled)
Lb = (hb + 0.5) / 2 * math.log(2)
def smooth(S):
    key = a840 * 32 + bits; big = 2 ** (hb / 2) >= 1e7
    kap = {}
    for k in np.unique(key):
        m = (key == k) & big
        kap[k] = (S[m] / Lb[m] ** 2).sum() / n[m].sum() if n[m].sum() > 0 else np.nan
    K = np.array([kap[k] for k in key])
    t = {}
    for b in np.unique(hb):
        m = (hb == b) & ~np.isnan(K)
        t[b] = S[m].sum() / (n[m] * K[m] * Lb[m] ** 2).sum()
    return K * np.array([t[b] for b in hb]) * Lb ** 2
MUR = smooth(sR); MU8 = smooth(s8)
keep &= ~np.isnan(MUR) & ~np.isnan(MU8)
EMP = len(sys.argv) > 3 and sys.argv[3] == 'emp'
def fit(mu, z, nn, name):
    def nll(t):
        a, b = math.exp(t[0]), t[1]
        lp = -a * mu ** b                       # log P(zero)
        lp = np.minimum(lp, -1e-12)
        return -(z * lp + (nn - z) * np.log1p(-np.exp(lp))).sum()
    best = None
    for b0 in (0.6, 0.9, 1.2):
        r = minimize(nll, [math.log(0.5), b0], method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 4000})
        if best is None or r.fun < best.fun: best = r
    a, b = math.exp(best.x[0]), best.x[1]
    print(f"{name}: a={a:.4f} beta={b:.4f} nll={best.fun:.2f} zeros={z.sum():.0f} cells={len(z)} primes={nn.sum():.0f}")
    return a, b
def predict(mu, nn, a, b): return (nn * np.exp(-a * mu ** b)).sum()
mu8 = (s8 / n if EMP else MU8)[keep]; muR = (sR / n if EMP else MUR)[keep]
print(f"# file {fn}, cells with p >= {pmin:g}; mu = {'empirical' if EMP else 'smoothed'} cell mean")
a8, b8 = fit(mu8, z8[keep], n[keep], "R8 zero law")
aR, bR = fit(muR, zR[keep], n[keep], "R  zero law")
print(f"cross: R8-law predicts R zeros {predict(muR, n[keep], a8, b8):.2f} (observed {zR[keep].sum():.0f}); "
      f"R-law predicts R8 zeros {predict(mu8, n[keep], aR, bR):.1f} (observed {z8[keep].sum():.0f})")
# pooled (both counts as separate lotteries in one law)
mu = np.concatenate([mu8, muR]); z = np.concatenate([z8[keep], zR[keep]]); nn = np.concatenate([n[keep], n[keep]])
aP, bP = fit(mu, z, nn, "pooled R8+R")
# calibration table by mu bins (R8)
print("# R8 calibration by mu bin: mu_lo mu_hi primes zeros predicted(R8-law)")
for lo, hi in [(0, 2), (2, 4), (4, 6), (6, 8), (8, 10), (10, 12), (12, 15), (15, 20), (20, 30), (30, 99)]:
    m = (mu8 >= lo) & (mu8 < hi)
    if m.sum(): print(f"  [{lo},{hi}) {n[keep][m].sum():.0f} {z8[keep][m].sum():.0f} {predict(mu8[m], n[keep][m], a8, b8):.1f}")
print("# R calibration by mu bin: mu_lo mu_hi primes zeros predicted(R-law) predicted(R8-law) predicted(pooled)")
for lo, hi in [(0, 6), (6, 8), (8, 10), (10, 14), (14, 18), (18, 22), (22, 30), (30, 99)]:
    m = (muR >= lo) & (muR < hi)
    if m.sum(): print(f"  [{lo},{hi}) {n[keep][m].sum():.0f} {zR[keep][m].sum():.0f} {predict(muR[m], n[keep][m], aR, bR):.2f} {predict(muR[m], n[keep][m], a8, b8):.2f} {predict(muR[m], n[keep][m], aP, bP):.2f}")
