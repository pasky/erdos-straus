#!/usr/bin/env python3
"""z58 STRUCT2: report for the strong-approximation test (output of z58_struct2_sa.c).
For each coordinate condition 'x ≡ r (mod m)', list the number of odd non-square n ≡ 1 (4) (resp. primes) without a
positive point in that class, and the last such n, per input file.  EVIDENCE.
Usage: python3 scripts/z58_struct2_sa_report.py FILE [FILE ...]"""
import sys
from math import isqrt
names = [('d', 2), ('c', 2), ('a', 3), ('c', 3), ('d', 3), ('c', 5), ('d', 5), ('a', 4), ('c', 4), ('d', 4)]
for fn in sys.argv[1:]:
    miss = {}; tot = totp = 0
    for line in open(fn):
        v = list(map(int, line.split())); n, N, pr = v[:3]
        if isqrt(n) ** 2 == n or n == 1: continue
        tot += 1; totp += pr
        for (x, m), mask in zip(names, v[3:]):
            for r in range(m):
                if not mask >> r & 1:
                    e = miss.setdefault((x, m, r), [0, 0, 0, 0]); e[0] += 1; e[1] = n
                    if pr: e[2] += 1; e[3] = n
    print(f'== {fn}: {tot} odd non-square n ≡ 1 (4) ({totp} primes)')
    print('class        #missing  last_missing   #primes_missing  last_prime_missing')
    for (x, m) in names:
        for r in range(m):
            e = miss.get((x, m, r), [0, '-', 0, '-'])
            print(f'{x} ≡ {r} mod {m}   {e[0]:8d}  {str(e[1]):>12}   {e[2]:8d}  {str(e[3]):>12}')
