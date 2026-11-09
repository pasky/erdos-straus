# z68_sign_kt3c.py — KT3 after review: correlation of f3 with the -1 fraction of length-4 words admitting NO outgoing
# rescaling move at any cut (incl. endpoint cuts), data from z68_sign_moves.c.
import numpy as np
from scipy.stats import spearmanr
d = np.loadtxt('data/z68/sign/kt3_moves_2e5.txt', dtype=np.int64)
p, L3, n3, L4, n4, NO, nNO, IS, nIS = d.T
m = (L3 >= 10) & (NO >= 10)
f3, f4, fno = n3[m] / L3[m], n4[m] / L4[m], nNO[m] / NO[m]
def resid(f, cls):
    out = f.copy()
    for c in np.unique(cls):
        k = cls == c; out[k] = f[k] - f[k].mean()
    return out
cls = p[m] % 9240
print(f"N={m.sum()} primes p = 1 (8) in (1e4, 2e5] with |L3|, |NOOUT| >= 10; NOOUT share of L4 = {NO[m].sum()/L4[m].sum():.4f}")
print(f"rho(f3, f4 all) = {spearmanr(f3, f4).statistic:+.3f};  rho(f3, f4 NOOUT) = {spearmanr(f3, fno).statistic:+.3f} "
      f"(within mod 9240: {spearmanr(resid(f3, cls), resid(fno, cls)).statistic:+.3f})")
q = np.quantile(f3, 0.01); h = f3 <= q
print(f"hardest 1% by f3 (n={h.sum()}): mean NOOUT -1 fraction {fno[h].mean():.3f} vs all {fno.mean():.3f}")
print(f"ISOL (no move in or out at any cut): share of L4 = {IS.sum()/L4.sum():.4f} (too small per prime for a correlation)")
