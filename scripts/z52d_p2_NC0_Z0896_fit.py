"""Z0896 analysis: fit log(S(p)+1) (signed sibling count, scripts/z52d_p2_NC0_Z0896.c, z<=p^2) and log(U(p)+1)
(ES count, data/z52b/raw) on the same primes p = 1 (mod 4), 101 <= p <= 2e5, with the lfit-style character regressors
  log L_Q(chi) with chi = (./p) [twist 'p'] or (-p/.) [twist '-p'];  compare alpha and R^2 gains; Spearman of residuals.
Input: /tmp/z52d_big/G2/z0896_2e5.txt (cols p S O minz). Output: data/z52b/pass2/NC0/sub/Z0896_fit.json
"""
import numpy as np, json, os
from sympy import primerange, legendre_symbol, jacobi_symbol
from scipy.stats import spearmanr
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = np.loadtxt('/tmp/z52d_big/G2/z0896_2e5.txt', dtype=np.int64)
A = A[A[:, 0] > 100]
P = A[:, 0]; S = A[:, 1]; MINZ = A[:, 3]
R = ROOT + '/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
G = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
UU = {int(r[0]): int(r[1]) for r in np.vstack([F, G])}
U = np.array([UU[int(p)] for p in P], dtype=np.int64)
lp = np.log(P.astype(float))
base = np.vstack([np.ones_like(lp), lp, np.log(lp)]).T
def LQ(Q, twist):
    out = np.zeros(len(P))
    for q in primerange(2, Q + 1):
        if twist == 'p':
            chi = np.array([legendre_symbol(q, int(p)) if q > 2 else (1 if int(p) % 8 == 1 else -1) for p in P])
        else:
            chi = np.array([jacobi_symbol(-int(p), q) if q > 2 else (1 if (-int(p)) % 8 == 1 else -1) for p in P])
        out += -np.log(1 - chi.astype(float) / q)
    return out
def fit(t, x):
    y = np.log(t.astype(float) + 1)
    b0 = np.linalg.lstsq(base, y, rcond=None)[0]; r0 = y - base @ b0; v0 = r0.var()
    X = np.hstack([base, x[:, None]]); b = np.linalg.lstsq(X, y, rcond=None)[0]; r = y - X @ b
    return float(b[-1]), float(1 - r.var() / v0), r0, r
out = {'n_primes': int(len(P)), 'S_zero': int((S == 0).sum()), 'U_zero': int((U == 0).sum())}
res = {}
for twist in ['p', '-p']:
    for Q in [2, 3, 5, 7, 13, 31, 100]:
        x = LQ(Q, twist)
        aS, gS, r0S, rS = fit(S, x); aU, gU, r0U, rU = fit(U, x)
        res[f'{twist}|Q={Q}'] = dict(alpha_S=round(aS, 3), R2gain_S=round(gS, 3), alpha_U=round(aU, 3), R2gain_U=round(gU, 3))
out['fits'] = res
# growth exponent of S and U (median of count/log^2 p by window) and residual correlation with U
rho, pv = spearmanr(r0S, r0U)
out['spearman_resid_S_vs_U'] = [round(float(rho), 4), float(pv)]
ratio = S / np.log(P.astype(float)) ** 2
out['S_over_log2_median_by_window'] = {}
for X in [100, 1000, 10000, 50000, 100000]:
    m = (P >= X) & (P < 2 * X)
    if m.sum():
        out['S_over_log2_median_by_window'][f'[{X},{2*X})'] = dict(n=int(m.sum()), med=round(float(np.median(ratio[m])), 3),
                                                              min=round(float(ratio[m].min()), 3))
# minz: min z over solutions, growth vs p^2 cap
out['minz_over_p_median_by_window'] = {}
for X in [100, 1000, 10000, 100000]:
    m = (P >= X) & (P < 2 * X)
    if m.sum():
        out['minz_over_p_median_by_window'][f'[{X},{2*X})'] = round(float(np.median(MINZ[m] / P[m])), 3)
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0896_fit.json', 'w'), indent=1)
print(json.dumps(out, indent=1))

# chi_p-adjusted residuals (twist 'p', Q=31): Spearman between S- and U-residuals after the character regressor
from scipy.stats import spearmanr as _sp
_x = LQ(31, 'p')
_, _, _, _rS = fit(S, _x); _, _, _, _rU = fit(U, _x)
_rho, _pv = _sp(_rS, _rU)
out2 = dict(spearman_adjusted_resid_S_vs_U_chi31=[round(float(_rho), 4), float(_pv)])
json.dump(dict(out, **out2), open(ROOT + '/data/z52b/pass2/NC0/sub/Z0896_fit.json', 'w'), indent=1)
print(out2)
