# TO2 part 6: size-of-solution analyses from repo count outputs (cols: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm)
# Z0511 (log z_min / log p), Z0521 ((x_min - p/4)/log^2 p), Z0624 (z_min / p^2), Z0610-ish (regime of x_min/p)
import numpy as np, json
D = 'data/z52b/raw/'
a = np.loadtxt(D + 'f4_all_30000.txt', dtype=np.int64); b = np.loadtxt(D + 'pr_20001_200000.txt', dtype=np.int64)
w6 = np.loadtxt(D + 'pr_1e6_window.txt', dtype=np.int64)
A_ = np.vstack([a, b])
s = np.ones(A_[:, 0].max()+1, bool); s[:2] = False
for i in range(2, int(A_[:, 0].max()**0.5)+1):
    if s[i]: s[i*i::i] = False
M = A_[s[A_[:, 0]] & (A_[:, 0] > 5) & (A_[:, 0] % 4 == 1)]
p = M[:, 0].astype(float); zmin = M[:, 4].astype(float); xmin = M[:, 8].astype(float); xmax = M[:, 7].astype(float)
out = {'n_p1mod4_gt5_le_2e5': int(len(M))}
e = np.log(zmin)/np.log(p)
out['log_zmin_over_logp_max'] = float(e.max()); out['argmax'] = int(M[np.argmax(e), 0])
out['log_zmin_over_logp_median'] = float(np.median(e))
out['zmin_over_p2_max'] = float((zmin/p**2).max()); out['zmin_over_p2_argmax'] = int(M[np.argmax(zmin/p**2), 0])
out['zmin_over_p2_median'] = float(np.median(zmin/p**2))
out['zmin_over_p2_p90'] = float(np.percentile(zmin/p**2, 90))
g = (xmin - p/4)/np.log(p)**2
out['(xmin-p/4)/log2p_max'] = float(g.max()); out['argmax'] = int(M[np.argmax(g), 0])
out['(xmin-p/4)/log2p_median'] = float(np.median(g))
out['xmin_over_p_min'] = float((xmin/p).min()); out['xmin_over_p_median'] = float(np.median(xmin/p))
out['xmin_over_p_max'] = float((xmin/p).max())
out['frac_xmin_within_p/4+p^0.5'] = float(np.mean(xmin - p/4 <= np.sqrt(p)))
out['frac_xmin_within_p/4+log2p'] = float(np.mean(xmin - p/4 <= np.log(p)**2))
out['xmin_minus_p4_over_p_max'] = float(((xmin - p/4)/p).max())
json.dump(out, open('data/z52b/pass2/TO2/an6.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
