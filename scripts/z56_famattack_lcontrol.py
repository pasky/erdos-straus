# F1 refinement: remove the global (genus/BM) main-term driver before measuring cross-window association.
# Covariates: one-hot p mod l (l in 8,3,5,7,...,31) plus log L_Y(1,chi_p), log L_Y(1,chi_{-4p}) (Euler products to Y)
# and their squares. Report residual correlations for u-windows and C-windows, and the residual off-diagonal covariance share.
import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load, corr_matrix
from sympy import primerange
def logL(p, Y, twist4=False):
    s = np.zeros(len(p))
    for l in primerange(3, Y):
        sq = np.zeros(l, dtype=np.int8); sq[(np.arange(1, l) ** 2) % l] = 1
        r = p % l; chi = np.where(r == 0, 0, np.where(sq[r] == 1, 1, -1)).astype(float)
        if twist4: chi *= (1 if l % 4 == 1 else -1)
        s -= np.log1p(-chi / l)
    return s
for fn in sys.argv[1:]:
    p, R, g = load(fn); N = len(p); se = 1/np.sqrt(N)
    cols = [np.ones(N)]
    for l in (8, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        r = p % l
        for v in np.unique(r)[1:]: cols.append((r == v).astype(float))
    L1 = logL(p, 20000); L2 = logL(p, 20000, True)
    for c in (L1, L2, L1**2, L2**2, L1*L2): cols.append(c)
    A = np.column_stack(cols)
    for name, X in (("u-windows", g.sum(2)), ("C-windows", g.sum(1)), ("total", (R // 2)[:, None])):
        X = X.astype(float)
        res = X - A @ np.linalg.lstsq(A, X, rcond=None)[0]
        r2 = 1 - res.var(0) / X.var(0)
        if X.shape[1] > 1:
            C = corr_matrix(res - res.mean(0))
            cov = np.cov(res.T); off = cov.sum() - np.trace(cov)
            print(f"{fn} {name}: R^2 by covariates {np.round(r2,3)}; residual corr " + " ".join(f"({i}{j}){C[i,j]:+.3f}" for i in range(5) for j in range(i+1,5)) + f"; resid off-diag cov share {off/cov.sum():+.3f}; se {se:.4f}")
        else:
            print(f"{fn} total unordered: R^2 by covariates {r2[0]:.3f}; corr(total, logL(chi_p)) {np.corrcoef(X[:,0], L1)[0,1]:+.3f}, corr(total, logL(chi_-4p)) {np.corrcoef(X[:,0], L2)[0,1]:+.3f}")
