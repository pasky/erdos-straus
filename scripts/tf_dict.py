"""TORSION_FIRING §1 checks (O207).
(1) Lemma 1.1: group structure of y^2 = x^3 + Dx over F_h (h = 3 mod 4) and y^2 = x^3 + B (h = 2 mod 3),
    by brute force (count points, compute exponent via orders of all points).
(2) Prop 1.2(b): Type II firing at prime h (box criterion) <=> 2-torsion criterion on E_{pd}; for all odd n in
    a range (primes and odd squares as T1 control), all primes h = 3 mod 4 up to (n+1)(n+5)/4.
Usage: PYTHONPATH=scripts uv run python scripts/tf_dict.py HMAX NMAX
"""
import sys
from sympy import primerange, isprime


def ec_points(h, a, b):
    pts = [None]
    sq = {}
    for y in range(h):
        sq.setdefault(y * y % h, []).append(y)
    for x in range(h):
        r = (x * x * x + a * x + b) % h
        for y in sq.get(r, []):
            pts.append((x, y))
    return pts


def ec_add(P, Q, h, a):
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and (P[1] + Q[1]) % h == 0:
        return None
    if P == Q:
        l = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, h) % h
    else:
        l = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, h) % h
    x = (l * l - P[0] - Q[0]) % h
    return (x, (l * (P[0] - x) - P[1]) % h)


def ec_mul(n, P, h, a):
    R = None
    while n:
        if n & 1:
            R = ec_add(R, P, h, a)
        P = ec_add(P, P, h, a)
        n >>= 1
    return R


def divisors(n):
    ds = [d for d in range(1, int(n ** 0.5) + 1) if n % d == 0]
    return sorted(set(ds + [n // d for d in ds]))


def order(P, N, h, a):
    o = N
    for q in sorted(set(f for f in divisors(N) if f > 1 and isprime(f))):
        while o % q == 0 and ec_mul(o // q, P, h, a) is None:
            o //= q
    return o


def structure(h, a, b):
    pts = ec_points(h, a, b)
    N = len(pts)
    expo = 1
    from math import lcm
    for P in pts[1:]:
        expo = lcm(expo, order(P, N, h, a))
    return N, expo  # group = Z/(N/expo) x Z/expo


def check_lemma(HMAX):
    bad = 0
    cnt = 0
    for h in primerange(5, HMAX):
        if h % 4 == 3:
            for D in [-1, 1, 2, -2, 3, 5, -7, 11]:
                if D % h == 0:
                    continue
                N, e = structure(h, D % h, 0)
                leg = pow(D % h, (h - 1) // 2, h)
                want = (h + 1) if leg == 1 else (h + 1) // 2
                cnt += 1
                if N != h + 1 or e != want:
                    bad += 1
                    print("LEMMA (a) FAIL", h, D, N, e)
        if h % 3 == 2:
            for B in [1, 2, -3, 5, 7]:
                if (6 * B) % h == 0:
                    continue
                N, e = structure(h, 0, B % h)
                cnt += 1
                if N != h + 1 or e != h + 1:
                    bad += 1
                    print("LEMMA (b) FAIL", h, B, N, e)
    print(f"Lemma 1.1: {cnt} (h, curve) cases checked, {bad} failures")


def fire_box(n, h):
    k = (h + 1) // 4
    t = (-n) % h
    for c in divisors(k):
        for j in divisors(k // c):
            if (c - t * j) % h == 0:
                return True
    return False


def fire_torsion(n, h):
    # exists d>=1, h∤d, 2-torsion point (x_T,0) != (0,0) of y^2 = x^3 + n d x over F_h,
    # x_T in [1,h), 2d | x_T, 2 x_T | h+1.  x_T <= (h+1)/2 so d <= (h+1)/4.
    for x in divisors((h + 1) // 2):
        if x % 2:
            continue
        for d in divisors(x // 2):
            if d % h and (x * x + n * d) % h == 0:
                return True
    return False


def check_prop(NMAX):
    mism = 0
    tot = 0
    fired = {}
    ns = [n for n in range(3, NMAX + 1, 2) if isprime(n)] + [m * m for m in range(3, int(NMAX ** 0.5) + 1, 2)]
    for n in ns:
        H = (n + 1) * (n + 5) // 4
        nf = 0
        for h in primerange(3, H + 1):
            if h % 4 != 3 or n % h == 0:
                continue
            a, b = fire_box(n, h), fire_torsion(n, h)
            tot += 1
            if a != b:
                mism += 1
                print("PROP MISMATCH", n, h, a, b)
            nf += a
        fired[n] = nf
    primes = [n for n in ns if isprime(n)]
    sq = [n for n in ns if not isprime(n)]
    print(f"Prop 1.2(b): {tot} (n,h) pairs, {mism} mismatches; primes with no firing h: "
          f"{[n for n in primes if fired[n] == 0]}; odd squares with a firing h: {[n for n in sq if fired[n] > 0]}")


if __name__ == "__main__":
    check_lemma(int(sys.argv[1]))
    check_prop(int(sys.argv[2]))
