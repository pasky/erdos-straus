"""O183: 'swapped' ES variant over Q: anchor at 2 (congruence normalisation), partner at infinity (sign pattern).

V_{t,M}(n):  t/n = 1/x + 1/y - 1/z,  x, y, z > 0,  x = y = 1 (mod M), z = -1 (mod M).
For each z <= Z all (x, y) are found exactly via (a x - b)(a y - b) = b^2, a/b = t/n + 1/z.
Reports shapes at n (Type I/II/other w.r.t. prime-power n) and local invariants of
alpha(u) = (-u1/u3, -u2/u3), u = (x, y, -z), at all places.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_swap.py t M Z n1 n2 ...
"""
import sys
from fractions import Fraction
from sympy import divisors, factorint
from geo_common import hilbert


def solutions_complete(t, n, M):
    """ALL solutions: x <= y forces x < 2n/t; for fixed x, 1/y - 1/z = r is a divisor problem."""
    out = set()
    for x in range(1, (2 * n) // t + 2):
        if x % M != 1 % M:
            continue
        r = Fraction(t, n) - Fraction(1, x)
        if r == 0:
            continue
        A, B = abs(r.numerator), r.denominator
        for d in divisors(B * B):
            # r>0: (A y - B)(A z + B) = -B^2 ; r<0: (A z - B)(A y + B) = -B^2 ; d = B^2/(A*w + B)
            w_plus = B * B // d - B  # = A * w for the '+B' variable w
            w_minus = B - d          # = A * v for the '-B' variable v (A v - B = -d)
            if w_plus <= 0 or w_minus <= 0 or w_plus % A or w_minus % A:
                continue
            wp, wm = w_plus // A, w_minus // A
            y, z = (wm, wp) if r > 0 else (wp, wm)
            if y < x or y % M != 1 % M or z % M != (-1) % M:
                continue
            assert Fraction(1, x) + Fraction(1, y) - Fraction(1, z) == Fraction(t, n)
            out.add((x, y, z))
    return sorted(out)


def solutions(t, n, M, Z):
    out = set()
    for z in range(M - 1, Z + 1, M):
        r = Fraction(t, n) + Fraction(1, z)
        a, b = r.numerator, r.denominator
        for d in divisors(b * b):
            # a x - b = d, a y - b = b^2/d  (positive branch: x,y>0 needs a x > b... allow both signs)
            for s in (1, -1):
                dd, ee = s * d, s * (b * b // d)
                if (dd + b) % a or (ee + b) % a:
                    continue
                x, y = (dd + b) // a, (ee + b) // a
                if x <= 0 or y <= 0 or x > y:
                    continue
                if x % M != 1 % M or y % M != 1 % M:
                    continue
                assert Fraction(1, x) + Fraction(1, y) - Fraction(1, z) == Fraction(t, n)
                out.add((x, y, z))
    return sorted(out)


def invariants(u):
    a = Fraction(-u[0], u[2])
    b = Fraction(-u[1], u[2])
    ps = set()
    for q in (a.numerator, a.denominator, b.numerator, b.denominator):
        ps |= set(factorint(abs(q)).keys())
    ps.add(2)
    inv = {'inf': hilbert(a, b, 'inf')}
    for p in sorted(ps):
        inv[p] = hilbert(a, b, p)
    return {k: v for k, v in inv.items() if v == -1}


def shape(sol, n):
    f = factorint(n)
    if len(f) != 1:
        return 'comp'
    (q, e), = f.items()
    vs = []
    for X in sol:
        v = 0
        while X % q == 0:
            X //= q
            v += 1
        vs.append(v)
    big = [v >= e for v in vs]
    zero = [v == 0 for v in vs]
    if sum(big) == 1 and sum(zero) == 2:
        return 'I'
    if sum(big) == 2 and sum(zero) == 1:
        return 'II'
    return 'other'


if __name__ == '__main__':
    t, M, Z = map(int, sys.argv[1:4])
    for n in map(int, sys.argv[4:]):
        sols = solutions_complete(t, n, M) if Z == 0 else solutions(t, n, M, Z)
        cnt = {}
        invset = {}
        for s in sols:
            sh = shape(s, n)
            cnt[sh] = cnt.get(sh, 0) + 1
            key = (sh, tuple(sorted(str(k) for k in invariants((s[0], s[1], -s[2])))))
            invset[key] = invset.get(key, 0) + 1
        print(n, factorint(n), cnt, invset, sols[:3])
