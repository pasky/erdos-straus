"""review_da_qpow.py (R178, from scratch): q-power ET families over Z.

For prime n and fixed q, decide whether n has a Type I solution with t = q^s (4abd = tn+1, t | a+b) or a
Type II solution with e = q^s (4abd = n+e, e | a+b), s >= 0, using COMPLETE bounds derived independently:
  * Type I: any denominator of a solution of 4/n = 1/x+1/y+1/z is <= 9n^4/8 (x1 <= 3n/4, x2 <= 2n x1,
    x3 <= n x1 x2); x = abdn and tn = 4abd - 1 = 4x/n - 1 give t < 9n^2/2.
  * Type II: a+b >= e and ab >= a+b-1 give n+e = 4abd >= 4(e-1), so e <= (n+4)/3.
Every solution found is rebuilt and 4/n checked in exact rationals.
usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_da_qpow.py q NMAX
"""
import sys
from fractions import Fraction as Fr
from sympy import factorint, primerange


def divs_from_fac(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def pair_ok(N, m):
    """exists a, b >= 1 with ab | N and a + b = 0 mod m ?  returns (a, b) or None."""
    fac = factorint(N)
    for D in divs_from_fac(fac):
        # a | D, b = D/a
        subfac = factorint(D) if D > 1 else {}
        for a in divs_from_fac(subfac):
            b = D // a
            if (a + b) % m == 0:
                return a, b
    return None


def solve(n, q):
    # interleave by s so that the cheap small-s cases are tried first
    s = 0
    tmax = 9 * n * n // 2 + 1
    emax = (n + 4) // 3
    while True:
        m = q**s
        if m > tmax and m > emax:
            return None
        if m <= tmax and (m * n + 1) % 4 == 0:
            N = (m * n + 1) // 4
            r = pair_ok(N, m)
            if r:
                a, b = r; d = N // (a * b); c = (a + b) // m
                assert Fr(4, n) == Fr(1, a * b * d * n) + Fr(1, a * c * d) + Fr(1, b * c * d)
                return ("I", s)
        if m <= emax and (n + m) % 4 == 0:
            N = (n + m) // 4
            r = pair_ok(N, m)
            if r:
                a, b = r; d = N // (a * b); c = (a + b) // m
                assert Fr(4, n) == Fr(1, a * b * d) + Fr(1, a * c * d * n) + Fr(1, b * c * d * n)
                return ("II", s)
        s += 1


if __name__ == "__main__":
    q, NMAX = int(sys.argv[1]), int(sys.argv[2])
    fails, maxs, cnt = [], 0, 0
    for n in primerange(5, NMAX + 1):
        cnt += 1
        r = solve(n, q)
        if r is None:
            fails.append(n)
        else:
            maxs = max(maxs, r[1])
    print("q=%d NMAX=%d primes(5..NMAX)=%d failures=%d max least s=%d" % (q, NMAX, cnt, len(fails), maxs))
    print("first failures:", fails[:20])
    print("FAILS", " ".join(map(str, fails)))
