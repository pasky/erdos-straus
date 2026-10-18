"""O272 Thm 3.2 check (m = 3) and spark 3 (cubes).
(a) For primes l, q = 1 (mod 3), lambda | l, pi | q primary in Z[w]: verify (q/lambda)_3 = x1 * x2^2 where
    x1 = (lambda/pi)_3, x2 = (lambda-bar/pi)_3   [exponents of w: k_S = k1 + 2 k2 mod 3], and D = (l/pi)_3 = x1 x2.
(b) Along the forced progression t = 4q = -1/n (mod l): distribution of k_D (l's cubic class mod q) for n = cubes, squares,
    generic -- uniform 1/3 expected (Thm 3.1); and k_S constant per (n, l)? (forcing fixes q mod l, hence S.)
"""
import math
from collections import Counter
from sympy import primerange


def primary(q):
    """primary pi = a + b w (w^2 + w + 1 = 0) with N(pi) = a^2 - ab + b^2 = q, a = 2 (3), b = 0 (3)."""
    for a in range(-2 * math.isqrt(q) - 2, 2 * math.isqrt(q) + 3):
        # solve b^2 - a b + a^2 - q = 0
        disc = a * a - 4 * (a * a - q)
        if disc < 0:
            continue
        r = math.isqrt(disc)
        if r * r != disc:
            continue
        for b2 in (a + r, a - r):
            if b2 % 2:
                continue
            b = b2 // 2
            if a % 3 == 2 and b % 3 == 0:
                return a, b
    raise ValueError(q)


def root_of(a, b, p):
    """cube root of unity r mod p with a + b r = 0 (mod p)."""
    for r in range(2, p):
        if (r * r + r + 1) % p == 0 and (a + b * r) % p == 0:
            return r
    raise ValueError


def expo(y, r, p):
    z = 1
    for k in range(3):
        if z == y % p:
            return k
        z = z * r % p
    raise ValueError((y, r, p))


def sym(c, d, a, b, q):
    """(c + d w / pi)_3 as exponent of w, pi = a + b w primary of norm q."""
    r = root_of(a, b, q)
    return expo(pow((c + d * r) % q, (q - 1) // 3, q), r, q)


def check_identity(L, Q):
    bad = tot = 0
    for l in primerange(7, L):
        if l % 3 != 1:
            continue
        c, d = primary(l)
        s = root_of(c, d, l)
        for q in primerange(7, Q):
            if q % 3 != 1 or q == l:
                continue
            a, b = primary(q)
            k1 = sym(c, d, a, b, q)
            k2 = sym(c - d, -d, a, b, q)          # conj(c + d w) = c + d w^2 = (c - d) - d w
            kS = expo(pow(q, (l - 1) // 3, l), s, l)
            tot += 1
            bad += (kS != (k1 + 2 * k2) % 3)
    return tot, bad


def forced(n, l, Q):
    tcls = (-pow(n, -1, l)) % l
    kD = Counter()
    kS = set()
    c, d = primary(l)
    s = root_of(c, d, l)
    for q in primerange(7, Q):
        if q % 3 != 1 or q == l or (4 * q) % l != tcls:
            continue
        a, b = primary(q)
        r = root_of(a, b, q)
        kD[(pow(l, (q - 1) // 3, q) == 1)] += 1     # l a cube mod q (choice-free)
        kS.add(expo(pow(q, (l - 1) // 3, l), s, l))
    return dict(kD), kS


if __name__ == "__main__":
    tot, bad = check_identity(60, 2000)
    print(f"(a) identity (q/lambda)_3 = x1 x2^2: {tot} pairs (l<60, q<2000), {bad} failures")
    print("(b) forced progression t=4q=-1/n (mod l), q<2e5 prime = 1 (3): {l cube mod q: count}, S-values")
    for n, l in [(27, 7), (125, 7), (343, 13), (27, 13), (729, 19), (9, 7), (25, 13), (7, 13), (131, 7), (241, 19)]:
        print(n, l, *forced(n, l, 200000))
