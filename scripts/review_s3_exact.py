"""R207 from-scratch census: primes p <= N, p not | M, for which M/p = 1/x+1/y+1/z has NO solution in
positive integers.  Method: x in (p/M, 3p/M]; a/b = M/p - 1/x reduced; a/b = 1/y + 1/z (y<=z) iff some
divisor d of b^2 with d <= b and d = -b (mod a)  [(ay-b)(az-b) = b^2].
Usage: review_s3_exact.py N M1 M2 ...   (prints failing primes per M)
"""
import sys
from math import gcd, isqrt


def spf_sieve(N):
    spf = list(range(N + 1))
    for i in range(2, isqrt(N) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(m, spf, extra):
    f = {}
    for q in extra:
        while m % q == 0:
            f[q] = f.get(q, 0) + 1
            m //= q
    while m > 1:
        q = spf[m]
        while m % q == 0:
            f[q] = f.get(q, 0) + 1
            m //= q
    return f


def two_unit(a, b, fb):
    """a/b reduced, fb = factorisation of b; is a/b = 1/y + 1/z?"""
    if a == 1:
        return True
    target = (-b) % a
    divs = [1]
    for q, e in fb.items():
        nd = []
        pw = 1
        for _ in range(2 * e + 1):
            for d in divs:
                nd.append(d * pw)
            pw *= q
        divs = nd
    for d in divs:
        if d <= b and d % a == target:
            return True
    return False


def solvable(M, p, spf):
    for x in range(p // M + 1, 3 * p // M + 1):
        a = M * x - p
        if a <= 0:
            continue
        b = p * x
        g = gcd(a, b)
        a //= g
        b //= g
        fx = factor(x, spf, ())
        fb = dict(fx)
        fb[p] = fb.get(p, 0) + 1
        # divide fb by g
        for q in list(fb):
            while g % q == 0 and fb[q] > 0:
                fb[q] -= 1
                g //= q
            if fb[q] == 0:
                del fb[q]
        assert g == 1
        if two_unit(a, b, fb):
            return True
    return False


if __name__ == "__main__":
    N = int(sys.argv[1])
    Ms = [int(t) for t in sys.argv[2:]]
    spf = spf_sieve(max(3 * N // min(Ms) + 10, 100))
    ps = [p for p in range(3, N + 1) if all(p % q for q in range(2, isqrt(p) + 1))] if N < 1000 else None
    if ps is None:
        sv = bytearray([1]) * (N + 1)
        sv[0:2] = b"\0\0"
        for i in range(2, isqrt(N) + 1):
            if sv[i]:
                sv[i * i::i] = bytearray(len(sv[i * i::i]))
        ps = [p for p in range(3, N + 1) if sv[p]]
    for M in Ms:
        fails = [p for p in ps if M % p and not solvable(M, p, spf)]
        print(f"M={M} N={N} fails({len(fails)}): {' '.join(map(str, fails))}", flush=True)
