# Compensation test: are witness-cluster counts at different scales correlated across primes after removing
# the local (p mod M) structure?  Negative = compensation (a conservation law), ~0 = independent scales.
import numpy as np, sys
d = np.loadtxt(sys.argv[1] if len(sys.argv) > 1 else '/tmp/z69mine/scales.txt', dtype=np.int64)
p = d[:, 0]; C = d[:, 1:].astype(float)
print('primes', len(p), 'mean clusters per bin', C.mean(0).round(2), 'var/mean', (C.var(0) / C.mean(0)).round(2))
band = np.minimum((np.log(p) - np.log(p.min())) / (np.log(p.max() + 1) - np.log(p.min())) * 20, 19).astype(np.int64)
for M, sz in ((1, 0), (1, 1), (15015, 0), (15015, 1), (15015 * 16, 1)):
    key = p % M + (M * band if sz else 0)
    u, inv = np.unique(key, return_inverse=True)
    R = np.empty_like(C); Rr = np.empty_like(C)
    for j in range(4):
        s = np.bincount(inv, weights=C[:, j]); c = np.bincount(inv)
        mu = s[inv] / c[inv]
        R[:, j] = C[:, j] - mu
        Rr[:, j] = (C[:, j] - mu) / np.sqrt(np.maximum(mu, 1e-9))
    cor = np.corrcoef(R.T)
    print('M=%d %s classes=%d  residual var/mean per bin %s' % (M, '(x 20 size bands)' if sz else '', len(u), (R.var(0) / C.mean(0)).round(2)))
    print('   residual correlations:\n', cor.round(3))
    tot = R.sum(1)
    print('   Var(sum residual) / sum Var(bin residuals) = %.3f (1 = independent, <1 = compensation)' % (tot.var() / R.var(0).sum()))
# richer local model: per-bin regression on one-hot residues p mod l (l <= 100) + p mod 64, 200k subsample,
# fitted on half, residual correlations on the other half
import sympy
rng = np.random.default_rng(1)
idx = rng.choice(len(p), 200000, replace=False); ps = p[idx]; Cs = C[idx]
cols = []
for l in [64] + list(sympy.primerange(3, 100)):
    for cl in range(1, l):
        if np.gcd(cl, l) == 1: cols.append((ps % l == cl).astype(np.float32))
lps = np.log(ps.astype(float))
X = np.vstack(cols + [lps.astype(np.float32), (lps**2).astype(np.float32), np.ones(len(ps), dtype=np.float32)]).T
tr = rng.random(len(ps)) < 0.5; te = ~tr
Rt = np.empty((te.sum(), 4))
for j in range(4):
    c, *_ = np.linalg.lstsq(X[tr], Cs[tr, j], rcond=None)
    Rt[:, j] = Cs[te, j] - X[te] @ c
print('one-hot local model (l<=100, p mod 64) + log p, log^2 p: held-out residual correlations\n', np.corrcoef(Rt.T).round(3))
print('   Var(sum)/sum Var = %.3f' % (Rt.sum(1).var() / Rt.var(0).sum()))
