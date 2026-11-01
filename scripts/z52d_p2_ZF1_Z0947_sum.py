"""Z0947 (ZF1 finisher): S(N) = Σ_{p≤N} O(p) (ordered ES solution counts at primes) / (N log²N), N = 1e3 … 1e8.
Exact for N ≤ 1e6 (fast U for all 78 498 primes ≤ 1e6, scripts/z52d_p2_ZF1_fastU.c; O = 3(T1+T2)).  For 1e6 < N ≤ 1e8:
20 log-spaced windows, 300 (≤1e7) / 120 (>1e7) uniformly random primes per window (seed 12345, /tmp/zf1/winsample.py),
window sum ≈ mean(O)·π(window) with standard error; cumulative sums and 1σ errors.  Fits ratio = c + d/log N.
Run: uv run --with numpy python scripts/z52d_p2_ZF1_Z0947_sum.py
"""
import numpy as np, json, os, gzip, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data/z52b/pass2/ZF1/Z0947')
A = np.loadtxt(gzip.open(os.path.join(D, 'U_allprimes_le1e6.txt.gz'), 'rt'), dtype=np.int64)
p = A[:, 0]; O = 3 * (A[:, 2] + A[:, 3])
B = np.loadtxt(os.path.join(D, 'U_window_samples.txt'), dtype=np.int64)
info = json.load(open(os.path.join(D, 'win_info.json')))
pb = B[:, 0]; Ob = 3 * (B[:, 2] + B[:, 3])
rows = []
def add(N, S, se):
    L = math.log(N); rows.append(dict(N=N, S=float(S), se=float(se), ratio=S / (N * L * L), ratio_se=se / (N * L * L), ratio_loglog=S / (N * L * L * math.log(L))))
for N in [10**3, 10**4, 5 * 10**4, 10**5, 2 * 10**5, 5 * 10**5, 10**6]:
    add(N, O[p <= N].sum(), 0.0)
S = float(O.sum()); var = 0.0
wins = []
for w in info:
    m = (pb >= w['lo']) & (pb < w['hi'])
    v = Ob[m].astype(float); n = w['nprimes']
    S += v.mean() * n; var += (v.std(ddof=1) / math.sqrt(len(v)) * n) ** 2
    L = math.log(math.sqrt(w['lo'] * w['hi']))
    wins.append(dict(lo=w['lo'], hi=w['hi'], k=int(len(v)), mean_O=float(v.mean()), mean_O_over_log3=float((v / np.log(pb[m]) ** 3).mean()), mean_O_over_log2=float((v / np.log(pb[m]) ** 2).mean())))
    add(w['hi'], S, math.sqrt(var))
Ns = np.array([r['N'] for r in rows], float); R = np.array([r['ratio'] for r in rows]); Lg = np.log(Ns)
c, d = np.linalg.lstsq(np.column_stack([np.ones(len(Ns)), 1 / Lg]), R, rcond=None)[0]
c2, d2, e2 = np.linalg.lstsq(np.column_stack([np.ones(len(Ns)), 1 / Lg, 1 / Lg ** 2]), R, rcond=None)[0]
# local mean O(p)/log^2 p and /log^3 p trend (what the ratio converges to: mean O(p)/(log p)^3 · (log p / log N)...)
out = dict(rows=rows, windows=wins, fit_c_plus_d_over_logN=[float(c), float(d)], fit_quadratic_in_1_over_logN=[float(c2), float(d2), float(e2)],
           rms_resid_linear=float(np.sqrt(np.mean((R - (c + d / Lg)) ** 2))))
json.dump(out, open(os.path.join(D, 'sum.json'), 'w'), indent=1)
for r in rows: print(r['N'], round(r['ratio'], 4), '±', round(r['ratio_se'], 4), round(r['ratio_loglog'], 4))
print('fit c + d/logN:', c, d, ' quad:', c2, d2, e2)
for w in wins: print(w['lo'], w['hi'], round(w['mean_O_over_log3'], 3), round(w['mean_O_over_log2'], 2))
