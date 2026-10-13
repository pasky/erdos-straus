"""O176 (bsC_) shared enumerators of ET Type I / Type II tuples for ALL odd n <= X (grouped by n).

Type I : a,b,c,d >= 1, 4abd = n e + 1, a + b = c e   (a <= b).   Loop a, d, e | 4a^2 d + 1, c.
Type II: a,b,c,d >= 1, 4abd = n + e, a + b = c e   (a <= b).     f = 4acd-1, f' = 4bcd-1, ff' = 1+4c^2 d n.
(Same loops as scripts/kud_typeI_diff.py / kud_typeII_diff.py, O172.)
"""
from collections import defaultdict
from sympy import divisors


def typeI_all(X):
    out = defaultdict(list)
    for a in range(1, X):
        if 2 * a > X + 2:
            break
        for d in range(1, X):
            if a * d > (X + 1) // 2 + 1:
                break
            F = 4 * a * a * d + 1
            for e in divisors(F):
                f = F // e
                c0 = max(1, -(-(2 * a) // e))
                for c in range(c0, 10**9):
                    n = 4 * a * c * d - f
                    if n > X:
                        break
                    if n < 1 or n % 2 == 0:
                        continue
                    b = c * e - a
                    out[n].append((a, b, c, d, e))
    return out


def typeII_all(X):
    out = defaultdict(list)
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
                    out[n].append((a, b, (a + b) // e, d, e))
    return out
