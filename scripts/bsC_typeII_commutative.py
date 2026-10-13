"""O176 memo bsC_typeII_commutative: check (2ad + k)(2bd + k) = de(1 + 2ck) in Z[k], k^2 = -d n, on all Type II tuples
of all odd n <= X, and the norm identities N(2ad+k) = d e f, N(1+2ck) = f f'.
Run: PYTHONPATH=scripts uv run python scripts/bsC_typeII_commutative.py X
"""
import sys
from bsC_common import typeII_all

X = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
bad = tot = 0
for n, L in typeII_all(X).items():
    for a, b, c, d, e in L:
        D = -d * n                         # k^2 = D
        x1, x2 = 2 * a * d, 2 * b * d      # (x1 + k)(x2 + k) = x1 x2 + D + (x1 + x2) k
        re, im = x1 * x2 + D, x1 + x2
        f, fp = 4 * a * c * d - 1, 4 * b * c * d - 1
        ok = (re == d * e and im == 2 * c * d * e and x1 * x1 - D == d * e * f and 1 - 4 * c * c * D == f * fp)
        bad += not ok
        tot += 1
print('Type II tuples:', tot, ' identity failures:', bad)
