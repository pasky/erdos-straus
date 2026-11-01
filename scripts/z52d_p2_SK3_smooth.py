# z52d pass2 SK3, item Z2148: does y-smoothness of the tied integer N=4Cp+1 raise P(level-C event)?
# Event E_C(p): exists d | N, d = -1 mod 4C, 1<d<N (equivalently R_C(p)>0). Smooth := largest prime factor P+(N) <= N^{1/2}.
# Also split by u = log N / log(P+(N)) buckets. Primes p = 1 mod 4 <= 10^6, C = 1..40.
import numpy as np, sys, math
LIM = 4*40*10**6 + 2
spf = np.zeros(LIM+1, dtype=np.int64)
for i in range(2, int(LIM**0.5)+1):
    if spf[i] == 0:
        s = spf[i*i::i]; m = (s == 0); s[m] = i; spf[i*i::i] = s
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx  # primes map to themselves
def lpf(n):
    best = 1
    while n > 1:
        q = int(spf[n]); best = max(best, q)
        while n % q == 0: n //= q
    return best
def has_level(N, C):
    m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
primes = [p for p in range(5, 10**6, 4) if spf[p] == p and p % 4 == 1] if False else None
sv = np.ones(10**6+1, dtype=bool); sv[:2] = False
for i in range(2, 1001):
    if sv[i]: sv[i*i::i] = False
P = [p for p in np.nonzero(sv)[0] if p % 4 == 1]
from collections import defaultdict
tot = defaultdict(lambda: [0, 0])   # (C-bucket) -> [n, events]
smooth_stat = defaultdict(lambda: [0, 0])
for C in range(1, 41):
    for p in P:
        N = 4*C*int(p) + 1
        ev = has_level(N, C)
        L = lpf(N); smooth = (L*L <= N)            # P+(N) <= sqrt N
        k = 'smooth' if smooth else 'rough'
        smooth_stat[(C <= 3, k)][0] += 1; smooth_stat[(C <= 3, k)][1] += ev
for key in sorted(smooth_stat):
    n, e = smooth_stat[key]
    print(f"C<=3:{key[0]} {key[1]:6s} n={n} P(E)={e/n:.4f}")

# Control: condition on tau(N) (number of divisors) bucket, C <= 3.
def tau(n):
    t = 1
    while n > 1:
        q = int(spf[n]); e = 0
        while n % q == 0: n //= q; e += 1
        t *= (e+1)
    return t
ctl = defaultdict(lambda: [0, 0])
for C in range(1, 4):
    for p in P:
        N = 4*C*int(p) + 1
        ev = has_level(N, C); L = lpf(N); smooth = (L*L <= N)
        tb = min(tau(N), 12)
        ctl[(tb, smooth)][0] += 1; ctl[(tb, smooth)][1] += ev
print("control by tau(N) (C<=3): tau bucket, smooth -> n, P(E)")
for tb in range(2, 13):
    a = ctl.get((tb, True), [0,0]); b = ctl.get((tb, False), [0,0])
    if a[0] and b[0]:
        print(f"tau={tb:2d}  smooth n={a[0]:7d} P={a[1]/a[0]:.3f} | rough n={b[0]:7d} P={b[1]/b[0]:.3f}")
