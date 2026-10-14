"""y5_mod16: second-order T1 shadow? For odd N <= X with N = 1 (mod 8), tally sign +1 words (o = 3 mod 8) by
(square?, N mod 32, edge position, o mod 32, (e/2 mod 8, e'/2 mod 8)) and report cells that are populated at
non-squares but EMPTY at squares (normalised per class of N mod 32), and vice versa.
usage: y5_mod16.py X"""
import sys
from collections import Counter, defaultdict
from math import isqrt

X = int(sys.argv[1])
T = defaultdict(Counter)  # key (sq, N mod 32) -> Counter of cells
NN = Counter()
for c in range(1, X + 3):
    for m in range(1, X + 3):
        if c * m - 1 - c > X and c * m > 1: break
        s = 1
        while True:
            N = c * m * s - c - s
            if N > X: break
            if N <= 0:
                if c * m - 1 <= 0: break
                s += 1; continue
            if N % 8 == 1 and N > 1:
                q = (m * s - 1, c, m, s, c * m - 1)
                ev = [i for i in range(5) if q[i] % 2 == 0]
                i = ev[0] if (ev[1] - ev[0]) % 5 == 1 else ev[1]
                o = q[(i + 3) % 5]; e, e2 = q[i], q[(i + 1) % 5]
                if o % 8 == 3:
                    sq = isqrt(N) ** 2 == N
                    pos = min(i, (1 - i) % 5) if False else i  # keep raw position
                    T[(sq, N % 32)][(pos, o % 32, (e // 2) % 8, (e2 // 2) % 8)] += 1
            s += 1
for r in range(1, 32, 8):
    A, B = T[(True, r)], T[(False, r)]
    onlyB = [k for k in B if k not in A]; onlyA = [k for k in A if k not in B]
    print(f"N=={r} mod 32: square words {sum(A.values())} cells {len(A)}; nonsq words {sum(B.values())} cells {len(B)};"
          f" cells only at nonsq: {len(onlyB)}; only at sq: {len(onlyA)}")
    print("   expected square counts in the cells empty at squares:", [round(B[k] * sum(A.values()) / sum(B.values()), 1) for k in onlyB])
    # coarser: (pos, o mod 16)
    for proj, name in ((lambda k: (k[0], k[1] % 16), "(pos, o mod 16)"), (lambda k: (k[0], k[1] % 32), "(pos, o mod 32)")):
        a = Counter(); b = Counter()
        for k, v in A.items(): a[proj(k)] += v
        for k, v in B.items(): b[proj(k)] += v
        za = sorted(k for k in b if k not in a)
        print(f"   {name}: empty at squares but populated at non-squares: {za}")
        if name.endswith("16)"):
            print("   square freq:", {k: round(a[k] / max(1, sum(a.values())), 3) for k in sorted(set(a) | set(b))})
            print("   nonsq  freq:", {k: round(b[k] / max(1, sum(b.values())), 3) for k in sorted(set(a) | set(b))})
