"""z56 PRIMET1: the local model 𝓛 of Z56_PRIMET1.md §3.2 — design matrix, quasi-Poisson IRLS fit (chunked), NB shape by
moments, prediction, Pearson residual and mid-PIT.

Library + CLI:
  fit:     python z56_primet1_local.py fit TRAIN.npy MODEL.npz [opts]       (TRAIN: structured p,r from the sieve split)
  predict: python z56_primet1_local.py predict MODEL.npz DATA.npy OUT.npy     (OUT: p, R, mu, resid, pit, hard)
opts: --drop13 (positive control PC1: no p mod 13 one-hot), --Q0 N (Legendre/Euler-product cutoff, default 1000),
      --qmax N (largest prime with one-hot residues, default 47)
Y := R/2. Everything is a function of p only through size, p mod q (q <= Q0) and the near-square distance kappa.
"""
import sys, math, argparse
import numpy as np

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]

def legendre_table(q):
    t = np.full(q, -1, np.int8); t[0] = 0
    for x in range(1, q): t[x * x % q] = 1
    return t

class Design:
    def __init__(self, Q0=1000, qmax=47, drop13=False):
        self.Q0, self.qmax, self.drop13 = Q0, qmax, drop13
        self.onehot = [(16, [1, 9]), (9, [1, 4, 7]), (35, [r for r in range(35) if math.gcd(r, 35) == 1])]
        for q in primes_upto(qmax):
            if q <= 7: continue
            if drop13 and q == 13: continue
            self.onehot.append((int(q), list(range(1, q))))
        self.eul = [int(q) for q in primes_upto(Q0) if q > 2]
        self.tabs = {q: legendre_table(q) for q in self.eul}
        self.f1q = [q for q in self.eul if q >= 53]
        names = ['1', 'logL', 'invL']
        for q, cl in self.onehot:
            names += [f'p%{q}={c}' for c in cl[1:]]
        names += ['tau', 'tau2', 'f1', 'k16', 'k128', 'k1024', 'logk']
        self.names = names

    def tau(self, p):
        """E_{Q0}(chi_p) L_{Q0}(1,chi_p)^2 / 4 for p ≡ 1 (8) (chi(2) = +1), via (q/p) = (p/q)."""
        logL1 = np.full(len(p), -math.log(1 - 0.5))  # q = 2, chi = +1
        logE = np.zeros(len(p))  # 2chi(2)-1 = 1
        for q in self.eul:
            c = self.tabs[q][(p % np.uint64(q)).astype(np.int64)].astype(np.float64)
            logL1 -= np.log1p(-c / q)
            e = 1 + 2 * c / (q * (q - 1)) - c * c * (q + 1) / (q * q * (q - 1))
            logE += np.log(e)
        return np.exp(logE + 2 * logL1) / 4, np.exp(logL1)

    def build(self, p):
        p = np.asarray(p, dtype=np.uint64)
        pf = p.astype(np.float64); L = np.log(pf)
        cols = [np.ones(len(p)), np.log(L), 1 / L]
        for q, cl in self.onehot:
            r = (p % np.uint64(q)).astype(np.int64)
            for c in cl[1:]: cols.append((r == c).astype(np.float64))
        t, _ = self.tau(p); t = t / L**2
        cols += [t, t * t]
        f1 = np.zeros(len(p))
        for q in self.f1q:
            f1 += np.where(p % np.uint64(q) == 1, math.log(q) / q, 0.0)
        cols.append(f1)
        m = np.floor(np.sqrt(pf)).astype(np.uint64)
        while True:
            bad = m * m > p
            if not bad.any(): break
            m[bad] -= np.uint64(1)
        while True:
            bad = (m + np.uint64(1)) * (m + np.uint64(1)) <= p
            if not bad.any(): break
            m[bad] += np.uint64(1)
        k = np.minimum(p - m * m, (m + np.uint64(1)) * (m + np.uint64(1)) - p).astype(np.float64)
        cols += [(k <= 16).astype(float), (k <= 128).astype(float), (k <= 1024).astype(float), np.log1p(k) / L]
        return np.column_stack(cols)

