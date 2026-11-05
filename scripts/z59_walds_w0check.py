#!/usr/bin/env python3
"""z59 WALDS: finite sanity check of Lemma W0 on diagonal ternary forms <a,b,c> = ax^2+by^2+cz^2, 1 <= a <= b <= c <= C.
Level of <a,b,c> divides 4N with N = lcm(a,b,c). For every form that represents no odd square m^2 <= X (T1-valid
at all odd squares in range), list how many n in C1(2N) = {n = 1 mod 8, n a non-zero square mod every odd prime | N},
n <= X, it represents (Lemma W0 predicts 0). Also report, as a contrast, forms that miss odd squares only for primes
l >= 11 (Thm F hypothesis) -- same prediction.
Usage: python3 scripts/z59_walds_w0check.py C X
"""
import sys
from math import gcd, isqrt

C, X = int(sys.argv[1]), int(sys.argv[2])


def lcm(a, b):
    return a * b // gcd(a, b)


def oddprimes(n):
    ps, q = [], 3
    while n % 2 == 0:
        n //= 2
    while q * q <= n:
        if n % q == 0:
            ps.append(q)
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        ps.append(n)
    return ps


def reps(a, b, c):
    s = bytearray(X + 1)
    for x in range(isqrt(X // a) + 1):
        ax = a * x * x
        for y in range(isqrt((X - ax) // b) + 1):
            axy = ax + b * y * y
            for z in range(isqrt((X - axy) // c) + 1):
                s[axy + c * z * z] = 1
    return s


nforms = nvalid = nviol = 0
odd_sq = [m * m for m in range(1, isqrt(X) + 1, 2)]
for a in range(1, C + 1):
    for b in range(a, C + 1):
        for c in range(b, C + 1):
            if gcd(gcd(a, b), c) != 1:
                continue
            nforms += 1
            s = reps(a, b, c)
            if any(s[q] for q in odd_sq):
                continue
            nvalid += 1
            N = lcm(lcm(a, b), c)
            ops = oddprimes(N)
            hits = [n for n in range(1, X + 1, 8) if s[n] and all(n % q and pow(n % q, (q - 1) // 2, q) == 1 for q in ops)]
            if hits:
                nviol += 1
                print(f"VIOLATION <{a},{b},{c}> N={N}: represents C1 members {hits[:5]}")
print(f"primitive diagonal forms {nforms}; missing all odd squares <= {X}: {nvalid}; "
      f"of these representing some n in C1(2N), n <= {X}: {nviol}")
