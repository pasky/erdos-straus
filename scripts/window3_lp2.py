#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §4-§5 -- sparse reformulation of window3_lp.py --swz (switched families).

Same LP as window3_lp.py --swz=K:MODE[:J], with auxiliary variables
  y[q,i,P] = sum_{C_q' with key P} p(C_q') x_(C_q=i, C_q')      (key P: first occupied cell for
  MODE=prefix, occupancy set for MODE=all), and family rows
  sum_{P compatible with Z} y[q,i,P] <= K p(S_Z)    for C_q = i != empty and each Z.
--Kz=FILE: per-family constants for prefix mode, JSON list K(zeta_j), j=0..K (overrides K).
--drop=T: restrict joint columns to mu(C) >= T*mu(empty) (fakes found remain valid fakes).
Usage: window3_lp2.py EPS K THETA --swz=K:MODE[:J] [--vis=rep] [--N=4000] [--drop=T] [--dump=F]
"""
import sys, json, time, itertools
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog
import window3_model as M
from window3_lp import arg, build


def main():
    eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    vis = arg("vis", "rep"); N = int(arg("N", "4000"))
    t0 = time.time()
    L, W, mu1, A, rho, cols_mu = build(eps, K, theta, vis, N, False)
    nW = len(W); z = W.index(tuple([0] * K))
    s = arg("swz").split(":"); Kcap = float(s[0]); mode = s[1] if len(s) > 1 else "prefix"
    jmax = int(s[2]) if len(s) > 2 else K
    Kz = json.load(open(arg("Kz"))) if arg("Kz") else None
    drop = float(arg("drop", "0")); cgen = "--cg" in sys.argv
    Afull = A.tocsc(); nfull = nW * nW
    IA, IB = np.divmod(np.arange(nfull), nW)
    p1 = mu1 / mu1.sum()
    occ = np.array([[C[k] > 0 for k in range(K)] for C in W])
    if mode == "prefix":
        key = np.array([int(np.argmax(o)) if o.any() else K for o in occ])   # first occupied cell (K = empty)
        keys = list(range(K + 1))
        Zs = [np.arange(K) < j for j in range(jmax + 1)]
        compat = lambda P, Z: P == K or not Z[P]
    else:
        pat = [tuple(np.where(o)[0]) for o in occ]
        keys = sorted(set(pat)); kid = {P: t for t, P in enumerate(keys)}
        key = np.array([kid[P] for P in pat])
        Zs = [np.array(list(b) + [0] * (K - jmax), dtype=bool) for b in itertools.product([0, 1], repeat=jmax)]
        compat = lambda P, Z: not any(Z[k] for k in keys[P])
    nk = len(keys); sel = [i for i in range(nW) if i != z]
    sidx = np.full(nW, -1); sidx[sel] = np.arange(len(sel))
    ny = 2 * len(sel) * nk
    # aux coefficients of every full column: two (row, value) pairs (or none if own config empty)
    auxrow = np.full((2, nfull), -1); auxval = np.zeros((2, nfull))
    for q, (own, oth) in enumerate(((IA, IB), (IB, IA))):
        m = own != z
        auxrow[q, m] = q * len(sel) * nk + sidx[own[m]] * nk + key[oth[m]]
        auxval[q, m] = -p1[oth[m]]
    # family rows (on y only)
    R, Cc, V, b = [], [], [], []
    keyp = np.array([p1[key == P].sum() for P in range(nk)])
    r = 0
    for zi, Z in enumerate(Zs):
        cp = [P for P in range(nk) if compat(P, Z)]; pz = keyp[cp].sum()
        Kc = Kz[zi] if Kz else Kcap
        for q in range(2):
            for t in range(len(sel)):
                for P in cp:
                    R.append(r); Cc.append(q * len(sel) * nk + t * nk + P); V.append(1.0 / pz)
                b.append(Kc); r += 1
    Fy = sp.csr_matrix((V, (R, Cc)), shape=(r, ny)); b = np.array(b)
    j0full = z * nW + z
    keep = np.where(cols_mu >= drop * cols_mu[j0full])[0] if drop > 0 else np.arange(nfull)
    it = 0
    while True:
        it += 1
        n = len(keep); j0 = int(np.where(keep == j0full)[0][0])
        A = Afull[:, keep]
        rr = auxrow[:, keep]; vv = auxval[:, keep]; mm = rr >= 0
        cols = np.tile(np.arange(n), (2, 1))
        Ax = sp.csr_matrix((vv[mm], (rr[mm], cols[mm])), shape=(ny, n))
        mA = A.shape[0]; Ie = sp.identity(mA, format="csr"); BIG = 100.0
        Aeq = sp.vstack([sp.hstack([A, sp.csr_matrix((mA, ny)), Ie, -Ie]),
                         sp.hstack([Ax, sp.identity(ny, format="csr"), sp.csr_matrix((ny, 2 * mA))])]).tocsr()
        beq = np.concatenate([np.ones(mA), np.zeros(ny)])
        Aub = sp.hstack([sp.csr_matrix((r, n)), Fy, sp.csr_matrix((r, 2 * mA))]).tocsr()
        cm = np.concatenate([np.asarray(abs(A).max(axis=0).todense()).ravel(), np.ones(ny + 2 * mA)])
        cm[cm == 0] = 1
        D = sp.diags(1 / cm)
        c = np.zeros(n + ny + 2 * mA); c[j0] = 1; c[n + ny:] = BIG
        res = linprog(c / cm, A_eq=(Aeq @ D).tocsr(), b_eq=beq, A_ub=(Aub @ D).tocsr(), b_ub=b,
                      bounds=(0, None), method="highs")
        if res.status != 0 or not cgen:
            break
        lam = res.eqlin.marginals; lamA = lam[:A.shape[0]]; lamY = lam[A.shape[0]:]
        rc = -(Afull.T @ lamA)
        for q in range(2):
            m = auxrow[q] >= 0
            rc[m] -= auxval[q, m] * lamY[auxrow[q, m]]
        rc[j0full] += 1.0
        rc_rel = rc / np.maximum(np.asarray(abs(Afull).max(axis=0).todense()).ravel(), 1e-300)
        inset = np.zeros(nfull, bool); inset[keep] = True
        cand = np.where((~inset) & (rc_rel < -1e-9))[0]
        print(json.dumps({"cg_iter": it, "cols": n, "obj": float(res.x[j0] / cm[j0]), "neg_rc": int(len(cand)),
                          "min_rc": float(rc_rel[~inset].min()) if (~inset).any() else 0.0}), file=sys.stderr, flush=True)
        if len(cand) == 0:
            break
        cand = cand[np.argsort(rc_rel[cand])[:max(10000, n // 4)]]
        keep = np.sort(np.concatenate([keep, cand]))
    out = {"eps": eps, "K": K, "theta": theta, "vis": vis, "nW": nW, "ny": ny, "famrows": r,
           "swz": arg("swz"), "Kz": arg("Kz"), "drop": drop, "cols": int(len(keep)), "status": int(res.status), "msg": res.message[:50]}
    out["cg_iters"] = it
    if res.status == 0:
        x = res.x / cm
        out["min_nu0"] = float(x[j0]); out["resid"] = float(np.abs(A @ x[:n] - 1).max())
        out["aux_resid"] = float(np.abs(Aeq @ x - beq).max())
        out["fam_viol"] = float(max(0.0, (Aub @ x - b).max())); out["max_x"] = float(x[:n].max())
        out["elastic"] = float(np.abs(x[n + ny:]).sum())
        if arg("dump"):
            np.savez_compressed(arg("dump"), x=x[:n], keep=keep, W=np.array(W), mu1=mu1)
    out["sec"] = round(time.time() - t0, 1)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
