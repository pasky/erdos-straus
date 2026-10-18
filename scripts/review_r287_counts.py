"""R287: from-scratch recount of POWER_LADDER_ES §2.3 statistics.
(a) least r = 3 (4) prime with (p/r) = -1 for p = 1 (4) prime <= N (k = 2 theorem prime): histogram;
(b) number of primes p = 1 (4) <= N for which p + 4 has no prime factor = 3 (4)."""
import sys
from math import isqrt
N = int(sys.argv[1])
s = bytearray([1]) * (N + 5); s[0] = s[1] = 0
for i in range(2, isqrt(N + 4) + 1):
    if s[i]:
        s[i * i::i] = bytearray(len(s[i * i::i]))
rs = [r for r in range(3, 2000) if s[r] and r % 4 == 3]
hist, fail = {}, 0
for p in range(5, N + 1, 4):
    if not s[p]:
        continue
    r = next(r for r in rs if pow(p % r, (r - 1) // 2, r) == r - 1)
    hist[r] = hist.get(r, 0) + 1
    m, d, has3 = p + 4, 3, False
    while d * d <= m:
        while m % d == 0:
            has3 |= d % 4 == 3; m //= d
        d += 2
    has3 |= m > 1 and m % 4 == 3
    fail += not has3
print("least r histogram (first 6):", sorted(hist.items())[:6], "max r", max(hist))
print("p = 1 (4) with p + 4 having no prime factor = 3 (4):", fail)
