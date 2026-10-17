"""O252 / FORCED_WINDOW Hypothesis W: how balanced are relation lattices of the first odd primes modulo primes q?

For S = odd primes <= y (k of them), q prime = 3 (mod 8) in [QLO, QHI], U_q = squares (order n = (q-1)/2, odd),
g_s = s^2.  L_min(q) := least L with {prod g_s^{j_s} : 0 <= j_s <= L} = U_q (inf if <g_s> != U_q), computed exactly by
bitset sumsets of arithmetic progressions in Z_n (discrete logs).  rho(q) := (L_min + 1) / n^{1/k} >= 1 (Minkowski).
Reports the distribution of rho, the worst q, and for each class a mod 8P (a = 3 mod 8, P = prod S) the best rho among
q in the class (Hypothesis W asks every class to contain a balanced q).
usage: z24_balanced.py y QLO QHI
"""
import sys
import numpy as np
from sympy import primerange, primitive_root, discrete_log
from math import gcd, prod
from collections import defaultdict

y, QLO, QHI = map(int, sys.argv[1:4])
S = [s for s in primerange(3, y + 1)]
k = len(S); P = prod(S)


def covers(logs, n, L):
    A = np.zeros(n, dtype=bool); A[0] = True
    for a in logs:
        B = A.copy()
        sh = 0
        for _ in range(L):
            sh = (sh + a) % n
            B |= np.roll(A, sh)
        A = B
        if A.all():
            return True
    return A.all()


res = []
for q in primerange(QLO, QHI):
    if q % 8 != 3 or P % q == 0:
        continue
    n = (q - 1) // 2
    g = primitive_root(q)
    h = g * g % q                       # generator of U_q
    logs = [discrete_log(q, s * s % q, h) % n for s in S]
    if gcd(gcd(*logs), n) != 1 if k > 1 else gcd(logs[0], n) != 1:
        res.append((q, None, None)); continue
    lo, hi = max(0, int(n ** (1 / k)) - 2), 1
    while not covers(logs, n, hi):
        hi *= 2
    lo = min(lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if covers(logs, n, mid):
            hi = mid
        else:
            lo = mid + 1
    res.append((q, hi, (hi + 1) / n ** (1 / k)))

ok = [r for r in res if r[1] is not None]
print('y', y, 'S', S, 'k', k, '8P', 8 * P, 'q in', (QLO, QHI), 'q=3(8):', len(res), 'non-generating:', len(res) - len(ok))
rh = sorted(r[2] for r in ok)
qs = lambda f: rh[min(len(rh) - 1, int(f * len(rh)))]
print('rho quantiles 0/10/50/90/99/100%%: %.2f %.2f %.2f %.2f %.2f %.2f' % (rh[0], qs(.1), qs(.5), qs(.9), qs(.99), rh[-1]))
print('worst q (q, L_min, rho):', sorted(ok, key=lambda r: -r[2])[:8])
cls = defaultdict(list)
for r in res:
    cls[r[0] % (8 * P)].append(r)
best = []
for a in sorted(cls):
    v = [r[2] for r in cls[a] if r[2] is not None]
    best.append((min(v) if v else float('inf'), a, len(cls[a])))
best.sort()
print('classes a mod 8P represented:', len(best), ' per-class best rho: min %.2f median %.2f max %.2f' % (
    best[0][0], best[len(best) // 2][0], best[-1][0]))
print('worst classes (best rho, a, #q):', best[-5:])
