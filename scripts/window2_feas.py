#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.5 -- feasibility LP: fake with nu(empty)=0, minimising the
L-infinity relative correlation residual t (rows scaled by rho).  Reuses the
model construction of window2_lp.py by importing it.  t ~ 0  => fake exists.
Usage: window2_feas.py EPS K THETA [--one] [--dump=F]
"""
import sys, json
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog
import window2_lp as L

def build(eps, K, theta, one):
    # run window2_lp.main's construction by capturing locals via a light refactor
    import itertools
    from math import comb, factorial
    g, w = L.bins(eps, K)
    W = [m for m in L.multisets(g, 1.0, True) if sum(m) % 2 == 0]
    def mu_win(m):
        s = float(np.dot(m, g)); v = max(1 - s, 1e-3) ** -0.5
        for k, mk in enumerate(m): v *= w[k] ** mk / factorial(mk)
        return v
    muW = np.array([mu_win(m) for m in W])
    Vis1 = L.multisets(g, theta, False); sums1 = {s: float(np.dot(s, g)) for s in Vis1}
    configs = [(m,) for m in W] if one else [(a, b) for a in W for b in W]
    mu = muW if one else np.outer(muW, muW).ravel()
    vis = [(s,) for s in Vis1] if one else [(a, b) for a in Vis1 for b in Vis1 if sums1[a] + sums1[b] <= theta + 1e-12]
    vidx = {s: i for i, s in enumerate(vis)}
    Wsub = {}
    for m in W:
        lst = []
        for s in itertools.product(*[range(mk + 1) for mk in m]):
            if s in sums1:
                e = 1
                for mk, sk in zip(m, s): e *= comb(mk, sk)
                lst.append((s, e, sums1[s]))
        Wsub[m] = lst
    R, Cc, V = [], [], []
    for j, C in enumerate(configs):
        if one:
            for s, e, _ in Wsub[C[0]]: R.append(vidx[(s,)]); Cc.append(j); V.append(e)
        else:
            for s3, e3, t3 in Wsub[C[0]]:
                for s7, e7, t7 in Wsub[C[1]]:
                    if t3 + t7 <= theta + 1e-12: R.append(vidx[(s3, s7)]); Cc.append(j); V.append(e3 * e7)
    A = sp.csr_matrix((V, (R, Cc)), shape=(len(vis), len(configs)))
    rho = A @ mu; keep = rho > 0
    A, rho = A[keep], rho[keep]
    j0 = configs.index(tuple((0,) * K for _ in range(1 if one else 2)))
    return g, w, configs, mu, A, rho, j0

def main():
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    one = "--one" in sys.argv
    g, w, configs, mu, A, rho, j0 = build(eps, K, theta, one)
    As = (sp.diags(1 / rho) @ A @ sp.diags(mu)).tocsr()
    n, m = As.shape[1], As.shape[0]
    # variables (x_1..x_n, t); minimise t;  As x - t <= 1, -As x - t <= -1
    I = sp.csr_matrix(np.ones((m, 1)))
    Aub = sp.vstack([sp.hstack([As, -I]), sp.hstack([-As, -I])]).tocsr()
    bub = np.concatenate([np.ones(m), -np.ones(m)])
    c = np.zeros(n + 1); c[-1] = 1
    bounds = [(0, None)] * n + [(0, None)]
    bounds[j0] = (0, 0)
    res = linprog(c, A_ub=Aub, b_ub=bub, bounds=bounds, method="highs")
    x = res.x[:n]
    out = {"eps": eps, "K": K, "theta": theta, "one": one, "status": res.status,
           "min_Linf_rel_residual": float(res.fun), "check_resid": float(np.max(np.abs(As @ x - 1)))}
    for a in sys.argv:
        if a.startswith("--dump="):
            json.dump({"eps": eps, "K": K, "theta": theta, "g": list(map(float, g)), "w": list(map(float, w)),
                       "configs": [list(map(list, C)) for C in configs], "nu": list(map(float, x * mu)),
                       "mu": list(map(float, mu))}, open(a[7:], "w"))
    print(json.dumps(out))

if __name__ == "__main__":
    main()
