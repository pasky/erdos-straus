"""z56 PRIMET1 S5 (Z56_PRIMET1.md §3.5): HC (z53 HCHYP data, 20 000 primes p ≡ 1 (8) from 10^12) restricted to p ≡ 1 (24):
logistic LR test of 1[HC > its 99th percentile] on each family G1–G16 (no local covariates), Holm within S5.
Usage: python z56_primet1_s5.py HCFILE FEAT.npy CF4.txt OUT"""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_tests import families, logit_LR, holm, FAMS
hc = np.loadtxt(sys.argv[1], dtype=np.int64); hc = hc[hc[:, 0] % 24 == 1]
feat = np.load(sys.argv[2]); fi = {int(x): i for i, x in enumerate(feat['p'])}
feat = feat[np.array([fi[int(x)] for x in hc[:, 0]])]
cf = np.loadtxt(sys.argv[3], dtype=np.int64); cfd = {int(r[0]): r[1] for r in cf}
F = families(feat, np.array([cfd[int(x)] for x in hc[:, 0]], dtype=float))
q99 = np.percentile(hc[:, 1], 99); y = (hc[:, 1] > q99).astype(float)
rows = []
for g in FAMS:
    X = F[g][0]; X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
    try:
        LR, pv, m = logit_LR(y, X); rows.append((g, X.shape[1], LR, pv))
    except Exception as e:
        rows.append((g, X.shape[1], float('nan'), 1.0))
adj = holm([r[3] for r in rows])
with open(sys.argv[4], 'w') as f:
    f.write(f'# S5 n={len(y)} HC 99th pct={q99} events (HC > q99)={int(y.sum())}; HC histogram: '
            + ' '.join(f'{v}:{c}' for v, c in zip(*np.unique(hc[:, 1], return_counts=True))) + '\n')
    f.write('family\tdf\tLR\tp_raw\tp_holm\n')
    for r, a in zip(rows, adj): f.write('%s\t%d\t%.3f\t%.3e\t%.3e\n' % (r + (a,)))
print(open(sys.argv[4]).read())
