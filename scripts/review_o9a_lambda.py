"""R34a: from-scratch check of Case A lambda bound in OMEGA9 Thm 1.1.

lambda = 1 - x^{beta-1}/beta, u = (1-beta) log x.  Claim: lambda >= min(u,1)/2
when log x >= 16 (and beta >= 1/2, i.e. u <= log x / 2).
Also checks the author's intermediate steps:
  (s1) 1/beta <= 1 + 2(1-beta) for beta >= 1/2
  (s2) 2(1-beta) e^{-u} <= 2 min(u,1)/log x  (true for all u since u e^{-u} <= 1/e;
       the author's stated justification for u>1 is different, see review m3)
"""
import numpy as np

worst = np.inf
worst_at = None
for lx in np.concatenate([np.linspace(16, 100, 300), np.geomspace(100, 1e8, 300)]):
    u = np.concatenate([np.geomspace(1e-12, 1, 2000), np.linspace(1, lx / 2, 2000)])
    beta = 1 - u / lx
    lam = 1 - np.exp(-u) / beta
    ratio = lam / (np.minimum(u, 1) / 2)
    i = np.argmin(ratio)
    if ratio[i] < worst:
        worst, worst_at = ratio[i], (lx, u[i])
    assert np.all(1 / beta <= 1 + 2 * (1 - beta) + 1e-15)
    assert np.all(2 * (1 - beta) * np.exp(-u) <= 2 * np.minimum(u, 1) / lx + 1e-15)
print("min over grid of lambda/(min(u,1)/2) = %.6f at log x=%.3g, u=%.3g" % (worst, *worst_at))
assert worst >= 1
# below log x = 16 the claim can fail? probe
for lx in [2, 4, 8, 12]:
    u = np.geomspace(1e-9, lx / 2, 20000)
    beta = 1 - u / lx
    lam = 1 - np.exp(-u) / beta
    print("log x=%g: min ratio %.4f" % (lx, np.min(lam / (np.minimum(u, 1) / 2))))
