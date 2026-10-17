"""O252: exact check of the construction in FORCED_WINDOW Lemma 1.1 / Thm 4.3.

For Mordell-hard primes p <= N: take forced prime windows q = 3 (mod 8), q = -p (mod P), P = prod of odd primes <= y, q <= QMAX.
Target t = -c, c = prod of primes of K with odd exponent; find j in [0, L]^k with prod (s^2)^{j_s} = t (mod q), s | P, minimal
max j; build delta_s = -eps_s + 2 j_s (all primes of K), check it is a certificate of cap <= max(0, maxj - 1) and rebuild the
ES^{(y,e)} solution with exact rationals (z22_common.verify).
usage: z24_thm43_check.py N y QMAX
"""
import sys
from itertools import product
from math import prod
from sympy import primerange, isprime, factorint
from z22_common import verify

N, y, QMAX = map(int, sys.argv[1:4])
S = list(primerange(3, y + 1)); P = prod(S)
HARD = {1, 121, 169, 289, 361, 529}
checked = 0; maxe = 0; worst = None; nwin = 0
for p in primerange(5, N + 1):
    if p % 840 not in HARD:
        continue
    q = None
    for cand in range((-p) % P, QMAX, P):
        if cand > 3 and cand % 8 == 3 and isprime(cand) and pow(p, (cand - 1) // 2, cand) == cand - 1:
            q = cand; break        # (p/q) = -1  <=>  (q/p) = -1  (p = 1 mod 4)
    if q is None:
        continue
    nwin += 1
    K = (p + q) // 4
    fs = factorint(K)
    assert all(K % s == 0 for s in S) and K % 2 == 1
    c = prod(s for s, b in fs.items() if b % 2)
    t = (-c) % q
    g = [pow(s, 2, q) for s in S]
    best = None
    for L in range(0, 400):
        # layer search: some j with max j = L
        found = None
        for j in product(range(L + 1), repeat=len(S)):
            if max(j) != L:
                continue
            if prod(pow(gs, jj, q) for gs, jj in zip(g, j)) % q == t:
                found = j; break
        if found:
            best = found; break
    assert best is not None
    jd = dict(zip(S, best))
    vec = []
    e = 0
    for s, b in fs.items():
        d = -(b % 2) + 2 * jd.get(s, 0)
        if d > b:
            e = max(e, (d - b) // 2)
        vec.append((s, d))
    assert e <= max(0, max(best) - 1)
    verify(p, q, vec, e)
    checked += 1
    if e > maxe:
        maxe = e; worst = (p, q, K, dict(fs), best)
print('y', y, 'P', P, 'hard p <=', N, 'windows found', nwin, 'certificates verified exactly', checked,
      'max cap', maxe, 'at', worst)
