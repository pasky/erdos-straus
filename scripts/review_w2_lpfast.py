#!/usr/bin/env python3
"""R29: lean float version of review_w2_lp.py (two windows, primal only) for larger grids.
Same model (own code).  Usage: review_w2_lpfast.py EPS K THETA
"""
import sys, itertools
from math import comb, factorial, log, exp, sqrt
import numpy as np, scipy.sparse as sp
from scipy.optimize import linprog
eps, K, th = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
E = [exp(log(eps) * (1 - i / K)) for i in range(K + 1)]
g = [sqrt(E[i] * E[i + 1]) * (1 + 1e-7 * (i + 1)) for i in range(K)]
w = [0.5 * log(E[i + 1] / E[i]) for i in range(K)]
gs = lambda m: sum(a * b for a, b in zip(m, g))
W = [m for m in itertools.product(*[range(int(1 / x) + 1) for x in g]) if gs(m) < 1 and sum(m) % 2 == 0]
def muw(m):
    v = max(1 - gs(m), 1e-3) ** -0.5
    for k in range(K): v *= w[k] ** m[k] / factorial(m[k])
    return v
mu1 = np.array([muw(m) for m in W]); n = len(W)
V1 = [m for m in itertools.product(*[range(int(th / x) + 1) for x in g]) if gs(m) <= th]
vid = {m: i for i, m in enumerate(V1)}; vs = np.array([gs(m) for m in V1])
# one-window embedding matrix B[s, c] = emb(s, c) for visible s
r_, c_, v_ = [], [], []
for j, c in enumerate(W):
    for s in itertools.product(*[range(x + 1) for x in c]):
        if s in vid:
            e = 1
            for a, b in zip(s, c): e *= comb(b, a)
            r_.append(vid[s]); c_.append(j); v_.append(e)
B = sp.csr_matrix((v_, (r_, c_)), shape=(len(V1), n))
pairs = [(a, b) for a in range(len(V1)) for b in range(len(V1)) if vs[a] + vs[b] <= th + 1e-12]
print(f"window configs {n}, joint {n*n}, visible {len(pairs)}", flush=True)
# joint row (a,b) = kron(B[a], B[b]); scale columns by mu, rows by rho
Bm = (B @ sp.diags(mu1)).tocsr()
rows = []
for a, b in pairs:
    rows.append(sp.kron(Bm[a], Bm[b], format="csr"))
A = sp.vstack(rows).tocsr()
rho = np.asarray(A.sum(axis=1)).ravel()
A = (sp.diags(1 / rho) @ A).tocsr()
z = W.index(tuple([0] * K))
c = np.zeros(n * n); c[z * n + z] = 1
cm = np.asarray(abs(A).max(axis=0).todense()).ravel() if "--colnorm" in sys.argv else np.ones(A.shape[1]); cm[cm == 0] = 1
A = (A @ sp.diags(1 / cm)).tocsr()          # column-normalised; variable x' = x*cm
c = c / cm
meth = "highs-ipm" if "--ipm" in sys.argv else "highs-ds"
CAP = next((float(a[6:]) for a in sys.argv if a.startswith("--cap=")), None)
r = linprog(c, A_eq=A, b_eq=np.ones(len(pairs)), bounds=(0, None if CAP is None else CAP), method=meth)
if r.status == 0:
    r.x = r.x / cm; A = (A @ sp.diags(cm)).tocsr(); r.fun = r.x[z * n + z]
print("status", r.status, "min nu(empty)/tau =", r.fun)
if r.status == 0:
    x = r.x; print("max rel residual:", np.abs(A @ x - 1).max(), " support:", (x > 1e-12).sum(), " max nu/mu:", x.max())
    supp = np.where(x > 1e-12)[0]
    As = A[:, supp].toarray()
    sol, *_ = np.linalg.lstsq(As, np.ones(len(pairs)), rcond=None)
    print("re-solve on support (float64): min nu/mu =", sol.min(), " residual =", np.abs(As @ sol - 1).max(),
          " cond =", np.linalg.cond(As), " empty in support:", (z * n + z) in set(supp.tolist()))
    np.save("/tmp/r29_supp_%s_%s.npy" % (eps, K), np.stack([supp, sol]))
