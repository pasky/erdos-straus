"""Pass-2 TO3 (Z0797): representation numbers r_Q(p) of diagonal positive ternary forms Q=x^2+a y^2+b z^2 (1<=a<=b<=20)
at primes p=1 mod 4, p<=2e4; Spearman with the residual log U(p) (after log p, loglog p). Multiple forms => report the
distribution and the best |rho|, not a single claim. Writes data/z52b/pass2/TO3/forms_results.json"""
import numpy as np, csv, json, math
from scipy.stats import spearmanr
NMAX = 20000
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
pr = [int(r['p']) for r in rows if int(r['mod4']) == 1 and 100 < int(r['p']) <= NMAX]
U = np.array([float(r['U']) for r in rows if int(r['mod4']) == 1 and 100 < int(r['p']) <= NMAX])
lp = np.log(np.array(pr, dtype=float))
X = np.column_stack([np.ones(len(pr)), lp, np.log(lp)])
resU = np.log(U) - X @ np.linalg.lstsq(X, np.log(U), rcond=None)[0]
isp = np.zeros(NMAX + 1, bool); isp[pr] = True
out = {'n_primes': len(pr), 'NMAX': NMAX}
res = []
prime_idx = np.array(pr)
for a in range(1, 21):
    for b in range(a, 21):
        cnt = np.zeros(NMAX + 1, dtype=np.int64)
        R = int(math.isqrt(NMAX)) + 1
        xs = np.arange(-R, R + 1)
        yb = int(math.isqrt(NMAX // a)) + 1; zb = int(math.isqrt(NMAX // b)) + 1
        ys = np.arange(-yb, yb + 1); zs = np.arange(-zb, zb + 1)
        XX, YY, ZZ = np.meshgrid(xs, ys, zs, indexing='ij')
        Q = XX * XX + a * YY * YY + b * ZZ * ZZ
        Q = Q[(Q <= NMAX) & (Q > 0)]
        cnt += np.bincount(Q, minlength=NMAX + 1)
        r = cnt[prime_idx].astype(float)
        rho = float(spearmanr(r, resU)[0]) if r.std() > 0 else float('nan')
        res.append((a, b, rho))
res = [t for t in res if not math.isnan(t[2])]
best = sorted(res, key=lambda t: -abs(t[2]))[:8]
out['n_forms'] = len(res)
out['best_forms_by_abs_rho'] = [(a, b, round(r, 3)) for a, b, r in best]
out['median_abs_rho'] = round(float(np.median([abs(t[2]) for t in res])), 3)
out['frac_forms_abs_rho_gt_0.2'] = round(float(np.mean([abs(t[2]) > 0.2 for t in res])), 3)
out['rho_x2_y2_z2'] = [round(t[2], 3) for t in res if (t[0], t[1]) == (1, 1)]
out['rho_x2_y2_4z2'] = [round(t[2], 3) for t in res if (t[0], t[1]) == (1, 4)]
json.dump(out, open('data/z52b/pass2/TO3/forms_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
