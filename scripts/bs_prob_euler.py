"""O142(b): how much of f_II(p)/log^3 p is a 'singular series' S(p) = prod_l sigma_l(p mod l)?
Fit sigma_l(r) = E[f/L^3 | p = r mod l] / E[f/L^3] (marginal, l prime, l^2 for l=2,3 via mod 8, 9)
on half the primes in [2^24, 1e8], test R^2 of log f vs log S_y on the other half, as y grows.
Also: residual dispersion of f around lambda(p) = c*L^3*S_y(p), and the lower tail.
Input /tmp/fII_1e8.bin (scripts/bs_prob_fII.c). Run: PYTHONPATH=scripts uv run python scripts/bs_prob_euler.py"""
import numpy as np

A = np.fromfile('/tmp/fII_1e8.bin', dtype=np.uint32).reshape(-1, 3)
p = A[:, 0].astype(np.int64); f = A[:, 1].astype(float)
m = p >= 2**24
p, f = p[m], f[m]
L = np.log(p.astype(float)); r = f / L**3
train = np.arange(len(p)) % 2 == 0; test = ~train
def primes(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
mods = [8, 9] + [int(q) for q in primes(400) if q > 3]
logS = np.zeros(len(p))
mean_tr = r[train].mean()
y_report = {8, 9, 5, 7, 11, 13, 17, 29, 47, 97, 199, 397}
print("y  R2(log r ~ log S_y, test)  CV of r/S_y (test)")
for q in mods:
    cls = p % q
    sums = np.bincount(cls[train], weights=r[train], minlength=q)
    cnts = np.bincount(cls[train], minlength=q)
    sig = np.where(cnts > 0, sums / np.maximum(cnts, 1) / mean_tr, 1.0)
    logS += np.log(sig[cls])
    if q in y_report:
        x = logS[test]; yv = np.log(r[test])
        c = np.corrcoef(x, yv)[0, 1]
        resid = r[test] / np.exp(logS[test])
        print(f"{q:4d} {c*c:.3f}  {resid.std()/resid.mean():.3f}")
# residual dispersion: f vs lambda = k * L^3 * S (k fitted on train)
S = np.exp(logS)
k = (f[train]).sum() / (L[train]**3 * S[train]).sum()
lam = k * L**3 * S
z = f[test] / lam[test]
print("lambda range (test):", lam[test].min(), np.median(lam[test]), lam[test].max())
print("Var(f-lam)/E(lam) on test:", ((f[test]-lam[test])**2).mean() / lam[test].mean())
print("quantiles of f/lambda:", np.quantile(z, [0, 1e-5, 1e-4, 1e-3, 1e-2, .1, .5, .9]).round(3))
print("quantiles of S:", np.quantile(S[test], [0, 1e-5, 1e-4, 1e-3, 1e-2, .1, .5, .9, .99]).round(3))
i = np.argmin(f[test]); pt = p[test][i]
print("min f at p =", pt, "f =", f[test][i], "lambda =", round(lam[test][i], 1), "S =", round(S[test][i], 3),
      "p mod 840 =", pt % 840)
