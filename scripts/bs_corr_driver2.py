"""Extra candidate drivers of the common part of f_I(p), f_II(p) (p = 1 (24)), on top of M2
(bs_corr_driver.feats level 2): T = log p, log log p; S_X = sum_{l<=X} (l/p) log l / l (X = 1e3, 1e4);
non-abelian residue symbols: [l is a 4th power mod p] for l in {2,3,5,7} (when (l/p)=1), [l is a cube mod p]
for l in {2,3,5,7}; and the total f_I/f_II large-part (from logs/bs_corr_split_p24.txt).
Prints R^2 and residual correlation of log(1+f_I_large), log(1+f_II_large) after each addition."""
import sys, math
import numpy as np
sys.argv = [sys.argv[0]]
from bs_corr_driver import feats
from sympy import legendre_symbol, primerange
rows = [tuple(map(int, l.split())) for l in open('logs/bs_corr_split_p24.txt')]
yI = np.array([math.log(1 + r[3]) for r in rows]); yII = np.array([math.log(1 + r[4]) for r in rows])
L3 = list(primerange(3, 1000)); L4 = list(primerange(3, 10000))
def extra(p, lev):
    f = []
    if lev >= 1: f += [math.log(p), math.log(math.log(p))]
    if lev >= 2: f += [sum(legendre_symbol(l, p) * math.log(l) / l for l in L) for L in (L3, L4)]
    if lev >= 3:
        for l in (2, 3, 5, 7): f.append(1.0 if pow(l, (p - 1) // 4, p) == 1 else 0.0)
        for l in (2, 3, 5, 7): f.append(1.0 if pow(l, (p - 1) // 3, p) == 1 else 0.0)
    return f
base = np.array([feats(r[0], 2) for r in rows], dtype=float)
for lev, nm in enumerate(['M2', '+log p, loglog p', '+S_1e3, S_1e4', '+quartic/cubic symbols']):
    Z = np.hstack([base, np.array([extra(r[0], lev) for r in rows], dtype=float).reshape(len(rows), -1)]) if lev else base
    res, R2 = [], []
    for y in (yI, yII):
        beta, *_ = np.linalg.lstsq(Z, y, rcond=None); r = y - Z @ beta; res.append(r); R2.append(1 - r.var() / y.var())
    print('%-24s cols=%3d R2_Ilarge=%.3f R2_IIlarge=%.3f resid corr=%.3f' % (nm, Z.shape[1], R2[0], R2[1], np.corrcoef(*res)[0, 1]))
