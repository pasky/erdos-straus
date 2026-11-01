"""Fix round TO3 (Z0780, Z0781): Poisson / negative-binomial tests of R-zeros and of the R-value histogram against the
BM main term, on all primes 1 mod 4 in [1e4, 3e5) (M_BM from scripts/z52d_p2_TO3_mbm_full.py). Writes mbm_full_results.json"""
import json, math
import numpy as np
from scipy.optimize import minimize
D = np.load('/tmp/z52/big/mbm_full.npz'); P = D['p']; M = D['M']
N = 10**8
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 7))
R = np.asarray(W[P, 2]).astype(float)
out = {'n_primes': int(len(P)), 'M_range': [round(float(M.min()), 3), round(float(M.max()), 3)]}
bins = [0, 8, 10, 12, 14, 16, 18, 20, 25, 40]
rows = []
for a, b in zip(bins[:-1], bins[1:]):
    s = (M >= a) & (M < b)
    if s.sum() == 0: continue
    rows.append(dict(M_bin=[a, b], n=int(s.sum()), obs_R0=int((R[s] == 0).sum()), exp_R0_poisson=round(float(np.exp(-M[s]).sum()), 4),
                     mean_R=round(float(R[s].mean()), 2), mean_M=round(float(M[s].mean()), 2),
                     frac_R_le2=round(float((R[s] <= 2).mean()), 4)))
out['bins_zero_test'] = rows
out['total_obs_R0'] = int((R == 0).sum()); out['total_exp_R0_poisson'] = round(float(np.exp(-M).sum()), 4)
# negative binomial: P(R=0 | M) = (1 + c*M/k)^(-k) with mean c*M ; fit (c,k) by MLE on zero/non-zero indicator + R>0 using pmf
def nll(th):
    c, k = np.exp(th)
    mu = c * M
    p0 = (1 + mu / k) ** (-k)
    # NB pmf for R (count), use log-likelihood on all points
    from scipy.special import gammaln
    logp = gammaln(R + k) - gammaln(k) - gammaln(R + 1) + k * np.log(k / (k + mu)) + R * np.log(mu / (k + mu))
    return -np.sum(logp)
res = minimize(nll, x0=np.log([1.0, 5.0]), method='Nelder-Mead', options=dict(maxiter=400))
c, k = np.exp(res.x)
out['NB_fit_mean_c_times_M_and_k'] = dict(c=round(float(c), 4), k=round(float(k), 4), nll=round(float(res.fun), 2))
out['NB_expected_R0_total'] = round(float(((1 + c * M / k) ** (-k)).sum()), 3)
# Poisson fit in mean: MLE of c for Poisson pmf
cpois = float(np.sum(R) / np.sum(M))
out['Poisson_fit_c_meanR_over_M'] = round(cpois, 4)
out['Poisson_expected_R0_total_with_c'] = round(float(np.exp(-cpois * M).sum()), 4)
# histogram of R values vs Poisson(c M) for R in {0,2,4,6,8,10,12}
hist = {}
for r in [0, 2, 4, 6, 8, 10, 12]:
    hist[r] = dict(obs=int((R == r).sum()), NB=round(float(np.sum(np.exp(
        __import__('scipy.special', fromlist=['gammaln']).gammaln(r + k) - __import__('scipy.special', fromlist=['gammaln']).gammaln(k) - __import__('scipy.special', fromlist=['gammaln']).gammaln(r + 1)
        + k * np.log(k / (k + c * M)) + r * np.log(c * M / (k + c * M))))), 1))
out['R_value_hist_obs_vs_NB'] = hist
json.dump(out, open('data/z52b/pass2/TO3/mbm_full_results.json', 'w'), indent=1, default=str)
for kk, v in out.items(): print(kk, str(v)[:700])
