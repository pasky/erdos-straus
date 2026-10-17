"""O256 / BALANCED_LATTICE: dual (pretentious) side of balance for relation lattices of the first odd primes mod q.

For S = odd primes <= y (k of them), q prime = 3 (mod 8) (U_q = squares, order N = (q-1)/2 odd, cyclic), a_s = discrete log
of s^2 in U_q.  Exact brute force over all characters j in [1, N-1] of U_q:
    D(j) = sum_s || j a_s / N ||   (l1-pretentious distance of psi_j to 1 on S^2, BALANCED_LATTICE Def 1.2)
D_min = min_j D(j), attained at j*; ord(psi_min) = N / gcd(j*, N).  Normalised: nu := D_min * N^{1/k} (Minkowski: nu <=
(k!)^{1/k}; balance at the random-lattice scale = nu not small).  Also P+(N) and, for the visible-order question, the
fraction of q whose extremal character has order <= N^{1/2}, <= N^{3/(2k+4)}.  Random model: same for a uniform a.
usage: z27_dual.py y QLO QHI SAMPLE SEED [classes]
"""
import sys, random
import numpy as np
from sympy import primerange, primitive_root, discrete_log, factorint
from math import gcd, prod, log

y, QLO, QHI, SAMPLE, SEED = map(int, sys.argv[1:6])
CLASSES = len(sys.argv) > 6
S = list(primerange(3, y + 1)); k = len(S); P = prod(S)
rng = random.Random(SEED)


def dmin(a, N):
    best, bj = None, None
    CH = 1 << 21
    for st in range(1, N, CH):
        j = np.arange(st, min(N, st + CH), dtype=np.int64)
        D = np.zeros(len(j), dtype=np.int64)          # exact integer numerators N*D(j); ties -> smallest j
        for s in a:
            r = (j * s) % N
            D += np.minimum(r, N - r)
        i = int(np.argmin(D))
        if best is None or D[i] < best:
            best, bj = int(D[i]), int(j[i])
    return best / N, bj


qs = [q for q in primerange(QLO, QHI) if q % 8 == 3 and P % q]
if SAMPLE and SAMPLE < len(qs):
    qs = sorted(rng.sample(qs, SAMPLE))
rows = []
for q in qs:
    N = (q - 1) // 2
    h = pow(primitive_root(q), 2, q)
    a = [discrete_log(q, s * s % q, h) % N for s in S]
    D, j = dmin(a, N)
    ar = [rng.randrange(N) for _ in S]
    Dr, jr = dmin(ar, N)
    pplus = max(factorint(N)) if N > 1 else 1
    rows.append((q, N, D * N ** (1 / k), N // gcd(j, N), pplus, Dr * N ** (1 / k), N // gcd(jr, N), D == 0))


def qu(v):
    v = sorted(v); f = lambda t: v[min(len(v) - 1, int(t * len(v)))]
    return '%.3f/%.3f/%.3f/%.3f/%.3f/%.3f' % (v[0], f(.01), f(.1), f(.5), f(.9), v[-1])


print('y', y, 'S', S, 'k', k, 'q in', (QLO, QHI), '#q', len(rows), 'Minkowski cap (k!)^(1/k)=%.3f' % prod(range(1, k + 1)) ** (1 / k))
print('index-degenerate (D_min=0): true', sum(r[7] for r in rows), ' random', sum(r[5] == 0 for r in rows))
nd = [r for r in rows if not r[7]]
print('nu = D_min*N^(1/k) quantiles 0/1/10/50/90/100%%  true  :', qu([r[2] for r in nd]))
print('                                               random:', qu([r[5] for r in rows if r[5] > 0]))
print('(order statistics below are CONDITIONED on generation, D_min > 0; R-O256 repair 7)')
for lab, idx in (('true', 3), ('random', 6)):
    rr = nd if lab == 'true' else [r for r in rows if r[5] > 0]
    lo = [log(r[idx]) / log(r[1]) for r in rr]
    print('%-6s ord(psi_min): =N %.3f  >=N^0.9 %.3f  <=N^0.5 %.3f  <=N^(3/(2k+4)) %.4f   [log ord/log N quantiles %s]' % (
        lab, sum(r[idx] == r[1] for r in rr) / len(rr), sum(x >= .9 for x in lo) / len(rr),
        sum(x <= .5 for x in lo) / len(rr), sum(x <= 3 / (2 * k + 4) for x in lo) / len(rr), qu(lo)))
print('ord(psi_min) = P+(N)-free? frac with P+(N) | ord(psi_min): %.3f' % (sum(r[3] % r[4] == 0 for r in nd) / len(nd)))
print('worst q (q, nu, ord, N, P+N):', [(r[0], round(r[2], 3), r[3], r[1], r[4]) for r in sorted(nd, key=lambda r: r[2])[:5]])
if CLASSES:
    from collections import defaultdict
    cl = defaultdict(list)
    for r in rows:
        cl[r[0] % (8 * P)].append(0 if r[7] else r[2])
    best = sorted((max(v), min(v), c, len(v)) for c, v in cl.items())
    print('classes mod 8P:', len(best), ' per-class BEST nu: min %.3f median %.3f ; per-class WORST nu: min %.3f median %.3f' % (
        best[0][0], best[len(best) // 2][0], min(b[1] for b in best), sorted(b[1] for b in best)[len(best) // 2]))
    print('classes with smallest best-nu (bestnu, worstnu, class, #q):', [(round(b[0], 3), round(b[1], 3), b[2], b[3]) for b in best[:4]])
