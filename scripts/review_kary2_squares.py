"""Hostile-review brute force for KARY2 Lemmas 2.1-2.2 (independent code).

Checks that no residue of an R(M)-, (a,D)- or Case-A class is a square mod
its modulus, with a square test validated against exhaustive enumeration.
Also a stronger check of Lemma 2.1(2): no perfect square x^2 (1<=x<=X) lies
in any (a,D)-class (direct, not via the mod-G test).

usage: python review_kary2_squares.py AMAX DMAX DCASEA MMAX
"""
import sys
from math import gcd, isqrt


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


def is_sq_ppow(b, p, e):
    """Is b a square mod p^e (b arbitrary integer, units or not)?"""
    q = p ** e
    b %= q
    if b == 0:
        return True
    k = 0
    while b % p == 0:
        b //= p
        k += 1
    if k % 2:
        return False
    r = e - k  # need unit b to be a square mod p^r
    if p == 2:
        if r == 1:
            return True
        if r == 2:
            return b % 4 == 1
        return b % 8 == 1
    return pow(b % p, (p - 1) // 2, p) == 1


def is_sq(b, G):
    return all(is_sq_ppow(b, p, e) for p, e in factor(G).items())


def g_of(D):
    g = 1
    for p, e in factor(D).items():
        g *= p ** ((e + 1) // 2)
    return g


def validate(maxG=400):
    for G in range(1, maxG + 1):
        sq = {x * x % G for x in range(G)}
        for b in range(G):
            assert (b in sq) == is_sq(b, G), (b, G)


def main():
    AMAX, DMAX, DA, MMAX = map(int, sys.argv[1:5])
    validate()
    print("square test validated exhaustively for G <= 400")
    # (a,D)
    n = bad = 0
    maxG = 0
    for a in range(1, AMAX + 1):
        for D in range(1, DMAX + 1):
            G = 4 * a * g_of(D)
            b = -(4 * D + a) % G
            n += 1
            maxG = max(maxG, G)
            if is_sq(b, G):
                bad += 1
                print("(a,D) SQUARE:", a, D, G, b)
    print(f"(a,D): a<={AMAX}, D<={DMAX}: {n} classes, max G {maxG}, squares found {bad}")
    # direct: perfect squares in (a,D) classes, small a, D
    hits = 0
    for a in range(1, 31):
        for D in range(1, 301):
            G = 4 * a * g_of(D)
            b = -(4 * D + a) % G
            for x in range(1, 2 * G + 1):
                if (x * x - b) % G == 0:
                    hits += 1
    print(f"(a,D) direct x^2 in class, a<=30, D<=300, x<=2G: hits {hits}")
    # Case A: d = r h^2, r squarefree; m | 4d+1; class -m^{-1} mod 4rh
    n = bad = 0
    maxG = 0
    for d in range(1, DA + 1):
        fd = factor(d)
        r = 1
        h = 1
        for p, e in fd.items():
            if e % 2:
                r *= p
            h *= p ** (e // 2)
        G = 4 * r * h
        N = 4 * d + 1
        for m in range(1, isqrt(N) + 1):
            if N % m:
                continue
            for mm in {m, N // m}:
                assert gcd(mm, G) == 1
                b = -pow(mm, -1, G) % G
                n += 1
                maxG = max(maxG, G)
                if is_sq(b, G):
                    bad += 1
                    print("CaseA SQUARE:", d, r, h, mm, G, b)
    print(f"Case A: d<={DA}: {n} classes, max G {maxG}, squares found {bad}")
    # R(M): -4D mod M, D | A^2, M = 3 mod 4
    n = bad = 0
    for M in range(3, MMAX + 1, 4):
        A = (M + 1) // 4
        A2 = A * A
        fa = factor(A2)
        divs = [1]
        for p, e in fa.items():
            divs = [x * p ** k for x in divs for k in range(e + 1)]
        for D in divs:
            n += 1
            if is_sq(-4 * D, M):
                bad += 1
                print("R(M) SQUARE:", M, D)
    print(f"R(M): M<={MMAX}: {n} classes, squares found {bad}")
    # live control: shifted residues -(4D+a)+1 and -m^{-1}+1 should hit squares often
    ctl = tot = 0
    for a in range(1, 21):
        for D in range(1, 101):
            G = 4 * a * g_of(D)
            tot += 1
            ctl += is_sq(-(4 * D + a) + 1, G)
    print(f"control (a,D) shifted by +1: {ctl}/{tot} are squares")


if __name__ == "__main__":
    main()
