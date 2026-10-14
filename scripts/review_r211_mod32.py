"""R211 from-scratch check of O213 §4 (no second-order T1 shadow mod 16/32).
All formal words (c,m,s>=1) with N = cms-c-s <= X, N == 1 (8).  Compare the cell occupancy at odd squares with
that at non-square N with chi = +1 (non-certificates), per class N mod 32, at resolutions
  R1 = (edge position, o mod 32), R2 = (edge position, o mod 32, e mod 32, e' mod 32).
A cell 'empty at squares but populated at non-squares' is reported with its expected square count."""
import sys
from math import isqrt
from collections import Counter, defaultdict

X = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
sq = defaultdict(Counter); ns = defaultdict(Counter)
for c in range(1, X + 2):
    for m in range(1, X + 3):
        g = c * m - 1
        if g == 0: continue
        if g - c > X: break
        for s in range(1, (X + c) // g + 1):
            N = g * s - c
            if N < 1 or N % 8 != 1: continue
            q = (m * s - 1, c, m, s, g)
            if any(x % 4 == 0 for x in q): continue        # certificate (chi = -1): excluded
            ev = [i for i in range(5) if q[i] % 2 == 0]
            i0 = ev[0] if ev[1] - ev[0] == 1 else ev[1]
            o = q[(i0 + 3) % 5]; e, ep = q[i0], q[(i0 + 1) % 5]
            assert o % 8 == 3
            key = (i0, o % 32, e % 32, ep % 32)
            r = isqrt(N)
            (sq if r * r == N else ns)[N % 32][key] += 1
for cls in sorted(set(sq) | set(ns)):
    S, T = sq[cls], ns[cls]
    nS, nT = sum(S.values()), sum(T.values())
    for res, proj in (("R1", lambda k: k[:2]), ("R2", lambda k: k)):
        S1, T1 = Counter(), Counter()
        for k, v in S.items(): S1[proj(k)] += v
        for k, v in T.items(): T1[proj(k)] += v
        miss = sorted((round(nS * T1[k] / nT, 2), k) for k in T1 if k not in S1)
        extra = [k for k in S1 if k not in T1]
        print(f"N=={cls} (32) {res}: sq words {nS}, nonsq chi=+1 words {nT}, cells sq {len(S1)} nonsq {len(T1)}; "
              f"empty-at-squares cells (expected sq count): {len(miss)} cells, max expected {miss[-1][0] if miss else 0}, sum expected {round(sum(x[0] for x in miss),1)}; only-at-squares: {len(extra)}")
