# Q1: how much of W(p) is "local"? Multiplicative model E W = mu * prod_q g_q(p mod q) over prime powers / primes q,
# fitted by Poisson backfitting (iterative proportional fitting). 2-fold CROSS-FIT on the primes p = 1 mod 8 in
# (1e6, 1e8]: every prime gets an out-of-fold prediction E_cf. Saves (p, W, E_cf) to /tmp/z69mine/localfit_E.npy.
# Usage: python z69_mine_local.py [max prime modulus, default 200]   (input /tmp/z69mine/w1e8.tsv: p W fmin)
import numpy as np, sys, sympy
d = np.loadtxt('/tmp/z69mine/w1e8.tsv', dtype=np.int64)
p, W = d[:, 0], d[:, 1].astype(float)
sel = p > 10**6; p, W = p[sel], W[sel]
L = np.log(p.astype(float)); mu = 0.179 * L * L; w = W / mu
rng = np.random.default_rng(69); fold = rng.random(len(p)) < 0.5
mods = [16, 32, 64, 128] + list(sympy.primerange(3, int(sys.argv[1]) if len(sys.argv) > 1 else 200)) + [9, 27, 25, 49, 121]

def fit(tr, iters=4):
    G = {q: np.ones(q) for q in mods}
    def pred():
        s = np.zeros(len(p))
        for q in mods: s += np.log(G[q][p % q])
        return np.exp(s)
    for it in range(iters):
        for q in mods:
            P = pred(); key = p % q
            num = np.bincount(key[tr], weights=W[tr], minlength=q); den = np.bincount(key[tr], weights=(mu * P)[tr], minlength=q)
            G[q] = G[q] * np.where(den > 0, num / np.maximum(den, 1e-300), 1.0)
    return G, pred()

E = np.empty(len(p))
for tr in (fold, ~fold):
    G, P = fit(tr)
    E[~tr] = (mu * P)[~tr]          # out-of-fold prediction
    te = ~tr
    r2 = 1 - np.var((W - mu * P)[te] / mu[te]) / np.var(w[te])
    print('fold: held-out R2(w) = %.4f   Poisson floor share %.4f' % (r2, np.mean((mu * P / mu**2)[te]) / np.var(w[te])))
r2 = 1 - np.var((W - E) / mu) / np.var(w)
print('cross-fitted (all primes out-of-fold): R2(w) = %.4f, Poisson floor share %.4f' % (r2, np.mean(E / mu**2) / np.var(w)))
z = (W - E) / np.sqrt(E)
print('variance of Pearson residual (Poisson = 1): %.3f' % np.var(z))
for q in mods[:20]:
    g = G[q]; nz = [c for c in range(q) if np.gcd(c, q) == 1]
    print(q, 'min', round(g[nz].min(), 3), 'max', round(g[nz].max(), 3), 'g(1)', round(g[1], 3))
np.save('/tmp/z69mine/localfit_E.npy', np.stack([p, W, E]))
