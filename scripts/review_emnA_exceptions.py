"""R94 review A (from scratch): m-exceptional n <= N for small m, compared with PW Table 1.
Representability test: m/n = 1/x + R, R = a/b reduced, n/m < x <= 3n/m (x = smallest denominator),
and a/b = 1/y + 1/z  iff  exist d1, d2 | b with a | d1 + d2 (proved in the review file).
Primes p <= N tested; exceptional n must have only exceptional prime factors (divisor closure),
so composites are enumerated from exceptional primes and tested directly.
The two-term criterion is cross-checked by brute force on small fractions.
Usage: uv run python scripts/review_emnA_exceptions.py N mlo mhi
"""
import sys
from math import gcd
from fractions import Fraction

N = int(float(sys.argv[1])); mlo, mhi = int(sys.argv[2]), int(sys.argv[3])
XM = 3 * N // 4 + 2
spf = list(range(XM + 1))
for i in range(2, int(XM ** .5) + 1):
    if spf[i] == i:
        for j in range(i * i, XM + 1, i):
            if spf[j] == j: spf[j] = i

def fac(n, d):
    while n > 1 and n <= XM:
        p = spf[n]
        while n % p == 0:
            n //= p; d[p] = d.get(p, 0) + 1
    if n > 1:  # n > XM: trial division
        p = 2
        while p * p <= n:
            while n % p == 0:
                n //= p; d[p] = d.get(p, 0) + 1
            p += 1
        if n > 1: d[n] = d.get(n, 0) + 1
    return d

def two_unit(a, b, fb):
    """a/b reduced, fb = factorization of b. True iff a/b = 1/y+1/z."""
    divs = [1]
    for p, e in fb.items():
        divs = [d * p ** i for d in divs for i in range(e + 1)]
    res = set(d % a for d in divs)
    return any(((-r) % a) in res for r in res)

def two_unit_brute(a, b):
    for y in range(b // a + 1, 2 * b // a + 1):
        num = a * y - b
        if num > 0 and (b * y) % num == 0:
            return True
    return False

# cross-check the criterion
bad = 0
for b in range(1, 200):
    for a in range(1, 2 * b):
        if gcd(a, b) != 1: continue
        if two_unit(a, b, fac(b, {})) != two_unit_brute(a, b): bad += 1
print("two-unit criterion cross-check mismatches:", bad)

def representable(m, n):
    fn = fac(n, {})
    for x in range(n // m + 1, 3 * n // m + 1):
        a = m * x - n
        if a <= 0: continue
        b = n * x; g = gcd(a, b); a //= g; b //= g
        fb = dict(fn); fac(x, fb)
        # remove g from fb
        gg = g
        for p in list(fb):
            while gg % p == 0:
                gg //= p; fb[p] -= 1
            if fb[p] == 0: del fb[p]
        if two_unit(a, b, fb): return True
    return False

def brute_rep(m, n):  # independent naive check for tiny n
    for x in range(n // m + 1, 3 * n // m + 1):
        R = Fraction(m, n) - Fraction(1, x)
        if R <= 0: continue
        if two_unit_brute(R.numerator, R.denominator): return True
    return False

bad = sum(representable(m, n) != brute_rep(m, n) for m in range(4, 16) for n in range(1, 300))
print("representable vs naive mismatches (m<=15,n<300):", bad)

sieve = bytearray([1]) * (N + 1); sieve[0:2] = b"\x00\x00"
for i in range(2, int(N ** .5) + 1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2, N + 1) if sieve[i]]
for m in range(mlo, mhi + 1):
    ex_p = [p for p in primes if not representable(m, p)]
    # composites from exceptional primes
    cands = {1}
    frontier = [1]
    while frontier:
        new = []
        for c in frontier:
            for p in ex_p:
                if c * p > N: break
                if c * p not in cands:
                    cands.add(c * p); new.append(c * p)
        frontier = new
    ex = sorted(n for n in cands if n == 1 or n in ex_p or not representable(m, n))
    print(f"m={m}: #exceptional n<= {N}: {len(ex)}  {ex}")
    sys.stdout.flush()
