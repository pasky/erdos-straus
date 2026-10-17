"""O256 / BALANCED_LATTICE Hypothesis EQ, small-scale test: are pretentious primes (nu := D_min * N^{1/k} < t) spread evenly
over the reduced classes a mod 8P (a = 3 mod 8)?  All primes q = 3 (mod 8), q in [QLO, QHI], S = odd primes <= y.
Reports, per threshold t: #bad, per-class mean / max / max-over-mean, chi^2 against uniform (df = #classes - 1), and the
same for a uniform random relabelling of classes (null comparison).
Bad1 is existential (some character with D < eps and ord > 1/eps, eps = t N^{-1/k}; R-O256 repair 7); D in exact integers;
null = 300 permutations of the bad flags over q (class populations preserved).
usage: z27_eqcheck.py y QLO QHI
"""
import sys, random
import numpy as np
from sympy import primerange, primitive_root, discrete_log
from math import prod
from collections import Counter


def dprofile(a, N):
    """integer numerators D(j)*N (exact) and orders ord(psi_j) = N/gcd(j, N), j = 1..N-1."""
    j = np.arange(1, N, dtype=np.int64); D = np.zeros(N - 1, dtype=np.int64)
    for s in a:
        r = (j * s) % N; D += np.minimum(r, N - r)
    return D, N // np.gcd(j, N)


y, QLO, QHI = map(int, sys.argv[1:4])
S = list(primerange(3, y + 1)); k = len(S); P = prod(S); M = 8 * P
TS = (0.3, 0.5, 0.7)
rows = []   # (class, {t: in_all}, {t: in_Bad1})
for q in primerange(QLO, QHI):
    if q % 8 != 3 or P % q == 0:
        continue
    N = (q - 1) // 2
    h = pow(primitive_root(q), 2, q)
    a = [discrete_log(q, s * s % q, h) % N for s in S]
    D, od = dprofile(a, N)
    allb, b1 = {}, {}
    for t in TS:
        eps_num = t * N ** (1 - 1 / k)            # D(j)/N < t N^{-1/k}  <=>  D(j) < t N^{1-1/k}
        small = D < eps_num
        allb[t] = bool(small.any())
        b1[t] = bool((small & (od > N ** (1 / k) / t)).any())   # existential Bad1: some psi with D < eps AND ord > 1/eps
    rows.append((q % M, allb, b1))
classes = sorted({c for c in range(M) if c % 8 == 3 and np.gcd(c, P) == 1})
print('y', y, 'k', k, '8P', M, '#q', len(rows), '#classes', len(classes))
rng = np.random.default_rng(1)
lab = np.array([r[0] for r in rows]); idx = {c: i for i, c in enumerate(classes)}
li = np.array([idx[c] for c in lab]); sizes = np.bincount(li, minlength=len(classes))
for mode in ('all', 'Bad1'):
    for t in TS:
        flag = np.array([(r[1] if mode == 'all' else r[2])[t] for r in rows])
        nb = int(flag.sum()); exp = sizes * nb / len(rows)
        chi = lambda f: float((((np.bincount(li[f], minlength=len(classes)) - exp) ** 2) / exp).sum())
        c0 = chi(flag); null = []
        for _ in range(300):
            null.append(chi(rng.permutation(flag)))
        pv = (1 + sum(x >= c0 for x in null)) / 301
        print('%-4s t=%.1f  #bad %5d (%.3f)  per-class mean %.2f max %d  chi2 %.1f (df %d)  perm-null chi2 median %.1f  p=%.3f' % (
            mode, t, nb, nb / len(rows), exp.mean(), np.bincount(li[flag], minlength=len(classes)).max(), c0,
            len(classes) - 1, float(np.median(null)), pv))
