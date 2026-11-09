# Q1b: is the local part of W(p) a function of the Legendre symbols chi_p(l) only?  And its relation to
# L(1, chi_p) (= h(p) log eps_p / sqrt p).  Input /tmp/z69mine/w1e8.tsv (p W fmin for primes p = 1 mod 8 <= 1e8).
import numpy as np, sympy
d = np.loadtxt('/tmp/z69mine/w1e8.tsv', dtype=np.int64)
p, W = d[:, 0], d[:, 1].astype(float)
sel = p > 10**6; p, W = p[sel], W[sel]
mu = 0.179 * np.log(p.astype(float))**2; w = W / mu; lw = np.log(w)
rng = np.random.default_rng(69); tr = rng.random(len(p)) < 0.5; te = ~tr
ells = list(sympy.primerange(3, 2000))
chi = {}
for l in ells:
    qr = np.zeros(l, dtype=np.int8) - 1; qr[(np.arange(1, l)**2) % l] = 1; qr[0] = 0
    chi[l] = qr[p % l]
def r2(pred, y=lw):
    A = np.vstack([pred, np.ones_like(pred)]).T
    c, *_ = np.linalg.lstsq(A[tr], y[tr], rcond=None)
    res = y[te] - A[te] @ c
    return 1 - res.var() / y[te].var(), c
for Y in (13, 50, 200, 2000):
    logL = sum(-np.log(1 - chi[l] / l) for l in ells if l <= Y)
    R, c = r2(logL)
    print('log L_y(1,chi_p), y=%5d : R2(log w) = %.4f  slope %.3f' % (Y, R, c[0]))
# free linear model in chi_p(l), l <= 200 (one coefficient per prime)
X = np.vstack([chi[l] for l in ells if l <= 200] + [np.ones(len(p))]).T.astype(float)
c, *_ = np.linalg.lstsq(X[tr], lw[tr], rcond=None)
res = lw[te] - X[te] @ c
print('free linear model in chi_p(l), l<=200: R2(log w) = %.4f' % (1 - res.var() / lw[te].var()))
coef = c[:-1]; L200 = [l for l in ells if l <= 200]
print('coef*l (should be ~ const if ~ -kappa*chi/l):', [round(coef[i] * L200[i], 2) for i in range(12)])
# four twisted Euler products L_y(1, chi_p psi), psi in {1, chi_-4, chi_8, chi_-8} (y = 2000)
psi = {'1': lambda l: 1, '-4': lambda l: 1 if l % 4 == 1 else -1, '8': lambda l: 1 if l % 8 in (1, 7) else -1,
       '-8': lambda l: 1 if l % 8 in (1, 3) else -1}
LL = {k: sum(-np.log(1 - fn(l) * chi[l] / l) for l in ells) for k, fn in psi.items()}
X4 = np.vstack([LL[k] for k in psi] + [np.ones(len(p))]).T
c4, *_ = np.linalg.lstsq(X4[tr], lw[tr], rcond=None)
res4 = lw[te] - X4[te] @ c4
print('4 twisted L(1) model: R2(log w) = %.4f coefs %s' % (1 - res4.var() / lw[te].var(), dict(zip(psi, np.round(c4[:-1], 3)))))
# per-class-mod-8 Euler sums S_a = sum_{l = a mod 8, l<=2000} chi_p(l)/l
S = {a: sum(chi[l] / l for l in ells if l % 8 == a) for a in (1, 3, 5, 7)}
X5 = np.vstack([S[a] for a in S] + [np.ones(len(p))]).T
c5, *_ = np.linalg.lstsq(X5[tr], lw[tr], rcond=None)
res5 = lw[te] - X5[te] @ c5
print('class-mod-8 Euler sums: R2(log w) = %.4f coefs %s' % (1 - res5.var() / lw[te].var(), dict(zip(S, np.round(c5[:-1], 3)))))
# one-hot residue classes p mod l, l <= 60, on a 400k subsample
sub = rng.random(len(p)) < 0.3
cols = []
for l in [l for l in ells if l <= 60]:
    for cl in range(1, l):
        cols.append((p[sub] % l == cl).astype(np.float32))
X2 = np.vstack(cols + [np.ones(sub.sum(), dtype=np.float32)]).T
trs, tes = tr[sub], te[sub]; ys = lw[sub]
c2, *_ = np.linalg.lstsq(X2[trs], ys[trs], rcond=None)
res2 = ys[tes] - X2[tes] @ c2
print('one-hot residue-class model p mod l, l<=60: R2(log w) = %.4f' % (1 - res2.var() / ys[tes].var()))
Xc = np.vstack([chi[l][sub] for l in ells if l <= 60] + [np.ones(sub.sum())]).T.astype(float)
cc, *_ = np.linalg.lstsq(Xc[trs], ys[trs], rcond=None); resc = ys[tes] - Xc[tes] @ cc
print('free chi model l<=60 (same subsample): R2(log w) = %.4f' % (1 - resc.var() / ys[tes].var()))
print('approx noise share of Var(log w): %.3f' % (np.mean(1 / W[te]) / lw[te].var()))
