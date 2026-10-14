"""R212 from-scratch checks of FOUR_SPECIFIC Prop 1.1 / Cor 1.2 (M-shot T1 classification).

(1) Jacobi constancy of (-M/g) on odd g = -1 (mod M), g < 40*M, M = 3..80.
(2) T1 brute force: odd-g shots g | k^2 + M Q^2 at odd squares k^2 (gcd(k,M)=1, gcd(Q,k)=1).
(3) Explicit shots at odd squares for M = 1,2 (mod 4) via a prime g with (-M/g) = +1, with
    the full Lemma 1.0 solution verified in exact rationals and den(z) checked odd & prime to n.
(4) M^box at odd non-squares via the Cor 1.2(a) construction, verified exactly.
(5) 11/37 identity.
"""
from fractions import Fraction as F
from math import gcd, isqrt
import sys


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
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
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def shot(M, n, g, Q):
    """Lemma 1.0 recomputed from scratch; returns (x, y, z) or None."""
    if (n + M * Q * Q) % g or (g + 1) % M:
        return None
    m1 = (n + M * Q * Q) // g
    if (n + m1) % M or (n * (g + 1)) % M:
        return None
    x = (n + m1) // M
    y = n * (g + 1) // M
    z = F(n * x * (g + 1), M * Q * Q)
    assert F(M, n) == F(1, x) + F(1, y) + 1 / z, (M, n, g, Q)
    return x, y, z


def main():
    bad = 0
    # (1)
    for M in range(3, 81):
        signs = set()
        for g in range(M - 1, 40 * M, M):
            if g % 2 == 1 and g > 1:
                signs.add(jacobi(-M, g))
        const = signs == {-1}
        pred = M % 4 in (0, 3)
        if const != pred:
            print("Prop1.1 MISMATCH", M, signs)
            bad += 1
    print("(1) Jacobi constancy M=3..80 done, mismatches", bad)
    # (2) T1 brute
    for M in range(3, 41):
        odd_shots = 0
        even_shots = 0
        for k in range(1, 60, 2):
            if gcd(k, M) != 1:
                continue
            for Q in range(1, 30):
                if gcd(Q, k) != 1:
                    continue
                N = k * k + M * Q * Q
                for g in range(M - 1, N + 1, M):
                    if g > 1 and N % g == 0:
                        if g % 2:
                            odd_shots += 1
                        else:
                            even_shots += 1
        t1 = odd_shots == 0
        if t1 != (M % 4 in (0, 3)):
            print("T1 MISMATCH", M, odd_shots)
            bad += 1
        if even_shots and not (M % 8 == 3 or M % 4 == 1):
            print("unexpected even shot", M, even_shots)
        print(f"  M={M:2d} M%4={M%4} M%8={M%8} odd_shots={odd_shots} even_shots={even_shots}")
    # (3) explicit shots at odd squares for M = 1, 2 mod 4
    for M in [m for m in range(3, 41) if m % 4 in (1, 2)]:
        g = next(g for g in range(M - 1, 10**6, M)
                 if g > 2 and isprime(g) and jacobi(-M, g) == 1)
        for k in (1, 3, 5, 7, 9, 11, 13, 15, 21, 25, 99):
            if gcd(k, M) != 1 or k % g == 0:
                continue
            n = k * k
            # Q^2 = -k^2/M mod g, Q odd, gcd(Q, k) = 1
            sol = None
            for Q in range(1, 40 * g, 2):
                if (n + M * Q * Q) % g == 0 and gcd(Q, k) == 1:
                    sol = shot(M, n, g, Q)
                    if sol:
                        break
            assert sol, (M, k, g)
            z = sol[2]
            d = z.denominator
            assert d % 2 == 1 and gcd(d, n) == 1 and isqrt(d) ** 2 == d, (M, k, sol)
        print(f"  (3) M={M}: shot prime g={g}, M^box shots at all tested odd squares OK")
    # (4) M^box at odd non-squares via Cor 1.2(a)
    cnt = 0
    for M in range(3, 31):
        for n in range(3, 400, 2):
            if gcd(n, M) != 1 or isqrt(n) ** 2 == n:
                continue
            found = False
            for g in range(M - 1, 10**5, M):
                if g < 3 or g % 2 == 0 or not isprime(g) or n % g == 0:
                    continue
                if jacobi(n, g) != jacobi(-M, g):
                    continue
                for Q in range(1, 4 * g, 2):
                    if (n + M * Q * Q) % g == 0 and gcd(Q, n) == 1:
                        x, y, z = shot(M, n, g, Q)
                        d = z.denominator
                        assert d % 2 == 1 and gcd(d, n) == 1 and isqrt(d) ** 2 == d
                        found = True
                        break
                if found:
                    break
            assert found, (M, n)
            cnt += 1
    print("(4) M^box at odd non-squares (M=3..30, n<400):", cnt, "verified")
    # (5)
    print("(5) 11/37 == 1/8+1/148+49/296:", F(11, 37) == F(1, 8) + F(1, 148) + F(49, 296))
    print("TOTAL mismatches", bad)


if __name__ == "__main__":
    main()
