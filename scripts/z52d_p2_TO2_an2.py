# TO2 analysis part 2 (Schinzel m/p family from repo raw files m{m}_pr1e5.txt; cols: p U D O minz ...; U = #unordered 3-unit-fraction reps of m/p)
import numpy as np, math, json
out = {}
data = {}
for m in range(5, 49):
    d = np.loadtxt(f'data/z52b/raw/m{m}_pr1e5.txt', dtype=np.int64, usecols=(0, 1))
    data[m] = d  # p, U
# Z0566 / Z0478-ish: smallest m with a prime p in (m^2, 2m^2) having U=0
first_fail = None; fails_by_m = {}
for m in range(5, 49):
    p, U = data[m][:, 0], data[m][:, 1]
    sel = (p > m*m) & (p < 2*m*m)
    f = p[sel & (U == 0)]
    fails_by_m[m] = [int(x) for x in f]
    if len(f) and first_fail is None: first_fail = m
out['smallest_m_with_failure_in_(m^2,2m^2)'] = first_fail
out['failures_in_(m^2,2m^2)_m5_to_48'] = {m: v[:6] for m, v in fails_by_m.items() if v}
out['count_m_with_any_failure_in_(m^2,2m^2)'] = sum(1 for v in fails_by_m.values() if v)
# Z0521/Z0511 style: failures of m/p over all primes p<=1e5 by m
tab = {}
for m in range(5, 49):
    p, U = data[m][:, 0], data[m][:, 1]
    big = p > 1000
    tab[m] = dict(n_primes_gt1000=int(big.sum()), fails_gt1000=int(((U == 0) & big).sum()),
                  largest_fail=int(p[(U == 0)].max()) if (U == 0).any() else None)
out['schinzel_table'] = tab
# Z0514 / Z0515: largest exceptional prime (<=1e5) per m vs PW table values quoted in the item (m=8:241, m=12:12241, m=15:20521)
out['pw_quoted_check'] = {m: tab[m]['largest_fail'] for m in (8, 12, 15)}
# Z0559: Poisson calibration: P(U=0) for primes p in [10^3, 1e5] vs (log p)^3/m
cal = []
for m in range(5, 49):
    p, U = data[m][:, 0], data[m][:, 1]
    sel = p > 1000
    x = np.log(p[sel].astype(float))**3 / m
    z = (U[sel] == 0)
    cal.append((m, float(z.mean()), float(np.median(x)), int(z.sum())))
out['calibration_m_frac0_medLog3overm_nzero'] = cal
json.dump(out, open('data/z52b/pass2/TO2/an2.json', 'w'), indent=1)
print(json.dumps({k: out[k] for k in ['smallest_m_with_failure_in_(m^2,2m^2)', 'count_m_with_any_failure_in_(m^2,2m^2)', 'pw_quoted_check']}, default=str))
print(json.dumps(out['failures_in_(m^2,2m^2)_m5_to_48'], default=str)[:1500])
for m in [5,6,7,8,9,10,11,12,13,14,15,16,20,24,30,36,40,48]:
    print(m, tab[m])
print(cal[:12])
# --- Z0566 / Z0559 calibration: no-failure m list, and log-linear fit of P(U=0) vs (log p)^3/m over p in (1e4,1e5]
nofail = [m for m in range(5, 49) if not fails_by_m[m]]
print('m in [5,48] with NO prime p in (m^2,2m^2) failing (p<=1e5):', nofail)
rows = []
for m in range(5, 49):
    p, U = data[m][:, 0], data[m][:, 1]
    sel = (p > 1e4)
    f = float((U[sel] == 0).mean())
    x = float(np.mean(np.log(p[sel].astype(float))**3 / m))
    rows.append((m, f, x, int((U[sel] == 0).sum())))
rows_pos = [r for r in rows if r[1] > 0]
X = np.array([r[2] for r in rows_pos]); Y = np.log(np.array([r[1] for r in rows_pos]))
A = np.vstack([X, np.ones_like(X)]).T
coef, res, *_ = np.linalg.lstsq(A, Y, rcond=None)
pred = A @ coef
r2 = 1 - ((Y - pred)**2).sum() / ((Y - Y.mean())**2).sum()
print('fit log P(U=0) = a + b*(mean (log p)^3/m) over m with fails, p in (1e4,1e5]:', coef, 'R2', r2, 'n_m', len(X))
print('rows (m, frac0, mean x, count0):', [(r[0], round(r[1], 5), round(r[2], 2), r[3]) for r in rows])
out['fit_logP0_vs_x'] = dict(slope=float(coef[0]), intercept=float(coef[1]), R2=float(r2), n_m=int(len(X)))
out['nofail_m'] = nofail
out['calib_rows_m_frac0_meanx_count0_p>1e4'] = rows
json.dump(out, open('data/z52b/pass2/TO2/an2.json', 'w'), indent=1)
