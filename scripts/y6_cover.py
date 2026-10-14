"""y6_cover.py — which odd n <= N have a k=1 cap-2 shot (CAP_TWO Thm 1.1) with g = c*a*B - 1 <= G?
For each triple (a = 4a', B odd sqfree, c odd sqfree, gcd(c,B)=1, g <= G), W_n holds iff n = -B^2/(4a^2) (mod g)
(g | 4na^2 + B^2). Marks odd n in that class with gcd(caB, n) = 1, processing triples by increasing g.
Output: uncovered count (non-squares / squares), histogram of minimal g by decade, and the uncovered non-squares.
Usage: y6_cover.py N G [primes_only]"""
import sys, numpy as np
from math import gcd, isqrt
from sympy import primefactors
N, G = int(sys.argv[1]), int(sys.argv[2]); primes_only = len(sys.argv) > 3
sqf = np.ones(G+1, bool)
for p in range(2, isqrt(G)+1): sqf[p*p::p*p] = False
trip = []
for a in range(4, G+2, 4):
    for B in range(1, (G+1)//a + 1, 2):
        if not sqf[B]: continue
        for c in range(1, (G+1)//(a*B) + 1, 2):
            if sqf[c] and gcd(c, B) == 1: trip.append((c*a*B - 1, a, B, c))
trip.sort()
best = np.zeros(N+1, np.int64)   # minimal g
bB = np.zeros(N+1, np.int64); bc = np.zeros(N+1, np.int64)
for g, a, B, c in trip:
    n0 = (-B*B*pow(4*a*a, -1, g)) % g
    if n0 % 2 == 0: n0 += g
    idx = np.arange(n0, N+1, 2*g)
    if idx.size == 0: continue
    ok = best[idx] == 0
    for p in primefactors(c*a*B):
        if p > 2: ok &= (idx % p != 0)
    best[idx[ok]] = g; bB[idx[ok]] = B; bc[idx[ok]] = c
ns = np.arange(3, N+1, 2)
if primes_only:
    from sympy import primerange
    ns = np.array(list(primerange(3, N+1)))
sq = np.array([isqrt(int(v))**2 == v for v in ns])
unc = ns[(best[ns] == 0)]
print(f"N={N} G={G} triples={len(trip)} tested={len(ns)}; squares covered: {int((best[ns][sq] > 0).sum())} of {int(sq.sum())}")
uns = [int(v) for v in unc if isqrt(int(v))**2 != v]
print(f"uncovered non-squares: {len(uns)}", uns[:40])
b = best[ns][~sq]; b = b[b > 0]
print("min-g decade histogram:", {d: int(((b >= 10**d) & (b < 10**(d+1))).sum()) for d in range(0, 9)})
bn = ns[~sq]; bn = bn[best[bn] > 0]
print("max minimal g:", int(best[bn].max()), "at n =", int(bn[np.argmax(best[bn])]))
for r in (1, 3):
    s_ = bn[bn % 4 == r]
    print(f"n = {r} mod 4: {len(s_)}; minimal shot has B = 1 (cap <= 1): {int((bB[s_] == 1).sum())}, B > 1 (cap exactly 2): {int((bB[s_] > 1).sum())}; c = 1 = B (ES shot): {int(((bB[s_]==1)&(bc[s_]==1)).sum())}")
np.save('/tmp/y6_best.npy', np.stack([best, bB, bc]))
