#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.5 -- feasibility LP: fake with nu(empty)=0, minimising the
L-infinity relative correlation residual t (rows scaled by rho).  Reuses the
model construction of window2_lp.py by importing it.  t ~ 0  => fake exists.
Usage: window2_feas.py EPS K THETA [--one] [--dump=F] [--v=V] [--swcap=K:ALPHA] [--cap=C]
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
    if "--bisect" in sys.argv:            # minimal v = nu(empty)/tau with residual <= 1e-9
        import subprocess
        lo, hi = 0.0, 1.0
        base = [a for a in sys.argv if a != "--bisect" and not a.startswith("--v=") and not a.startswith("--dump=")]
        def ok(v):
            r = subprocess.run([sys.executable] + base + [f"--v={v}"], capture_output=True, text=True)
            return json.loads(r.stdout.strip().splitlines()[-1])["check_resid"] <= 1e-9
        if ok(0.0):
            print(json.dumps({"args": base[1:], "min_v": 0.0})); return
        for _ in range(12):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if ok(mid) else (mid, hi)
        print(json.dumps({"args": base[1:], "min_v_in": [lo, hi]})); return
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    one = "--one" in sys.argv
    g, w, configs, mu, A, rho, j0 = build(eps, K, theta, one)
    As0 = (sp.diags(1 / rho) @ A @ sp.diags(mu)).tocsc()
    # column normalisation (HiGHS drops |a_ij| < small_matrix_value): y = x * colmax
    colmax = np.maximum(abs(As0).max(axis=0).toarray().ravel(), 1e-300)
    As = (As0 @ sp.diags(1 / colmax)).tocsr()
    n, m = As.shape[1], As.shape[0]
    # variables (x_1..x_n, t); minimise t;  As x - t <= 1, -As x - t <= -1
    I = sp.csr_matrix(np.ones((m, 1)))
    Aub = sp.vstack([sp.hstack([As, -I]), sp.hstack([-As, -I])]).tocsr()
    bub = np.concatenate([np.ones(m), -np.ones(m)])
    c = np.zeros(n + 1); c[-1] = 1
    bounds = [(0, None)] * n + [(0, None)]
    v = 0.0
    for a in sys.argv:
        if a.startswith("--v="):
            v = float(a[4:])                 # fix nu(empty)/tau = v
        if a.startswith("--swcap="):         # nu <= Ksw*mu on configs with a point >= alpha
            Ksw, alpha = map(float, a[8:].split(":"))
            for j, C in enumerate(configs):
                mx = max([g[k] for mm in C for k in range(K) if mm[k] > 0], default=0.0)
                if mx >= alpha:
                    bounds[j] = (0, Ksw)
        if a.startswith("--cap="):
            Cc = float(a[6:])
            bounds = [(0, min(Cc, b[1]) if b[1] is not None else Cc) for b in bounds[:n]] + [(0, None)]
    bounds[j0] = (v, v)
    bounds = [(lo * colmax[j], None if hi is None else hi * colmax[j]) for j, (lo, hi) in enumerate(bounds[:n])] + [(0, None)]
    res = linprog(c, A_ub=Aub, b_ub=bub, bounds=bounds, method="highs")
    x = res.x[:n] / colmax
    As = As0
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
