"""Z0705/Z0898 check: minz(p) (column 4 of the repo's count program output, see scripts/z52b_fingerprint_count.c)
over the existing per-prime files. Reports max minz/p, max minz/p^2, max log(minz)/log p per file, and a dyadic-ish trend."""
import numpy as np, math, json
R = 'data/z52b/raw/'
files = ['pr_20001_200000.txt', 'pr_1e6_window.txt', 'pr_1e7_window.txt']
out = {}
for f in files:
    A = np.loadtxt(R + f, dtype=np.int64)
    A = A[A[:, 0] % 4 == 1]
    p = A[:, 0].astype(float); m = A[:, 4].astype(float)
    r1 = m / p; r2 = m / p**2; lg = np.log(m) / np.log(p)
    i1, i2, i3 = np.argmax(r1), np.argmax(r2), np.argmax(lg)
    out[f] = dict(n_p1mod4=int(len(A)), pmin=int(p.min()), pmax=int(p.max()),
                  max_minz_over_p=[round(r1[i1], 3), int(p[i1])],
                  max_minz_over_p2=[round(r2[i2], 5), int(p[i2])],
                  max_logminz_over_logp=[round(lg[i3], 4), int(p[i3])],
                  median_minz_over_p=round(float(np.median(r1)), 3),
                  frac_minz_div_p=round(float(np.mean(A[:, 4] % A[:, 0] == 0)), 4),
                  n_minz_over_p2_gt_0p4=int(np.sum(r2 > 0.4)))
    print(f, out[f])
json.dump(out, open('data/z52b/pass1/U04/minz_windows.json', 'w'), indent=1)
