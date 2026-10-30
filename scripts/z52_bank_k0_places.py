"""k = 0 (ES itself): on positive integer ES solutions of 4/p, list the finite places where (-q,-d)_l = -1
(q = 4y-p, d = qz-py) and whether l divides d, q, p; compare with Bright-Loughran's class (-x/z,-y/z)."""
from fractions import Fraction as Fr
from z52_bank_bm_check import hilbert, primes_of
from sympy import primerange
import itertools
def es_solutions(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        m = 4 * x - p
        y = max(x, (p * x) // m)
        while m * y <= 2 * p * x:
            den = m * y - p * x
            if den > 0 and (p * x * y) % den == 0:
                z = p * x * y // den
                if z >= y: out.append((x, y, z))
            y += 1
    return out
stats = {}
for p in primerange(5, 400):
    for (x, y, z) in es_solutions(p):
        for (a, b, c) in set(itertools.permutations((x, y, z))):   # all labelings (y is distinguished in q,d)
            q = 4 * b - p; d = q * c - p * b
            if q == 0 or d == 0: continue
            assert q > 0 and d > 0
            bad = [l for l in sorted(primes_of(a, b, c, q, d, p)) if hilbert(-Fr(q), -Fr(d), l) == -1]
            assert len(bad) % 2 == 1   # real place gives -1, product formula
            for l in bad:
                key = ('l=p' if l == p else ('l=2' if l == 2 else 'other odd l'),
                       'l|d' if d % l == 0 else 'l∤d', 'l|q' if q % l == 0 else 'l∤q')
                stats[key] = stats.get(key, 0) + 1
            blbad = [l for l in sorted(primes_of(a, b, c, p)) if hilbert(-Fr(a, c), -Fr(b, c), l) == -1]
            stats[('BL bad places', tuple('p' if l == p else l for l in blbad))] = stats.get(('BL bad places', tuple('p' if l == p else l for l in blbad)), 0) + 1
for k in sorted(stats, key=str): print(k, stats[k])
