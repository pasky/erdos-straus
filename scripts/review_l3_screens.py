"""R205 checks for LENGTH_THREE §7.1 and §7.4.

7.4: for every cube point (c,d,j) of a prime p: (-d/h) = -1 and (p/h) = -1 (Jacobi), h = 4cdj - 1.
7.1: for primes p = 1 (4): some FORMAL word (a letter 1) at p has a variable c,m,s,h,h' = 0 (mod 4)
     <=> (p+1)/2 has a prime factor = 3 (mod 4).
Usage: PYTHONPATH=scripts uv run python scripts/review_l3_screens.py PMAX
"""
import sys
from review_l3_cube import primes, cube_points
from review_l3_words import jacobi


def formal_words(p):
    # c = 1: (m-1)s = p+1 ; s = 1: (m-1)c = p+1 ; m = 1: (c-1)(s-1) = p+1
    n1 = p + 1
    for a in range(1, n1 + 1):
        if n1 % a:
            continue
        b = n1 // a
        yield (1, a + 1, b)        # c = 1, m - 1 = a, s = b
        yield (b, a + 1, 1)        # s = 1
        yield (a + 1, 1, b + 1)    # m = 1


def main():
    PMAX = int(sys.argv[1])
    bad74 = 0; n74 = 0
    for p in primes(PMAX):
        if p < 5:
            continue
        for c, d, j in cube_points(p):
            h = 4 * c * d * j - 1
            n74 += 1
            if jacobi(-d, h) != -1 or jacobi(p, h) != -1:
                bad74 += 1
    bad71 = 0; n71 = 0
    for p in primes(PMAX):
        if p % 4 != 1:
            continue
        n71 += 1
        hit = False
        for c, m, s in formal_words(p):
            assert m * c * s - c - s == p and min(c, m, s) == 1
            if any(x % 4 == 0 for x in (c, m, s, c * m - 1, m * s - 1)):
                hit = True
        q = (p + 1) // 2
        f, has3 = 3, False
        while q > 1 and f * f <= q:
            while q % f == 0:
                has3 |= f % 4 == 3; q //= f
            f += 2
        has3 |= q > 1 and q % 4 == 3
        if hit != has3:
            bad71 += 1
    print(f"7.4: {n74} cube points p<={PMAX}, Jacobi failures {bad74}; 7.1: {n71} primes = 1 (4), mismatches {bad71}")


if __name__ == "__main__":
    main()
