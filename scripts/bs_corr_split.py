"""Correlations between small-modulus (q=4ad <= sqrt p) and large-modulus parts of f_I(p), f_II(p),
p = 1 (24), raw and after regressing out M2 (profile l<=100 + residue classes, see bs_corr_driver.py).
Input: logs/bs_corr_split_p24.txt (from bs_corr_count_split.c)."""
import sys, math
import numpy as np
sys.argv = [sys.argv[0]]  # feats() only
from bs_corr_driver import feats
rows = [tuple(map(int, l.split())) for l in open('logs/bs_corr_split_p24.txt')]
V = {'I_small': [], 'I_large': [], 'II_small': [], 'II_large': []}
for n, I, II, bI, bII in rows:
    for k, v in (('I_small', I - bI), ('I_large', bI), ('II_small', II - bII), ('II_large', bII)):
        V[k].append(math.log(1 + v))
V = {k: np.array(v) for k, v in V.items()}
Z = np.array([feats(r[0], 2) for r in rows], dtype=float)
R = {}
for k, y in V.items():
    beta, *_ = np.linalg.lstsq(Z, y, rcond=None); R[k] = y - Z @ beta
    print('%-9s mean count %.1f  R2(M2)=%.3f' % (k, np.mean(np.exp(y) - 1), 1 - R[k].var() / y.var()))
ks = list(V)
for i in range(4):
    for j in range(i + 1, 4):
        a, b = ks[i], ks[j]
        print('%-9s ~ %-9s raw corr %.3f   resid corr %.3f' % (a, b, np.corrcoef(V[a], V[b])[0, 1], np.corrcoef(R[a], R[b])[0, 1]))
