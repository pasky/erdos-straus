"""z56 PRIMET1 S4 (Z56_PRIMET1.md §3.5): nonlinear omnibus. Gradient-boosted trees trained on D (residual r, resp. hard flag)
with all family features jointly; out-of-sample R^2 (resp. AUC) on C; null = row permutations of the C feature matrix.
S4b (registered before S4 was run): the same restricted to the shadow-free families G2, G3, G4, G8, G9, G10, G12, G13.
Usage: python z56_primet1_s4.py PRED_D FEAT_D CF_D PRED_C FEAT_C CF_C OUT [nperm]
"""
import sys, math
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_tests import families, load_aligned, FAMS

def mat(pred, feat, cf, fams):
    pred, feat, cfl = load_aligned(pred, feat, cf)
    F = families(feat, cfl)
    X = np.column_stack([F[g][0] for g in fams]); X[~np.isfinite(X)] = np.nan
    return X, pred['resid'], (pred['pit'] < 0.01).astype(int)

if __name__ == '__main__':
    from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
    from sklearn.metrics import roc_auc_score
    nperm = int(sys.argv[8]) if len(sys.argv) > 8 else 200
    out = open(sys.argv[7], 'w')
    rng = np.random.default_rng(5604)
    for label, fams in [('S4-all', FAMS), ('S4b-shadowfree', ['G2', 'G3', 'G4', 'G8', 'G9', 'G10', 'G12', 'G13'])]:
        XD, rD, hD = mat(np.load(sys.argv[1]), np.load(sys.argv[2]), sys.argv[3], fams)
        XC, rC, hC = mat(np.load(sys.argv[4]), np.load(sys.argv[5]), sys.argv[6], fams)
        reg = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=31, random_state=1).fit(XD, rD)
        clf = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=15, random_state=1).fit(XD, hD)
        def r2(X): pr = reg.predict(X); return 1 - np.sum((rC - pr)**2) / np.sum((rC - rC.mean())**2)
        def auc(X): return roc_auc_score(hC, clf.predict_proba(X)[:, 1])
        R2, AUC = r2(XC), auc(XC)
        nr, na = [], []
        for k in range(nperm):
            Xp = XC[rng.permutation(len(XC))]; nr.append(r2(Xp)); na.append(auc(Xp))
        nr, na = np.array(nr), np.array(na)
        line = (f'{label}\tR2_oos={R2:.6f}\tnull_R2 mean={nr.mean():.6f} max={nr.max():.6f}\tp={(1+np.sum(nr>=R2))/(1+nperm):.4f}'
                f'\tAUC_oos={AUC:.4f}\tnull_AUC mean={na.mean():.4f} max={na.max():.4f}\tp={(1+np.sum(na>=AUC))/(1+nperm):.4f}')
        print(line, flush=True); out.write(line + '\n'); out.flush()
