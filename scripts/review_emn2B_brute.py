"""R102B (review B of EXCEPTIONAL_MN2): from-scratch exact m-representability of primes.

m/p = 1/x+1/y+1/z (positive integers).  Take x = min denominator: p/m < x <= 3p/m.
Then A/B := m/p - 1/x (reduced) = 1/y + 1/z  <=>  (Ay-B)(Az-B) = B^2 with both factors > 0
<=>  exists delta | B^2 with delta == -B (mod A) and B^2/delta == -B (mod A).
Independent of PW Cor 2.2/2.4 and of the author's u,v-criterion.

Usage:
  review_emn2B_brute.py list m1,m2,.. P1 P2         -> per m: exceptional primes p in (P1,P2], p not | m
  review_emn2B_brute.py frac m N [stride]           -> proportion representable among primes in (N/2,N]
"""
import sys
from math import gcd


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def two_unit(A, B, fB):
    """1/y+1/z = A/B solvable (gcd(A,B)=1, fB = factorization of B)."""
    if A == 0:
        return False
    B2 = B * B
    f2 = {q: 2 * e for q, e in fB.items()}
    r = (-B) % A
    for d in divisors_from(f2):
        if d % A == r and (B2 // d) % A == r:
            return True
    return False


def representable(m, p):
    xlo = p // m + 1
    xhi = (3 * p) // m
    for x in range(xlo, xhi + 1):
        A = m * x - p
        B = p * x
        g = gcd(A, B)
        A //= g
        B //= g
        fB = factor(B)
        if two_unit(A, B, fB):
            return True
    return False


def primes_in(P1, P2):
    return [p for p in range(P1 + 1, P2 + 1) if is_prime(p)]


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'list':
        ms = [int(x) for x in sys.argv[2].split(',')]
        P1, P2 = int(sys.argv[3]), int(sys.argv[4])
        ps = primes_in(P1, P2)
        for m in ms:
            exc = [p for p in ps if m % p and not representable(m, p)]
            print(m, len([p for p in ps if m % p]), len(exc), ' '.join(map(str, exc)), flush=True)
    elif mode == 'frac':
        m, N = int(sys.argv[2]), int(sys.argv[3])
        stride = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        ps = [p for p in primes_in(N // 2, N) if m % p][::stride]
        rep = sum(representable(m, p) for p in ps)
        print(m, N, len(ps), rep, '%.4f' % (rep / len(ps)), flush=True)
