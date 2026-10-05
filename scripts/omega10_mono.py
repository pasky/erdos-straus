"""OMEGA10: test event-monotonicity  G_{F(1-A)} <= G_F * (1 + P(A)(w_A-2)_+).
Usage: omega10_mono.py seed trials lammax"""
import sys, numpy as np
from omega10_gen import *
seed, trials = int(sys.argv[1]), int(sys.argv[2]); lmax = float(sys.argv[3])
rng = np.random.default_rng(seed)
def Gw(F, lam):
    w = es_weights(F); n = F.ndim
    return sum(w[U]*np.prod([lam[i] for i in range(n) if (U>>i)&1]) for U in range(1<<n))
worst = -9
for t in range(trials):
    q = int(rng.choice([2,3,4,5])); n = int(rng.integers(2, 6 if q>3 else 8))
    k = int(rng.integers(1, n+1)); m = int(rng.integers(0, 3*n))
    ev = random_system(rng, q, n, k, m) if m else []
    A = random_system(rng, q, n, k, 1)
    lam = 1 + rng.random(n)*(lmax-1)
    F0 = good_indicator(q, n, ev) if ev else np.ones((q,)*n)
    F1 = good_indicator(q, n, ev + A)
    wA = np.prod([lam[c] for c in A[0]])
    r = Gw(F1, lam) / (Gw(F0, lam)*(1 + q**-len(A[0])*max(wA-2,0)))
    if r - 1 > worst:
        worst = r - 1; print("ratio-1 = %.4g  wA=%.3f"%(worst, wA), q, n, k, m, flush=True)
