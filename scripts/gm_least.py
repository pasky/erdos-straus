"""gm_least.py — least overflow B for the ES^{[2]} / ES^{(y,1)} shot family at primes (GROWING_MUTE §4).

(A,B) form (Prop 1.1): need A = 2k, B odd, gcd(A,B) = 1, gcd(B,p) = 1, and a divisor g of N = 4k^2 p + B^2 with
g ≡ -1 (mod 4kB).  B = 1 is ES (Type II, d = 1 slice of the certificate cube).
Stage 1 (vectorised over all primes p ≡ 1 mod 4 < PMAX): B = 1, k ≤ K1 (divisor pairs are symmetric, so g ≤ sqrt N).
Stage 2 (leftovers): B = 1, 3, 5, ... ≤ BMAX, k ≤ K2, full divisor scan with sympy; report least (B, k).
p ≡ 3 (mod 4) is free (k = 1, B = 1: p + 4 ≡ 3 mod 4 has a prime factor ≡ 3 mod 4 — here 4p + 1? see note) and skipped.
Usage: gm_least.py PMAX K1 K2 BMAX
"""
import sys
from math import gcd, isqrt
import numpy as np
from sympy import primerange, divisors

PMAX, K1, K2, BMAX = map(int, sys.argv[1:5])
ps = np.array([p for p in primerange(5, PMAX) if p % 4 == 1], dtype=object)
P = np.array(ps, dtype=np.int64)
solved = np.zeros(len(P), dtype=bool)
leastk = np.zeros(len(P), dtype=np.int64)
for k in range(1, K1 + 1):
    N = 4 * k * k * P + 1  # < 2^63 for PMAX*K1^2 small
    tmax = isqrt(int(N.max())) // (4 * k) + 2
    hit = np.zeros(len(P), dtype=bool)
    for t in range(1, tmax + 1):
        g = 4 * k * t - 1
        hit |= (N % g == 0) & (g * g <= N)
    new = hit & ~solved
    leastk[new] = k
    solved |= hit
print(f"primes p ≡ 1 (4), 5 ≤ p < {PMAX}: {len(P)}; ES (B = 1) with k ≤ {K1}: {solved.sum()}")
hist = np.bincount(leastk[solved])
print("least k histogram (B = 1):", {i: int(c) for i, c in enumerate(hist) if c})

def solve(p, B, k):
    N = 4 * k * k * p + B * B
    M = 4 * k * B
    for g in divisors(N):
        if (g + 1) % M == 0:
            return g
    return None

left = [int(p) for p, s in zip(P, solved) if not s]
print(f"leftovers after stage 1: {len(left)}")
stats = {}
for p in left:
    best = None
    for B in range(1, BMAX + 1, 2):
        if gcd(B, p) != 1:
            continue
        for k in range(1, K2 + 1):
            if gcd(2 * k, B) != 1:
                continue
            g = solve(p, B, k)
            if g:
                best = (B, k, g)
                break
        if best:
            break
    stats[p] = best
    print(p, best)
