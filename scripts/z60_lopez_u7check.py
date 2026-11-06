"""z60 LOPEZ: independent checks of the U_7 census (scripts/z60_lopez_u7.c).
U_7(n): exists f ≡ 7 (mod 8) with r = (-n mod f) dividing f+1  <=>  n = xyz - x - z, x,y,z >= 1, 8 | xy.
(1) word enumeration (numpy slices) for all odd n <= N: list of odd non-square zeros;
(2) verify every LATE certificate "LATE n f" in the given .gz files;
(3) for S random odd n ≡ 1 (4) in [lo, hi): direct least witness by a plain loop over f (no bitmaps).
Usage: python z60_lopez_u7check.py N S lo hi files..."""
import sys, gzip, math, random
import numpy as np
import os
MORD = os.environ.get('Z60_MORD') == '1'   # sample n mod 840 in Mordell classes
N = int(sys.argv[1]); S = int(sys.argv[2]); lo = int(sys.argv[3]); hi = int(sys.argv[4])
hit = np.zeros(N + 1, dtype=np.uint8)
x = 1
while x <= N + 2:
    y = 1
    while True:
        if (x * y) % 8:
            y += 1
            if x * y - 1 - x > N + 8 * x: break
            continue
        d = x * y - 1
        if d - x > N: break
        # n = d z - x, z >= 1
        z0 = 1
        if d * z0 - x < 1: z0 = (x + 1 + d - 1) // d
        st = d * z0 - x
        if st <= N: hit[st::d] = 1
        y += 1
    x += 1
zeros = [n for n in range(1, N + 1, 2) if not hit[n] and math.isqrt(n) ** 2 != n]
sqhit = [n for n in range(1, N + 1, 2) if hit[n] and math.isqrt(n) ** 2 == n]
print("(1) word enumeration N =", N, ": odd non-square zeros", zeros, "; odd squares with a word:", sqhit[:5])
bad = 0; cnt = 0
for fn in sys.argv[5:]:
    for line in gzip.open(fn, 'rt'):
        if line.startswith('LATE'):
            _, n, f = line.split(); n = int(n); f = int(f); r = (-n) % f
            cnt += 1
            if not (f % 8 == 7 and r > 0 and (f + 1) % r == 0): bad += 1
print("(2) LATE certificates checked", cnt, "bad", bad)
random.seed(60)
mism = 0
for _ in range(S):
    if MORD:
        n = random.randrange(lo // 840, hi // 840) * 840 + random.choice([1, 121, 169, 289, 361, 529])
    else:
        n = random.randrange(lo, hi) | 1
        if n % 4 == 3: n += 2
    if math.isqrt(n) ** 2 == n: continue
    f = 7
    while True:
        r = (-n) % f
        if r and (f + 1) % r == 0: break
        f += 8
        if f > 2 * n + 1: f = None; break
    if f is None: mism += 1; print("NO WITNESS", n)
print("(3) random sample", S, "in", [lo, hi], "without witness:", mism)
