# TO2 part 3: Z0515 (m=12 anomaly vs arithmetic of m), Z0514 (largest exception scale), from an2 raw data
import numpy as np, math, json
from scipy.stats import spearmanr
out = {}
rows = []
for m in range(5, 49):
    d = np.loadtxt(f'data/z52b/raw/m{m}_pr1e5.txt', dtype=np.int64, usecols=(0, 1))
    p, U = d[:, 0], d[:, 1]
    sel = p > 1000
    z = (U[sel] == 0)
    x = float(np.mean(np.log(p[sel].astype(float))**3 / m))
    phi = sum(1 for k in range(1, m+1) if math.gcd(k, m) == 1)
    tau = sum(1 for k in range(1, m+1) if m % k == 0)
    lg = (p[(U == 0)])
    largest = int(lg.max()) if len(lg) else 0
    rows.append(dict(m=m, fails_gt1e3=int(z.sum()), x=x, phi_over_m=phi/m, tau=tau, largest=largest,
                     xlargest=float(np.log(largest)**3/m) if largest else None))
out['rows'] = rows
# rate normalised by Poisson-type exp(-b x) with b from an2 fit, correlation with arithmetic of m (m>=12)
sub = [r for r in rows if r['m'] >= 12]
f = np.array([r['fails_gt1e3'] for r in sub], float)
rho_phi = spearmanr([r['phi_over_m'] for r in sub], f)[0]
rho_tau = spearmanr([r['tau'] for r in sub], f)[0]
rho_x = spearmanr([r['x'] for r in sub], f)[0]
out['spearman_m>=12_fails_vs_phi_over_m'] = float(rho_phi)
out['spearman_m>=12_fails_vs_tau'] = float(rho_tau)
out['spearman_m>=12_fails_vs_x'] = float(rho_x)
out['largest_exc_m12_15_8'] = {r['m']: (r['largest'], r['xlargest']) for r in rows if r['m'] in (8, 12, 15, 16, 20, 24, 36, 48)}
json.dump(out, open('data/z52b/pass2/TO2/an3.json', 'w'), indent=1)
print(json.dumps({k: out[k] for k in out if k != 'rows'}, indent=1, default=str))
for r in rows:
    if r['m'] in (8, 10, 11, 12, 13, 14, 15, 16, 24, 36, 48): print(r)
