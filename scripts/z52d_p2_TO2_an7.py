# TO2 part 7: Z0528/Z0531 (exact Type I / Type II counts for p≡1 mod 24, p<=1e6 via bs_corr_count.c), Z0565 (h(-4p) mod 8 vs counts)
import numpy as np, json
from scipy.stats import spearmanr
out = {}
F = np.loadtxt('data/z52b/pass2/TO2/fIfII_p24_1e6.txt', dtype=np.int64)
p, fI, fII = F[:, 0], F[:, 1], F[:, 2]
out['n_primes_p1mod24_le_1e6'] = int(len(p))
out['zeros_fI'] = int((fI == 0).sum()); out['zeros_fII'] = int((fII == 0).sum())
out['min_fI_over_log3'] = float((fI / np.log(p.astype(float))**3).min()); out['min_fII_over_log3'] = float((fII / np.log(p.astype(float))**3).min())
out['argmin_fI'] = int(p[np.argmin(fI)]); out['argmin_fII'] = int(p[np.argmin(fII)])
L = np.log(p.astype(float))
out['pearson_log'] = float(np.corrcoef(np.log(fI), np.log(fII))[0, 1])
out['spearman'] = float(spearmanr(fI, fII)[0])
# residual correlation after regressing on log p and log p^2
X = np.column_stack([np.ones_like(L), L, L**2])
rI = np.log(fI) - X @ np.linalg.lstsq(X, np.log(fI), rcond=None)[0]
rII = np.log(fII) - X @ np.linalg.lstsq(X, np.log(fII), rcond=None)[0]
out['resid_corr_after_logp_quadratic'] = float(np.corrcoef(rI, rII)[0, 1])
# bottom-5% joint
q_I = np.quantile(fI, 0.05); q_II = np.quantile(fII, 0.05)
both = int(((fI <= q_I) & (fII <= q_II)).sum()); exp = (fI <= q_I).mean() * (fII <= q_II).sum()
out['bottom5pct_joint_observed_vs_indep_expect'] = [both, float(exp)]
out['mean_fI_over_log2_by_window'] = {}
for lo, hi in [(1e3, 1e4), (1e4, 1e5), (1e5, 1e6)]:
    m = (p >= lo) & (p < hi)
    out['mean_fI_over_log2_by_window'][f'{int(lo)}-{int(hi)}'] = [float((fI[m]/np.log(p[m].astype(float))**2).mean()), float((fII[m]/np.log(p[m].astype(float))**2).mean()), int(m.sum())]
# Z0565: h(-4p) mod 8 vs normalised R (R from /tmp/r1e7.txt) and U (repo count) for p≡1 mod 4 ≤ 2e5
H = np.loadtxt('data/z52b/pass2/TO2/hD_p1mod4_2e5.txt', dtype=np.int64)
hp, h4 = H[:, 0], H[:, 1]
Rf = np.loadtxt('/tmp/r1e7.txt', dtype=np.int64); Rmap = np.zeros(10**7+1, np.int64); Rmap[Rf[:, 0]] = Rf[:, 1]
R = Rmap[hp].astype(float); Lp = np.log(hp.astype(float))**2
tab = {}
for r in range(8):
    m = (h4 % 8 == r)
    tab[r] = [int(m.sum()), float((R[m]/Lp[m]).mean())]
out['h4mod8_count_and_mean_R_over_log2'] = tab
out['R_zero_by_h4mod8'] = {r: int(((R == 0) & (h4 % 8 == r)).sum()) for r in range(8)}
json.dump(out, open('data/z52b/pass2/TO2/an7.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
