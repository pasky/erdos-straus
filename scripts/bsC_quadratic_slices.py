"""O176 memo bsC_parity_quadratic_only: how much of ES is reachable through slices whose ray condition is purely
quadratic, i.e. M = 4cd | 24 ((Z/M)^x elementary 2-group).  Type I ray condition f = -p (mod 4cd) [f | p^2+4c^2 d],
Type II f = -1 (mod 4cd).  Reports, for primes p <= X: covered by a quadratic slice (Type I or II), by class mod 24;
and odd squares (T1 control).
Run: PYTHONPATH=scripts uv run python scripts/bsC_quadratic_slices.py X
"""
import sys
from math import isqrt
from collections import Counter
from sympy import isprime
from bsC_common import typeI_all, typeII_all

X = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
I, II = typeI_all(X), typeII_all(X)
tot, cov = Counter(), Counter()
for p in range(5, X + 1, 2):
    if not isprime(p):
        continue
    r = p % 24
    tot[r] += 1
    q = any(24 % (4 * t[2] * t[3]) == 0 for t in I.get(p, []) + II.get(p, []))
    cov[r] += q
print('p mod 24: covered by a slice with 4cd | 24 / total')
for r in sorted(tot):
    print(r, cov[r], '/', tot[r])
sq = [m * m for m in range(3, isqrt(X) + 1, 2)]
print('odd squares with any tuple:', sum(1 for s in sq if I.get(s) or II.get(s)))
