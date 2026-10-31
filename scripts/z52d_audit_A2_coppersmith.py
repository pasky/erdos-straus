#!/usr/bin/env python3
"""z52d audit A2, item Z1767: (★) solutions 4uBC-u-B=p split by regime of the modulus s=4C vs N=4Cp+1.
Coppersmith/CHN regime: s >= N^{1/4}  <=>  (4C)^3 >= p (approx)  <=> uB <~ p^{2/3}
Lenstra regime:         s >  N^{1/3}  <=>  (4C)^2 >  p          <=> uB <~ p^{1/2}
For each prime p = 1 mod 4 <= X record whether (★) has a solution in each regime (exact test on C)."""
import sys, numpy as np
from math import gcd
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(X**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
anyR = np.zeros(X + 1, dtype=bool); cop = np.zeros(X + 1, dtype=bool); len_ = np.zeros(X + 1, dtype=bool)
# enumerate pairs (u,B), gcd=1, u+B odd ; p = 4uBC - u - B, C>=1
P = 0
u = 1
while 4*u*1 - u - 1 <= X:
    B = 1
    while 4*u*B - u - B <= X:
        if gcd(u, B) == 1 and (u + B) % 2 == 1:
            q = 4*u*B
            Cmax = (X + u + B) // q
            C = np.arange(1, Cmax + 1, dtype=np.int64)
            p = q*C - u - B
            p = p[p <= X]; C = C[:len(p)]
            anyR[p] = True
            s = 4*C
            cop[p[(s.astype(np.float64)**4 >= (4.0*C*p + 1))]] = True
            len_[p[(s.astype(np.float64)**3 > (4.0*C*p + 1))]] = True
        B += 1
    u += 1
ps = np.nonzero(sieve)[0]; ps = ps[(ps % 4 == 1)]
for lo, hi in [(10, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, X)]:
    sel = ps[(ps >= lo) & (ps <= hi)]
    if len(sel) == 0: continue
    print(f"p in [{lo},{hi}] n={len(sel)}: no(★)={np.sum(~anyR[sel])}, "
          f"no Coppersmith-regime(★)={np.sum(~cop[sel])} ({np.mean(~cop[sel]):.4f}), "
          f"no Lenstra-regime(★)={np.sum(~len_[sel])} ({np.mean(~len_[sel]):.4f})")
big = ps[ps > 10**6]
print("largest primes lacking Coppersmith-regime (★):", big[~cop[big]][-5:].tolist())
