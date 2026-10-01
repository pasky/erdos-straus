#!/usr/bin/env python3
"""Hostile review of POINTWISE_SIZE Lemma CT -- independent enumeration.

Enumerates every solution 4/p = 1/x+1/y+1/z, x<=y<=z, for primes p = 1 (4), p <= N,
by: x in (p/4, 3p/4];  a/b = (4x-p)/(px) reduced;  (ay-b)(az-b) = b^2 with
d = ay-b a positive divisor of b^2, d <= b, d = -b (mod a);  keep y >= x.
(No code shared with scripts/pointwise_size_ct_check.py.)

Checks CT(a): every p-free denominator has a prime factor l with (l/p) = -1;
       CT(b): if exactly one denominator is divisible by p, its cofactor has one;
       CT(c): if exactly two are, the product of the cofactors has one;
and counts how often, in the two-p-divisible case, some single cofactor has none.
Also checks Lemma 1.3 (p divides one or two denominators).

Usage: uv run python scripts/review_pointwise_size_ct.py [N]
"""
import sys
from math import gcd

import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 0:
            blk = s[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(s == 0)[0]
    s[idx] = idx
    return s


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    BMAX = N * (3 * N // 4 + 1)
    spf = spf_sieve(int(BMAX ** 0.5) + 2)
    small_primes = [int(i) for i in range(2, len(spf)) if spf[i] == i]

    def factor(n):
        f = {}
        for l in small_primes:
            if l * l > n:
                break
            while n % l == 0:
                n //= l
                f[l] = f.get(l, 0) + 1
        if n > 1:
            f[n] = f.get(n, 0) + 1
        return f

    def isprime(n):
        return n > 1 and factor(n) == {n: 1}

    nprimes = nsol = 0
    one = two = 0
    viol_a = viol_b = viol_c = viol_13 = 0
    single_cofactor_without = 0
    for p in range(5, N + 1, 4):
        if not isprime(p):
            continue
        nprimes += 1

        def qnr_factor(n):
            return any(pow(l, (p - 1) // 2, p) == p - 1 for l in factor(n))

        for x in range(p // 4 + 1, 3 * p // 4 + 1):
            num, den = 4 * x - p, p * x
            if num <= 0:
                continue
            g = gcd(num, den)
            a, b = num // g, den // g
            fb = factor(b)
            divs = [1]
            for l, e in fb.items():
                divs = [d * l ** i for d in divs for i in range(2 * e + 1)]
            for d in divs:
                if d > b or (d + b) % a:
                    continue
                y = (d + b) // a
                if y < x:
                    continue
                z = (b * b // d + b) // a
                if (b * b // d + b) % a:
                    continue
                assert 4 * x * y * z == p * (x * y + y * z + z * x)
                nsol += 1
                sol = (x, y, z)
                pdiv = [s for s in sol if s % p == 0]
                pfree = [s for s in sol if s % p]
                if len(pdiv) not in (1, 2):
                    viol_13 += 1
                for s in pfree:
                    if not qnr_factor(s):
                        viol_a += 1
                if len(pdiv) == 1:
                    one += 1
                    if not qnr_factor(pdiv[0] // p):
                        viol_b += 1
                else:
                    two += 1
                    c1, c2 = pdiv[0] // p, pdiv[1] // p
                    if not qnr_factor(c1 * c2):
                        viol_c += 1
                    if not (qnr_factor(c1) and qnr_factor(c2)):
                        single_cofactor_without += 1
    print(f"primes p=1(4), 5<=p<={N}: {nprimes}; solutions x<=y<=z: {nsol}")
    print(f"  exactly one p-divisible: {one}; exactly two: {two}; Lemma 1.3 violations: {viol_13}")
    print(f"  CT(a) violations: {viol_a}; CT(b): {viol_b}; CT(c): {viol_c}")
    print(f"  two-p-divisible solutions with some single cofactor lacking a QNR factor: "
          f"{single_cofactor_without}")
    ok = viol_a == viol_b == viol_c == viol_13 == 0
    print("OK" if ok else "FAILED")


if __name__ == '__main__':
    main()
