"""Valuation patterns of solutions of 4/p^2 (and 4/p^k): do 'mixed' solutions
(not all denominators divisible by p) exist? If never, then W(p^2) != {} => W(p) != {}."""
import sys
from collections import Counter
from sympy import primerange
from z25_common import W


def v(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


P = int(sys.argv[1]) if len(sys.argv) > 1 else 60
for p in primerange(3, P):
    sols = W(p * p)
    pats = Counter(tuple(sorted((v(t, p) for t in s), reverse=True)) for s in sols)
    mixed = {k: c for k, c in pats.items() if min(k) == 0}
    print(p, p % 24, len(sols), dict(sorted(pats.items())), "MIXED" if mixed else "")
