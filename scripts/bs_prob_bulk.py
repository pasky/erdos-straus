"""O142(b): compound-Poisson calibration of the 'bulk' (e>256) part of f_II(p), 2^20 <= p <= 3e7.
Input: /tmp/fII5_3e7.bin from scripts/bs_prob_fII.c (records p, f, g, f[e<=16], f[e<=256]).
Model (Assessment): bulk(p) ~ kappa * Poisson(lam(p)/kappa), lam(p) = mean of bulk over primes in the
same class mod 120120 and the same dyadic range (local data = quenched disorder).
Run: uv run --with scipy --with numpy python scripts/bs_prob_bulk.py"""
import numpy as np
from scipy.stats import poisson
A = np.fromfile('/tmp/fII5_3e7.bin', dtype=np.uint32).reshape(-1, 5).astype(np.int64)
p, f, g, s16, s256 = A.T
m = p >= 2**20; p, f, s16, s256 = p[m], f[m], s16[m], s256[m]
L = np.log(p.astype(float)); k = np.floor(np.log2(p)).astype(int)
print("share of f from e<=16: %.3f, e<=256: %.3f" % (s16.sum()/f.sum(), s256.sum()/f.sum()))
for nm, x in [("e<=16", s16), ("e<=256", s256), ("e>256", f-s256)]:
    print(f"{nm}: mean {x.mean():.1f} CV {x.std()/x.mean():.3f} corr(x,f) {np.corrcoef(x,f)[0,1]:.3f}")
big = f - s256; Q = 120120; lam = np.zeros(len(p))
for kk in np.unique(k):
    mm = k == kk; u, inv, c = np.unique(p[mm] % Q, return_inverse=True, return_counts=True)
    lam[mm] = (np.bincount(inv, weights=big[mm]) / c)[inv]
kap = ((big-lam)**2).sum() / lam.sum()
print("kappa (number variance/mean, weight-2 units) = %.2f" % kap)
cdf = poisson.cdf(np.floor(big/kap), lam/kap)
for t in [1e-2, 1e-3, 1e-4, 1e-5]:
    print(f"lower tail: model level {t:.0e}, observed fraction {np.mean(cdf < t):.2e}")
rng = np.random.default_rng(1)
sims = [(kap*rng.poisson(lam/kap)/L**3).min() for _ in range(20)]
print("min bulk/L^3: observed %.5f; model (20 sims) median %.5f range [%.5f, %.5f]" %
      ((big/L**3).min(), np.median(sims), min(sims), max(sims)))
print("model expected #{bulk=0} over these primes: %.3g" % np.exp(-lam/kap).sum())
for kk in np.unique(k):
    mm = k == kk
    print(f"2^{kk}: min-cell lam/L^3 {(lam[mm]/L[mm]**3).min():.4f}, median {np.median(lam[mm]/L[mm]**3):.4f}")
