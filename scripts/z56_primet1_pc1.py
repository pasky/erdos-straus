"""z56 PRIMET1 PC1 (Z56_PRIMET1.md §3.6): with 𝓛 refitted without the p mod 13 one-hot, the P-cont / P-tail pipeline must
detect 'p mod 13' (12 df) on C.  Usage: python z56_primet1_pc1.py PRED_C_DROP13.npy"""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_tests import ols_F, logit_LR
pred = np.load(sys.argv[1]); p = pred['p']; r = pred['resid']; L = np.log(p.astype(float))
h = (pred['pit'] < 0.01).astype(float)
X = np.column_stack([(p % np.uint64(13) == np.uint64(c)).astype(float) for c in range(2, 13)])
X0 = np.column_stack([np.ones(len(r)), np.log(L)])
F, pc, df = ols_F(r, X0, X); LR, pt, _ = logit_LR(h, X)
print(f'PC1 p mod 13 (df {df}): P-cont F={F:.2f} p={pc:.3e}; P-tail LR={LR:.2f} p={pt:.3e}; n_hard={int(h.sum())}')
