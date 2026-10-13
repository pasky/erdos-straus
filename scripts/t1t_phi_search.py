"""O183: general search for V_phi(n) solutions (any shape), to test the full T1 at squares.

For x in a box (sigma1(x) in (n/4, 3n/4], |sigma2(x)| <= B2), solve 1/y + 1/z = 4/n - 1/x = P/Q exactly:
(P y - Q)(P z - Q) = Q^2, D runs over ALL divisors of Q^2 up to units, times units +-phi^j, |j| <= J.
Every solution of V_phi(n) has a denominator with sigma1 <= 3n/4 (sigma1 > 0 for all three), so the search is
complete except for the box in sigma2 and the unit range J.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_phi_search.py B2 J n1 n2 ...
"""
import sys
import math
from itertools import product
from sympy import factorint
from t1t_phi import mul, add, conj, norm, s1, s2, exact_div, phipow, egcd_prime

SQ5 = (-1, 2)  # 2 phi - 1 = sqrt5


def prime_elements(ell):
    """list of (prime element, ideal-norm) above rational prime ell."""
    if ell == 5:
        return [SQ5]
    if ell % 5 in (2, 3):
        return [(ell, 0)]
    for r in range(ell):
        if (r * r - r - 1) % ell == 0:
            q1 = egcd_prime((-r, 1), ell)  # gcd(ell, phi - r)
            q2 = conj(q1)
            return [q1, q2]
    raise ValueError


def factor_O(a):
    """factorisation of a in Z[phi] as dict prime -> exponent (up to a unit)."""
    out = {}
    N = abs(norm(a))
    for ell in factorint(N):
        for q in prime_elements(ell):
            v = 0
            while True:
                b = exact_div(a, q)
                if b is None:
                    break
                a = b
                v += 1
            if v:
                out[q] = v
    assert abs(norm(a)) == 1, a
    return out


def divisors_O(fac):
    items = list(fac.items())
    for exps in product(*[range(e + 1) for _, e in items]):
        d = (1, 0)
        for (q, _), k in zip(items, exps):
            for _ in range(k):
                d = mul(d, q)
        yield d


def box(n, B2):
    lo, hi = n / 4, 3 * n / 4
    # a + b*phi : s1 = a + 1.618 b, s2 = a - 0.618 b ; b = (s1 - s2)/sqrt5
    bmax = int((hi + B2) / math.sqrt(5)) + 1
    for b in range(-bmax, bmax + 1):
        for a in range(int(lo - 2 * abs(b)) - 2, int(hi + 2 * abs(b)) + 3):
            x = (a, b)
            if lo < s1(x) <= hi and abs(s2(x)) <= B2:
                yield x


def vq(a, q):
    v = 0
    while True:
        b = exact_div(a, q)
        if b is None or b == (0, 0):
            return v
        a = b
        v += 1


def solve(n, B2, J):
    units = [mul((s, 0), phipow(j)) for s in (1, -1) for j in range(-J, J + 1)]
    sols = set()
    for x in box(n, B2):
        P = add((4, 0), mul((-n, 0), (1, 0)))  # placeholder, replaced below
        # 4/n - 1/x = (4x - n)/(n x)
        P = add(mul((4, 0), x), (-n, 0))
        Q = mul((n, 0), x)
        if P == (0, 0):
            continue
        Q2 = mul(Q, Q)
        for d0 in divisors_O(factor_O(Q2)):
            for u in units:
                D = mul(d0, u)
                y = exact_div(add(Q, D), P)
                if y is None or y == (0, 0):
                    continue
                Dp = exact_div(Q2, D)
                z = exact_div(add(Q, Dp), P)
                if z is None or z == (0, 0):
                    continue
                trip = (x, y, z)
                if min(s1(t) for t in trip) <= 0:
                    continue
                sg = {s2(t) > 0 for t in trip}
                if len(sg) != 2:
                    continue
                lhs = mul((4, 0), mul(x, mul(y, z)))
                rhs = mul((n, 0), add(add(mul(y, z), mul(x, z)), mul(x, y)))
                assert lhs == rhs
                sols.add(tuple(sorted(trip)))
    return sols


def shape(trip, n):
    fac = factor_O((n, 0))
    if len(fac) != 1:
        return 'comp'
    (q, e), = fac.items()
    vs = [vq(t, q) for t in trip]
    big = sum(v >= e for v in vs)
    zero = sum(v == 0 for v in vs)
    if big == 1 and zero == 2:
        return 'I'
    if big == 2 and zero == 1:
        return 'II'
    return 'other'


if __name__ == '__main__':
    B2, J = float(sys.argv[1]), int(sys.argv[2])
    for n in map(int, sys.argv[3:]):
        sols = solve(n, B2, J)
        cnt = {}
        for t in sols:
            # shape relative to each prime of n (n = rational prime power: may split in O)
            fac = factor_O((n, 0))
            shp = []
            for q, e in fac.items():
                vs = [vq(s, q) for s in t]
                big = sum(v >= e for v in vs)
                zero = sum(v == 0 for v in vs)
                shp.append('I' if (big, zero) == (1, 2) else 'II' if (big, zero) == (2, 1) else 'o')
            key = ''.join(shp)
            cnt[key] = cnt.get(key, 0) + 1
        print(n, 'primes of n in O:', len(factor_O((n, 0))), 'solutions', len(sols), 'shapes', cnt)
