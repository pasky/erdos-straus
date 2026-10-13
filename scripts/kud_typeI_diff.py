"""O172 KUDLA_ES Thm 1.2 check: Diff(T) for Type I certificates of ALL odd n <= X.

Type I(n) tuple (ET param): a,b,c,d >= 1, 4abd = n e + 1, a + b = c e  (enumerated with a <= b;
n composite allowed).  T = Gram of (u,v), u^2=-d, v^2=-ab, uv+vu=1 in B = (-d, -d(4dab-1)) = (-d, -d n e).
Checks: (i) 2 not in Ram(B); (ii) Ram_fin(B) == P(n,d,e) := {l | n : l odd, l !| e, v_l(n) odd, (-d/l) = -1};
(iii) |Ram_fin(B)| odd; (iv) no tuple at odd squares n.
Run: PYTHONPATH=scripts uv run python scripts/kud_typeI_diff.py X
"""
import sys
from math import isqrt
from collections import Counter
from sympy import factorint, divisors, jacobi_symbol
from geo_common import hilbert

X = int(sys.argv[1]) if len(sys.argv) > 1 else 2000


def ram_fin(A, B):
    ps = set(factorint(abs(A))) | set(factorint(abs(B))) | {2}
    return frozenset(q for q in ps if hilbert(A, B, q) == -1)


stats = Counter()
per_n = Counter()
for a in range(1, X):
    for d in range(1, X):
        if a * d > (X + 1) // 2 + 1:
            break
        F = 4 * a * a * d + 1
        for e in divisors(F):
            f = F // e
            c0 = max(1, -(-(2 * a) // e))          # b = c e - a >= a
            for c in range(c0, 10**9):
                n = 4 * a * c * d - f
                if n > X:
                    break
                if n < 1 or n % 2 == 0:
                    continue
                b = c * e - a
                assert 4 * a * b * d == n * e + 1
                per_n[n] += 1
                R = ram_fin(-d, -d * n * e)
                fn = factorint(n)
                P = frozenset(l for l, v in fn.items()
                              if l != 2 and e % l and v % 2 == 1 and jacobi_symbol(-d % l, l) == -1)
                stats['2 in Ram'] += (2 in R)
                stats['Ram==P'] += (R == P)
                stats['Ram!=P'] += (R != P)
                stats['|Ram| odd'] += (len(R) % 2 == 1)
                stats['tuples'] += 1
sq = [m * m for m in range(1, isqrt(X) + 1, 2)]
stats['tuples at odd squares'] = sum(per_n[s] for s in sq)
odd_n = [n for n in range(3, X + 1, 2)]
stats['odd n<=X with no tuple (non-square)'] = sum(1 for n in odd_n if per_n[n] == 0 and isqrt(n) ** 2 != n)
print(dict(stats))
