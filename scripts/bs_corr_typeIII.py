"""Correlation of f_I(p) and f_II(p) (a<=b counts from bs_corr_count.c) across primes; also vs the
least quadratic non-residue n_p and the number of small primes l<=29 with (l/p)=-1.
Usage: bs_corr_typeIII.py countfile [countfile ...]"""
import sys, math
from sympy import isprime, legendre_symbol, primerange
import numpy as np
P = []
import os
MOD = tuple(map(int, os.environ["MOD"].split(","))) if os.environ.get("MOD") else None  # e.g. MOD=24,1
for fn in sys.argv[1:]:
    for line in open(fn):
        n, a, b = map(int, line.split())
        if isprime(n) and (MOD is None or n % MOD[0] == MOD[1]): P.append((n, a, b))
smallp = list(primerange(2, 30))
X = np.array([[a / math.log(n) ** 3, b / math.log(n) ** 3,
               sum(1 for l in smallp if l != n and (l == 2 and n % 8 in (3, 5) or l > 2 and legendre_symbol(l, n) == -1)),
               next(l for l in primerange(2, 10**4) if (l == 2 and n % 8 in (3, 5)) or (l > 2 and legendre_symbol(l, n) == -1))]
              for n, a, b in P])
print('primes', len(P))
print('corr(fI, fII) = %.3f' % np.corrcoef(X[:, 0], X[:, 1])[0, 1])
rI = X[:, 0].argsort().argsort(); rII = X[:, 1].argsort().argsort()
print('Spearman(fI, fII) = %.3f' % np.corrcoef(rI, rII)[0, 1])
for j, nm in ((2, '#nonres l<=29'), (3, 'n_p')):
    print('corr(fI,%s)=%.3f corr(fII,%s)=%.3f' % (nm, np.corrcoef(X[:, 0], X[:, j])[0, 1], nm, np.corrcoef(X[:, 1], X[:, j])[0, 1]))
q = len(P) // 20
lowI = set(np.argsort(X[:, 0])[:q]); lowII = set(np.argsort(X[:, 1])[:q])
print('bottom-5%% overlap: %d of %d (independent: %.1f)' % (len(lowI & lowII), q, q * q / len(P)))
r = (X[:, 0] + X[:, 1]); i = r.argmin(); print('min (fI+fII)/log^3 = %.4f at p=%d (fI=%d fII=%d)' % (r[i], P[i][0], P[i][1], P[i][2]))
