"""z56 PRIMET1 post-review S4b-r: the nonlinear omnibus of S4b repeated against the COMPLETE known-model null.
Target: the null residual e of z56_primet1_robust.py (outcome residualised on 𝓛⁺⁺⁺ by least squares) and its lower-tail
indicator 1[e < 1 % quantile]. Features: raw columns of the shadow-free families G2, G3, G4, G8, G9, G10, G12, G13.
Cross-fit inside the sample: train on bit 32 of splitmix64(p) = 0, evaluate on bit 32 = 1; null = 200 row permutations of
the evaluation feature matrix.  Usage: python z56_primet1_s4r.py NULLRESID.npy FEAT.npy CF4.txt OUT [nperm] [comma-separated family list]"""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_tests import families
from z56_primet1_split import splitmix64
from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
nr = np.load(sys.argv[1]); feat = np.load(sys.argv[2]); nperm = int(sys.argv[5]) if len(sys.argv) > 5 else 200
fi = {int(x): i for i, x in enumerate(feat['p'])}; feat = feat[np.array([fi[int(x)] for x in nr['p']])]
cf = np.loadtxt(sys.argv[3], dtype=np.int64); cfd = {int(r[0]): r[1] for r in cf}
F = families(feat, np.array([cfd[int(x)] for x in nr['p']], dtype=float))
FAM = sys.argv[6].split(',') if len(sys.argv) > 6 else ['G2', 'G3', 'G4', 'G8', 'G9', 'G10', 'G12', 'G13']
X = np.column_stack([F[g][0] for g in FAM])
e = nr['e'].astype(float); t = (e < np.quantile(e, 0.01)).astype(int)
h = ((splitmix64(nr["p"].astype(np.uint64)) >> np.uint64(32)) & np.uint64(1)) == 0  # high bit: independent of the mod-16 sample definition
reg = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=31, random_state=1).fit(X[h], e[h])
clf = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=15, random_state=1).fit(X[h], t[h])
Xe, ee, te = X[~h], e[~h], t[~h]
def r2(M): pr = reg.predict(M); return 1 - np.sum((ee - pr)**2) / np.sum((ee - ee.mean())**2)
def auc(M): return roc_auc_score(te, clf.predict_proba(M)[:, 1])
R2, AUC = r2(Xe), auc(Xe); rng = np.random.default_rng(5605); a, b = [], []
for k in range(nperm):
    M = Xe[rng.permutation(len(Xe))]; a.append(r2(M)); b.append(auc(M))
a, b = np.array(a), np.array(b)
line = (f'S4b-r (complete null) fams={",".join(FAM)} n_eval={len(ee)}\tR2_oos={R2:.6f}\tnull mean={a.mean():.6f} max={a.max():.6f}\tp={(1+np.sum(a>=R2))/(1+nperm):.4f}'
        f'\tAUC_lowtail={AUC:.4f}\tnull mean={b.mean():.4f} max={b.max():.4f}\tp={(1+np.sum(b>=AUC))/(1+nperm):.4f}')
open(sys.argv[4], 'w').write(line + '\n'); print(line)
