#!/usr/bin/env python3
"""Review of EXCEPTIONAL_TUPLES.md §5(c): iid-sampling noise model.
If [1,N] were N iid draws from the CRT law (independent Bern(p_l)), the sd of
S_j/N is sqrt(Var binom(f,j)/N). Compare max_j sd with eta_K = e^{-K/e^2}/K.
Second block: growth rate log(max_j E binom(f,j)^2)/mu for Poisson(mu) (-> 3)."""
import sys
from math import comb, exp, sqrt
import numpy as np
from mpmath import mp, binomial, factorial, mpf, exp as mexp, log as mlog
sys.path.insert(0, 'scripts')
from tuples_moments import primes_upto, R_set

P = [int(l) for l in primes_upto(3000) if l % 4 == 3]
print("# y K mu eta_K | max_j sd(S_j/N) under iid CRT sampling at N=1e6,1e7,1e8 (argmax j)")
for y, K in [(100, 22), (300, 32), (1000, 46), (3000, 60)]:
    ps = [len(R_set(l)) / l for l in P if l <= y]
    pmf = np.zeros(len(ps) + 1); pmf[0] = 1
    for p in ps:
        pmf[1:] = pmf[1:] * (1 - p) + p * pmf[:-1]; pmf[0] *= (1 - p)
    row = []
    for N in (1e6, 1e7, 1e8):
        sd = []
        for j in range(K + 1):
            b = np.array([comb(m, j) for m in range(len(pmf))], float)
            m1 = (b * pmf).sum(); m2 = (b * b * pmf).sum()
            sd.append(sqrt(max(m2 - m1 * m1, 0) / N))
        row.append(f"{max(sd):.2e}(j={int(np.argmax(sd))})")
    print(y, K, f"{sum(ps):.3f}", f"{exp(-K/exp(2))/K:.2e}", "|", *row)
mp.dps = 30
print("# Poisson(mu): log(max_j E binom(f,j)^2)/mu")
for mu in (5, 10, 20, 40):
    M = int(10 * mu + 60)
    pmf = [mexp(-mu) * mpf(mu) ** m / factorial(m) for m in range(M)]
    best = max(sum(binomial(m, j) ** 2 * pmf[m] for m in range(M)) for j in range(4 * mu))
    print(mu, f"{float(mlog(best) / mu):.4f}")
