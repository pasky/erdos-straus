"""R197: MODEL_SPECIFIC §4.1 spot-check: unit classes mod L not covered by the ET-shaped atoms
Type II (u,v,w): M = m*u*v*w - 1, n == -u * v^{-1} (mod M); Type I (a,d,f): K = m*a*d, f | m*a^2*d + 1, n == -f (mod K);
only atoms whose modulus divides L. Sanity: every prime < 2e5 in a covered class must be solvable (checked with the
author-independent engine review_ms_census via a failing-prime list file)."""
import sys
from math import gcd

m, L = int(sys.argv[1]), int(sys.argv[2])
fails = set(int(x) for x in open(sys.argv[3]).read().split()) if len(sys.argv) > 3 else set()
cov = set()
for u in range(1, L + 1):
    for v in range(1, L // (m * u) + 2):
        for w in range(1, L // (m * u * v) + 2):
            M = m * u * v * w - 1
            if M < 2 or L % M or gcd(v, M) != 1:
                continue
            r = (-u * pow(v, -1, M)) % M
            cov.update(c for c in range(r, L, M))
for a in range(1, L + 1):
    for d in range(1, L // (m * a) + 1):
        K = m * a * d
        if L % K:
            continue
        N = m * a * a * d + 1
        for f in range(1, N + 1):
            if N % f == 0:
                r = (-f) % K
                cov.update(c for c in range(r, L, K))
units = [c for c in range(L) if gcd(c, L) == 1]
unc = [c for c in units if c not in cov]
sq = {(x * x) % L for x in range(L) if gcd(x, L) == 1}
print("m=%d L=%d units=%d uncovered=%d (squares %d)" % (m, L, len(units), len(unc), sum(c in sq for c in unc)))
if len(unc) <= 40:
    print("uncovered:", unc)
print("131 mod L uncovered:", 131 % L in unc, " 241 mod L uncovered:", 241 % L in unc)
bad = [p for p in fails if gcd(p, L) == 1 and p % L in cov]
print("known failing primes in covered classes:", bad)
