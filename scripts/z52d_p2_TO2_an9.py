# TO2 part 9: Z0511 (fraction of primes whose minimal max-denominator exceeds p^k), Z0579/Z0580 (least primitive root / least QNR vs U(p), p≡1 mod 4, p<=2e5)
import numpy as np, json
from scipy.stats import spearmanr
out = {}
D = 'data/z52b/raw/'
a = np.loadtxt(D + 'f4_all_30000.txt', dtype=np.int64); b = np.loadtxt(D + 'pr_20001_200000.txt', dtype=np.int64)
A_ = np.vstack([a, b])
s = np.ones(A_[:, 0].max()+1, bool); s[:2] = False
for i in range(2, int(A_[:, 0].max()**0.5)+1):
    if s[i]: s[i*i::i] = False
M = A_[s[A_[:, 0]] & (A_[:, 0] > 5)]
p = M[:, 0]; zmin = M[:, 4].astype(float); U = M[:, 1].astype(float)
out['frac_zmin_gt_p^k'] = {str(k): float((zmin > p.astype(float)**k).mean()) for k in [1.5, 1.75, 1.9, 2.0]}
out['max_k_needed_over_primes_gt_5_le_2e5'] = float((np.log(zmin)/np.log(p.astype(float))).max())
sel = p % 4 == 1
pp = p[sel]
def ordn(g, q):
    k = 1; x = g % q
    while x != 1: x = x*g % q; k += 1
    return k
def phi_factors(n):
    f = []; x = n; d = 2
    while d*d <= x:
        if x % d == 0:
            f.append(d)
            while x % d == 0: x //= d
        d += 1
    if x > 1: f.append(x)
    return f
gprim = []; lqnr = []
for q in pp.tolist():
    fs = phi_factors(q-1)
    g = 2
    while any(pow(g, (q-1)//r, q) == 1 for r in fs): g += 1
    gprim.append(g)
    h = 2
    while pow(h, (q-1)//2, q) != q-1: h += 1
    lqnr.append(h)
gprim = np.array(gprim); lqnr = np.array(lqnr); Up = U[sel]
out['spearman_U_vs_least_primitive_root'] = float(spearmanr(Up, gprim)[0])
out['spearman_U_vs_least_QNR_recomputed'] = float(spearmanr(Up, lqnr)[0])
out['max_least_primitive_root_le_2e5'] = int(gprim.max()); out['max_least_QNR_le_2e5'] = int(lqnr.max())
out['mean_U_by_least_QNR_(3,5,7,>=11)'] = [float(Up[lqnr == 3].mean()), float(Up[lqnr == 5].mean()), float(Up[lqnr == 7].mean()), float(Up[lqnr >= 11].mean())]
out['n_p1mod4'] = int(len(pp))
json.dump(out, open('data/z52b/pass2/TO2/an9.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
# Z0696 (tie-aware Spearman; an4 used argsort ranks which are tie-naive): U and k1 vs #QNR <= log p
qn = np.array([sum(1 for q in range(2, int(np.log(x))+1) if pow(q, (x-1)//2, x) == x-1) for x in pp.tolist()])
k1 = M[sel, 10].astype(float)
out['spearman_U_numQNR_le_logp'] = float(spearmanr(Up, qn)[0])
out['spearman_k1_numQNR_le_logp'] = float(spearmanr(k1, qn)[0])
out['pearson_logU_numQNR'] = float(np.corrcoef(np.log(Up), qn)[0, 1])
json.dump(out, open('data/z52b/pass2/TO2/an9.json', 'w'), indent=1)
print({k: out[k] for k in ['spearman_U_numQNR_le_logp','spearman_k1_numQNR_le_logp','pearson_logU_numQNR']})
