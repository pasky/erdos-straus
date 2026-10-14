"""R207: verify M^box and M^(S) certificates at every failing pair (M,p) of the independent census
(/tmp/r207_exact_*.log produced by review_s3_exact.py), from scratch.
 - M^box: least prime g = -1 (mod M), g not | p, with some odd Q prime to p, g | p + M Q^2; solution verified exactly.
 - M^(S), S={3,5,7,11}, p not in S: least Q in <S> such that p + M Q^2 has a divisor g>1, g = -1 (mod M);
   solution verified exactly, den(z) in <S>^2.
 - overflow profile: min over shots with Q <= 60 (gcd(Q,p)=1, any g) of Q1 = Q/gcd(Q,(g+1)/M).
Usage: review_s3_certs.py LOG [LOG...]
"""
import sys, re
from fractions import Fraction
from math import gcd, isqrt

S = (3, 5, 7, 11)


def divisors(m):
    ds = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            ds.append(i)
            if i * i != m:
                ds.append(m // i)
        i += 1
    return sorted(ds)


def isprime(m):
    return m > 1 and all(m % q for q in range(2, isqrt(m) + 1))


def solve(M, n, Q, g):
    mp = (n + M * Q * Q) // g
    x = (n + mp) // M
    y = n * (g + 1) // M
    z = Fraction(n * x * (g + 1), M * Q * Q)
    assert (n + M * Q * Q) % g == 0 and (n + mp) % M == 0 and (n * (g + 1)) % M == 0
    assert Fraction(M, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    return x, y, z


def in_S(m):
    for q in S:
        while m % q == 0:
            m //= q
    return m == 1


def S_numbers(B):
    out = [1]
    for q in S:
        out = [a * q ** e for a in out for e in range(40) if a * q ** e <= B]
    return sorted(set(out))


def box_cert(M, p):
    g = M - 1
    while True:
        if isprime(g) and p % g:
            t = (-p * pow(M, -1, g)) % g
            for s in range(1, g):
                if s * s % g == t:
                    Q = s if s % 2 else s + g  # odd representative; gcd(Q,p)=1 as Q< 2g < p or check
                    while gcd(Q, p) != 1:
                        Q += 2 * g
                    x, y, z = solve(M, p, Q, g)
                    d = z.denominator
                    assert d % 2 and isqrt(d) ** 2 == d and gcd(d, p) == 1
                    return g, Q, (x, y, z)
        g += M


def S_cert(M, p, SN):
    for Q in SN:
        N = p + M * Q * Q
        for g in divisors(N):
            if g > 1 and (g + 1) % M == 0:
                x, y, z = solve(M, p, Q, g)
                d = z.denominator
                assert in_S(isqrt(d)) and isqrt(d) ** 2 == d
                return Q, g, d == 1
    return None


def overflow(M, p, QB=60):
    best = None
    for Q in range(1, QB + 1):
        if gcd(Q, p) != 1:
            continue
        for g in divisors(p + M * Q * Q):
            if g > 1 and (g + 1) % M == 0:
                Q1 = Q // gcd(Q, (g + 1) // M)
                best = Q1 if best is None else min(best, Q1)
    return best


if __name__ == "__main__":
    pairs = []
    for fn in sys.argv[1:]:
        for L in open(fn):
            m = re.match(r"M=(\d+) N=\d+ fails\(\d+\): (.*)", L)
            if m:
                pairs += [(int(m.group(1)), int(t)) for t in m.group(2).split()]
    pairs = sorted(set(pairs))
    SN = S_numbers(10 ** 7)
    maxg = {}
    maxQS = 0
    nS = 0
    exactS = 0
    ov = {}
    missing = []
    for M, p in pairs:
        g, Q, sol = box_cert(M, p)
        maxg[M] = max(maxg.get(M, 0), g)
        if p not in S:
            r = S_cert(M, p, SN)
            if r is None:
                missing.append((M, p))
            else:
                nS += 1
                maxQS = max(maxQS, r[0])
                exactS += r[2]
        o = overflow(M, p)
        ov[(M, p)] = o
    print(f"pairs: {len(pairs)}; per M: {[(M, sum(1 for a, _ in pairs if a == M)) for M in sorted(maxg)]}")
    print(f"M^box certified at all; max least prime g per M: {maxg}")
    print(f"M^(S): certified {nS} pairs (p not in S), missing {missing}, max least Q {maxQS}, exact(den 1) {exactS}")
    print(f"overflow: min Q1 over all pairs = {min(v for v in ov.values() if v is not None)}; None: "
          f"{[k for k, v in ov.items() if v is None]}; Q1=3 at {[k for k, v in ov.items() if v == 3]}")
    print("8/131 check:", Fraction(8, 131) == Fraction(1, 20) + Fraction(1, 131) + Fraction(9, 2620))
