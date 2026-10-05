"""OMEGA10 numerics (see POINTWISE_OMEGA10.md)."""
import sys, numpy as np
from omega10_gen import *
rng = np.random.default_rng(int(sys.argv[1]))
worst = {"max":-9,"min":-9}
for t in range(int(sys.argv[2])):
    q = int(rng.choice([2,3,4,5])); n = int(rng.integers(2, 7 if q>3 else 8))
    k = int(rng.integers(1, n+1)); m = int(rng.integers(1, 3*n))
    ev = random_system(rng, q, n, k, m)
    lam = 1 + rng.random(n)*rng.choice([0.3,1.0,2.0])
    grids = np.indices((q,)*n)
    h = np.zeros((q,)*n); Wmax = np.zeros((q,)*n); Wmin = np.full((q,)*n, np.inf)
    for E in ev:
        A = np.ones((q,)*n, dtype=bool)
        for c,v in E.items(): A &= grids[c]==v
        wE = np.prod([lam[c] for c in E])
        h = np.maximum(h, A); Wmax = np.where(A, np.maximum(Wmax,wE), Wmax); Wmin = np.where(A, np.minimum(Wmin,wE), Wmin)
    w = es_weights(h)
    Gh = sum(w[U]*np.prod([lam[i] for i in range(n) if (U>>i)&1]) for U in range(1<<n))
    Emax = (h*Wmax).mean(); Emin = (np.where(h>0, Wmin, 0)).mean()
    for key,val in (("max",Gh/Emax-1),("min",Gh/Emin-1)):
        if val > worst[key]:
            worst[key]=val; print(key, "ratio-1=%.4g"%val, q,n,k,m, flush=True)
