"""Z0786: number of elliptic curves (Cremona allcurves, all curves, not classes) of conductor N in {p,2p,4p,8p,16p}
vs the ES count U(p), for primes p = 1 (mod 4), 101 <= p <= 30000 (N=16p <= 480000 < 500000).
Data: https://github.com/JohnCremona/ecdata allcurves/*  (downloaded to /tmp/z52d_big/G2/ec/, 113 MB, not in repo).
Run: ulimit -v 4000000; uv run --with numpy --with sympy python scripts/z52d_p2_NC0_Z0786.py
"""
import glob, os, json, collections
import numpy as np
from scipy.stats import spearmanr
from sympy import primerange
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cnt = collections.Counter(); maxN = 0
for f in glob.glob('/tmp/z52d_big/G2/ec/allcurves.*'):
    with open(f) as fh:
        for line in fh:
            N = int(line.split(None, 1)[0]); cnt[N] += 1
print('curves read:', sum(cnt.values()), 'max conductor:', max(cnt))
F = np.loadtxt(ROOT + '/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
U = {int(r[0]): int(r[1]) for r in F}
ps = [p for p in primerange(101, 30001) if p % 4 == 1]
ps = [p for p in ps if p in U]
p = np.array(ps, dtype=float); y = np.log(np.array([U[q] for q in ps], dtype=float) + 1)
base = np.vstack([np.ones_like(p), np.log(p), np.log(np.log(p))]).T
res = y - base @ np.linalg.lstsq(base, y, rcond=None)[0]
out = {'n_primes': len(ps)}
for k in [1, 2, 4, 8, 16]:
    c = np.array([cnt.get(k * q, 0) for q in ps], dtype=float)
    rho, pv = spearmanr(c, res)
    # residual of log(c+1) on the same base (to remove the growth of counts with p)
    lc = np.log(c + 1); rc = lc - base @ np.linalg.lstsq(base, lc, rcond=None)[0]
    rho2, pv2 = spearmanr(rc, res)
    out[f'N={k}p'] = dict(mean_count=round(float(c.mean()), 3), zero_rate=round(float((c == 0).mean()), 4),
                          spearman_raw=round(float(rho), 4), p_raw=round(float(pv), 4),
                          spearman_resid_count=round(float(rho2), 4), p_resid=round(float(pv2), 4))
# control: N = 3p (not an 'ES-natural' conductor) and N = p+2 (random-like)
for lab, f in [('N=3p (control)', lambda q: 3 * q), ('N=p+2 (control)', lambda q: q + 2)]:
    c = np.array([cnt.get(f(q), 0) for q in ps], dtype=float)
    rho, pv = spearmanr(c, res); out[lab] = dict(mean_count=round(float(c.mean()), 3), spearman_raw=round(float(rho), 4), p_raw=round(float(pv), 4))
# also: is the ES residual correlated with curves of conductor p itself, restricted to p with >=1 curve?
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0786_ec_corr.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
