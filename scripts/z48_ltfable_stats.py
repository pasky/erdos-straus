#!/usr/bin/env python3
"""z48_ltfable_stats.py — statistics from the z48_ltfable_lines binary (8 saturating uint8 arrays W,MP,ST,SU,SAB,ANY,I3,W2).
Reports mean/min of each count over (a) primes p=1(4), (b) odd squares, (c) all n, in windows near the top, normalised by log^2 n.
Usage: uv run python scripts/z48_ltfable_stats.py data/z48_ltfable/lines_1e7.bin 10000000
"""
import sys, numpy as np, math
fn, N = sys.argv[1], int(sys.argv[2])
A = np.fromfile(fn, dtype=np.uint8).reshape(10, N + 1)
names = ["W", "MP", "ST", "SU", "SAB", "ANY", "I3", "W2", "L3", "L1"]
# primes
s = np.ones(N + 1, dtype=bool); s[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if s[i]: s[i * i::i] = False
idx = np.arange(N + 1)
L2 = np.log(np.maximum(idx, 2)) ** 2
def report(mask, label):
    m = mask & (idx >= N // 10)
    print(f"{label}: n in [{N//10},{N}], count {m.sum()}")
    for k, nm in enumerate(names):
        a = A[k][m].astype(float); l2 = L2[m]
        sat = (a >= 255).mean()
        print(f"  {nm:4s} mean/L2={np.mean(a / l2):.4f}  min={int(a.min())}  zero-frac={np.mean(a == 0):.2e}  sat-frac={sat:.1e}")
report(s & (idx % 4 == 1), "primes p=1(4)")
sq = np.zeros(N + 1, dtype=bool); r = np.arange(1, int(N ** 0.5) + 1); sq[r * r] = True
report(sq & (idx % 2 == 1), "odd squares")
report(sq & (idx % 2 == 0), "even squares")
report(~sq & (idx % 2 == 1), "odd non-squares")
report(~sq & (idx % 2 == 0), "even non-squares")
report(idx % 4 == 1, "all n = 1 (4)")
