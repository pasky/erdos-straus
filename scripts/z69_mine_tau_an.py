# Does the divisor structure of the small shifts p + c, c p + 1 (c <= 8) explain W(p) beyond p mod small primes?
import numpy as np, sympy, gzip
T = np.loadtxt('/tmp/z69mine/tau1e7.txt', dtype=np.int64)
Wd = {int(a): int(b) for a, b, c in (l.split() for l in gzip.open('data/z69/mine/W_1e7.tsv.gz', 'rt'))}  # p W fmin
p = T[:, 0]; sel = p > 10**5; T = T[sel]; p = p[sel]
W = np.array([Wd[int(q)] for q in p], dtype=float)
lw = np.log(W / (0.179 * np.log(p.astype(float))**2))
lt = np.log(T[:, 1:].astype(float))
rng = np.random.default_rng(3); tr = rng.random(len(p)) < 0.5; te = ~tr
cols = []
for l in [64] + list(sympy.primerange(3, 100)):
    for cl in range(1, l):
        if np.gcd(cl, l) == 1: cols.append((p % l == cl).astype(np.float32))
Xloc = np.vstack(cols).T
def fit(X, name):
    X = np.hstack([X, np.ones((len(p), 1))])
    c, *_ = np.linalg.lstsq(X[tr], lw[tr], rcond=None)
    res = lw[te] - X[te] @ c
    print('%-40s held-out R2(log w) = %.4f' % (name, 1 - res.var() / lw[te].var()))
    return c
fit(Xloc, 'local one-hot (l<100, mod 64)')
c = fit(lt, 'log tau(p+c), log tau(cp+1), c<=8')
print('   coefs p+c:', c[:8].round(3), ' cp+1:', c[8:16].round(3))
fit(np.hstack([Xloc, lt]), 'local + shifts')
print('noise share approx %.3f' % (np.mean(1 / W[te]) / lw[te].var()))
# H-like tail: mean of sum log tau for the lowest-w 0.1% vs all
s = lt.sum(1); o = np.argsort(lw)
print('sum log tau: lowest 0.1%% w: %.2f   all: %.2f' % (s[o[:len(o) // 1000]].mean(), s.mean()))
# Tail calibration on (1e5, 1e7]: 2-fold cross-fitted log-linear predictor (local one-hot + shifts) -> E = mu*exp(pred)*c,
# c fixing the mean; negative binomial with the residual variance inflation; observed vs expected tail counts.
from scipy.stats import nbinom, poisson
X = np.hstack([Xloc, lt.astype(np.float32), np.ones((len(p), 1), dtype=np.float32)]).astype(np.float32)
del Xloc
pred = np.empty(len(p))
for trm in (tr, te):        # ridge-stabilised normal equations (memory-light), fold-wise
    idx = np.where(trm)[0]
    XtX = np.zeros((X.shape[1], X.shape[1])); Xty = np.zeros(X.shape[1])
    for i0 in range(0, len(idx), 20000):
        B = X[idx[i0:i0 + 20000]].astype(np.float64); XtX += B.T @ B; Xty += B.T @ lw[idx[i0:i0 + 20000]]
    c = np.linalg.solve(XtX + 1e-6 * np.eye(len(XtX)), Xty)
    oth = np.where(~trm)[0]
    for i0 in range(0, len(oth), 20000):
        pred[oth[i0:i0 + 20000]] = X[oth[i0:i0 + 20000]].astype(np.float64) @ c
mu = 0.179 * np.log(p.astype(float))**2
E = mu * np.exp(pred); E *= W.sum() / E.sum()
for name, EE in (('local+shifts', E), ('size only', mu * W.sum() / mu.sum())):
    phi = np.var((W - EE) / np.sqrt(EE)); n_nb = EE / (phi - 1); pr = 1 / phi
    cdfN = nbinom.cdf(W, n_nb, pr); cdfP = poisson.cdf(W, EE)
    ts = (1e-2, 1e-3, 1e-4)
    eN = {t: np.zeros(len(p)) for t in ts}
    for k in range(0, 150):
        fN = nbinom.cdf(k, n_nb, pr)
        for t in ts: eN[t] = np.where(fN <= t, fN, eN[t])
    print('%s: Pearson variance inflation %.3f; ' % (name, phi) + '; '.join(
        't=%g obs %d exp %.1f (Poisson obs %d)' % (t, (cdfN <= t).sum(), eN[t].sum(), (cdfP <= t).sum()) for t in ts))
