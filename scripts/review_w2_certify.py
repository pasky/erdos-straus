#!/usr/bin/env python3
"""R29 from-scratch re-verification of Prop 3.7 (POINTWISE_WINDOW2 §3.7).

Does NOT import or copy the author's scripts.  Model is rebuilt from the
textual definition in POINTWISE_WINDOW2 §3.1/§3.3/§3.5 (+ the documented
tie-break g_k *= 1+1e-7 k and the clip max(1-s,1e-3)):
  * K log-spaced bins on [eps,1]; rep. value g_k = geometric midpoint;
    mass w_k = (1/2) ln(e_{k+1}/e_k).
  * window config = multiplicity vector m, |m| even, sum m_k g_k < 1,
    mu_win(m) = prod w_k^{m_k}/m_k! * (1-sum)^{-1/2}.
  * joint config (m3,m7), mu = product.
  * visible S=(s3,s7) any parity, total <= theta; rho(S)=sum_C nu(C) prod C(C_k,S_k).
Checks:
  1. config set in dump == independently enumerated set; mu agrees.
  2. nu >= 0, nu(empty) = 0, all visible correlations matched (float).
  3. high-precision (mpmath, 60 digits) re-solve of the square system on the
     support: exact solution of the exactly-specified system exists, is
     positive, and the empty config is absent from the support.
Usage: review_w2_certify.py DUMP.json.gz
"""
import sys, gzip, json, itertools
from math import comb
import mpmath as mp

mp.mp.dps = 60
d = json.load(gzip.open(sys.argv[1]))
eps, K, theta = mp.mpf(d["eps"]), d["K"], mp.mpf(d["theta"])
e = [mp.e ** (mp.log(eps) + (0 - mp.log(eps)) * i / K) for i in range(K + 1)]
g = [mp.sqrt(e[i] * e[i + 1]) * (1 + mp.mpf("1e-7") * (i + 1)) for i in range(K)]
w = [mp.log(e[i + 1] / e[i]) / 2 for i in range(K)]
print("bins g:", [mp.nstr(x, 5) for x in g])
print("max |g - dump g|:", mp.nstr(max(abs(a - mp.mpf(b)) for a, b in zip(g, d["g"])), 3))


def windows():
    out = []
    # bounded multiplicities: m_k <= floor(1/g_k)
    ranges = [range(int(1 / g[k]) + 1) for k in range(K)]
    for m in itertools.product(*ranges):
        s = sum(mk * gk for mk, gk in zip(m, g))
        if s < 1 and sum(m) % 2 == 0:
            out.append(m)
    return out


def muw(m):
    s = sum(mk * gk for mk, gk in zip(m, g))
    v = max(1 - s, mp.mpf("1e-3")) ** mp.mpf(-0.5)
    for k in range(K):
        v *= w[k] ** m[k] / mp.factorial(m[k])
    return v


W = windows()
print("window configs:", len(W), " joint:", len(W) ** 2)
mine = {(a, b) for a in W for b in W}
dumpC = [(tuple(c[0]), tuple(c[1])) for c in d["configs"]]
assert set(dumpC) == mine and len(dumpC) == len(mine), "config set mismatch"
muW = {m: muw(m) for m in W}
mu = [muW[a] * muW[b] for a, b in dumpC]
print("max rel |mu - dump mu|:", mp.nstr(max(abs(x - mp.mpf(y)) / x for x, y in zip(mu, d["mu"])), 3))

# visible S: all pairs of multiplicity vectors with total <= theta (any parity)
def subvecs(cap):
    ranges = [range(int(cap / g[k]) + 1) for k in range(K)]
    return [m for m in itertools.product(*ranges) if sum(mk * gk for mk, gk in zip(m, g)) <= cap]
V1 = subvecs(theta)
gs = {m: sum(mk * gk for mk, gk in zip(m, g)) for m in V1}
VIS = [(a, b) for a in V1 for b in V1 if gs[a] + gs[b] <= theta]
print("visible correlations:", len(VIS))
# closeness of visible/invisible boundary (fragility of tie-break)
all1 = subvecs(mp.mpf(1))
sums1 = sorted({float(sum(mk * gk for mk, gk in zip(m, g))) for m in all1})
near = sorted({abs(x + y - float(theta)) for x in sums1 for y in sums1})[:3]
print("closest S-total to theta (distances):", near)
def emb(S, C):
    r = 1
    for sk, ck in zip(S, C):
        if sk > ck:
            return 0
        r *= comb(ck, sk)
    return r

nu = [mp.mpf(x) for x in d["nu"]]
j0 = dumpC.index((tuple([0] * K), tuple([0] * K)))
print("nu(empty)/tau:", nu[j0] / mu[j0], " min nu:", min(d["nu"]))
supp = [j for j, x in enumerate(d["nu"]) if x > 0]
print("support size:", len(supp), " min nu/mu on support:",
      mp.nstr(min(nu[j] / mu[j] for j in supp), 5), " max:", mp.nstr(max(nu[j] / mu[j] for j in supp), 5))
# float residual of the dumped nu
worst = 0
A = []
rhs = []
for S in VIS:
    rm = mp.mpf(0); rn = mp.mpf(0)
    for j, (a, b) in enumerate(dumpC):
        t = emb(S[0], a)
        if t:
            t *= emb(S[1], b)
            if t:
                rm += t * mu[j]
                if d["nu"][j] > 0:
                    rn += t * nu[j]
    worst = max(worst, abs(rn - rm) / rm)
    A.append([emb(S[0], dumpC[j][0]) * emb(S[1], dumpC[j][1]) for j in supp])
    rhs.append(rm)
print("max rel residual of dumped nu:", mp.nstr(worst, 3))
# high-precision exact solve on support (scaled by mu)
M = mp.matrix(len(VIS), len(supp))
for i in range(len(VIS)):
    for k, j in enumerate(supp):
        M[i, k] = A[i][k] * mu[j] / rhs[i]
b = mp.matrix([1] * len(VIS))
print("system shape:", M.rows, M.cols)
if M.rows == M.cols:
    x = mp.lu_solve(M, b)
    print("hp solution: min nu/mu =", mp.nstr(min(x), 8), " max =", mp.nstr(max(x), 8))
    print("hp vs dump max rel diff:", mp.nstr(max(abs(x[k] - nu[j] / mu[j]) / x[k] for k, j in enumerate(supp)), 3))
    r = M * x - b
    print("hp residual:", mp.nstr(max(abs(t) for t in r), 3))
    Minv = mp.inverse(M)
    cond = mp.mnorm(M, 1) * mp.mnorm(Minv, 1)
    print("cond_1(M) =", mp.nstr(cond, 5))
