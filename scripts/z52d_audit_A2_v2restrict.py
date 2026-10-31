#!/usr/bin/env python3
"""z52d audit A2, item Z0872: (★) solutions x=uBC, y=pBC, z=puC with no denominator divisible by 4.
For odd p the 2-adic analysis forces exactly two denominators = 2 mod 4 and one odd; inside (★) (u+B odd) this is
C odd and v2(uB) = 1. Count primes p = 1 mod 4 <= X lacking such a (★) solution (all (★) failures are known: 14 <= 1e10)."""
import sys, numpy as np
from math import gcd
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(X**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
ok = np.zeros(X + 1, dtype=bool); anyR = np.zeros(X + 1, dtype=bool)
u = 1
while 3*u - 1 <= X:
    B = 1
    while 4*u*B - u - B <= X:
        if gcd(u, B) == 1 and (u + B) % 2 == 1:
            q = 4*u*B
            C = np.arange(1, (X + u + B)//q + 1, dtype=np.int64)
            p = q*C - u - B; m = p <= X; p = p[m]; C = C[m]
            anyR[p] = True
            if (u*B) % 4 == 2:
                ok[p[C % 2 == 1]] = True
        B += 1
    u += 1
ps = np.nonzero(sieve)[0]; ps = ps[ps % 4 == 1]
for lo, hi in [(5, 10**4), (10**4, 10**5), (10**5, X)]:
    sel = ps[(ps >= lo) & (ps <= hi)]
    print(f"[{lo},{hi}] n={len(sel)} no(★)={np.sum(~anyR[sel])} no 4-free (★)={np.sum(~ok[sel])} "
          f"({np.mean(~ok[sel]):.4f}) examples={sel[~ok[sel]][-6:].tolist()}")
