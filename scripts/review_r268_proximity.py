"""R268 from-scratch check of §5 (v): (1) # primes p = 1 (4) <= 1e8 with p - 1 11-smooth; (2) b = 1 counts (t-form,
= number of (a, c, d)) by 11-smooth part S of p - 1 for p in [1e4, 4e4]; (3) Mordell square classes mod 840, p in [1e6, 3e6]:
mean b = 1 count WITH standard errors."""
import numpy as np
from sympy import primerange


def smooth11(n):
    S = 1
    for q in (2, 3, 5, 7, 11):
        while n % q == 0: n //= q; S *= q
    return S, n == 1


def b1_count(p):
    t = np.arange(1, (p + 1) // 3 + 1, dtype=np.int64)
    g = (-p) % (4 * t)
    return int(((t + 1) % g == 0).sum())


# (1) enumerate 11-smooth m = p - 1 <= 1e8 with 4 | m
from sympy import isprime
sm = [1]
for q in (2, 3, 5, 7, 11):
    sm = [s * q ** e for s in sm for e in range(0, 60) if s * q ** e <= 10**8]
cnt = sum(1 for m in sm if m % 4 == 0 and isprime(m + 1))
print("(1) primes p = 1 (4) <= 1e8 with p - 1 11-smooth:", cnt)

# (2)
groups = {0: [], 1: [], 2: []}
for p in primerange(10**4, 4 * 10**4):
    if p % 4 != 1: continue
    S, _ = smooth11(p - 1)
    groups[0 if S < 50 else 1 if S < 500 else 2].append(b1_count(p))
for k, nm in zip(range(3), ["S<50", "50<=S<500", "S>=500"]):
    v = np.array(groups[k]); print(f"(2) {nm}: n={len(v)} mean b1 count {v.mean():.2f} (SE {v.std(ddof=1)/np.sqrt(len(v)):.2f})")

# (3)
res = {c: [] for c in (1, 121, 169, 289, 361, 529)}
for p in primerange(10**6, 3 * 10**6):
    if p % 840 in res: res[p % 840].append(b1_count(p))
for c, v in res.items():
    v = np.array(v); print(f"(3) p = {c} mod 840: n={len(v)} mean b1 {v.mean():.2f}  SE {v.std(ddof=1)/np.sqrt(len(v)):.2f}")
