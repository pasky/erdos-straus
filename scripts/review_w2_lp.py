#!/usr/bin/env python3
"""R29 from-scratch LP for the discrete T P(theta) model, with a rigorously
checked DUAL certificate (lower bound on nu(empty)/tau).

Model rebuilt from POINTWISE_WINDOW2 §3.1/§3.3/§3.5 text (independent code).
Primal: min nu(empty)  s.t.  sum_C nu(C) emb(S,C) = rho_mu(S)  (S visible), nu >= 0
        [optional: nu(C) <= cap*mu(C)  for all C]
Dual (no cap): max sum_S y_S rho(S)  s.t.  sum_S y_S emb(S,C) <= [C=empty]  for all C.
A feasible y (checked EXACTLY in rationals after rounding) proves nu(empty) >= y.rho
for every fake.  rho evaluated in mpmath (40 digits).
Usage: review_w2_lp.py EPS K THETA [--one]
"""
import sys, itertools
from fractions import Fraction as F
from math import comb
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
import mpmath as mp

mp.mp.dps = 40
eps, K, theta = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
one = "--one" in sys.argv
E = [mp.e ** (mp.log(eps) * (1 - mp.mpf(i) / K)) for i in range(K + 1)]
g = [mp.sqrt(E[i] * E[i + 1]) * (1 + mp.mpf("1e-7") * (i + 1)) for i in range(K)]
w = [mp.log(E[i + 1] / E[i]) / 2 for i in range(K)]
gf = [float(x) for x in g]


def vecs(cap, strict):
    out = []
    for m in itertools.product(*[range(int(cap / gf[k]) + 1) for k in range(K)]):
        s = sum(a * b for a, b in zip(m, g))
        if (s < cap) if strict else (s <= cap):
            out.append(m)
    return out


Wn = [m for m in vecs(1, True) if sum(m) % 2 == 0]
def muw(m):
    s = sum(a * b for a, b in zip(m, g))
    v = max(1 - s, mp.mpf("1e-3")) ** mp.mpf(-0.5)
    for k in range(K):
        v *= w[k] ** m[k] / mp.factorial(m[k])
    return v
muW = {m: muw(m) for m in Wn}
V1 = vecs(theta, False)
sz = {m: sum(a * b for a, b in zip(m, g)) for m in V1}
if one:
    C = [(m,) for m in Wn]; mu = [muW[m] for m in Wn]
    VIS = [(s,) for s in V1]
else:
    C = [(a, b) for a in Wn for b in Wn]; mu = [muW[a] * muW[b] for a, b in C]
    VIS = [(a, b) for a in V1 for b in V1 if sz[a] + sz[b] <= theta]
def emb(S, c):
    r = 1
    for Sw, cw in zip(S, c):
        for s, x in zip(Sw, cw):
            if s > x:
                return 0
            r *= comb(x, s)
    return r
rows, cols, vals = [], [], []
rho = []
for i, S in enumerate(VIS):
    t = mp.mpf(0)
    for j, c in enumerate(C):
        e_ = emb(S, c)
        if e_:
            rows.append(i); cols.append(j); vals.append(e_); t += e_ * mu[j]
    rho.append(t)
j0 = C.index(tuple(tuple([0] * K) for _ in C[0]))
tau = mu[j0]
print(f"configs={len(C)} visible={len(VIS)} tau={mp.nstr(tau,6)}")
# scaled primal: x_j = nu_j/mu_j, row i divided by rho_i
A = sp.csr_matrix((np.array([v * float(mu[j] / rho[i]) for i, j, v in zip(rows, cols, vals)]),
                   (rows, cols)), shape=(len(VIS), len(C)))
c = np.zeros(len(C)); c[j0] = 1.0
r = linprog(c, A_eq=A, b_eq=np.ones(len(VIS)), bounds=(0, None), method="highs")
print("primal status:", r.status, " min nu(empty)/tau ≈", r.fun)
# dual of the scaled problem: max sum z_i s.t. sum_i z_i A_ij <= c_j ; y_S = z_i/rho_i
Ad = sp.csr_matrix((np.array(vals, float), (rows, cols)), shape=(len(VIS), len(C)))
# unscaled dual: max sum y_i rho_i  s.t. sum_i y_i emb_ij <= [j=j0]
rhof = np.array([float(x) for x in rho])
scale = 1 / rhof
M = Ad.T.tocsr().multiply(scale[None, :]).tocsr()   # z_i = y_i*rho_i
bub = np.zeros(len(C)); bub[j0] = 1.0
d = linprog(-np.ones(len(VIS)), A_ub=M, b_ub=bub, bounds=(None, None), method="highs")
print("dual status:", d.status, " dual value ≈", -d.fun)
# rigorous check: rationalise y, then repair with the S=empty row (emb=1 for all C):
# lower y_empty by the max exact violation; this keeps feasibility exactly.
y = [F(float(z) / float(rho[i])).limit_denominator(10**25) for i, z in enumerate(d.x)]
iE = VIS.index(tuple(tuple([0] * K) for _ in VIS[0]))
Adc = Ad.tocsc()
viol = F(0)
for j in range(len(C)):
    st, en = Adc.indptr[j], Adc.indptr[j + 1]
    tot = sum((y[i] * int(v) for i, v in zip(Adc.indices[st:en], Adc.data[st:en])), F(0))
    viol = max(viol, tot - (1 if j == j0 else 0))
y[iE] -= viol
lb = sum(mp.mpf(yi.numerator) / yi.denominator * rho[i] for i, yi in enumerate(y))
print(f"max exact violation repaired: {float(viol):.3e}")
print(f"CERTIFIED (exact dual feasibility, 40-digit rho): nu(empty)/tau >= {mp.nstr(lb / tau, 8)}")
# optional: certify the primal (fake) when min ≈ 0: re-solve on the basic support in high precision
if "--certify-primal" in sys.argv:
    xs = r.x
    supp = [j for j in range(len(C)) if xs[j] > 1e-12 and j != j0]
    print("primal support:", len(supp))
    Mm = mp.matrix(len(VIS), len(supp))
    Acsr = Ad.tocsr()
    for i in range(len(VIS)):
        st, en = Acsr.indptr[i], Acsr.indptr[i + 1]
        pos = {j: v for j, v in zip(Acsr.indices[st:en], Acsr.data[st:en])}
        for k, j in enumerate(supp):
            if j in pos:
                Mm[i, k] = int(pos[j]) * mu[j] / rho[i]
    bb = mp.matrix([1] * len(VIS))
    if len(supp) == len(VIS):
        sol = mp.lu_solve(Mm, bb)
    else:
        sol = mp.qr_solve(Mm, bb)[0]
    res = max(abs(t) for t in (Mm * sol - bb))
    print("hp support solve: min nu/mu =", mp.nstr(min(sol), 6), " residual =", mp.nstr(res, 3))
