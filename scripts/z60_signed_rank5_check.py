#!/usr/bin/env python3
"""z60 SIGNED: numerical check of the internal reviewer's counterexample to a mixed-nebentypus higher-weight S3.
g = E2/E2(1) - (3/2) E1/E1(1) with E1 = theta of x1^2+...+x5^2 (r(1) = 10), E2 = theta of x1^2+..+x4^2+2x5^2 (r(1) = 8).
(Both genera have one class -- assumed here, so theta = genus theta; the check is of the coefficient inequalities only.)
Checks g(m^2) < 0 for odd m <= sqrt(X) and g(p) > 0 for primes p = 17 (mod 24) <= X; also reports g at Mordell-class primes.
Usage: python3 scripts/z60_signed_rank5_check.py X"""
import sys, math
X = int(sys.argv[1])
r4 = [0] * (X + 1)
# r4: representations by sum of four squares via r2 convolution
r2 = [0] * (X + 1)
s = int(math.isqrt(X))
for a in range(-s, s + 1):
    for b in range(-s, s + 1):
        n = a * a + b * b
        if n <= X:
            r2[n] += 1
for i in range(X + 1):
    if r2[i]:
        for j in range(X + 1 - i):
            if r2[j]:
                r4[i + j] += r2[i] * r2[j]
def r5(n, w):
    tot = 0
    x = 0
    while w * x * x <= n:
        tot += r4[n - w * x * x] * (1 if x == 0 else 2)
        x += 1
    return tot
g = lambda n: r5(n, 2) / 8 - 1.5 * r5(n, 1) / 10
sq = [(m, g(m * m)) for m in range(1, s + 1, 2)]
print("max g(m^2)/m^3 over odd m <= %d: %.4f (at m=%d); any g(m^2) >= 0: %s" % (s, max(v / m**3 for m, v in sq), max(sq, key=lambda t: t[1] / t[0]**3)[0], any(v >= 0 for m, v in sq)))
def isprime(n):
    if n < 2: return False
    for q in range(2, int(math.isqrt(n)) + 1):
        if n % q == 0: return False
    return True
P17 = [p for p in range(17, X + 1, 24) if isprime(p)]
print("primes = 17 mod 24 <= X:", len(P17), " with g(p) <= 0:", [p for p in P17 if g(p) <= 0][:10], " min g(p)/p^1.5 = %.4f" % min(g(p) / p**1.5 for p in P17))
M = {1, 121, 169, 289, 361, 529}
PM = [p for p in range(3, X + 1) if p % 840 in M and isprime(p)]
print("Mordell primes <= X:", len(PM), " with g(p) > 0:", sum(1 for p in PM if g(p) > 0))
