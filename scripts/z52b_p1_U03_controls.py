"""z52b Pass-1 U03 controls: (i) Z0789 shift correlations after removing class means mod 840 (and log p);
(ii) Z0912 lag-1 after class removal; (iii) Z0960 least prime q=1 mod p vs R_K, partial on log p."""
import numpy as np
from math import isqrt
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64); L = np.log1p(R.sum(1))
PM = 10**5 + 60
tau = np.zeros(PM + 1, np.int32)
for dd in range(1, PM + 1): tau[dd::dd] += 1
cls = pr % 840
def resid(v):
    out = v.astype(float).copy()
    for c in np.unique(cls):
        m = cls == c
        if m.sum() > 1: out[m] -= out[m].mean()
    return out
def pc(a, b): return float(np.corrcoef(a, b)[0, 1])
Lr = resid(L)
print("(i) class-mod-840 residual corr of L with log tau(p+s):")
for s in [1, 2, 3, 4, 12, 20]:
    print("  s=%d raw %.3f  resid %.3f" % (s, pc(L, np.log(tau[pr + s])), pc(Lr, resid(np.log(tau[pr + s])))))
print("(ii) lag-1 of residual L (class mod 840 removed):", round(float(np.corrcoef(Lr[:-1], Lr[1:])[0, 1]), 4))
# (iii) least prime q = 1 mod p : recompute (same as analyse) and partial on log p
from math import log
Q = 3 * 10**7
sv = np.ones(Q + 1, bool); sv[:2] = False
for i in range(2, isqrt(Q) + 1):
    if sv[i]: sv[i*i::i] = False
least = []
for p in pr:
    p = int(p); q = 0
    for k in range(1, 10**6):
        c = k * p + 1
        if c > Q: break
        if sv[c]: q = c; break
    least.append(q)
lq = np.log(np.array(least, float)); lp = np.log(pr.astype(float))
def rk(x): return np.argsort(np.argsort(x)).astype(float)
A = np.vstack([np.ones_like(lp), lp]).T
rq = rk(lq) - A @ np.linalg.lstsq(A, rk(lq), rcond=None)[0]
rL = rk(L) - A @ np.linalg.lstsq(A, rk(L), rcond=None)[0]
print("(iii) spearman(log q, L) raw %.3f ; partial on log p %.3f" % (pc(rk(lq), rk(L)), pc(rq, rL)))
# (iv) add size detrending: regress on [1, log p, log^2 p] globally, then class means mod 840
def detrend(v):
    v = v.astype(float); B = np.vstack([np.ones_like(lp), lp, lp**2]).T
    return v - B @ np.linalg.lstsq(B, v, rcond=None)[0]
Ld = resid(detrend(L))
print("(iv) size-detrended + class-mod-840 residual:")
for s in [1, 2, 3, 4, 12, 20]:
    print("  s=%d corr %.3f" % (s, pc(Ld, resid(detrend(np.log(tau[pr + s]))))))
print("  lag-1 of detrended+class residual L:", round(float(np.corrcoef(Ld[:-1], Ld[1:])[0, 1]), 4))
