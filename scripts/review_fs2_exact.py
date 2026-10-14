"""review_fs2_exact.py (R218): EXACT rational evaluation of the finite Case B part of (Σ) for q = 3^r, s <= S,
using the exact-integer route bounds of review_fs2_bounds.py; cross-checks review_fs2_sum.c (long double).
usage: uv run python scripts/review_fs2_exact.py r S"""
import sys
from fractions import Fraction
sys.path.insert(0, 'scripts')
from review_fs2_bounds import make
r, S = int(sys.argv[1]), int(sys.argv[2]); q = 3**r
B = make(q); tot = Fraction(0)
for s in range(3, S + 1):
    acc = 0
    for a, z, y, t in B['patterns'](s):
        acc += (2 if a < y + t else 1) * min(B['routes'](s, a, z, y, t).values())
    term = Fraction(acc, q**((s + 1) // 2 - 1)); tot += term
    print(f"s={s} term={float(term):.12e} cum={float(tot):.12e}", flush=True)
print(f"r={r} S={S} exact finite total = {float(tot):.15e}")
