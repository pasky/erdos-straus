"""OMEGA10: test C-exp:  G_F(lam) <= exp( sum_E P(E) (w_E - 2)_+ )  on random systems,
plus structured coincidence systems.  Usage: omega10_cexp.py seed trials lammax"""
import sys, numpy as np
from omega10_gen import *
seed, trials = int(sys.argv[1]), int(sys.argv[2]); lmax = float(sys.argv[3])
rng = np.random.default_rng(seed)
def Gw(F, lam):
    w = es_weights(F); n = F.ndim
    return sum(w[U]*np.prod([lam[i] for i in range(n) if (U>>i)&1]) for U in range(1<<n))
worst = -9
for t in range(trials):
    q = int(rng.choice([2,3,4,5])); n = int(rng.integers(2, 7 if q>3 else 8))
    if rng.random() < 0.3:   # coincidence system on n coords, width 2
        ev = [{i:c, j:c} for i in range(n) for j in range(i+1,n) for c in range(q)]
    else:
        k = int(rng.integers(1, n+1)); m = int(rng.integers(1, 3*n))
        ev = random_system(rng, q, n, k, m)
    lam = 1 + rng.random(n)*(lmax-1)
    F = good_indicator(q, n, ev)
    lhs = np.log(Gw(F, lam))
    rhs = sum(q**-len(E)*max(np.prod([lam[c] for c in E])-2, 0) for E in ev)
    if lhs - rhs > worst:
        worst = lhs - rhs; print("log G - bound = %.4g  (logG=%.4g bound=%.4g)"%(worst,lhs,rhs), q,n,len(ev), flush=True)
