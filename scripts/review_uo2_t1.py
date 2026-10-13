"""R190 reviewer-2: from-scratch T1 check for ES^(S), S = {3,5,7,11} (UNIT_ORBIT_ES Lemma 1.1, Cor 1.2, Thm 2.4(b)).

Bounded search: x in (n/4, XB*n], y in [x, YB*n]; z = 1/(4/n - 1/x - 1/y) > 0 with z in Z[1/S] and
(mode 'mute') every negative q-valuation of z even, or (mode 'free') no parity condition.
For each solution compute Hilbert-symbol invariants of alpha = (-x/z, -y/z) at oo, 2, q in S, l | n
(own Hilbert symbol code), check the product formula, and record the shape at each prime of n
(I: one denominator with v >= v(n), other two units; II: one unit, two with v >= v(n); o: other).
Usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_uo2_t1.py mode XB YB n...
"""
import sys
from fractions import Fraction
from collections import Counter
import numpy as np
from sympy import factorint, legendre_symbol

S = [3, 5, 7, 11]
mode, XB, YB = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ns = [int(t) for t in sys.argv[4:]]


def v(p, f):
    f = Fraction(f)
    a, b, k = f.numerator, f.denominator, 0
    while a % p == 0:
        a //= p; k += 1
    while b % p == 0:
        b //= p; k -= 1
    return k


def unitpart(p, f):
    f = Fraction(f) / Fraction(p) ** v(p, f)
    return f.numerator * f.denominator  # same square class, integer, prime to p


def hilbert(a, b, p):
    """(a,b)_p in {+1,-1} for nonzero rationals a, b; p prime or 0 (= real place)."""
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, be = v(p, a), v(p, b)
    u, w = unitpart(p, a), unitpart(p, b)
    if p != 2:
        s = (-1) ** ((al * be * ((p - 1) // 2)) % 2)
        return s * legendre_symbol(u % p, p) ** (be % 2) * legendre_symbol(w % p, p) ** (al % 2)
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    return (-1) ** ((eps(u) * eps(w) + al * om(w) + be * om(u)) % 2)


def ok_z(num, den):
    """z = den/num reduced? we get z = By/(Ay-B); test denominator of reduced z."""
    return num


for n in ns:
    fn = factorint(n)
    places = [0, 2] + S + sorted(fn)
    sols = []
    for x in range(n // 4 + 1, XB * n + 1):
        R1 = Fraction(4, n) - Fraction(1, x)
        if R1 <= 0:
            continue
        A, B = R1.numerator, R1.denominator
        ylo = max(x, B // A + 1)
        ys = np.arange(ylo, YB * n + 1, dtype=np.int64)
        num = A * ys - B          # 1/z = num/(B*y)
        den = B * ys
        g = np.gcd(num, den)
        zden = num // g           # z = (den/g)/(num/g): denominator of z is num/g
        rest = zden.copy()
        okpar = np.ones_like(rest, dtype=bool)
        for q in S:
            e = np.zeros_like(rest)
            m = rest % q == 0
            while m.any():
                rest = np.where(m, rest // q, rest)
                e += m
                m = rest % q == 0
            okpar &= (e % 2 == 0)
        sel = rest == 1
        if mode == "mute":
            sel &= okpar
        for y in ys[sel]:
            y = int(y)
            z = 1 / (R1 - Fraction(1, y))
            sols.append((x, y, z))
    inv_stats, shape_stats, qnonzero = Counter(), Counter(), 0
    for (x, y, z) in sols:
        assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
        a, b = -Fraction(x) / z, -Fraction(y) / z
        hs = {p: hilbert(a, b, p) for p in places}
        prod = 1
        for p in places:
            prod *= hs[p]
        assert prod == 1, (n, x, y, z, hs)   # product formula (no other bad places: x,y,z S-integral)
        if any(hs[q] == -1 for q in S):
            qnonzero += 1
        assert hs[0] == -1  # inv_oo = 1/2 (all positive)
        assert hs[2] == 1, (n, x, y, z)
        key = tuple(hs[l] for l in sorted(fn))
        inv_stats[key] += 1
        shp = []
        for l, t in sorted(fn.items()):
            vs = [v(l, x), v(l, y), v(l, z)]
            big = sum(1 for w in vs if w >= t)
            unit = sum(1 for w in vs if w == 0)
            shp.append("I" if (big == 1 and unit == 2) else "II" if (big == 2 and unit == 1) else "o")
        shape_stats["".join(shp) if len(shp) == 1 else "/".join(shp)] += 1
    print(f"[{mode}] n={n} {dict(fn)}: {len(sols)} sols; inv(l|n) sign-vectors {dict(inv_stats)}; "
          f"shapes {dict(shape_stats)}; sols with some inv_q=1/2: {qnonzero}")
