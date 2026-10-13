"""O176: coverage of primes p = 1 (mod 24) by the 'quadratic' slices 4cd | 24 (cd | 6), via the divisor forms
  Type I : exists f | p^2 + 4c^2 d, f = -p (mod 4cd)
  Type II: exists f | 1 + 4c^2 d p, f = -1 (mod 4cd)
(STATUS 'useful PROVED structure').  Cross-checked against the tuple enumerator for p <= XCHK.
Run: PYTHONPATH=scripts uv run python scripts/bsC_quad_slices_fast.py X XCHK
"""
import sys
from sympy import primerange, divisors
from bsC_common import typeI_all, typeII_all

X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
XCHK = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
SL = [(c, d) for c in (1, 2, 3, 6) for d in (1, 2, 3, 6) if 6 % (c * d) == 0]


def cov(p):
    for c, d in SL:
        M = 4 * c * d
        if any((f + p) % M == 0 for f in divisors(p * p + 4 * c * c * d)):
            return True
        if any((f + 1) % M == 0 for f in divisors(1 + 4 * c * c * d * p)):
            return True
    return False


I, II = typeI_all(XCHK), typeII_all(XCHK)
bad = 0
for p in primerange(5, XCHK):
    q = any(24 % (4 * t[2] * t[3]) == 0 for t in I.get(p, []) + II.get(p, []))
    bad += (q != cov(p))
print('cross-check mismatches p <', XCHK, ':', bad)
fails, n = [], 0
edges = [10**4, 10**5, 3 * 10**5, 10**6, 3 * 10**6]
k = 0
for p in primerange(5, X):
    if p % 24 != 1:
        continue
    n += 1
    if not cov(p):
        fails.append(p)
    while k < len(edges) and p > edges[k]:
        k += 1
    pass
for E in edges:
    if E <= X:
        m = sum(1 for p in primerange(5, E) if p % 24 == 1)
        print('p<', E, ' p=1(24):', m, ' uncovered by quadratic slices:', sum(1 for q in fails if q < E))
print('first uncovered:', fails[:12])
