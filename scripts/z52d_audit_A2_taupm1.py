#!/usr/bin/env python3
"""z52d audit A2, item Z0698: does tau(p-1) stay correlated with ES hardness after controlling for L(1,chi_p)?
Input: lines 'p U ...' (U = #unordered solutions of 4/p, from z52d_audit_A2_variants3.c). p = 1 mod 4 only.
Residual hardness: r = log U - fit(log log p) (OLS on [1, log log p]). L(1,chi_p) by Euler product over primes < 2e5.
Reports Spearman/Pearson of r with tau(p-1), sigma(p-1)/(p-1), and the partial correlation controlling for log L(1,chi_p)
and additionally for the number of q in {3,5,7,11,13,16} dividing p-1 (the RESIDUE_HARDNESS small-modulus effect)."""
import sys, numpy as np
from sympy import factorint, primerange
def spearmanr(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b)); return (np.corrcoef(ra, rb)[0, 1],)
A = np.loadtxt(sys.argv[1], dtype=np.int64); lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
A = A[(A[:, 0] % 4 == 1) & (A[:, 0] >= lo)]
p = A[:, 0]; U = A[:, 1].astype(float)
ell = np.array(list(primerange(3, 200000)), dtype=np.int64)
def leg(a, q):  # vectorised Legendre (a/q) over q-array for fixed a... use Euler criterion per q
    return np.array([pow(int(a) % int(qq), (int(qq) - 1) // 2, int(qq)) for qq in q])
logL = np.zeros(len(p))
for i, pp in enumerate(p):
    # chi_p(l) = (l/p) = (p/l) for p = 1 mod 4 (reciprocity); l=2: (2/p)
    e = np.array([pow(int(pp) % int(l), (int(l) - 1) // 2, int(l)) if pp % l else 0 for l in ell[:3000]])
    chi = np.where(e == 1, 1.0, np.where(e == 0, 0.0, -1.0))
    c2 = 1.0 if pp % 8 == 1 else -1.0
    logL[i] = -np.log(1 - c2/2) - np.sum(np.log(1 - chi/ell[:3000]))
tau = np.zeros(len(p)); sig = np.zeros(len(p)); nsmall = np.zeros(len(p))
for i, pp in enumerate(p):
    f = factorint(int(pp) - 1); t = 1; s = 1.0
    for q, e in f.items(): t *= e + 1; s *= (1 - q**-(e + 1)) / (1 - 1/q)
    tau[i] = t; sig[i] = s
    nsmall[i] = sum((pp - 1) % q == 0 for q in (3, 5, 7, 11, 13, 16))
X0 = np.column_stack([np.ones(len(p)), np.log(np.log(p))])
def resid(y, X):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); return y - X @ b
r = resid(np.log(U), X0)
print(f"n={len(p)} p in [{p.min()},{p.max()}]")
for nm, v in [("tau(p-1)", tau), ("log tau(p-1)", np.log(tau)), ("sigma(p-1)/(p-1)", sig), ("log L(1,chi_p)", logL), ("#small q|p-1", nsmall)]:
    print(f"  corr(resid, {nm:18s}): pearson {np.corrcoef(r, v)[0,1]:+.3f}  spearman {spearmanr(r, v)[0]:+.3f}")
for ctrl_nm, C in [("logL", [logL]), ("logL + #small", [logL, nsmall]), ("logL + #small + 1[8|p-1]", [logL, nsmall, (p % 8 == 1).astype(float)])]:
    X = np.column_stack([X0] + C)
    rr = resid(np.log(U), X)
    for nm, v in [("log tau(p-1)", np.log(tau)), ("sigma(p-1)/(p-1)", sig)]:
        vv = resid(v, X)
        print(f"  partial corr | {ctrl_nm:26s} {nm:18s}: {np.corrcoef(rr, vv)[0,1]:+.3f}")
    print(f"  R^2 of controls ({ctrl_nm}): {1 - np.var(rr)/np.var(r):.3f}")
