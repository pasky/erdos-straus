"""Per-prime classes: F/U = forced/unforced; sub-jac = killed by χ_{-e}; sub-twist = killed by another odd real
(genus-twist) character only; sub-nonreal = killed only by non-real (2-power order) characters; F-all = #forced windows.
Optional 2nd arg EMIN restricts to windows e ≥ EMIN (selection check: m_II-hard primes fail every e < m_II ≤ 107).
Where does the hard-prime excess of obstructed windows sit, and is it explained by BM-layer data?
Per prime: counts (per window class) of U:jac (unforced windows killed by χ_{-e} = χ_p on factors), F-pov, F-ok, U-ok;
covariates: qr = fraction of primes 11 ≤ ℓ ≤ 97 with (ℓ/p) = 1 (controls are matched mod 840, so ℓ ≤ 7 agree),
w = mean ω(N_e) over the windows.  OLS  y ~ 1 + qr + w + hard, with classical t-statistics.
Counts are normalised per 500 windows (409 and 577 have fewer valid windows since e < 3p)."""
import sys, json, gzip
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
from z52d_fourier_lib import jacobi, small_primes
P = json.load(open('../data/z52d/fourier/primes.json')); hard = set(P['hard'])
EMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 0
print('windows with e >=', EMIN)
op = gzip.open if sys.argv[1].endswith('.gz') else open
D = defaultdict(lambda: defaultdict(float))
for l in op(sys.argv[1], 'rt'):
    r = json.loads(l); d = D[r['p']]
    if r['e'] < EMIN: continue
    cls = ('F' if r['forced'] else 'U') + '-' + r['type']
    if r['type'] == 'sub': cls += '-jac' if r['kill_jac'] else '-twist' if r['kill_real'] else '-nonreal'
    d[cls] += 1; d['n'] += 1; d['wsum'] += r['omega']; d['F-all'] += r['forced']
ls = [l for l in small_primes(100) if 11 <= l <= 97]
ps = sorted(D)
X = []; Y = defaultdict(list)
for p in ps:
    d = D[p]
    qr = sum(1 for l in ls if jacobi(p, l) == 1) / len(ls)
    X.append([1.0, qr, d['wsum'] / d['n'], 1.0 if p in hard else 0.0])
    for k in ('U-sub-jac', 'U-sub-twist', 'U-pov', 'U-ok', 'F-all', 'F-pov', 'F-sub-twist', 'F-sub-nonreal', 'F-ok'):
        Y[k].append(d[k] / d['n'] * 500)  # per 500 windows (p = 409, 577 have only e < 3p)
X = np.array(X)
print('mean qr hard %.3f ctrl %.3f; mean ω hard %.3f ctrl %.3f' % (X[X[:, 3] == 1, 1].mean(), X[X[:, 3] == 0, 1].mean(),
                                                           X[X[:, 3] == 1, 2].mean(), X[X[:, 3] == 0, 2].mean()))
for k, y in Y.items():
    y = np.array(y)
    raw = y[X[:, 3] == 1].mean() - y[X[:, 3] == 0].mean()
    b, res, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ b; s2 = resid @ resid / (len(y) - X.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    print(f'{k:10s} raw hard−ctrl {raw:+7.2f} | OLS qr {b[1]:+8.1f} (t={b[1]/se[1]:+.1f})  ω {b[2]:+8.1f} (t={b[2]/se[2]:+.1f})'
          f'  hard {b[3]:+6.2f} (t={b[3]/se[3]:+.1f})')
