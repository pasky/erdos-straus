"""Pass-2 TO3 final small checks: (Z0918) rank correlation of residual U / k2 with h(-4p)/sqrt p (p=1 mod 4 <=2e5);
(Z0924) decade profile of exception counts from the word census (n<=3e6); (Z0970) hall-of-fame membership table.
Writes data/z52b/pass2/TO3/final_results.json"""
import csv, json, math
import numpy as np
from scipy.stats import spearmanr
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
S = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0]
p = np.array([int(r['p']) for r in S]); U = np.array([float(r['U']) for r in S]); k2 = np.array([float(r['k2']) for r in S])
h = np.array([float(r['h4p']) for r in S]); lp = np.log(p.astype(float))
X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
rU = np.log(U) - X @ np.linalg.lstsq(X, np.log(U), rcond=None)[0]
rk2 = np.log(k2) - X @ np.linalg.lstsq(X, np.log(k2), rcond=None)[0]
hn = h / np.sqrt(p)
out['Z0918'] = dict(n=len(p), rho_hn_resU=round(float(spearmanr(hn, rU)[0]), 3), rho_hn_resk2=round(float(spearmanr(hn, rk2)[0]), 3),
                    rho_h_resU=round(float(spearmanr(h, rU)[0]), 3), nss_equals_h4p_over_2_all=True,
                    note='exact check p<=1200 (p=1 mod 4): #supersingular j in F_p = h(-4p)/2 for all 95 primes')
# ---- Z0924 decades from word census ----
W = np.loadtxt('/tmp/z52/words3e6.txt', dtype=np.int64)
n = W[:, 0]; R = W[:, 3]; I3 = W[:, 2]; Uv = W[:, 4]
dec = {}
for lo in [10, 100, 1000, 10**4, 10**5, 10**6]:
    hi = min(10 * lo, 3 * 10**6 + 1)
    s = (n >= lo) & (n < hi)
    dec[f'[{lo},{hi})'] = dict(R0=int((R[s] == 0).sum()), I3_0=int((I3[s] == 0).sum()), Uv0=int((Uv[s] == 0).sum()))
out['Z0924_decades_word_census'] = dec
# ---- Z0970 hall of fame ----
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
A400619 = {2, 5, 73, 1129, 1201, 21169, 118801}
rel = {}
hard_sorted = [int(q) for q in p[np.argsort(U / lp ** 3)][:30]]
rel['U_over_log3_top30'] = hard_sorted
ex = {}
for m in (12, 16, 20):
    W_ = np.loadtxt(f'/tmp/z52/ex_m{m}_1e7.txt', dtype=np.int64) if False else None
import subprocess
fails = {}
for m in (8, 12, 16, 20, 24):
    f = [int(l.split()[0]) for l in open(f'/tmp/z52/ex_m{m}_1e7.txt') if l.split()[1] == '0']
    fails[m] = f
rel['fail_12_16_20_24_last'] = {m: fails[m][-1] for m in fails}
rel['Rzeros_primes_le3e6'] = [int(q) for q in n[(R == 0)] if all(q % d for d in range(2, int(q ** .5) + 1)) and q > 1]
rel['A400619_records'] = sorted(A400619)
rel['Type_A_193_2521_66529'] = [193, 2521, 66529]
cands = [193, 241, 577, 1201, 2521, 3361, 21169, 409, 5569, 9601, 12601, 66529, 20521, 21841, 118801, 83449]
tab = {}
for q in cands:
    tab[q] = dict(in_U_top30=q in hard_sorted, in_fail8=q in fails[8], in_fail12=q in fails[12], in_fail16=q in fails[16],
                  in_fail20=q in fails[20], in_fail24=q in fails[24], in_A400619=q in A400619,
                  in_Rzero=q in rel['Rzeros_primes_le3e6'], in_TypeA=q in rel['Type_A_193_2521_66529'])
out['Z0970_membership'] = tab
json.dump(out, open('data/z52b/pass2/TO3/final_results.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:3500])

# ---- Z0700 decomposition (residual correlations of log U with log eps, log h, log L1) ----
import math as _m
_R = np.array([float(r['Rreal']) for r in S]); _L = np.array([float(r['L1real']) for r in S]); _hr = np.array([float(r['hreal']) for r in S])
_res = lambda y: y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
out['Z0700_residual_decomposition'] = dict(rho_resU_res_logeps=round(float(spearmanr(rU, _res(np.log(_R)))[0]), 3),
                                          rho_resU_res_logh=round(float(spearmanr(rU, _res(np.log(_hr)))[0]), 3),
                                          rho_resU_res_logL1=round(float(spearmanr(rU, _res(np.log(_L)))[0]), 3),
                                          frac_hreal_equals_1=round(float((_hr == 1).mean()), 3))
json.dump(out, open('data/z52b/pass2/TO3/final_results.json', 'w'), indent=1, default=str)
print('Z0700 residual decomposition', out['Z0700_residual_decomposition'])
