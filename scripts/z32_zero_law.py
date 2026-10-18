"""O262: fit the universal zero law P0(mu) = exp(-a mu^beta) on the ladder units (z32_universal.py -> units.npy;
columns m, k, mu, n, zeros, <=2) by binomial maximum likelihood on a grid; out-of-sample test: train on p < 2^K,
predict the zeros at p >= 2^K for every m; also leave-one-m-out."""
import sys, numpy as np
R = np.load('/tmp/z32/units.npy'); m, k, mu, n, z = R[:, 0], R[:, 1], R[:, 2], R[:, 3], R[:, 4]
def fit(s):
    best = None
    for beta in np.arange(0.5, 1.21, 0.01):
        x = mu[s]**beta
        for a in np.exp(np.arange(np.log(0.05), np.log(3), 0.01)):
            lp = -a*x; p0 = np.exp(lp); ll = (z[s]*lp + (n[s]-z[s])*np.log1p(-np.minimum(p0, 1-1e-12))).sum()
            if best is None or ll > best[0]: best = (ll, a, beta)
    return best[1], best[2]
pred = lambda a, b, s: (n[s]*np.exp(-a*mu[s]**b)).sum()
a, b = fit(np.ones(len(R), bool)); print(f'ALL: a={a:.3f} beta={b:.2f}')
for K in (18, 20, 22):
    tr = k < K; a, b = fit(tr); print(f'train p<2^{K}: a={a:.3f} beta={b:.2f}')
    for mm in range(4, 25):
        s = (~tr) & (m == mm); print(f'   m={mm}: predicted {pred(a,b,s):.1f} observed {int(z[s].sum())}')
print('leave-one-m-out (all p):')
for mm in range(4, 25):
    a, b = fit(m != mm); s = m == mm; print(f'   m={mm}: a={a:.3f} b={b:.2f} predicted {pred(a,b,s):.1f} observed {int(z[s].sum())}')
