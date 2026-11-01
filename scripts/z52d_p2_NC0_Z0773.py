"""Z0773: calibrate ESC(p)/log^2 p vs U(p)/log^2 p over dyadic windows [X,2X] of primes p ≡ 1 (mod 4).
ESC(p) = col 4 of z52d_p2_NC0_Z0773_words.c (words tuv-u-v=n with a coordinate in 4Z or 8Z-n), computed to 3e6.
U(p) = column 1 of data/z52b/raw/f4_all_30000.txt and pr_20001_200000.txt (only available up to 2e5).
Run: ulimit -v 4000000; python3 scripts/z52d_p2_NC0_Z0773.py
"""
import numpy as np, json, subprocess, os
from sympy import primerange
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = '/tmp/z52d_big/G2/'
W = np.loadtxt(TMP + 'words_3e6.txt', dtype=np.int64)  # n W I3 R Uv ESC T1 T2
N = W.shape[0]
n = W[:, 0]; ESC = W[:, 5]; I3 = W[:, 2]
R = ROOT + '/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
G = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
UU = {}
for row in np.vstack([F, G]):
    UU[int(row[0])] = int(row[1])
P = np.array([p for p in primerange(101, N + 1) if p % 4 == 1], dtype=np.int64)
ESCp = ESC[P - 1].astype(float); lp2 = np.log(P.astype(float)) ** 2
out = {'N': N, 'n_primes_1mod4': int(len(P)), 'windows': []}
X = 1000
while 2 * X <= N:
    m = (P >= X) & (P < 2 * X)
    if m.sum() < 20:
        X *= 2; continue
    e = ESCp[m] / lp2[m]
    rec = dict(X=X, count=int(m.sum()), esc_min=float(e.min()), esc_q001=float(np.quantile(e, 0.001)),
               esc_med=float(np.median(e)), esc_min_over_med=float(e.min() / np.median(e)),
               esc_argmin_p=int(P[m][np.argmin(e)]), esc_zero_rate=float((ESCp[m] == 0).mean()))
    if 2 * X <= 200000:
        pu = [p for p in P[m].tolist() if p in UU]
        if len(pu) >= 20:
            u = np.array([UU[p] for p in pu], dtype=float) / np.log(np.array(pu, dtype=float)) ** 2
            rec.update(U_min=float(u.min()), U_q001=float(np.quantile(u, 0.001)), U_med=float(np.median(u)),
                       U_min_over_med=float(u.min() / np.median(u)), U_argmin_p=int(pu[int(np.argmin(u))]),
                       U_zero_rate=float((u == 0).mean()))
    out['windows'].append(rec)
    X *= 2
# stability: coefficient of variation of e over the whole range, and robust min/median ratio across windows
for key in ['esc_min_over_med']:
    out['mean_' + key] = float(np.mean([w[key] for w in out['windows']]))
out['U_mean_min_over_med'] = float(np.mean([w['U_min_over_med'] for w in out['windows'] if 'U_min_over_med' in w]))
out['ESC_mean_min_over_med_le_2e5'] = float(np.mean([w['esc_min_over_med'] for w in out['windows'] if 'U_min' in w]))
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0773_esc_windows.json', 'w'), indent=1)
for w in out['windows']:
    print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in w.items()})
print('mean min/med ESC (windows<=2e5):', round(out['ESC_mean_min_over_med_le_2e5'], 4),
      ' U:', round(out['U_mean_min_over_med'], 4))