def fit(p, y, des, iters=25, chunk=200000, tol=1e-9):
    nb = len(des.names)
    beta = np.zeros(nb); beta[0] = math.log(y.mean())
    for it in range(iters):
        A = np.zeros((nb, nb)); g = np.zeros(nb); dev = 0.0
        for s in range(0, len(p), chunk):
            X = des.build(p[s:s + chunk]); yy = y[s:s + chunk]
            eta = X @ beta; mu = np.exp(eta)
            z = eta + (yy - mu) / mu
            A += (X * mu[:, None]).T @ X; g += (X * mu[:, None]).T @ z
            dev += 2 * np.sum(np.where(yy > 0, yy * np.log(np.maximum(yy, 1e-300) / mu), 0) - (yy - mu))
        newb = np.linalg.solve(A + 1e-8 * np.eye(nb), g)
        step = np.max(np.abs(newb - beta)); beta = newb
        print(f'iter {it} dev {dev:.2f} step {step:.2e}', file=sys.stderr, flush=True)
        if step < tol * 1e3 and it > 2: break
    # NB shape by moments and Pearson dispersion
    num = 0.0; den = 0.0; pear = 0.0
    for s in range(0, len(p), chunk):
        X = des.build(p[s:s + chunk]); yy = y[s:s + chunk]; mu = np.exp(X @ beta)
        num += np.sum((yy - mu)**2 - mu); den += np.sum(mu * mu); pear += np.sum((yy - mu)**2 / mu)
    invk = max(num / den, 1e-6)
    cov = np.linalg.inv(A + 1e-8 * np.eye(nb)) * (pear / (len(p) - nb))
    return beta, 1 / invk, pear / (len(p) - nb), cov

def predict(p, y, des, beta, k, chunk=200000):
    from scipy.stats import nbinom
    mus = []
    for s in range(0, len(p), chunk):
        mus.append(np.exp(des.build(p[s:s + chunk]) @ beta))
    mu = np.concatenate(mus)
    resid = (y - mu) / np.sqrt(mu + mu * mu / k)
    pr = k / (k + mu)
    pit = nbinom.cdf(y - 1, k, pr) + 0.5 * nbinom.pmf(y, k, pr)
    return mu, resid, pit

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd'); ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('c', nargs='?')
    ap.add_argument('--drop13', action='store_true'); ap.add_argument('--Q0', type=int, default=1000)
    ap.add_argument('--qmax', type=int, default=47)
    a = ap.parse_args()
    if a.cmd == 'fit':
        d = np.load(a.a); p = d['p']; y = d['r'].astype(np.float64) / 2
        des = Design(a.Q0, a.qmax, a.drop13)
        beta, k, phi, cov = fit(p, y, des)
        np.savez(a.b, beta=beta, k=k, phi=phi, cov=cov, names=np.array(des.names), Q0=a.Q0, qmax=a.qmax, drop13=a.drop13)
        print('k', k, 'phi', phi, 'nparams', len(beta))
        se = np.sqrt(np.diag(cov))
        for nm, b, s in zip(des.names, beta, se):
            if not nm.startswith('p%'): print(f'  {nm:8s} {b:+.5f} ± {s:.5f}')
    elif a.cmd == 'predict':
        m = np.load(a.a); des = Design(int(m['Q0']), int(m['qmax']), bool(m['drop13']))
        d = np.load(a.b); p = d['p']; y = d['r'].astype(np.float64) / 2
        mu, resid, pit = predict(p, y, des, m['beta'], float(m['k']))
        out = np.zeros(len(p), dtype=[('p', '<u8'), ('R', '<i4'), ('mu', '<f8'), ('resid', '<f8'), ('pit', '<f8')])
        out['p'] = p; out['R'] = d['r']; out['mu'] = mu; out['resid'] = resid; out['pit'] = pit
        np.save(a.c, out)
        print('n', len(p), 'mean resid', resid.mean(), 'sd resid', resid.std(), 'frac pit<0.01', (pit < 0.01).mean(),
              'frac pit<0.001', (pit < 0.001).mean(), 'corr(log mu, log(Y+1/2))', np.corrcoef(np.log(mu), np.log(y + 0.5))[0, 1])
