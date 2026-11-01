"""Z0961: partial Spearman of the U-residual with ord_p(10)/(p-1), controlling for (2/p) and (5/p), over primes p = 1 (mod 4),
101 <= p <= 2e5 (U data: data/z52b/raw/f4_all_30000.txt + pr_20001_200000.txt). Also a null: controls by mod-8 class,
and the same statistic with ord_p(2) and ord_p(3) (decimal-period analogues) as a family check.
Run: ulimit -v 4000000; uv run --with numpy --with sympy --with scipy python scripts/z52d_p2_NC0_Z0961.py
"""
import numpy as np, json, os
from sympy import primerange, legendre_symbol, n_order
from scipy.stats import spearmanr, rankdata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = ROOT + '/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64); G = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
UU = {int(r[0]): int(r[1]) for r in np.vstack([F, G])}
P = np.array([p for p in primerange(101, 200001) if p % 4 == 1 and p in UU], dtype=np.int64)
U = np.array([UU[int(p)] for p in P], dtype=float)
lp = np.log(P.astype(float))
base = np.vstack([np.ones_like(lp), lp, np.log(lp)]).T
y = np.log(U + 1); res = y - base @ np.linalg.lstsq(base, y, rcond=None)[0]
c2 = np.array([legendre_symbol(2, int(p)) for p in P], dtype=float)
c5 = np.array([legendre_symbol(5, int(p)) for p in P], dtype=float)
def partial_spearman(a, b, covs):
    ra, rb = rankdata(a), rankdata(b)
    Z = np.column_stack([np.ones(len(a))] + covs)
    ea = ra - Z @ np.linalg.lstsq(Z, ra, rcond=None)[0]
    eb = rb - Z @ np.linalg.lstsq(Z, rb, rcond=None)[0]
    rho = np.corrcoef(ea, eb)[0, 1]
    n = len(a); k = Z.shape[1]
    t = rho * np.sqrt((n - 2 - k + 1) / max(1e-12, 1 - rho ** 2))
    from scipy.stats import t as tdist
    return float(rho), float(2 * tdist.sf(abs(t), n - 2 - k + 1))
out = {'n_primes': int(len(P))}
ordr = {}
for name, b in [('ord_p(10)', 10), ('ord_p(2)', 2), ('ord_p(3)', 3)]:
    o = np.array([n_order(b, int(p)) for p in P], dtype=float) / (P - 1).astype(float)
    ordr[name] = o
    rho0, p0 = spearmanr(res, o)
    rho, pv = partial_spearman(res, o, [c2, c5])
    out[name] = dict(raw_spearman_with_Uresid=round(float(rho0), 4), p_raw=float(p0),
                     partial_given_2p_5p=round(rho, 4), p_partial=float(pv))
# null-style check: the same partial statistic against a shuffled-within-class copy of ord_p(10)
rng = np.random.default_rng(0); o = ordr['ord_p(10)']
ns = []
for _ in range(200):
    perm = rng.permutation(len(o)); ns.append(partial_spearman(res, o[perm], [c2, c5])[0])
out['null_shuffled_partial_mean_sd'] = [round(float(np.mean(ns)), 4), round(float(np.std(ns)), 4)]
# by mod 8 classes: partial correlation within p mod 8 (controls for (2/p) which is a function of p mod 8)
for r8 in [1, 5]:
    m = (P % 8) == r8
    rho, pv = partial_spearman(res[m], ordr['ord_p(10)'][m], [c5[m]])
    out[f'p_mod8={r8}_partial_given_5p'] = [round(rho, 4), float(pv), int(m.sum())]
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0961_partial.json', 'w'), indent=1)
print(json.dumps(out, indent=1))

# Stronger controls: all quadratic symbols (q/p), q prime <= 47, and the index i_p(10) = (p-1)/ord_p(10) itself
from sympy import primerange as _pr
qs = list(_pr(2, 48))
covQ = [np.array([legendre_symbol(q, int(p)) for p in P], dtype=float) for q in qs]
o10 = ordr['ord_p(10)']
idx = (P - 1).astype(float) / (o10 * (P - 1).astype(float))  # = 1/ratio, kept for clarity
rho_q, p_q = partial_spearman(res, o10, covQ)
out3 = {'partial_given_all_quadratic_symbols_q<=47': [round(rho_q, 4), float(p_q)], 'n_covariates': len(covQ)}
# index-of-10 classes: is the residual different across the 'index' classes once quadratic symbols are controlled?
ind = np.round(1.0 / o10).astype(int)  # index i = (p-1)/ord (ord/(p-1)=1/i)
out3['index_classes_mean_Uresid'] = {int(k): [round(float(res[ind == k].mean()), 4), int((ind == k).sum())]
                                     for k in [1, 2, 3, 4, 6, 8, 12] if (ind == k).sum() > 30}
json.dump(dict(out, **out3), open(ROOT + '/data/z52b/pass2/NC0/sub/Z0961_partial.json', 'w'), indent=1)
print(out3)
