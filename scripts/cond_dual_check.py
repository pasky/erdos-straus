"""O127 §6: check the dual form of X_slice: exists m = 0 (mod 4), gcd(m,p)=1, g = (-p^{-1} mod m) in [1,m]
with g | m+1; each hit is turned into the Lemma 1.1 factorisation gp+1 = m*m2, m2 = -1 (mod g), and
4/p is checked.  Usage: PYTHONPATH=scripts uv run python scripts/cond_dual_check.py X"""
import sys
from fractions import Fraction
from sympy import primerange
X = int(sys.argv[1]); bad = []
for p in primerange(3, X):
    ok = False
    for m in range(4, 2 * p + 3, 4):
        if m % p == 0:
            continue
        g = (-pow(p, -1, m)) % m or m
        if (m + 1) % g == 0:
            N = g * p + 1; assert N % m == 0; m2 = N // m; assert m2 % g == (g - 1) % g
            f, c = (m + 1) // g, (m2 + 1) // g; d = m // 4; b = (p + c) // f
            assert (p + c) % f == 0 and b >= 1
            assert Fraction(4, p) == Fraction(1, b*d*p) + Fraction(1, c*d) + Fraction(1, b*c*d)
            ok = True; break
    if not ok: bad.append(p)
print("primes <", X, "failing dual form:", bad)
