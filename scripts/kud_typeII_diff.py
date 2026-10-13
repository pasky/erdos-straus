"""O172 KUDLA_ES Thm 1.4 check: Diff(T') for Type II certificates of ALL odd n <= X.

Type II(n) tuple (ET param, QUATERNION_ES l.97): a,b,c,d >= 1, 4abd = n + e, a + b = c e (a <= b), f = 4acd - 1,
f' = 4bcd - 1, f f' = 1 + 4 c^2 d n, f = f' = -1 (mod 4cd).
T' = [[f,1],[1,f']] ; B_{T'} = (-f, -f(ff'-1)).  Checks: (i) 2 not in Ram; (ii) Ram_fin == P := {l | n odd :
v_l(n) odd, (-f/l) = -1}; (iii) |Ram_fin| odd; (iv) no tuples at odd squares.
Also records whether B_{T'} = B_{Gram(x,y)} with x = 2ai+j, y = 2bi-j in (-d,-n) (Gram e T').
Run: PYTHONPATH=scripts uv run python scripts/kud_typeII_diff.py X
"""
import sys
from math import isqrt
from collections import Counter
from sympy import factorint, jacobi_symbol, divisors
from geo_common import hilbert

X = int(sys.argv[1]) if len(sys.argv) > 1 else 2000


def ram_fin(A, B):
    ps = set(factorint(abs(A))) | set(factorint(abs(B))) | {2}
    return frozenset(q for q in ps if hilbert(A, B, q) == -1)


stats = Counter()
per_n = Counter()
for a in range(1, X):
    if 4 * a * a - 2 * a > X + 2 * a:
        break
    for d in range(1, X):
        if 4 * a * a * d - 2 * a > X:
            break
        for b in range(a, 10**9):
            if 4 * a * b * d - (a + b) > X:
                break
            for e in divisors(a + b):
                n = 4 * a * b * d - e
                if n < 1 or n > X or n % 2 == 0:
                    continue
                c = (a + b) // e
                f, fp = 4 * a * c * d - 1, 4 * b * c * d - 1
                assert f * fp == 1 + 4 * c * c * d * n
                per_n[n] += 1
                stats['tuples'] += 1
                R = ram_fin(-f, -f * (f * fp - 1))
                P = frozenset(l for l, v in factorint(n).items()
                              if v % 2 == 1 and jacobi_symbol(-f % l, l) == -1)
                stats['2 in Ram'] += (2 in R)
                stats['Ram==P'] += (R == P)
                stats['|Ram| odd'] += (len(R) % 2 == 1)
                if stats['tuples'] <= 3000:
                    stats['B(T\')==(-d,-n) (first 3000)'] += (R == ram_fin(-d, -n))
sq = [m * m for m in range(1, isqrt(X) + 1, 2)]
stats['tuples at odd squares'] = sum(per_n[s] for s in sq)
stats['odd non-square n with no tuple'] = sum(1 for n in range(3, X + 1, 2)
                                              if per_n[n] == 0 and isqrt(n) ** 2 != n)
print(dict(stats))
