"""R207 from-scratch checks of SYNTHESIS_SPARKS3 Lemma 1.0 and Thm 1.1.

(1) Lemma 1.0: random (M, n, Q, g) with g | n + M Q^2, g = -1 mod M (g composite allowed):
    identity M/n = 1/x+1/y+1/z exact, x,y integers, den(z) == (Q/gcd(Q,k))^2 when gcd(Q,n)=1.
(2) (*) : Jacobi (-M/g) = -1 for every odd g = -1 mod M, all M = 0 mod 4 up to MMAX, g < GMAX.
(3) Thm 1.1(a): every odd non-square n < NMAX prime to M gets a shot with a PRIME g = -1 (mod M), g not | n,
    Q odd prime to n; solution verified exactly, den(z) odd square prime to n.
(4) Thm 1.1(b): no (g>1, Q) with g = -1 mod M, gcd(Q,k)=1, g | k^2 + M Q^2 (all divisors g), k, Q < KMAX.
Usage: review_s3_thm11.py NMAX MMAX GMAX KMAX
"""
import sys, random
from fractions import Fraction
from math import gcd, isqrt


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


def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\0\0"
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def divisors(m):
    ds = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            ds.append(i)
            if i * i != m:
                ds.append(m // i)
        i += 1
    return ds


def shot(M, n, Q, g):
    assert (n + M * Q * Q) % g == 0 and (g + 1) % M == 0
    mp = (n + M * Q * Q) // g
    assert (n + mp) % M == 0 and (n * (g + 1)) % M == 0
    x = (n + mp) // M
    y = n * (g + 1) // M
    z = Fraction(n * x * (g + 1), M * Q * Q)
    assert Fraction(M, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    return x, y, z


def is_sq(m):
    r = isqrt(m)
    return r * r == m


def check_lemma(trials=200000, seed=1):
    rnd = random.Random(seed)
    bad = 0
    tested = 0
    for _ in range(trials):
        M = rnd.randint(1, 60)
        n = rnd.randint(1, 3000)
        Q = rnd.randint(1, 300)
        N = n + M * Q * Q
        gs = [d for d in divisors(N) if (d + 1) % M == 0]
        for g in gs:
            x, y, z = shot(M, n, Q, g)
            tested += 1
            if gcd(Q, n) == 1:
                k = (g + 1) // M
                if z.denominator != (Q // gcd(Q, k)) ** 2:
                    bad += 1
    print(f"(1) Lemma 1.0: {tested} shots tested, den-formula failures: {bad}")


def check_star(MMAX, GMAX):
    bad = 0
    cnt = 0
    for M in range(4, MMAX + 1, 4):
        for g in range(M - 1, GMAX, M):
            if g % 2 == 0:
                continue
            cnt += 1
            if jacobi(-M, g) != -1:
                bad += 1
    print(f"(2) (*): {cnt} (M,g) pairs, failures {bad}")


def check_a(NMAX, Ms=(4, 8, 12, 16, 20, 24)):
    P = primes_upto(20000)
    for M in Ms:
        gl = [g for g in P if g % M == M - 1]
        maxg = 0
        cnt = 0
        for n in range(3, NMAX, 2):
            if gcd(n, M) != 1 or is_sq(n):
                continue
            found = False
            for g in gl:
                if n % g == 0:
                    continue
                # need Q with M Q^2 = -n mod g
                t = (-n * pow(M, -1, g)) % g
                if pow(t, (g - 1) // 2, g) != 1:
                    continue
                s = next(s for s in range(1, g) if s * s % g == t)
                # Q odd, prime to n, Q = +-s mod g
                Q = None
                for cand in range(1, 2 * g * 50):
                    if cand % 2 and (cand % g in (s, g - s)) and gcd(cand, n) == 1:
                        Q = cand
                        break
                assert Q is not None
                x, y, z = shot(M, n, Q, g)
                den = z.denominator
                assert den % 2 == 1 and is_sq(den) and gcd(den, n) == 1
                found = True
                maxg = max(maxg, g)
                break
            assert found, (M, n)
            cnt += 1
        print(f"(3) Thm1.1(a) M={M}: {cnt} odd non-squares < {NMAX} certified; max prime g {maxg}")


def check_b(KMAX, Ms=(4, 8, 12, 16, 20, 24, 36, 100, 60, 28)):
    for M in Ms:
        hits = 0
        tested = 0
        for k in range(1, KMAX, 2):
            if gcd(k, M) != 1:
                continue
            for Q in range(1, KMAX):
                if gcd(Q, k) != 1:
                    continue
                N = k * k + M * Q * Q
                tested += 1
                for g in divisors(N):
                    if g > 1 and (g + 1) % M == 0:
                        hits += 1
        print(f"(4) Thm1.1(b) M={M}: {tested} (k,Q) pairs, shots found: {hits}")


if __name__ == "__main__":
    NMAX, MMAX, GMAX, KMAX = map(int, sys.argv[1:5])
    check_lemma()
    check_star(MMAX, GMAX)
    check_b(KMAX)
    check_a(NMAX)
