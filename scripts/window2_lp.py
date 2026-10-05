#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.5 -- discretised Type-I + parity LP (model 𝒯𝒫(θ)).

Points (log-sizes of bad primes >= eps) live on K log-spaced bins with
representative values g_k; bin mass w_k = (1/2) ln(e_{k+1}/e_k).
Window configuration = multiset m (multiplicities over bins), |m| even,
sum g < 1;  mu_win(m) = prod w_k^{m_k}/m_k! * (1 - sum)^(-1/2)  (clean = 1).
Joint configuration C = (m3, m7) (or one window only with --one).
Visible S = (s3, s7), any parity, sum <= theta.  emb(S,C) = prod binom(C_k, S_k).

PRIMAL: min nu(empty) s.t. nu >= 0, sum_C nu(C) emb(S,C) = rho_mu(S) for all visible S.
Output nu(empty)/tau  (tau = mu(empty) = 1).  0 => a fake exists in the
discrete model; > 0 => the dual is a Type-I+parity lower bound in the model.

Usage: window2_lp.py EPS K THETA [--one] [--cap=2] [--show]
"""
import sys
import json
import itertools
from math import comb, factorial, log
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def bins(eps, K):
    e = np.exp(np.linspace(log(eps), 0.0, K + 1))
    g = np.sqrt(e[:-1] * e[1:]) * (1 + 1e-7 * np.arange(1, K + 1))   # break ties
    w = 0.5 * np.log(e[1:] / e[:-1])
    return g, w


def multisets(g, cap, strict):
    """all multiplicity tuples with sum g < cap (strict) or <= cap."""
    K = len(g)
    out = []

    def rec(k, cur, s):
        if k == K:
            out.append(tuple(cur))
            return
        m = 0
        while True:
            ss = s + m * g[k]
            if (ss >= cap - 1e-12) if strict else (ss > cap + 1e-12):
                break
            cur.append(m)
            rec(k + 1, cur, ss)
            cur.pop()
            m += 1
    rec(0, [], 0.0)
    return out


def main():
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    one = "--one" in sys.argv
    CAP = None
    METHOD = "highs-ds" if "--ds" in sys.argv else "highs"
    for a in sys.argv:
        if a.startswith("--cap="):
            CAP = float(a[6:])          # nu <= CAP*mu (2 = 'bounded fake', Lemma 3.6)
    g, w = bins(eps, K)
    W = [m for m in multisets(g, 1.0, True) if sum(m) % 2 == 0]
    def mu_win(m):
        s = float(np.dot(m, g))
        v = (max(1.0 - s, 1e-3)) ** -0.5
        for k, mk in enumerate(m):
            v *= w[k] ** mk / factorial(mk)
        return v
    muW = np.array([mu_win(m) for m in W])
    Vis1 = multisets(g, theta, False)          # visible one-window multisets (any parity)
    sums1 = {s: float(np.dot(s, g)) for s in Vis1}
    if one:
        configs = [(m,) for m in W]
        mu = muW
        vis = [(s,) for s in Vis1]
    else:
        configs = [(a, b) for a in W for b in W]
        mu = np.outer(muW, muW).ravel()
        vis = [(a, b) for a in Vis1 for b in Vis1 if sums1[a] + sums1[b] <= theta + 1e-12]
    vidx = {s: i for i, s in enumerate(vis)}
    Wsub = {}
    for m in W:   # visible sub-multisets of a window config, with emb counts
        lst = []
        for s in itertools.product(*[range(mk + 1) for mk in m]):
            if s in sums1:
                e = 1
                for mk, sk in zip(m, s):
                    e *= comb(mk, sk)
                lst.append((s, e, sums1[s]))
        Wsub[m] = lst
    rows, cols, vals = [], [], []
    for j, C in enumerate(configs):
        if one:
            for s, e, _ in Wsub[C[0]]:
                rows.append(vidx[(s,)]); cols.append(j); vals.append(e)
        else:
            for s3, e3, t3 in Wsub[C[0]]:
                for s7, e7, t7 in Wsub[C[1]]:
                    if t3 + t7 <= theta + 1e-12:
                        rows.append(vidx[(s3, s7)]); cols.append(j); vals.append(e3 * e7)
    A = sp.csr_matrix((vals, (rows, cols)), shape=(len(vis), len(configs)))
    rho = A @ mu
    j0 = configs.index(tuple((0,) * K for _ in range(1 if one else 2)))
    c = np.zeros(len(configs)); c[j0] = 1.0
    # rescale: variables x = nu/mu (x = 1 is feasible), rows divided by rho(S)
    keep = rho > 0                       # rows with rho=0: S in no configuration
    A, rho = A[keep], rho[keep]
    vis = [v for v, k in zip(vis, keep) if k]
    As = sp.diags(1.0 / rho) @ A @ sp.diags(mu)
    cs = c * mu
    res = linprog(cs, A_eq=As, b_eq=np.ones(len(vis)), bounds=(0, CAP), method=METHOD,
                  options={"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10})
    nu = res.x * mu if res.status == 0 else None
    resid = float(np.max(np.abs(As @ res.x - 1.0))) if res.status == 0 else None
    out = {"eps": eps, "K": K, "theta": theta, "one_window": one,
           "n_configs": len(configs), "n_visible": len(vis), "nnz": int(A.nnz),
           "status": res.status, "message": res.message,
           "tau": float(mu[j0]), "max_rel_residual": resid, "P_target": float(mu[j0] / mu.sum()),
           "min_fake_target_over_tau": (float(res.fun) / float(mu[j0])) if res.status == 0 else None}
    if nu is not None and "--show" in sys.argv:
        dif = nu - mu
        order = np.argsort(dif)
        def fmt(C):
            return [[round(float(g[k]), 3) for k in range(K) for _ in range(m[k])] for m in C]
        out["most_removed"] = [(fmt(configs[j]), float(dif[j] / mu[j0])) for j in order[:12]]
        out["most_added"] = [(fmt(configs[j]), float(dif[j] / mu[j0])) for j in order[::-1][:12]]
    for a in sys.argv:
        if a.startswith("--dump=") and nu is not None:
            json.dump({"eps": eps, "K": K, "theta": theta, "g": list(map(float, g)), "w": list(map(float, w)),
                       "configs": [list(map(list, C)) for C in configs], "nu": list(map(float, nu)),
                       "mu": list(map(float, mu))}, open(a[7:], "w"))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
