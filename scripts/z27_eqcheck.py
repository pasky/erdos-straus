"""O256 / BALANCED_LATTICE Hypothesis EQ, small-scale test: are pretentious primes (nu := D_min * N^{1/k} < t) spread evenly
over the reduced classes a mod 8P (a = 3 mod 8)?  All primes q = 3 (mod 8), q in [QLO, QHI], S = odd primes <= y.
Reports, per threshold t: #bad, per-class mean / max / max-over-mean, chi^2 against uniform (df = #classes - 1), and the
same for a uniform random relabelling of classes (null comparison).
usage: z27_eqcheck.py y QLO QHI
"""
import sys, random
import numpy as np
from sympy import primerange, primitive_root, discrete_log
from math import prod
from collections import Counter


def dmin(a, N):  # as in z27_dual.py: min over characters j of sum_s ||j a_s / N||
    j = np.arange(1, N, dtype=np.int64); D = np.zeros(N - 1)
    for s in a:
        r = (j * s) % N; D += np.minimum(r, N - r) / N
    i = int(np.argmin(D)); return float(D[i]), int(j[i])

y, QLO, QHI = map(int, sys.argv[1:4])
S = list(primerange(3, y + 1)); k = len(S); P = prod(S); M = 8 * P
rows = []
for q in primerange(QLO, QHI):
    if q % 8 != 3 or P % q == 0:
        continue
    N = (q - 1) // 2
    h = pow(primitive_root(q), 2, q)
    a = [discrete_log(q, s * s % q, h) % N for s in S]
    D, j = dmin(a, N)
    from math import gcd
    rows.append((q % M, D * N ** (1 / k), N // gcd(j, N), N))
classes = sorted({c for c in range(M) if c % 8 == 3 and np.gcd(c, P) == 1})
print('y', y, 'k', k, '8P', M, '#q', len(rows), '#classes', len(classes))
rng = random.Random(1)
for t, mode in [(t, m) for m in ('all', 'Bad1') for t in (0.3, 0.5, 0.7)]:
    bad = [r[0] for r in rows if r[1] < t and (mode == 'all' or r[2] > r[3] ** (1 / k) / t)]
    cnt = Counter(bad); allc = Counter(r[0] for r in rows)
    exp = np.array([allc[c] * len(bad) / len(rows) for c in classes])
    obs = np.array([cnt[c] for c in classes])
    chi = float(((obs - exp) ** 2 / exp).sum())
    perm = [rng.choice(classes) for _ in bad]
    pc = Counter(perm)
    print(mode, 't=%.1f  #bad %5d (%.3f)  per-class mean %.1f max %d  max/mean %.2f  chi2 %.1f (df %d)  | null max/mean %.2f' % (
        t, len(bad), len(bad) / len(rows), exp.mean(), obs.max(), obs.max() / exp.mean(), chi, len(classes) - 1,
        max(pc.values()) / exp.mean()))
