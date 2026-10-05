#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.5 -- polish an LP fake: restrict to its support, re-solve the
equality system As[:,supp] z = 1 (z = nu/mu) by least squares in float64, then by a
nonnegative LP on the support, and report the residual; dump the polished fake.
Usage: window2_polish.py EPS K THETA IN.json OUT.json
"""
import sys, json
import numpy as np, scipy.sparse as sp
from scipy.optimize import nnls
import window2_feas as F
eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
g, w, configs, mu, A, rho, j0 = F.build(eps, K, theta, False)
d = json.load(open(sys.argv[4]))
x = np.array(d["nu"]) / mu
As = (sp.diags(1 / rho) @ A @ sp.diags(mu)).tocsr()
supp = np.nonzero(x > 1e-12)[0]
supp = supp[supp != j0]
M = As[:, supp].toarray()
z, rn = nnls(M, np.ones(M.shape[0]), maxiter=50 * M.shape[1])
xx = np.zeros_like(x); xx[supp] = z
r = float(np.max(np.abs(As @ xx - 1)))
print(json.dumps({"support": int(len(supp)), "rows": int(M.shape[0]), "nnls_resid_norm": float(rn),
                  "max_rel_residual": r, "nu_empty": float(xx[j0]), "min_x": float(xx.min())}))
json.dump({**d, "nu": list(map(float, xx * mu))}, open(sys.argv[5], "w"))
