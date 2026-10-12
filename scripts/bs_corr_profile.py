"""Within primes p = 1 (mod 24) in the count files: regress log f_I(p) and log f_II(p) (a<=b counts,
normalised by log^3 p) on the quadratic profile ((l/p))_{5<=l<=L} (+ intercept), report R^2 and the
correlation of the residuals of Type I and Type II (does a common driver beyond the profile exist?).
Usage: bs_corr_profile.py L countfile [...]"""
import sys, math
import numpy as np
from sympy import isprime, legendre_symbol, primerange
L = int(sys.argv[1]); P = []
for fn in sys.argv[2:]:
    for line in open(fn):
        n, a, b = map(int, line.split())
        if n % 24 == 1 and isprime(n): P.append((n, a, b))
ls = list(primerange(5, L + 1))
Z = np.array([[1.0] + [float(legendre_symbol(l, n)) for l in ls] for n, a, b in P], dtype=float)
yI = np.array([math.log(a / math.log(n) ** 3) for n, a, b in P]); yII = np.array([math.log(b / math.log(n) ** 3) for n, a, b in P], dtype=float)
def fit(y):
    beta, *_ = np.linalg.lstsq(Z, y, rcond=None); r = y - Z @ beta
    return beta, r, 1 - r.var() / y.var()
bI, rI, R2I = fit(yI); bII, rII, R2II = fit(yII)
print('primes p=1 (24): %d, profile primes 5..%d (%d regressors)' % (len(P), L, len(ls)))
print('R^2 (log fI ~ profile) = %.3f ; R^2 (log fII ~ profile) = %.3f' % (R2I, R2II))
print('corr(log fI, log fII) raw = %.3f ; corr of residuals = %.3f' % (np.corrcoef(yI, yII)[0, 1], np.corrcoef(rI, rII)[0, 1]))
print('residual sd: I %.3f  II %.3f' % (rI.std(), rII.std()))
print('coefficients (l: beta_I, beta_II) for first 8 l:', [(l, round(bI[i + 1], 3), round(bII[i + 1], 3)) for i, l in enumerate(ls[:8])])
