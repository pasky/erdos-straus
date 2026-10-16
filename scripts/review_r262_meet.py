"""R262 from-scratch: primes p = 1 (4), p <= N, with empty d = 1 meeting locus M(p).

Method A (Prop 1.1(iii), re-derived in the review): M(p) != {} iff exists a <= (1 + sqrt(4p+1))/4 and a divisor
g of p + 4a^2 with g = -1 (mod 4a).
Method B (independent, only for p <= NB): full Type II enumeration (x in (p/4, p/2], delta | x^2) and the ET
parameter d_ET = gcd(x, Y, Z); a d = 1 representation exists iff d_ET is a perfect square (dilation (a,b,c,d) ->
(as, bs, cs, d/s^2)).  So M(p) != {} iff some Type II solution has gcd(x, Y, Z) a square.
usage: review_r262_meet.py N [NB]
"""
import sys
import math
import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, math.isqrt(n) + 1):
        if s[i] == 0:
            blk = s[i * i::i]
            blk[blk == 0] = i
    s[s == 0] = np.arange(n + 1, dtype=np.int32)[s == 0]
    return s


def factor(n, spf):
    f = {}
    while n > 1:
        q = int(spf[n])
        f[q] = f.get(q, 0) + 1
        n //= q
    return f


def divs_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds


def meet_nonempty(p, spf):
    A = int((1 + math.isqrt(4 * p + 1) + 1) // 4) + 1
    for a in range(1, A + 1):
        if 4 * a - 1 > (1 + math.sqrt(4 * p + 1)):  # (4a-1) <= sqrt(4p+1) needed for a = min(a,b)
            break
        n = p + 4 * a * a
        for g in divs_from(factor(n, spf)):
            if g % (4 * a) == 4 * a - 1:
                # exact check of the ES identity
                m = n // g
                b = (p + m) // (4 * a)
                k = (g + 1) // (4 * a)
                assert (p + m) % (4 * a) == 0 and a + b == k * (4 * a * b - p)
                return True
    return False


def methodB(p, spf):
    for x in range(p // 4 + 1, p // 2 + 1):
        m = 4 * x - p
        fx = factor(x, spf)
        f2 = {q: 2 * e for q, e in fx.items()}
        for de in divs_from(f2):
            if (x + de) % m == 0 and (x + x * x // de) % m == 0:
                Y, Z = (x + de) // m, (x + x * x // de) // m
                d = math.gcd(x, math.gcd(Y, Z))
                if math.isqrt(d) ** 2 == d:
                    return True
    return False


if __name__ == "__main__":
    N = int(sys.argv[1])
    NB = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    spf = spf_sieve(2 * N + 10)
    empt, cnt = [], 0
    for p in range(5, N + 1, 4):
        if spf[p] != p:
            continue
        cnt += 1
        if not meet_nonempty(p, spf):
            empt.append(p)
        if p <= NB:
            assert methodB(p, spf) == (p not in empt[-1:]), p
    print("primes p=1(4) <=", N, ":", cnt, " empty M(p):", len(empt))
    print("blocks:", [sum(1 for q in empt if lo < q <= hi) for lo, hi in [(0, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 10**7)]])
    print("all = 1 mod 12:", all(q % 12 == 1 for q in empt))
    print(empt)
    if NB:
        print("method B agreed on all primes <=", NB)
    # odd squares (Cor 1.2(a)) via method A with p replaced by c^2
    bad = [c for c in range(3, math.isqrt(min(N, 10**6)) + 1, 2) if meet_nonempty(c * c, spf)]
    print("odd squares c^2 <=", min(N, 10**6), "with nonempty locus:", bad)
