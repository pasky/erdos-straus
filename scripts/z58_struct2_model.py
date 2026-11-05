#!/usr/bin/env python3
"""z58 STRUCT2: how surprising is N_II(4545) = 0?  Poisson log-linear regression of N_II(n) on the local type of n
(n mod 8; for each prime l in PR: n mod l in {0, QR, QNR}; offset log L^3), fitted on all odd non-square n ≡ 1 (4),
NLO <= n < 120001 (data/z58/struct2/counts_*.txt).  Reports the fitted mean at 4545, the over-dispersion, the
smallest fitted-mean-adjusted tail probabilities, and the fitted factors.  EVIDENCE only.
Usage: uv run --with numpy python scripts/z58_struct2_model.py [NLO] [COL]   (COL 1 = N_II, 3 = coprime count)"""
import sys, numpy as np
from math import isqrt, log
NLO = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
COL = int(sys.argv[2]) if len(sys.argv) > 2 else 1     # 1: N_II, 3: coprime count
PR = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
rows = []
for fn in ['data/z58/struct2/counts_1_2e4.txt', 'data/z58/struct2/counts_2e4_1.2e5.txt']:
    for l in open(fn):
        n, N, R, Cp = map(int, l.split())
        if n < NLO or isqrt(n) ** 2 == n: continue
        rows.append((n, [None, N, R, Cp][COL]))
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else 2)
names = ['const', 'n=5mod8'] + [f'{p}:{t}' for p in PR for t in ('0', 'N')]
def feats(n):
    x = [1.0, 1.0 if n % 8 == 5 else 0.0]
    for p in PR:
        c = leg(n, p); x += [1.0 if c == 0 else 0.0, 1.0 if c == 2 else 0.0]
    return x
X = np.array([feats(n) for n, _ in rows]); y = np.array([N for _, N in rows], float)
off = np.array([3 * log(log(n)) for n, _ in rows])
beta = np.zeros(X.shape[1]); beta[0] = log(y.mean()) - off.mean()
for it in range(50):                       # IRLS for Poisson GLM
    mu = np.exp(X @ beta + off); W = mu
    z = X @ beta + (y - mu) / mu
    beta_new = np.linalg.solve(X.T @ (X * W[:, None]), X.T @ (W * z))
    if np.max(abs(beta_new - beta)) < 1e-10: beta = beta_new; break
    beta = beta_new
mu = np.exp(X @ beta + off)
phi = float(np.sum((y - mu) ** 2 / mu) / (len(y) - len(beta)))
print(f'column {COL}: fit on {len(y)} odd non-square n ≡ 1 (4) in [{NLO}, 120001); Pearson dispersion phi = {phi:.2f}')
for nm, b in zip(names, beta): print(f'  {nm:8s} factor {np.exp(b):.3f}')
# negative binomial with variance mu + mu^2/k, k from moments: var = phi*mu ~ mu + mu^2/k -> fit k
k = float(np.sum(mu ** 2) / max(1e-9, np.sum((y - mu) ** 2 - mu)))
print(f'NB shape k (moment fit) = {k:.2f}')
def p0(m): return (k / (k + m)) ** k        # NB probability of 0
order = np.argsort(y / mu)
print('lowest observed/fitted:')
for i in order[:15]:
    n = rows[i][0]
    print(f'  n={n} N={int(y[i])} fitted={mu[i]:.1f} Poisson P0={np.exp(-mu[i]):.2e} NB P0={p0(mu[i]):.2e}')
i45 = [i for i, (n, _) in enumerate(rows) if n == 4545]
if i45:
    m = mu[i45[0]]; print(f'4545: fitted mean {m:.2f}; Poisson P(0) = {np.exp(-m):.2e}; NB P(0) = {p0(m):.2e}')
print(f'expected number of zeros among fitted n (NB): {sum(p0(m) for m in mu):.3f}; observed: {int(sum(y == 0))}')
