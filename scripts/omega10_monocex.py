"""OMEGA10: counterexample to MONO (POINTWISE_OMEGA10 §2): system = all cylinders with an even (>=2) number of mismatches with c=0 on n coords; adding A={x=0} raises G."""
import numpy as np, itertools
from omega10_gen import *
def Lam(f, lam):
    g = f.copy()
    for v in range(f.ndim):
        g = lam[v]*g - (lam[v]-1)*g.mean(axis=v, keepdims=True)
    return g
for q in [3,5,8]:
  for n in [2,3,4]:
    lam = np.full(n, 2**(1/n))
    ev = []
    for T in itertools.combinations(range(n), 2) if n>=2 else []:
        pass
    # bad iff even (>=2) number of mismatches with c=0
    for r in range(2, n+1, 2):
        for T in itertools.combinations(range(n), r):
            for vals in itertools.product(range(1,q), repeat=r):
                E = {v:0 for v in range(n)}
                for v,b in zip(T, vals): E[v]=b
                ev.append(E)
    F = good_indicator(q, n, ev)
    C = {v:0 for v in range(n)}
    F1 = good_indicator(q, n, ev+[C])
    G0 = (F*Lam(F,lam)).mean(); G1 = (F1*Lam(F1,lam)).mean()
    print(f"q={q} n={n} events={len(ev)} S={len(ev)*q**-n:.3f}: G_F={G0:.5f} G_F'={G1:.5f} increase={G1-G0:.3g}")
