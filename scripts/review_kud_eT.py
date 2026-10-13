"""R172: for Type II tuples at PRIME n <= N, distribution of Diff(e*T') = Ram_fin((-d,-n)) (the algebra of the
natural pair (2ai+j, 2bi-j)) versus Diff(T') = {n}.  Uses review_kud_tuples' own Hilbert symbol.
Run: PYTHONPATH=scripts uv run --with sympy python scripts/review_kud_eT.py 5000"""
import sys
from collections import Counter
from sympy import divisors, isprime
from review_kud_tuples import diff_from_gram
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
C = Counter()
for a in range(1, N):
    if 2 * a * (2 * a - 1) > N: break
    for d in range(1, N):
        if 2 * a * (2 * a * d - 1) > N: break
        b = a
        while 2 * b * (2 * a * d - 1) <= N:
            for c in divisors(a + b):
                e = (a + b) // c; n = 4 * a * b * d - e
                if 3 <= n <= N and isprime(n):
                    f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
                    assert diff_from_gram(f, 2, f2) == {n}
                    De = diff_from_gram(e * f, 2 * e, e * f2)
                    C['tot'] += 1
                    C['Diff(eT)=={p}' if De == {n} else ('p in Diff(eT), |.|=3+' if n in De else 'p not in Diff(eT)')] += 1
            b += 1
print(dict(C))
