#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §7 -- full two-type model: bad AND good prime factors >= x^eps recorded.

Window configuration (B, G): multiplicity vectors of bad / good points on K log cells, |B| even.
Law: mu(B,G) = w^B/B! w^G/G! * sum_j (d_B * d_G)[j] H[j]  (sub-grid N), where H (density of the
x^eps-smooth bad-free remainder) is the exact discrete solution of
   sum_t E[t] H[s+t] = cofw[s],   E = sum_G w^G/G! d_G   (good-point sum distribution),
so that summing out G reproduces the bad-only cell-integrated law of window3_model exactly.
Data: all (S_B, S_G) with sum <= theta (rep convention), one window or jointly.
Objective: min nu{B_3 = B_7 = empty (any G)} / mu{same}.
Families (--swz=K): for each window q and each C_q=(B_q,G_q) with B_q != empty and each prefix
Z=[eps,zeta): sum over C_q' with B_q' having no point in Z  of nu <= K * same for mu.
Usage: window3_full.py EPS K THETA [--one] [--N=2000] [--swz=K [--swgood]] [--badonly]
--swgood: also families with C_q=(empty, G_q), G_q nonempty (switching a GOOD prime of n_q).
"""
import sys, json, time, itertools
from math import factorial, comb
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog
import window3_model as M


def arg(name, default=None):
    for a in sys.argv:
        if a.startswith(f"--{name}="):
            return a.split("=", 1)[1]
    return default


def configs2(e, K):
    lo = e[:-1]; out = []
    def rec(k, cur, s):
        if k == 2 * K:
            if sum(cur[:K]) % 2 == 0:
                out.append((tuple(cur[:K]), tuple(cur[K:])))
            return
        m = 0
        while s + m * lo[k % K] < 1 - 1e-12:
            cur.append(m); rec(k + 1, cur, s + m * lo[k % K]); cur.pop(); m += 1
    rec(0, [], 0.0)
    return out


def main():
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    N = int(arg("N", "2000")); one = "--one" in sys.argv
    t0 = time.time()
    L = M.Law(eps, K, N)
    # good-point sum distribution E (all G), then H by back-substitution
    E = np.zeros(N + 1); E[0] = 1.0
    lam = sum(L.w[k] * L.single[k] for k in range(K))
    term = E.copy()
    for k in range(1, 60):
        term = np.convolve(term, lam)[: N + 1] / k; E += term
    H = np.zeros(N + 1); cof = L.cofw
    for s in range(N, -1, -1):
        H[s] = cof[s] - float(E[1: N + 1 - s] @ H[s + 1:])
    W = configs2(L.e, K)
    def dist(m):
        d = np.zeros(N + 1); d[0] = 1; c = 1.0
        for k, mk in enumerate(m):
            if mk:
                d = np.convolve(d, L.sumdist(k, mk))[: N + 1]; c *= L.w[k] ** mk / factorial(mk)
        return d, c
    mu = []
    for B, G in W:
        dB, cB = dist(B); dG, cG = dist(G)
        mu.append(cB * cG * float(np.convolve(dB, dG)[: N + 1] @ H))
    mu = np.array(mu)
    neg = float(mu.min())
    ok = mu > 1e-14 * mu.max()
    W = [w for w, o in zip(W, ok) if o]; mu = mu[ok]; nW = len(W)
    clean = np.array([not any(B) for B, G in W])
    V1, sums = M.visible_one(L.e, theta, "rep")
    items = [(S, T) for S in V1 for T in V1 if sums[S] + sums[T] <= theta + 1e-12]
    isum = np.array([sums[S] + sums[T] for S, T in items]); iid = {it: i for i, it in enumerate(items)}
    if "--badonly" in sys.argv:
        z0 = tuple([0] * K); items = [it for it in items if it[1] == z0]
        isum = np.array([sums[S] for S, T in items]); iid = {it: i for i, it in enumerate(items)}
    r_, c_, v_ = [], [], []
    for j, (B, G) in enumerate(W):
        for S in itertools.product(*[range(x + 1) for x in B]):
            for T in itertools.product(*[range(x + 1) for x in G]):
                i = iid.get((S, T))
                if i is not None:
                    r_.append(i); c_.append(j); v_.append(M.emb(S, B) * M.emb(T, G) * mu[j])
    Bm = sp.csr_matrix((v_, (r_, c_)), shape=(len(items), nW))
    if one:
        A = Bm; cmu = mu; tgt = clean.astype(float)
    else:
        pairs = [(a, b) for a in range(len(items)) for b in range(len(items)) if isum[a] + isum[b] <= theta + 1e-12]
        A = sp.vstack([sp.kron(Bm[a], Bm[b], format="csr") for a, b in pairs]).tocsr()
        cmu = np.outer(mu, mu).ravel(); tgt = np.outer(clean, clean).ravel().astype(float)
    rho = np.asarray(A.sum(axis=1)).ravel(); kp = rho > 0
    A = (sp.diags(1 / rho[kp]) @ A[kp]).tocsc()
    tau = float((cmu * tgt).sum())
    c = cmu * tgt / tau                     # objective: nu(target)/tau in x = nu/mu units
    Aub, bub = None, None
    if arg("swz") and not one:
        Kc = float(arg("swz")); p = mu / mu.sum()
        firstbad = np.array([int(np.argmax(np.array(B) > 0)) if any(B) else K for B, G in W])
        rows, R, Cc, V = 0, [], [], []
        idx = np.arange(nW * nW).reshape(nW, nW)
        for j in range(K + 1):                   # Z = cells [0, j)
            okz = firstbad >= j
            pz = p[okz].sum()
            for i in range(nW):
                if (clean[i] and "--swgood" not in sys.argv) or (not any(W[i][0]) and not any(W[i][1])):
                    continue
                for q in range(2):
                    cols = idx[i, okz] if q == 0 else idx[okz, i]
                    R += [rows] * len(cols); Cc += list(cols); V += list(p[okz] / pz); rows += 1
        Aub = sp.csr_matrix((V, (R, Cc)), shape=(rows, nW * nW)); bub = np.full(rows, Kc)
    cm = np.asarray(abs(A).max(axis=0).todense()).ravel(); cm[cm == 0] = 1
    D = sp.diags(1 / cm)
    kw = dict(A_eq=(A @ D).tocsr(), b_eq=np.ones(A.shape[0]), bounds=(0, None), method="highs")
    if Aub is not None:
        kw.update(A_ub=(Aub @ D).tocsr(), b_ub=bub)
    res = linprog(c / cm, **kw)
    out = {"eps": eps, "K": K, "theta": theta, "one": one, "badonly": "--badonly" in sys.argv, "swz": arg("swz"),
           "nW": nW, "rows": A.shape[0], "mu_min_raw": neg, "H_min": float(H.min()), "status": int(res.status)}
    if res.status == 0:
        x = res.x / cm
        out["min_target"] = float(c @ x); out["resid"] = float(np.abs(A @ x - 1).max()); out["max_x"] = float(x.max())
    out["sec"] = round(time.time() - t0, 1)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
