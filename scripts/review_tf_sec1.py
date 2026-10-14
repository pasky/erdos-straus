"""R206 from-scratch checks of TORSION_FIRING §1 (Lemma 1.1, Prop 1.2) and §5 Prop 5.1.

(1) Group structure of y^2 = x^3 + D x (h = 3 mod 4) and y^2 = x^3 + B (h = 2 mod 3) by brute force:
    point count and group exponent (max point order), also for h = 3 / small h edge cases.
(2) End-to-end: for every odd prime p <= PMAX, the set of PRIME moduli h = 4y'-1 arising from actual Type II
    solutions 4/p = 1/x + 1/(p y') + 1/(p z') (brute force over x, y') equals the set of primes h = 3 mod 4 for
    which some d >= 1, h !| d, has a 2-torsion point (x_T,0) != (0,0) of y^2 = x^3 + p d x over F_h with
    integer rep x_T in [1,h), 2d | x_T, 2 x_T | h+1.  Also checks Prop 1.2(a) form cd | (h+1)/4, h | p+4c^2d.
(3) Odd squares n = m^2: no 2-torsion point other than (0,0) on y^2 = x^3 + n d x at h = -1 mod 4d (Prop 5.1).
"""
import sys
from math import gcd
from sympy import isprime, primerange, divisors


def ec_add(P, Q, a, h):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % h == 0:
        return None
    if P == Q:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, h) % h
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, h) % h
    x3 = (lam * lam - x1 - x2) % h
    return (x3, (lam * (x1 - x3) - y1) % h)


def ec_mul(n, P, a, h):
    R = None
    while n:
        if n & 1:
            R = ec_add(R, P, a, h)
        P = ec_add(P, P, a, h)
        n >>= 1
    return R


def points(a, b, h):
    sq = {}
    for y in range(h):
        sq.setdefault(y * y % h, []).append(y)
    pts = []
    for x in range(h):
        for y in sq.get((x ** 3 + a * x + b) % h, []):
            pts.append((x, y))
    return pts


def structure(a, b, h):
    pts = points(a, b, h)
    N = len(pts) + 1
    divs = divisors(N)
    expo = 1
    for P in pts:
        o = next(dd for dd in divs if ec_mul(dd, P, a, h) is None)
        expo = expo * o // gcd(expo, o)
    return N, N // expo, expo  # (#E, m, n) with E = Z/m x Z/n


def legendre(a, h):
    a %= h
    if a == 0:
        return 0
    return 1 if pow(a, (h - 1) // 2, h) == 1 else -1


def check_lemma11(HMAX):
    bad = 0
    cases = 0
    for h in primerange(3, HMAX):
        if h % 4 == 3:
            for D in [1, -1, 2, -2, 3, -3, 5, 6, -7, 10, 11]:
                if D % h == 0:
                    continue
                N, m, n = structure(D, 0, h)
                exp_m = 2 if legendre(D, h) == -1 else 1
                cases += 1
                if N != h + 1 or m != exp_m:
                    bad += 1
                    print("Lemma1.1(a) FAIL", h, D, N, m, n)
        if h % 3 == 2:
            for B in [1, -1, 2, -3, 5, 7, 11]:
                if (6 * B) % h == 0:
                    continue
                N, m, n = structure(0, B, h)
                cases += 1
                if N != h + 1 or m != 1:
                    bad += 1
                    print("Lemma1.1(b) FAIL", h, B, N, m, n)
    # edge cases h = 2, 3 (not claimed; documented in review)
    print("lemma 1.1: cases", cases, "fail", bad)


def typeII_prime_moduli(p):
    """all h = 4y'-1 (both orders) from Type II solutions, brute force over x and y'."""
    hs = set()
    for x in range((p + 1) // 4, p):
        e = 4 * x - p
        if e <= 0 or x % p == 0:
            continue
        # e/x = 1/y' + 1/z', y' <= z'  => x/e < y' <= 2x/e
        lo = x // e + 1
        hi = (2 * x) // e
        for yp in range(lo, hi + 1):
            num = x * yp
            den = e * yp - x
            if den > 0 and num % den == 0:
                zp = num // den
                hs.add(4 * yp - 1)
                hs.add(4 * zp - 1)
    return {h for h in hs if isprime(h)}


def torsion_moduli(n, hmax):
    out = set()
    for h in primerange(3, hmax + 1):
        if h % 4 != 3 or n % h == 0:
            continue
        found = False
        d = 1
        while 4 * d <= h + 1 and not found:
            if d % h:
                for xT in range(2 * d, (h + 1) // 2 + 1, 2 * d):
                    if (h + 1) % (2 * xT) == 0 and (xT * xT + n * d) % h == 0:
                        found = True
                        break
            d += 1
        if found:
            out.add(h)
    return out


def torsion_moduli_fast(n, hmax):
    """same criterion, candidates x_T enumerated via divisors: x_T = 2cd with 4cd | h+1."""
    out = set()
    for h in primerange(3, hmax + 1):
        if h % 4 != 3 or n % h == 0:
            continue
        k = (h + 1) // 4
        if any((4 * cd * cd + n * d) % h == 0 for cd in divisors(k) for d in divisors(cd)):
            out.add(h)
    return out


def box_moduli(n, hmax):
    out = set()
    for h in primerange(3, hmax + 1):
        if h % 4 != 3 or n % h == 0:
            continue
        k = (h + 1) // 4
        if any((n + 4 * c * c * (cd // c)) % h == 0 for cd in divisors(k) for c in divisors(cd)):
            out.add(h)
    return out


def check_prop12(PMAX):
    mism = 0
    for p in primerange(3, PMAX + 1):
        hmax = (p + 1) * (p + 5) // 4
        A = typeII_prime_moduli(p)
        B = torsion_moduli(p, hmax)
        C = box_moduli(p, hmax)
        if not (A == B == C):
            mism += 1
            print("Prop1.2 MISMATCH p=", p, sorted(A ^ B), sorted(A ^ C))
    print("prop 1.2 end-to-end: primes <=", PMAX, "mismatches", mism)
    sq_fire = 0
    for m in range(3, 26, 2):
        n = m * m
        sq_fire += len(torsion_moduli_fast(n, (n + 1) * (n + 5) // 4))
    print("odd squares 9..625: torsion-firing (h,n) count", sq_fire)


if __name__ == "__main__":
    check_lemma11(int(sys.argv[1]) if len(sys.argv) > 1 else 400)
    check_prop12(int(sys.argv[2]) if len(sys.argv) > 2 else 120)
