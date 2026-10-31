"""mixing check for z1142: fraction of 1-entries moved by the null shuffles (load A, rerun curveball)."""
import numpy as np, importlib.util, sys
from sympy import nextprime
A = np.load("data/z52d/audit/A3/z1142_A_40_3000_1000000.npy")
ps=[]; p=10**6
while len(ps)<3000:
    p=nextprime(p)
    if p%4==1: ps.append(p)
ps=np.array(ps)
src=open("scripts/z52d_audit_A3_z1142.py").read()
ns={"np":np}
exec(src[src.index("rng ="):src.index("ps = []")], ns); exec(src[src.index("def curveball"):src.index("s0 = sv(A)")], ns)
for name, strata, it in [("global",None,4000),("mod840",[np.nonzero(ps%840==r)[0] for r in np.unique(ps%840)],20000),("mod840x5",[np.nonzero(ps%840==r)[0] for r in np.unique(ps%840)],100000)]:
    M=ns["curveball"](A,it,strata)
    print(name, "moved fraction of ones:", round(float((M.astype(bool)&~A.astype(bool)).sum()/A.sum()),3), "sv:", np.round(np.linalg.svd(M.astype(float),compute_uv=False)[:4],2))
