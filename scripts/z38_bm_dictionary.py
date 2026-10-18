"""z38_bm_dictionary.py (O268): exact checks of the Bright–Loughran <-> Brauer-character dictionary on (★).

For odd n and a pair (u,B) (gcd 1, u+B odd) put C = (n+u+B)/(4uB) in Q and the rational point
P = (x,y,z) = (uBC, nBC, nuC) of U_n: 4xyz = n(xy+xz+yz).  BL's class alpha = (-x/z, -y/z) = (-B/n, -B/u).
Checks:
 (1) P lies on U_n (exact rationals);
 (2) Hilbert reciprocity  prod_v (alpha)_v = 1, inv_inf = -1;
 (3) inv_ell = 1 for ell not dividing 2nuB; inv_2 = 1 whenever P is 2-integral (BL Lemma 3.8);
 (4) for n = p prime, p not dividing uB:  inv_p(P) = (-uB/p) = kron(-4uB, p);
 (5) identity kron(-4uB, -(u+B)) = -1 (the Brauer character takes the value -1 at the target class a);
 (6) every (★) hit (4uB | p+u+B) has kron(-4uB, p) = -1  (BL Cor 1.3 on (★));
 (7) n = m^2: kron(-4uB, n) = +1 for gcd(n, 2uB) = 1, so the BM main term vanishes.
usage: PYTHONPATH=scripts uv run python scripts/z38_bm_dictionary.py [P]
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import factorint, isprime
from sympy.ntheory import legendre_symbol


def kron(D, n):
    """Kronecker symbol (D/n) for integer D, odd or even n (n may be negative)."""
    if n == 0:
        return 1 if abs(D) == 1 else 0
    res = 1
    if n < 0:
        n = -n
        if D < 0:
            res = -res
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            res = -res
    # Jacobi (D/n), n odd
    a, m, t = D % n, n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                t = -t
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            t = -t
        a %= m
    return res * (t if m == 1 else 0)


def val(x, l):
    """l-adic valuation of a nonzero rational."""
    x = F(x)
    v = 0
    a, b = x.numerator, x.denominator
    while a % l == 0:
        a //= l; v += 1
    while b % l == 0:
        b //= l; v -= 1
    return v, F(a, b)


def hilbert(a, b, l):
    """(a,b)_l for nonzero rationals; l prime or 'inf'."""
    a, b = F(a), F(b)
    if l == 'inf':
        return -1 if (a < 0 and b < 0) else 1
    al, ua = val(a, l)
    be, ub = val(b, l)
    if l != 2:
        # unit parts as integers mod l
        def leg(u):
            return legendre_symbol(u.numerator * pow(u.denominator, -1, l) % l, l)
        s = (-1) ** (al * be * ((l - 1) // 2) % 2)
        return s * leg(ua) ** be * leg(ub) ** al
    ua8 = ua.numerator * pow(ua.denominator, -1, 8) % 8
    ub8 = ub.numerator * pow(ub.denominator, -1, 8) % 8
    eps = lambda u: ((u - 1) // 2) % 2
    om = lambda u: ((u * u - 1) // 8) % 2
    e = (eps(ua8) * eps(ub8) + al * om(ub8) + be * om(ua8)) % 2
    return -1 if e else 1


def check_n(n, stats, prime):
    for u in range(1, n):
        if 3 * u - 1 > n:
            break
        Bmax = (n + u) // (4 * u - 1)
        for B in range(1, Bmax + 1):
            if (u + B) % 2 == 0 or gcd(u, B) != 1:
                continue
            stats['pairs'] += 1
            C = F(n + u + B, 4 * u * B)
            x, y, z = u * B * C, n * B * C, n * u * C
            assert 4 * x * y * z == n * (x * y + x * z + y * z)              # (1)
            a1, a2 = -x / z, -y / z
            assert a1 == F(-B, n) and a2 == F(-B, u)
            places = set(factorint(2 * n * u * B).keys()) | set(factorint(a1.numerator * a1.denominator * a2.numerator * a2.denominator).keys())
            inv = {l: hilbert(a1, a2, l) for l in places}
            inv['inf'] = hilbert(a1, a2, 'inf')
            assert inv['inf'] == -1                                           # (2)
            prod = 1
            for v in inv.values():
                prod *= v
            assert prod == 1                                                  # (2)
            for l in places:                                                  # (3)
                if (2 * n * u * B) % l != 0:
                    assert inv[l] == 1
            if C.denominator % 2 == 1:
                assert inv[2] == 1, (n, u, B)
                stats['2int'] += 1
            assert kron(-4 * u * B, -(u + B)) == -1                           # (5)
            hit = C.denominator == 1
            if prime and (u * B) % n != 0:
                chi = kron(-4 * u * B, n)
                assert inv[n] == chi == legendre_symbol((-u * B) % n, n)      # (4)
                if hit:
                    assert chi == -1                                          # (6)
                    stats['hits'] += 1
            if not prime and gcd(n, 2 * u * B) == 1:
                assert kron(-4 * u * B, n) == 1                               # (7) (only called for squares)


if __name__ == '__main__':
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    st = {'pairs': 0, 'hits': 0, '2int': 0}
    np_ = 0
    for n in range(3, P, 2):
        if isprime(n):
            check_n(n, st, True); np_ += 1
    sq = 0
    for m in range(3, int(P ** 0.5) + 1, 2):
        check_n(m * m, st, False); sq += 1
    print(f"primes<{P}: {np_}, odd squares: {sq}, pairs checked {st['pairs']}, (★) hits {st['hits']}, 2-integral points {st['2int']}: all assertions (1)-(7) passed")
