"""Z1069: logarithmic / inverse weights on the same prime sample.  Primes p = 1 (mod 4), 101 <= p <= 2e5 (U data).
Weights: unweighted; w_tau = 1/tau(p-1) (reciprocal divisor); w_inv = 1/U(p) (inverse witness multiplicity, U>0 only);
w_log = 1/log p (log-weights).  Observables: O1 = U/log^2 p (moment), O2 = 1[U <= 4] (rare-witness frequency),
O3 = 1[R(p)=0] for p <= 3e6 (R from the word census, /tmp/z52d_big/G2/words_3e6.txt; the (*) failure set).
Reports weighted means and the ratio to the unweighted mean (rare-witness moments), and the effective sample size.
Output: data/z52b/pass2/NC0/sub/Z1069_weights.json
Run: ulimit -v 4000000; uv run --with numpy --with sympy python scripts/z52d_p2_NC0_Z1069.py
"""
import numpy as np, json, os
from sympy import primerange, divisor_count
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = ROOT + '/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64); G = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
UU = {int(r[0]): int(r[1]) for r in np.vstack([F, G])}
P = np.array([p for p in primerange(101, 200001) if p % 4 == 1 and p in UU], dtype=np.int64)
U = np.array([UU[int(p)] for p in P], dtype=float)
tau = np.array([divisor_count(int(p) - 1) for p in P], dtype=float)
lp = np.log(P.astype(float))
W = np.loadtxt('/tmp/z52d_big/G2/words_3e6.txt', dtype=np.int64)
Rc = W[:, 3]  # R(n) column (n=1..3e6); R=0 is the (*) failure set
mask3 = P <= 3000000
O1 = U / lp ** 2; O2 = (U <= 4).astype(float)
def stats(w, mask=None):
    m = np.ones(len(P), bool) if mask is None else mask
    ww = w[m]; ww = ww / ww.sum()
    return dict(O1=float((ww * O1[m]).sum()), O2=float((ww * O2[m]).sum()),
                ESS=float(1.0 / (ww ** 2).sum()), n=int(m.sum()))
sch = {'unweighted': np.ones(len(P)), 'w_tau=1/tau(p-1)': 1.0 / tau, 'w_inv=1/U': np.where(U > 0, 1.0 / np.maximum(U, 1), 0.0),
       'w_log=1/log p': 1.0 / lp}
out = {}
for name, w in sch.items():
    out[name] = stats(w)
base = out['unweighted']
for name in out:
    out[name]['O1_ratio_to_unweighted'] = round(out[name]['O1'] / base['O1'], 4)
    out[name]['O2_ratio_to_unweighted'] = round(out[name]['O2'] / max(base['O2'], 1e-12), 4)
# R-zero indicator on p <= 3e6 under the same weight families
Pz = P[mask3]; Rz = np.array([Rc[p - 1] for p in Pz], dtype=float); zero = (Rz == 0).astype(float)
out['R_zero_p_le_3e6'] = {}
for name, w in sch.items():
    ww = w[mask3]; ww = ww / ww.sum()
    out['R_zero_p_le_3e6'][name] = dict(weighted_rate=float((ww * zero).sum()), ESS=float(1.0 / (ww ** 2).sum()))
out['R_zero_p_le_3e6']['count_R_zero'] = int(zero.sum()); out['R_zero_p_le_3e6']['n_primes'] = int(len(Pz))
out['R_zero_primes'] = [int(x) for x in Pz[zero > 0]][:20]
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1069_weights.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
