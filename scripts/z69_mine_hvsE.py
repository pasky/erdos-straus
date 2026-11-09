# Hard primes vs the CROSS-FITTED local multiplicative model of z69_mine_local.py: local deficit E/mu vs total W/mu,
# and calibration of the lower tail: observed number of primes with P(X <= W) <= t versus the number expected under
# (a) Poisson(E) and (b) a negative binomial with the same mean and variance inflation as the Pearson residuals.
import numpy as np
from scipy.stats import poisson, nbinom
p, W, E = np.load('/tmp/z69mine/localfit_E.npy'); p = p.astype(np.int64)
mu = 0.179 * np.log(p)**2
H = set(int(l.split()[0]) for l in open('data/z69/mine/H.txt'))
m = np.array([int(q) in H for q in p])
print('H primes in (1e6,1e8]: %d' % m.sum())
print('median E/mu: H %.3f, all %.3f; percentile of the H median within all: %.4f' % (
    np.median(E[m] / mu[m]), np.median(E / mu), np.mean(E / mu < np.median(E[m] / mu[m]))))
print('median log(W/mu) H %.3f, median log(E/mu) H %.3f; ratio of means of logs %.3f' % (
    np.median(np.log(W[m] / mu[m])), np.median(np.log(E[m] / mu[m])), np.mean(np.log(E[m] / mu[m])) / np.mean(np.log(W[m] / mu[m]))))
phi = np.var((W - E) / np.sqrt(E))                 # variance inflation
# NB with mean E and variance phi*E: n = E/(phi-1), prob = 1/phi
n_nb = E / (phi - 1); pr = 1 / phi
cdfP = poisson.cdf(W, E); cdfN = nbinom.cdf(W, n_nb, pr)
print('variance inflation phi = %.3f' % phi)
ts = (1e-3, 1e-4, 1.118e-5, 1e-6)
eP = {t: np.zeros(len(p)) for t in ts}; eN = {t: np.zeros(len(p)) for t in ts}
for k in range(0, 200):                    # P(F(X) <= t) = F(k_t), k_t = max{k : F(k) <= t}
    fP = poisson.cdf(k, E); fN = nbinom.cdf(k, n_nb, pr)
    for t in ts:
        eP[t] = np.where(fP <= t, fP, eP[t]); eN[t] = np.where(fN <= t, fN, eN[t])
for t in ts:
    print('t=%.3g: observed Poisson-cdf<=t: %d (H %d), expected %.1f | observed NB-cdf<=t: %d (H %d), expected %.1f' % (
        t, (cdfP <= t).sum(), (cdfP[m] <= t).sum(), eP[t].sum(), (cdfN <= t).sum(), (cdfN[m] <= t).sum(), eN[t].sum()))
o = np.argsort(W / mu)[:15]
for i in o:
    print(int(p[i]), int(W[i]), 'E=%.1f mu=%.1f E/mu=%.2f Pcdf=%.1e NBcdf=%.1e' % (E[i], mu[i], E[i] / mu[i], cdfP[i], cdfN[i]))
