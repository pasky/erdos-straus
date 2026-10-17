"""R264 from-scratch T1 control: n = a^2 (a odd, n <= NMAX), windows m <= MMAX, m ≡ 3 (4), gcd(m, n) = 1:
look for divisors d1, d2 | K = (n+m)/4 with d1 + d2 ≡ 0 (mod m) (cap-0, delta_n = 0 slice)."""
import sys
from math import gcd, isqrt

NMAX, MMAX = int(sys.argv[1]), int(sys.argv[2])


def divisors(n):
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds += [d, n // d]
    return ds


hits = 0
cnt = 0
for a in range(1, isqrt(NMAX) + 1, 2):
    n = a * a
    if n == 1:
        continue
    cnt += 1
    for m in range(3, MMAX + 1, 4):
        if gcd(m, n) != 1:
            continue
        K = (n + m) // 4
        r = {d % m for d in divisors(K)}
        if any((-x) % m in r for x in r):
            hits += 1
            print("HIT", n, m)
print(f"odd squares 1 < a^2 <= {NMAX}: {cnt}; windows <= {MMAX}; hits: {hits}")
