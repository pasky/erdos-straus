#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §3 -- two-window Type-I + parity + switching LP on the cell-integrated law.

Variables x_C = nu(C)/mu(C) >= 0, C = (C3, C7) even/even.  Rows (scaled by rho(S)):
  sum_C emb(S,C) mu(C) x_C / rho(S) = 1      for visible S (convention --vis=rep|inner|outer).
Objective: min x_(empty,empty)  (= nu(empty)/tau).
Switching (--swm=K[:ALPHA]): marginal caps (SW_K) of §1, for both windows q and every
  window-q configuration C_q != empty whose largest occupied cell has lower edge >= ALPHA
  (default ALPHA=0: every C_q != empty):  sum_{C_q'} mu_q'(C_q')/M_q' * x_(C_q,C_q') <= K.
Per-configuration caps (--swpc=K:ALPHA, WINDOW2 §6.2 style): x_C <= K if some point of C has
  lower cell edge >= ALPHA.   --cap=C: x_C <= C for all C.
Dual certificate: from HiGHS duals, rigorous (up to float rounding) lower bound
  min x_empty >= y.1 - K lam.1 - max_j v_j^+ rho_0/mu_j     (v = dual violation).
Usage: window3_lp.py EPS K THETA [--vis=rep] [--swm=K[:A]] [--swpc=K:A] [--cap=C] [--N=4000]
       [--one] [--dump=FILE]
"""
import sys, json, time
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog
import window3_model as M


def arg(name, default=None):
    for a in sys.argv:
        if a.startswith(f"--{name}="):
            return a.split("=", 1)[1]
    return default


def build(eps, K, theta, vis, N, one):
    L = M.Law(eps, K, N)
    W = M.window_configs(L.e, 0)
    mu1 = np.array([L.mu(m) for m in W])
    okW = mu1 > 1e-14 * mu1.max()          # drop cells with (numerically) zero mass below sum 1
    W = [m for m, o in zip(W, okW) if o]; mu1 = mu1[okW]
    V1, sums = M.visible_one(L.e, theta, vis)
    import itertools
    from math import factorial
    good = "--good" in sys.argv
    if good:   # visible items (S, G): S bad sub-multiset, G good points (R29-M2 data)
        items = [(S, G) for S in V1 for G in V1 if sums[S] + sums[G] <= theta + 1e-12]
        isums = {it: sums[it[0]] + sums[it[1]] for it in items}
    else:
        items = [(S, None) for S in V1]; isums = {it: sums[it[0]] for it in items}
    r_, c_, v_ = [], [], []
    bySG = {}
    for i, it in enumerate(items): bySG.setdefault(it[0], []).append((i, it[1]))
    for j, C in enumerate(W):
        for s in itertools.product(*[range(x + 1) for x in C]):
            for i, G in bySG.get(s, []):
                if G is None or not any(G):
                    v = mu1[j]
                else:
                    CG = tuple(a + b for a, b in zip(C, G))
                    v = L.mu(CG)
                    for a, b in zip(C, G): v *= factorial(a + b) / (factorial(a) * factorial(b))
                if v > 0:
                    r_.append(i); c_.append(j); v_.append(M.emb(s, C) * v)
    B = sp.csr_matrix((v_, (r_, c_)), shape=(len(items), len(W)))
    V1 = items; sums = isums
    if one:
        A = B
        cols_mu = mu1
    else:
        pairs = [(a, b) for a in range(len(V1)) for b in range(len(V1))
                 if (sums[V1[a]] + sums[V1[b]] <= theta + 1e-12 if vis != "outer" else sums[V1[a]] + sums[V1[b]] < theta - 1e-12)]
        A = sp.vstack([sp.kron(B[a], B[b], format="csr") for a, b in pairs]).tocsr()
        cols_mu = np.outer(mu1, mu1).ravel()
    rho = np.asarray(A.sum(axis=1)).ravel()
    keep = rho > 0
    A = (sp.diags(1 / rho[keep]) @ A[keep]).tocsr()
    return L, W, mu1, A, rho[keep], cols_mu


def main():
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    vis = arg("vis", "rep"); N = int(arg("N", "4000")); one = "--one" in sys.argv
    t0 = time.time()
    L, W, mu1, A, rho, cols_mu = build(eps, K, theta, vis, N, one)
    nW = len(W); n = A.shape[1]
    z = W.index(tuple([0] * K)); j0 = z if one else z * nW + z
    lo_edge = L.e[:-1]
    maxpt = np.array([max([lo_edge[k] for k in range(K) if C[k]], default=-1.0) for C in W])
    ub = np.full(n, np.inf)
    G_rows, Kcap = [], None
    if arg("cap"):
        ub[:] = float(arg("cap"))
    if arg("swpc"):
        Kp, al = map(float, arg("swpc").split(":"))
        big = maxpt >= al
        mask = big if one else (big[:, None] | big[None, :]).ravel()
        ub[mask] = np.minimum(ub[mask], Kp)
    if arg("swm") and not one:
        s = arg("swm").split(":"); Kcap = float(s[0]); al = float(s[1]) if len(s) > 1 else 0.0
        p1 = mu1 / mu1.sum()
        G = []
        I = sp.identity(nW, format="csr")
        sel = np.where((maxpt >= al) & (np.arange(nW) != z))[0]
        e_ = sp.csr_matrix(p1.reshape(1, -1))
        for i in sel:   # window 3 config i fixed: columns (i, *) weighted by p1
            G.append(sp.kron(I[i], e_, format="csr"))
            G.append(sp.kron(e_, I[i], format="csr"))   # window 7 config i fixed
        G = sp.vstack(G).tocsr()
    elif arg("swz") and not one:
        # families F(q, C_q, Z): C_q fixed (!= empty), C_q' has no point in cell set Z.
        # mode prefix: Z = cells [0, j) for j = 0..jmax (j=0: marginal caps);  mode all: every Z.
        s = arg("swz").split(":"); Kcap = float(s[0]); mode = s[1] if len(s) > 1 else "prefix"
        jmax = int(s[2]) if len(s) > 2 else K
        p1 = mu1 / mu1.sum()
        occ = np.array([[C[k] > 0 for k in range(K)] for C in W])
        Zs = []
        if mode == "prefix":
            for j in range(jmax + 1):
                Zs.append(np.arange(K) < j)
        else:
            import itertools
            for bits in itertools.product([0, 1], repeat=jmax):
                Zs.append(np.array(list(bits) + [0] * (K - jmax), dtype=bool))
        I = sp.identity(nW, format="csr")
        sel = [i for i in range(nW) if i != z]
        G, b = [], []
        for Z in Zs:
            okZ = ~(occ & Z[None, :]).any(axis=1)
            pz = p1 * okZ
            e_ = sp.csr_matrix(pz.reshape(1, -1))
            Ri = sp.csr_matrix((np.ones(len(sel)), (np.arange(len(sel)), sel)), shape=(len(sel), nW))
            G.append(sp.kron(Ri, e_, format="csr")); G.append(sp.kron(e_, Ri, format="csr"))
            b += [pz.sum()] * (2 * len(sel))
        G = sp.vstack(G).tocsr(); b = np.array(b)
        G = (sp.diags(1 / b) @ G).tocsr()
        out_z = len(Zs)
    else:
        G = None
    c = np.zeros(n); c[j0] = 1
    # column normalisation (HiGHS drops tiny entries): x' = x * cm
    cm = np.asarray(abs(A).max(axis=0).todense()).ravel()
    if G is not None:
        cm = np.maximum(cm, np.asarray(abs(G).max(axis=0).todense()).ravel())
    cm[cm == 0] = 1.0
    D = sp.diags(1 / cm)
    bounds = np.stack([np.zeros(n), ub * cm], axis=1)
    kw = dict(A_eq=(A @ D).tocsr(), b_eq=np.ones(A.shape[0]), bounds=bounds, method="highs")
    if G is not None:
        kw.update(A_ub=(G @ D).tocsr(), b_ub=np.full(G.shape[0], Kcap))
    res = linprog(c / cm, **kw)
    if res.status == 0:
        res.x = res.x / cm; res.fun = res.x[j0]
    out = {"eps": eps, "K": K, "theta": theta, "vis": vis, "N": N, "one": one, "nW": nW, "cols": n,
           "rows": A.shape[0], "swm": arg("swm"), "swz": arg("swz"), "swpc": arg("swpc"), "cap": arg("cap"),
           "status": int(res.status), "msg": res.message[:60]}
    if res.status == 0:
        x = res.x
        out["min_nu0"] = float(res.fun)
        out["resid"] = float(np.abs(A @ x - 1).max())
        out["max_x"] = float(x.max())
        # dual bound
        y = res.eqlin.marginals
        val = float(y.sum()); viol = A.T @ y - c
        if G is not None:
            lam = -res.ineqlin.marginals; val -= Kcap * lam.sum(); viol -= G.T @ lam
        fin = np.isfinite(ub)
        if fin.any():   # upper bounds: their duals enter as -ub*max(viol,0) on capped columns
            val -= float((ub[fin] * np.maximum(viol[fin], 0)).sum()); viol[fin] = 0
        rho0 = rho[0] if True else None
        pen = float(np.max(np.maximum(viol, 0) * rho.max() / np.maximum(cols_mu, 1e-300) * (1 + 1e-9))) if not one else float(np.max(np.maximum(viol, 0) * rho.max() / mu1))
        out["dual_lb"] = val - pen
        out["dual_pen"] = pen
        if arg("dump"):
            np.savez_compressed(arg("dump"), x=x, y=y, W=np.array(W), mu1=mu1)
    if res.status == 0 and "--certify" in sys.argv:
        out.update(certify(res.x, A, G, Kcap, ub, j0))
    out["sec"] = round(time.time() - t0, 1)
    print(json.dumps(out))


def certify(x, A, G, Kcap, ub, j0, dps=50):
    """Exact-ish repair of a float fake: on the support J, solve the minimum-norm correction
    making A x = 1 and tight family rows = K hold in mpmath (dps digits), then check x >= 0,
    every family row <= K, every cap, and x_j0 = 0.  Data (mu, rho) are the float model data."""
    import mpmath as mp
    mp.mp.dps = dps
    J = np.where(x > 0)[0]
    if j0 in set(J.tolist()):
        return {"cert": False, "why": "target in support"}
    rows = [("A", i) for i in range(A.shape[0])]
    Gs = G[:, J].tocsr() if G is not None else None
    if G is not None:
        slack = Kcap - G @ x
        out_tight = int((slack < 1e-9).sum())   # tight rows are NOT pinned: run the LP with K slightly below the target K
    AJ = A[:, J].tocsr()
    Mrows = [AJ[i] if t == "A" else Gs[i] for t, i in rows]
    M = mp.matrix(len(rows), len(J))
    for r, R in enumerate(Mrows):
        R = R.tocoo()
        for cidx, v in zip(R.col, R.data): M[r, int(cidx)] = mp.mpf(float(v))
    xs = mp.matrix([mp.mpf(float(v)) for v in x[J]])
    b = mp.matrix([mp.mpf(1) if t == "A" else mp.mpf(Kcap) for t, i in rows])
    r = b - M * xs
    MMt = M * M.T
    try:
        yv = mp.lu_solve(MMt, r)
    except ZeroDivisionError:
        return {"cert": False, "why": "singular normal matrix"}
    xn = xs + M.T * yv
    res_eq = max(abs(v) for v in (b - M * xn))
    minx = min(xn)
    worst_fam = mp.mpf(-1)
    if G is not None:
        for i in range(Gs.shape[0]):
            R = Gs[i].tocoo()
            v = mp.fsum(mp.mpf(float(d)) * xn[int(cidx)] for cidx, d in zip(R.col, R.data))
            worst_fam = max(worst_fam, v - Kcap)
    capv = max([xn[k] - float(ub[J[k]]) for k in range(len(J)) if np.isfinite(ub[J[k]])], default=mp.mpf(-1))
    Kt = float(arg("certK", Kcap))       # the K for which the fake is certified (>= LP K)
    worst_fam = worst_fam + Kcap - Kt
    ok = minx > 0 and res_eq < mp.mpf(10) ** (-dps + 10) and worst_fam <= 0 and capv <= 0
    return {"cert": bool(ok), "support": int(len(J)), "tight_fam": out_tight if G is not None else 0,
            "cert_min_x": float(minx), "cert_eq_resid": float(res_eq), "cert_worst_fam_excess": float(worst_fam),
            "cert_shift": float(max(abs(v) for v in (M.T * yv)))}


if __name__ == "__main__":
    main()
