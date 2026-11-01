"""Fix round TO3: five-slice certificate counts (Z0700, Z0904).
L3(p) = number of ordered (t,u,v), all >= 2, with tuv-u-v = p (HJ length-3 words with letters >= 2; LENGTH_THREE.md),
computed by /tmp/z52/big/l3.c (source: scripts/z52d_p2_TO3_l3.c). Correlations with residual log U, CF period and log eps_p
on primes 1 mod 4 in (100, 2e5] (base table). Writes data/z52b/pass2/TO3/fiveslice_results.json"""
import csv, json, math
import numpy as np
from scipy.stats import spearmanr
L3 = np.loadtxt('/tmp/z52/big/l3_3e6.txt', dtype=np.int64)
L3d = dict(zip(L3[:, 0].tolist(), L3[:, 1].tolist()))
rows = [r for r in csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t')
        if int(r['mod4']) == 1 and 100 < int(r['p']) and float(r['U']) > 0 and r['Rreal'] != 'NA']
def cfperiod(n):
    a0 = math.isqrt(n); m, d, a = 0, 1, a0; per = 0
    while True:
        m = d * a - m; d = (n - m * m) // d; a = (a0 + m) // d; per += 1
        if a == 2 * a0: break
    return per
p = np.array([int(r['p']) for r in rows]); U = np.array([float(r['U']) for r in rows])
lp = np.log(p.astype(float)); X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
res = lambda y: y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
rU = res(np.log(U))
l3 = np.array([L3d[int(q)] for q in p], dtype=float)
cf = np.array([cfperiod(int(q)) for q in p], dtype=float)
leps = np.array([float(r['Rreal']) for r in rows])
out = {'n': len(p), 'frac_L3_zero': float((l3 == 0).mean())}
out['rho_L3_U_raw'] = round(float(spearmanr(l3, U)[0]), 3)
out['rho_resL3_resU'] = round(float(spearmanr(res(np.log(l3 + 1)), rU)[0]), 3)
out['rho_resL3_rescf'] = round(float(spearmanr(res(np.log(l3 + 1)), res(np.log(cf)))[0]), 3)
out['rho_resL3_reslogeps'] = round(float(spearmanr(res(np.log(l3 + 1)), res(np.log(leps)))[0]), 3)
out['rho_resU_rescf'] = round(float(spearmanr(rU, res(np.log(cf)))[0]), 3)
out['rho_resU_reslogeps'] = round(float(spearmanr(rU, res(np.log(leps)))[0]), 3)
out['rho_resL3_resU_partial_on_cf'] = None
# partial: regress both on resCF and correlate residuals
Xc = np.column_stack([np.ones(len(p)), res(np.log(cf))])
a1 = res(np.log(l3 + 1)); a2 = rU
ra = a1 - Xc @ np.linalg.lstsq(Xc, a1, rcond=None)[0]; rb = a2 - Xc @ np.linalg.lstsq(Xc, a2, rcond=None)[0]
out['pcorr_resL3_resU_given_cf'] = round(float(np.corrcoef(ra, rb)[0, 1]), 3)
out['median_L3_by_resU_quintile'] = [round(float(np.median(l3[(rU >= np.quantile(rU, a)) & (rU < np.quantile(rU, a + .2))])), 1) for a in (0, .2, .4, .6, .8)]
out['ES5_all_primes_1mod8_check'] = None
json.dump(out, open('data/z52b/pass2/TO3/fiveslice_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
