"""R279 from-scratch check of Thm 1.1 / Prop 4.1(a) of BM_CORRECTED_COUNT.md.

Own Hilbert symbols at every place, BL's class alpha = (-x/z, -y/z) (BL Thm 1.6, BL (1.1)-(1.2) with
(u1,u2,u3) = (x,y,z)), evaluated at P_{u,B} = (uBC, nBC, nuC), C = (n+u+B)/(4uB) in Q.
Usage: python review_r279_hilbert.py NMAX
"""
import sys
from fractions import Fraction as F
from math import gcd


def factor(n):
    n = abs(n); f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def vsplit(x, l):
    """x = l^v * w, w an l-unit rational; return (v, num, den) of w."""
    a, b = x.numerator, x.denominator
    v = 0
    while a % l == 0:
        a //= l; v += 1
    while b % l == 0:
        b //= l; v -= 1
    return v, a, b


def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    r = pow(a, (l - 1) // 2, l)
    return 1 if r == 1 else -1


def hilbert(a, b, l):
    """(a,b)_l for nonzero rationals a,b; l prime or 0 for infinity."""
    if l == 0:
        return -1 if (a < 0 and b < 0) else 1
    va, an, ad = vsplit(a, l)
    vb, bn, bd = vsplit(b, l)
    if l != 2:
        u = an * ad  # same square class as an/ad
        w = bn * bd
        e = ((l - 1) // 2) * va * vb
        s = (-1) ** (e % 2)
        s *= legendre(u, l) ** (vb % 2)
        s *= legendre(w, l) ** (va % 2)
        return s
    u = (an * ad) % 8
    w = (bn * bd) % 8
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    e = eps(u) * eps(w) + va * om(w) + vb * om(u)
    return -1 if e % 2 else 1


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))


def pairs(n):
    u = 1
    while 4 * u - u - 1 <= n:
        B = 1
        while 4 * u * B - u - B <= n:
            if gcd(u, B) == 1 and (u + B) % 2 == 1:
                yield u, B
            B += 1
        u += 1


def main(NMAX):
    stats = dict(pts=0, recip=0, inf=0, off=0, two_int=0, two_ok=0, invp=0, hits=0, hit_ok=0, hit_alloff=0,
                 target=0, sq0=0, nonhit_drop=0)
    bad = []
    for n in range(3, NMAX + 1, 2):
        prime = isprime(n)
        r = int(round(n ** .5))
        square = r * r == n
        if not (prime or square):
            continue
        for (u, B) in pairs(n):
            q = 4 * u * B
            # (2) chi_{-4uB}(-(u+B)) = -1 : Kronecker at negative odd argument = chi(-1)*Jacobi(-4uB/(u+B)), chi(-1)=-1
            if -1 * jacobi(-q, u + B) != -1:
                bad.append(('target', n, u, B))
            stats['target'] += 1
            C = F(n + u + B, q)
            x, y, z = u * B * C, n * B * C, n * u * C
            assert 4 * x * y * z == n * (x * y + x * z + y * z)
            a, b = -x / z, -y / z
            places = set([2]) | set(factor(a.numerator)) | set(factor(a.denominator)) \
                | set(factor(b.numerator)) | set(factor(b.denominator)) | set(factor(n))
            inv = {l: hilbert(a, b, l) for l in places}
            inf = hilbert(a, b, 0)
            stats['pts'] += 1
            prod = inf
            for l in inv:
                prod *= inv[l]
            stats['recip'] += prod == 1
            stats['inf'] += inf == -1
            off = [l for l in inv if l != 2 and (2 * n * u * B) % l]
            stats['off'] += all(inv[l] == 1 for l in off)
            if C.denominator % 2 == 1:
                stats['two_int'] += 1
                stats['two_ok'] += inv[2] == 1
            hit = (n + u + B) % q == 0
            if prime:
                ok = inv[n] == legendre(-u * B, n) == jacobi(-q % n, n)
                stats['invp'] += ok
                if not ok:
                    bad.append(('invp', n, u, B, inv[n]))
                if hit:
                    stats['hits'] += 1
                    stats['hit_ok'] += legendre(-u * B, n) == -1
                    stats['hit_alloff'] += all(inv[l] == 1 for l in inv if l != n)
                else:
                    # BM factor 1 + inv_inf inv_p versus full product over the 'dropped' places l | 2uB
                    dropped = 1
                    for l in inv:
                        if l != n:
                            dropped *= inv[l]
                    if dropped != 1:
                        stats['nonhit_drop'] += 1
            if square:
                stats['sq0'] += jacobi(-q % n, n) in (0, 1) and not hit
    print(stats)
    print('bad', len(bad), bad[:10])


if __name__ == '__main__':
    main(int(sys.argv[1]))
