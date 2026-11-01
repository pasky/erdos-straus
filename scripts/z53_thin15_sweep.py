# z53_thin15_sweep.py — small-height sweep of all four binomial menus (A, A', B, B') at mu = 0 of c0*2^s + 1, for
# RATIONAL u = r/v (gcd 1, r, v <= H, odd primes p <= P, a = c0 u^p - 1 > 0) and the Sophie-Germain shape
# K = 4 w^4, w = r/v (r, v <= H).  Exact and D-independent (z53_thin15_menus.test).  EVIDENCE (bounded heights) except
# where the memo proves the bounds.  Usage: z53_thin15_sweep.py c0 H P
import sys
from math import gcd
from fractions import Fraction as Fr
from z53_thin15_menus import test
c0, H, P = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
ps = [p for p in range(3, P + 1) if all(p % q for q in range(2, p))]
ntest = 0; hits = []
for r in range(1, H + 1):
    print('.. r=%d, tested %d, hits %d' % (r, ntest, len(hits)), flush=True)
    for v in range(1, H + 1):
        if gcd(r, v) != 1: continue
        shapes = [('p=%d' % p, Fr(r, v) ** p) for p in ps] + [('SG', 4 * Fr(r, v) ** 4)]
        for lab, K in shapes:
            a = c0 * K - 1
            if a <= 0: continue
            ntest += 1
            for h in test(c0, a, K):
                hits.append((lab, r, v) + h)
                print('HIT u=%d/%d %s a=%s menu=%s X=%s Xp=%s phi=%s phip=%s' % ((r, v, lab, a) + tuple(map(str, h))), flush=True)
from collections import Counter
print('c0=%d H=%d P=%d: %d (K, a) tested, %d limit hits; by menu %s' % (c0, H, P, ntest, len(hits), dict(Counter(h[3] for h in hits))))
