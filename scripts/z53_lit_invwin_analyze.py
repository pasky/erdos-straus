#!/usr/bin/env python3
"""z53 LIT F2b analysis: does the inverse-window discrepancy D predict R(p) beyond residue-class data?
Input: TSV from scripts/z53_lit_invwin_census.c (p R D G tm tp s50).
Reports Spearman/Pearson correlations of y = R/log^2 p with D, then partial correlation of D after OLS-adjusting
both y and D for small-divisor covariates (tm, tp, s50, and indicator dummies p mod 5,7,11,13 == 1 and p mod 8 == 1).
Usage: uv run --with numpy --with scipy python scripts/z53_lit_invwin_analyze.py data/z53/lit/invwin_2e6_1e7.tsv
"""
import sys
import numpy as np
from scipy import stats

a = np.loadtxt(sys.argv[1])
p, R, D, G, tm, tp, s50 = a.T
y = R / np.log(p) ** 2
print(f"n = {len(p)} primes p ≡ 1 (24) in [{int(p.min())}, {int(p.max())}]; zeros of R: {[int(x) for x in p[R == 0]]}")
print(f"mean y = {y.mean():.4f}; corr(y, D): Pearson {stats.pearsonr(y, D)[0]:+.4f}, Spearman {stats.spearmanr(y, D)[0]:+.4f}")
covs = [tm, tp, s50, (p % 8 == 1), (p % 5 == 1), (p % 7 == 1), (p % 11 == 1), (p % 13 == 1), np.log(p)]
X = np.column_stack([np.ones_like(p)] + [np.asarray(c, float) for c in covs])
def resid(v):
    beta, *_ = np.linalg.lstsq(X, v, rcond=None); return v - X @ beta
ry, rD = resid(y), resid(D)
r, pv = stats.pearsonr(ry, rD)
print(f"R^2 of covariates for y: {1 - ry.var() / y.var():.4f}; for D: {1 - rD.var() / D.var():.4f}")
print(f"partial corr(y, D | covariates) = {r:+.4f} (p-value {pv:.2e}); Spearman of residuals {stats.spearmanr(ry, rD)[0]:+.4f}")
for q in (0.5, 0.9, 0.99):
    thr = np.quantile(rD, q)
    print(f"  residual-D top {100*(1-q):.0f}%: mean y {y[rD > thr].mean():.4f} vs rest {y[rD <= thr].mean():.4f}")
low = y < np.quantile(y, 0.01)
print(f"lowest-1% y (n={low.sum()}): mean D {D[low].mean():.4f} vs all {D.mean():.4f}; mean residual-D {rD[low].mean():+.5f} (sd {rD.std():.5f})")
