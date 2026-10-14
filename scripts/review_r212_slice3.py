"""R212 from-scratch check of FOUR_SPECIFIC Prop 3.1 / 3.2 and the 9.1% e=3 statistic.

A Type II e-slice of M/p exists iff e = -p (mod M); a Type I e-slice iff e*p = -1 (mod M) (N = (p+e)/M resp. (ep+1)/M).
Classes are unit classes mod M (Dirichlet: every unit class contains primes p not dividing M).
Also verifies the slice identities M/p = 1/N + e/(pN) (II) and M/p = e/N + 1/(pN) (I) exactly on samples.
"""
from math import gcd, isqrt
from fractions import Fraction as F


def covered(M, E):
    units = [r for r in range(M) if gcd(r, M) == 1]
    cov = set()
    for e in E:
        if gcd(e, M) != 1:
            continue
        cov.add((-e) % M)                      # Type II: p = -e
        cov.add((-pow(e, -1, M)) % M)          # Type I: p = -e^{-1}
    return all(r in cov for r in units)


print("e in {1,3}:       M<200 with a slice at every prime:", [M for M in range(3, 200) if covered(M, [1, 3])])
print("e in {1,2,3,4,6}: M<200 with a slice at every prime:", [M for M in range(3, 200) if covered(M, [1, 2, 3, 4, 6])])
# 7: which classes need which e
cl = {}
for p in range(1, 7):
    cl[p] = [("II", e) for e in (1, 2, 3, 4, 6) if (p + e) % 7 == 0] + \
            [("I", e) for e in (1, 2, 3, 4, 6) if (e * p + 1) % 7 == 0]
print("M=7 classes p mod 7 -> slices:", cl)

# identities
for M, p, e in [(4, 13, 3), (7, 5, 2), (5, 7, 3), (7, 3, 4)]:
    if (p + e) % M == 0:
        N = (p + e) // M
        assert F(M, p) == F(1, N) + F(e, p * N)
    if (e * p + 1) % M == 0:
        N = (e * p + 1) // M
        assert F(M, p) == F(e, N) + F(1, p * N)


def all_1mod3(N):
    m = N
    q = 2
    while q * q <= m:
        while m % q == 0:
            if q % 3 != 1:
                return False
            m //= q
        q += 1
    return m == 1 or m % 3 == 1


def stats(X):
    sieve = bytearray([1]) * (X + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(X) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    tot = bad = 0
    first = []
    for p in range(13, X, 12):
        if sieve[p]:
            tot += 1
            if all_1mod3((p + 3) // 4) and all_1mod3((3 * p + 1) // 4):
                bad += 1
                if len(first) < 3:
                    first.append(p)
    return tot, bad, first


for X in (10**4, 10**6):
    tot, bad, first = stats(X)
    print(f"p = 1 mod 12 < {X}: {tot} primes, both e=3 slices empty for {bad} ({100*bad/tot:.1f}%), first {first}")


def failures_e3(path_fmt="/tmp/r212_f{}.txt"):
    """§3.3: census failures (from review_r212_census output files) lying in an e=3 class."""
    import os
    for M in range(5, 25):
        fn = path_fmt.format(M)
        if not os.path.exists(fn) or gcd(3, M) != 1:
            continue
        ps = [int(l.split('/')[1]) for l in open(fn) if l.startswith('FAIL')]
        inII = [p for p in ps if (p + 3) % M == 0]
        inI = [p for p in ps if (3 * p + 1) % M == 0]
        hits = sorted(set(inII) | set(inI))
        ok = all((p not in inII or all_1mod3((p + 3) // M)) and (p not in inI or all_1mod3((3 * p + 1) // M))
                 for p in hits)
        print(f"  M={M}: {len(hits)}/{len(ps)} failures in an e=3 class; all such N only primes = 1 (3): {ok}; {hits[:6]}")


if __name__ == "__main__":
    failures_e3()
