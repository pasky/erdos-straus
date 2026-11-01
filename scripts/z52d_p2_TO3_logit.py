"""Fix round TO3 (Z0802, Z0803, Z0805, Z0843): R-zeros among primes 1 mod 4 (words census + PARI table of
scripts/z52d_p2_TO3_bigtable.py, primes <= 3e6), quantiles, single-feature AUCs, logistic regression with Newton's method,
and a two-line (chi_p, chi_{-4p}) joint model. Writes data/z52b/pass2/TO3/logit_results.json"""
import json, math
import numpy as np
from scipy.stats import norm
T = np.load('/tmp/z52/big/primes_1mod4.npz')
p = T['p']; h4 = T['h4'].astype(float); hr = T['hr'].astype(float); L1 = T['L1']; L4 = T['L4']; lq = T['lqnr'].astype(float)
leg = T['leg']; QS = list(T['QS'])
N = 10**8
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 7))
R = np.asarray(W[p, 2]).astype(float); Uv = np.asarray(W[p, 3]).astype(float)
out = {'n_primes': int(len(p))}
z = R == 0
out['R0_primes_le3e6'] = [int(x) for x in p[z]]
def auc(pos, neg):
    allv = np.concatenate([pos, neg]); rk = allv.argsort().argsort() + 1
    return float((rk[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
def logit_fit(X, y, it=50):
    X1 = np.column_stack([np.ones(len(X)), X]); b = np.zeros(X1.shape[1])
    for _ in range(it):
        mu = 1 / (1 + np.exp(-X1 @ b)); W_ = mu * (1 - mu)
        H = X1.T @ (X1 * W_[:, None]) + 1e-9 * np.eye(X1.shape[1]); g = X1.T @ (y - mu)
        step = np.linalg.solve(H, g); b = b + step
        if np.max(np.abs(step)) < 1e-9: break
    se = np.sqrt(np.diag(np.linalg.inv(H)))
    return b, se
# quantiles of zeros within same size class (|log p - log p0| < 0.1) and same class mod 8
qz = {}
for q, rr in zip(p[z], range(z.sum())):
    i = np.where(p == q)[0][0]
    s = np.abs(np.log(p) - np.log(q)) < 0.1
    s8 = s & (p % 8 == q % 8)
    qz[int(q)] = dict(leastQNR=int(lq[i]), L1_quantile=round(float(np.mean(L1[s] < L1[i])), 3),
                      qnr_quantile=round(float(np.mean(lq[s] < lq[i])), 3),
                      h4_over_sqrt_quantile_mod8=round(float(np.mean((h4[s8] / np.sqrt(p[s8])) < h4[i] / np.sqrt(q))), 3),
                      h4_over_sqrt=round(float(h4[i] / np.sqrt(q)), 4))
out['Z0802_Z0803_zero_quantiles'] = qz
Lq = [v['L1_quantile'] for v in qz.values()]
out['Z0802_n_zeros_L1_quantile_gt_0.85'] = int(sum(1 for x in Lq if x > 0.85))
# Logistic regression on primes <= 3e6 with R=0 (events, 12 of them) ; features: log L1, log(h4/sqrt p), least QNR, Legendre(q/p) q<=47
lp = np.log(p.astype(float))
feat_sets = {
    'logL1': [np.log(L1)],
    'logh4_over_sqrtp': [np.log(h4 / np.sqrt(p))],
    'logL1_logh4': [np.log(L1), np.log(h4 / np.sqrt(p))],
    'logL1_logh4_qnr': [np.log(L1), np.log(h4 / np.sqrt(p)), np.log(lq)],
}
out['Z0843_logistic'] = {}
for name, fs in feat_sets.items():
    X = np.column_stack(fs); b, se = logit_fit(X, z.astype(float))
    score = X @ b[1:]
    out['Z0843_logistic'][name] = dict(coef=[round(float(c), 3) for c in b[1:]], se=[round(float(s), 3) for s in se[1:]],
                                       intercept=round(float(b[0]), 3), auc_in_sample=round(auc(score[z], score[~z]), 3))
# multi-feature with Legendre symbols of small primes and 1[q | 4Cp+1] style (only Legendre here)
Xl = np.column_stack([np.log(L1), np.log(h4 / np.sqrt(p))] + [leg[:, j].astype(float) for j in range(len(QS))])
b, se = logit_fit(Xl, z.astype(float))
out['Z0843_logistic_with_legendre47'] = dict(coef_logL1=round(float(b[1]), 3), coef_logh=round(float(b[2]), 3),
                                              n_features=int(Xl.shape[1]), note='only 12 events; coefficients not significant individually')
out['Z0843_auc_single'] = dict(L1=round(auc(np.log(L1)[z], np.log(L1)[~z]), 3), h4=round(auc(-np.log(h4 / np.sqrt(p))[z], -np.log(h4 / np.sqrt(p))[~z]), 3))
# Z0805: two-line model: log R on log L1 and log L4 (R>0), then P(R=0) via P(log R < log 1.5); compare with joint zeros R=0 & Uv=0
m = R > 0
Xj = np.column_stack([np.ones(m.sum()), np.log(L1[m]), np.log(L4[m])])
bj = np.linalg.lstsq(Xj, np.log(R[m]), rcond=None)[0]; sd = np.std(np.log(R[m]) - Xj @ bj)
mu_all = bj[0] + bj[1] * np.log(L1) + bj[2] * np.log(L4)
pz = norm.cdf((math.log(1.5) - mu_all) / sd)
out['Z0805_two_line_model'] = dict(coef=[round(float(c), 3) for c in bj], sd_logR=round(float(sd), 3),
                                   expected_R0_model=round(float(pz.sum()), 4), observed_R0=int(z.sum()))
Xc = np.column_stack([np.ones(len(p)), np.log(L1), np.log(L4)])
bu = np.linalg.lstsq(Xc[Uv > 0], np.log(Uv[Uv > 0]), rcond=None)[0]
sdu = np.std(np.log(Uv[Uv > 0]) - Xc[Uv > 0] @ bu)
pu = norm.cdf((math.log(1.5) - (Xc @ bu)) / sdu)
out['Z0805_joint_R0_and_Uv0'] = dict(expected_joint_indep=round(float((pz * pu).sum()), 6), observed_joint=int(((R == 0) & (Uv == 0)).sum()),
                                     Uv_coef=[round(float(c), 3) for c in bu], sd_logUv=round(float(sdu), 3),
                                     Uv0_observed=int((Uv == 0).sum()), expected_Uv0=round(float(pu.sum()), 4))
corr = float(np.corrcoef(np.log(L1), np.log(L4))[0, 1])
out['Z0805_corr_logL1_logL4'] = round(corr, 3)
json.dump(out, open('data/z52b/pass2/TO3/logit_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:600])
