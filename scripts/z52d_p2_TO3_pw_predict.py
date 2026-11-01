"""Fix round TO3 (Z0733): PW's Poisson heuristic (arXiv:2511.16817 Sec. 1: P(no solution at p) = exp(-(log p)^3/m))
applied to the window (m^2, 2m^2): expected number of exceptional primes vs the observed failing-prime counts from the
repo's count outputs (data/z52b/raw/m{m}_pr1e5.txt, primes <= 1e5). Writes data/z52b/pass2/TO3/pw_predict_results.json"""
import json, math
import numpy as np
from sympy import primerange
out = {}
rows = {}
for m in range(20, 49):
    A = np.loadtxt(f'data/z52b/raw/m{m}_pr1e5.txt', dtype=np.int64)
    obs = int(((A[:, 0] > m * m) & (A[:, 0] < 2 * m * m) & (A[:, 1] == 0)).sum())
    ps = list(primerange(m * m + 1, 2 * m * m))
    exp_pois = sum(math.exp(-(math.log(p) ** 3) / m) for p in ps)
    rows[m] = dict(n_primes_in_window=len(ps), observed_fail=obs, PW_poisson_expected=round(exp_pois, 6))
out['per_m'] = rows
out['sum_observed'] = sum(v['observed_fail'] for v in rows.values())
out['sum_expected'] = round(sum(v['PW_poisson_expected'] for v in rows.values()), 6)
json.dump(out, open('data/z52b/pass2/TO3/pw_predict_results.json', 'w'), indent=1)
print({m: rows[m] for m in (20, 30, 48)}, out['sum_observed'], out['sum_expected'])
