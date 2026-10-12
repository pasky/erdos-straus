"""Is the common driver of f_I, f_II (p = 1 (24)) congruence data at COMPOSITE small moduli?
Add C-slice covariates (Lemma 2.1 rows {a,b}): C_II(p) = #{a<=b, e | a+b : 4ab <= M, 4ab | p+e},
C_I(p) = #{a<=b, e | a+b : 4ab <= M, 4ab | pe+1}, as log(1+.), for M in (200, 2000).
Responses: log(1+f) for f in {I_small, I_large, II_small, II_large, I, II} (logs/bs_corr_split_p24.txt)."""
import sys, math
import numpy as np
sys.argv = [sys.argv[0]]
from bs_corr_driver import feats
rows = [tuple(map(int, l.split())) for l in open('logs/bs_corr_split_p24.txt')]
def cslice(p, M):
    cI = cII = 0
    for a in range(1, M):
        for b in range(a, M // (4 * a) + 1):
            q = 4 * a * b
            for e in range(1, a + b + 1):
                if (a + b) % e: continue
                if (p + e) % q == 0: cII += 1
                if (p * e + 1) % q == 0: cI += 1
    return cI, cII
Y = {'I': [math.log(1 + r[1]) for r in rows], 'II': [math.log(1 + r[2]) for r in rows],
     'I_large': [math.log(1 + r[3]) for r in rows], 'II_large': [math.log(1 + r[4]) for r in rows]}
Y = {k: np.array(v) for k, v in Y.items()}
base = np.array([feats(r[0], 2) + [math.log(r[0])] for r in rows], dtype=float)
C = {M: np.array([[math.log(1 + c) for c in cslice(r[0], M)] for r in rows]) for M in (200, 2000)}
for nm, Z in (('M2+log p', base), ('+C-slices M=200', np.hstack([base, C[200]])), ('+C-slices M=200,2000', np.hstack([base, C[200], C[2000]]))):
    R = {}
    for k, y in Y.items():
        beta, *_ = np.linalg.lstsq(Z, y, rcond=None); R[k] = y - Z @ beta
    print('%-22s R2: %s | resid corr I~II %.3f, I_large~II_large %.3f' % (nm, ' '.join('%s=%.2f' % (k, 1 - R[k].var() / Y[k].var()) for k in Y),
          np.corrcoef(R['I'], R['II'])[0, 1], np.corrcoef(R['I_large'], R['II_large'])[0, 1]))
