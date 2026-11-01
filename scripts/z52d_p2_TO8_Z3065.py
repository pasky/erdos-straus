# z52d P2 TO8 Z3040/Z3052/Z3065: periodic-in-s certificate covering for n_s = 15*2^s + 1.
# A hit (C,d): d ≡ -1 (mod 4C), d | 4C*n_s + 1  is a (★)-type divisor certificate => ES(n_s) (any odd n; FRONTIER §2.1 divisor form).
# Covers s if some (C,d) with C<=CMAX, d<=DMAX hits. Reports covered/uncovered s in [1, SMAX] and per-(C,d) residue structure.
import sys
CMAX, DMAX, SMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
pairs = []
for C in range(1, CMAX + 1):
    d = 4 * C - 1
    while d <= DMAX:
        if d > 1 and (d % 2 == 1):
            pairs.append((C, d))
        d += 4 * C
uncov = []; hits_by_s = {}
for s in range(1, SMAX + 1):
    hs = []
    for (C, d) in pairs:
        if (4 * C * (15 * pow(2, s, d) + 1) + 1) % d == 0:   # d | 4C(15*2^s+1)+1
            hs.append((C, d))
    hits_by_s[s] = hs
    if not hs: uncov.append(s)
print(f"pairs (C<= {CMAX}, d<= {DMAX}, d≡-1 mod 4C): {len(pairs)}; s in [1,{SMAX}] uncovered: {len(uncov)}; first uncovered: {uncov[:20]}")
from collections import Counter
cnt = Counter(len(v) for v in hits_by_s.values())
print("number of covering pairs per s (distribution, first 10):", sorted(cnt.items())[:10])
print("least certificate (C,d) for s=1..12:", [min(hits_by_s[s], key=lambda x: x[1]) if hits_by_s[s] else None for s in range(1, 13)])
print("s where only C=1 hits:", [s for s in range(1, SMAX + 1) if hits_by_s[s] and all(C == 1 for C, d in hits_by_s[s])][:20])
