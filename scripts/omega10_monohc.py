"""OMEGA10: hill-climb for a counterexample to MONO with all weights w_E<=2:
maximise G_{F(1-A)}/G_F.  Usage: omega10_monohc.py q n k steps seed"""
import sys, numpy as np
from omega10_gen import *
q, n, k, steps, seed = map(int, sys.argv[1:6])
rng = np.random.default_rng(seed)
def Lam(f, lam):
    g = f.copy()
    for v in range(f.ndim):
        g = lam[v]*g - (lam[v]-1)*g.mean(axis=v, keepdims=True)
    return g
def G(F, lam): return (F*Lam(F, lam)).mean()
def score(st):
    ev, A, a = st
    s = max(sum(a[c] for c in E) for E in ev + [A])
    lam = 2 ** (a / max(s, 1e-12))
    F0 = good_indicator(q, n, ev); F1 = good_indicator(q, n, ev + [A])
    return G(F1, lam) / G(F0, lam)
st = (random_system(rng, q, n, k, 3), random_system(rng, q, n, k, 1)[0], rng.random(n))
best = score(st); top = best
for s in range(steps):
    ev, A, a = st; ev = list(ev); A = dict(A); a = a.copy(); r = rng.random()
    if r < 0.25: ev += random_system(rng, q, n, k, 1)
    elif r < 0.4 and len(ev) > 1: ev.pop(rng.integers(len(ev)))
    elif r < 0.55: ev[rng.integers(len(ev))] = random_system(rng, q, n, k, 1)[0]
    elif r < 0.7: A = random_system(rng, q, n, k, 1)[0]
    else: a[rng.integers(n)] = rng.random() * rng.choice([0, 1, 3])
    new = (ev, A, a); sc = score(new)
    if sc >= best or rng.random() < 0.02: st, best = new, sc
    top = max(top, sc)
print(f"q={q} n={n} k={k}: max G(F(1-A))/G(F) = {top:.6f}")
