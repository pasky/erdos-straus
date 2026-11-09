# Does the divisor structure of the small shifts p + c, c p + 1 (c <= 8) explain W(p) beyond p mod small primes?
import numpy as np, sympy, gzip
T = np.loadtxt('/tmp/z69mine/tau1e7.txt', dtype=np.int64)
Wd = {int(a): int(b) for a, b, c in (l.split() for l in gzip.open('data/z69/mine/W_1e7.tsv.gz', 'rt'))}
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
