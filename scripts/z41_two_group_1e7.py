"""T2-only census to X (no all-level baseline): primes failing all 2-group levels, by decade; squares control."""
import sys
import numpy as np
from sympy import primerange
from z41_two_group import T2, hits
X = int(sys.argv[1])
L = T2(X)
h = hits(L, X)
sq_hit = sum(1 for m in range(1, int(X ** 0.5) + 1, 2) if h[m * m])
pf = [p for p in primerange(5, X + 1) if not h[p]]
print(f"X={X} |T2|={len(L)} squares hit={sq_hit} primes failing={len(pf)} largest={pf[-3:]}")
lo = 10**6
while lo < X:
    hi = 10 * lo
    a = sum(1 for p in pf if lo < p <= hi); b = len(list(primerange(lo + 1, hi + 1)))
    print(f"  ({lo},{hi}]: {a}/{b} = {a/b:.4f}"); lo = hi
