"""R42 from-scratch check: is every Type II solution of m/n of the form (5.1)?

(5.1): m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)  with  s(m*uvw - 1) = n*v + u.
Type II (n prime, m >= 4, n > m): exactly two denominators divisible by n.
For each Type II solution (x, n*y', n*z') we search w | gcd(x,y',z') and both orderings of (y',z')
for positive integers s,u,v with x = suw, y' = svw, z' = uvw.  We also check Lemma 5.1(i):
the residue n mod M (M = m*uvw - 1) lies in R_m(M) = {-mD mod M : D | A^2}, A = uvw.
Also composite n (n coprime to m) are tested, with Type II defined as: n | y, n | z, gcd(x, n) = 1
(the condition 'abd coprime to n' of Elsholtz-Tao Prop 2.6) and separately n | y, n | z, n does not divide x.
Run: PYTHONPATH=scripts uv run python scripts/review_tr_typeII.py
"""
from fractions import Fraction
from math import gcd, isqrt
import sys


def sols(m, n):
    """All (x<=y<=z) with m/n = 1/x+1/y+1/z."""
    out = []
    t = Fraction(m, n)
    x = n // m + 1
    while Fraction(3, x) >= t:
        r1 = t - Fraction(1, x)
        if r1 > 0:
            y = max(x, int(1 / r1) + 1)
            while Fraction(2, y) >= r1:
                r2 = r1 - Fraction(1, y)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                    out.append((x, y, r2.denominator))
                y += 1
        x += 1
    return out


def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]


def sq(a):
    r = isqrt(a)
    return r if r * r == a else None


def fits(m, n, x, yp, zp):
    for w in divisors(gcd(gcd(x, yp), zp)):
        X, Y, Z = x // w, yp // w, zp // w  # X = su, Y = sv, Z = uv
        if (X * Y) % Z or (X * Z) % Y or (Y * Z) % X:
            continue
        s, u, v = sq(X * Y // Z), sq(X * Z // Y), sq(Y * Z // X)
        if None in (s, u, v) or s * u != X or s * v != Y or u * v != Z:
            continue
        A = u * v * w
        M = m * A - 1
        assert s * M == n * v + u, (m, n, x, yp, zp)
        Rm = {(-m * D) % M for D in divisors(A * A)}
        assert n % M in Rm
        return (s, u, v, w, M)
    return None


def is_prime(k):
    return k > 1 and all(k % p for p in range(2, isqrt(k) + 1))


def check(m, nmax, composite=False):
    bad, tot = [], 0
    for n in range(m + 1, nmax + 1):
        if gcd(n, m) != 1 or (is_prime(n) == composite):
            continue
        for (x, y, z) in sols(m, n):
            trip = (x, y, z)
            for i in range(3):
                others = [trip[j] for j in range(3) if j != i]
                xi = trip[i]
                if all(o % n == 0 for o in others) and xi % n:
                    tot += 1
                    yp, zp = others[0] // n, others[1] // n
                    if not (fits(m, n, xi, yp, zp) or fits(m, n, xi, zp, yp)):
                        bad.append((n, trip, gcd(xi, n)))
    return tot, bad


if __name__ == "__main__":
    for m in (4, 5, 6, 7, 8, 11):
        tot, bad = check(m, 400 if m < 8 else 250)
        print(f"m={m} prime n: Type II solutions {tot}, not of form (5.1): {len(bad)}", bad[:3])
        assert not bad
    for m in (4, 5, 7):
        tot, bad = check(m, 150, composite=True)
        print(f"m={m} composite n (gcd(n,m)=1): Type II(n|y,z, n∤x) {tot}, not of form (5.1): {len(bad)};"
              f" of those with gcd(x,n)=1: {sum(1 for b in bad if b[2] == 1)}", bad[:3])
    sys.stdout.flush()
