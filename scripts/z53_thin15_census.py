# z53_thin15_census.py — census for n = 15*2^(60t)+1, t = 1..T: smallest prime factor below B (if any), via gcd with a
# primorial.  Every such q is < 10^17, so ES(q) holds by Salez's verification and ES(n) follows by scaling; but by
# paper Thm sterile no finite set of such divisor classes covers a neighbourhood of t = 0 (q | n at t = 0 means q | 16).
# Also checks n = 121 (mod 840) (Mordell-hard) for every t.  Usage: z53_thin15_census.py T B
import sys, gmpy2
from gmpy2 import mpz
T, B = int(sys.argv[1]), int(sys.argv[2])
s = bytearray([1]) * (B + 1); s[0:2] = b'\x00\x00'
for i in range(2, int(B ** 0.5) + 1):
    if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
PR = [i for i in range(3, B + 1) if s[i]]
P = mpz(1)
for q in PR: P *= q
from collections import Counter
cnt = Counter(); nofac = []; bad840 = 0
for t in range(1, T + 1):
    n = 15 * (mpz(1) << (60 * t)) + 1
    if n % 840 != 121: bad840 += 1
    g = gmpy2.gcd(n, P)
    if g == 1: nofac.append(t); continue
    q = next(q for q in PR if g % q == 0); cnt[q] += 1
print('t <= %d: n = 121 mod 840 fails for %d t; prime factor < %d for %d t (%.1f%%); none for %d t' %
      (T, bad840, B, T - len(nofac), 100 * (T - len(nofac)) / T, len(nofac)))
print('most frequent smallest factors:', cnt.most_common(12))
print('first t without factor < B:', nofac[:30])
