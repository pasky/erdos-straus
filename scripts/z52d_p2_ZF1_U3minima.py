"""Z0929 / Z0885 (ZF1 finisher): decade minima of U(p)/log³p and the search for primes beating 2521 (0.0187).
Data (fast exact U, scripts/z52d_p2_ZF1_fastU.c):
  full: all primes ≤ 1e6 (data/z52b/pass2/ZF1/Z0947/U_allprimes_le1e6.txt.gz);
  hard-class full: all 18 143 primes ≡ 1,121,169,289,361,529 (mod 840) in (1e6, 1e7] (Urecords/U_hardclasses_1e6_1e7.txt.gz);
  model-guided: top-K hard-class primes by the partial Euler product S(p) = Σ_{q≤400} −log(1−χ_p(q)/q)
     (scripts/z52d_p2_ZF1_Lproxy_top.c): K = 1000 of 158 955 in [1e7,1e8), 120 of 1 408 113 in [1e8,1e9),
     24 of 4 345 498 in [1e9, 4e9)  (U3minima/U_model.txt);
  random: 300/120 random primes per window 1e6…1e8 (Z0947/U_window_samples.txt); pseudosquare controls (Z0762).
Run: uv run --with numpy python scripts/z52d_p2_ZF1_U3minima.py
"""
import numpy as np, json, os, gzip, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Z = os.path.join(ROOT, 'data/z52b/pass2/ZF1')
def load(fn):
    op = gzip.open if fn.endswith('.gz') else open
    return np.loadtxt(op(fn, 'rt'), dtype=np.int64, ndmin=2)
A = load(os.path.join(Z, 'Z0947/U_allprimes_le1e6.txt.gz'))
H = load(os.path.join(Z, 'Urecords/U_hardclasses_1e6_1e7.txt.gz'))
M = load(os.path.join(Z, 'U3minima/U_model.txt'))
Wn = load(os.path.join(Z, 'Z0947/U_window_samples.txt'))
Pc = {}
for line in open(os.path.join(Z, 'Z0762/U_controls.txt')):
    a, b = line.split(); Pc[int(a)] = int(b)
r3 = lambda p, U: U / np.log(p.astype(float)) ** 3
out = {'decades': []}
def rec(lo, hi, p, U, method):
    m = (p >= lo) & (p < hi) & (p % 4 == 1)
    if not m.any(): return
    v = r3(p[m], U[m]); i = int(np.argmin(v))
    out['decades'].append(dict(lo=lo, hi=hi, method=method, n=int(m.sum()), min_U_over_log3=round(float(v[i]), 5),
                               argmin=int(p[m][i]), U=int(U[m][i]), median=round(float(np.median(v)), 4)))
for lo in (10**2, 10**3, 10**4, 10**5):
    rec(lo, 10 * lo, A[:, 0], A[:, 1], 'all primes p ≡ 1 (4)')
rec(10**6, 10**7, H[:, 0], H[:, 1], 'all Mordell-hard-class primes')
rec(10**6, 10**7, Wn[:, 0], Wn[:, 1], 'random sample (all classes)')
rec(10**7, 10**8, Wn[:, 0], Wn[:, 1], 'random sample (all classes)')
rec(10**7, 10**8, M[:, 0], M[:, 1], 'model-guided top-1000 hard (S-proxy)')
rec(10**8, 10**9, M[:, 0], M[:, 1], 'model-guided top-120 hard (S-proxy)')
rec(10**9, 4 * 10**9, M[:, 0], M[:, 1], 'model-guided top-24 hard (S-proxy)')
pc = np.array(sorted(Pc.items()), dtype=np.int64)
rec(10**8, 10**9, pc[:, 0], pc[:, 1], 'pseudosquare neighbourhoods (Z0762 controls)')
rec(10**9, 4 * 10**9, pc[:, 0], pc[:, 1], 'pseudosquare neighbourhoods (Z0762 controls)')
# global: any p > 2e5 with U/log^3 p < 0.0187 (2521) or < 0.03 ?
allp = np.concatenate([A[:, 0], H[:, 0], M[:, 0], Wn[:, 0], pc[:, 0]]); allU = np.concatenate([A[:, 1], H[:, 1], M[:, 1], Wn[:, 1], pc[:, 1]])
_, ix = np.unique(allp, return_index=True); allp, allU = allp[ix], allU[ix]
v = r3(allp, allU); big = allp > 2 * 10**5
out['n_primes_total'] = int(len(allp))
out['beats_2521_above_2e5'] = [int(x) for x in allp[big & (v < 0.0187)]]
out['below_0.03_above_2e5'] = sorted([(int(a), int(b), round(float(c), 4)) for a, b, c in zip(allp[big & (v < 0.03)], allU[big & (v < 0.03)], v[big & (v < 0.03)])], key=lambda t: t[2])[:40]
out['n_below_0.03_above_2e5'] = int((big & (v < 0.03)).sum())
# model validation in [1e6,1e7]: rank by S of the bottom primes (recomputed here)
json.dump(out, open(os.path.join(Z, 'U3minima/minima.json'), 'w'), indent=1)
for d in out['decades']: print(d)
print('beats 2521:', out['beats_2521_above_2e5'], ' #below 0.03 above 2e5:', out['n_below_0.03_above_2e5'])
print(out['below_0.03_above_2e5'][:15])
