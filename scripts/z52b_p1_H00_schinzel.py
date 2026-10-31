"""Z0121 pass-1: largest prime exception P(m) ≤ 1e5 of m/p = 1/x+1/y+1/z for m = 5..48, from the (untracked) raw counts
data/z52b/raw/m{m}_pr1e5.txt of the main checkout (col 0 = p, col 1 = #solutions). Fit log P(m) vs log m and vs
the Pomerance–Weingartner Poisson heuristic (count ≍ (log p)^3/m)."""
import numpy as np, json, os
R = os.environ.get('RAW', '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/')
rows = []
for m in range(5, 49):
    f = R + f'm{m}_pr1e5.txt'
    if not os.path.exists(f): continue
    A = np.loadtxt(f, dtype=np.int64); P, c = A[:, 0], A[:, 1]
    z = P[(c == 0) & (P > m)]                     # p > m (p | m trivial cases excluded)
    hi = (P > 50000)
    rows.append(dict(m=m, n_exc=int(len(z)), last=int(z.max()) if len(z) else 0, exc_frac_5e4_1e5=float((c[hi] == 0).mean()),
                     mean_count_5e4_1e5=float(c[hi].mean()), last5=[int(x) for x in z[-5:]]))
for r in rows: print(r['m'], r['n_exc'], r['last'], round(r['exc_frac_5e4_1e5'], 4), round(r['mean_count_5e4_1e5'], 1), r['last5'])
M = np.array([r['m'] for r in rows]); mc = np.array([r['mean_count_5e4_1e5'] for r in rows])
sel = np.array([0 < r['last'] < 90000 for r in rows])     # unsaturated: largest exception well inside the range
b = np.polyfit(np.log(M[sel]), np.log(np.log([r['last'] for r in np.array(rows)[sel]])), 1)
print('fit log log P(m) = %.3f log m + %.3f  (on %d unsaturated m)' % (b[0], b[1], sel.sum()))
b2 = np.polyfit(np.log(M), np.log(mc), 1); print('mean count at p~7.5e4 ∝ m^%.3f' % b2[0])
json.dump(dict(rows=rows, fit_loglogP_vs_logm=list(b), fit_logcount_vs_logm=list(b2)), open('data/z52b/pass1/H00/schinzel_table.json', 'w'), indent=1)
