#!/usr/bin/env python3
"""z62 INVERSE test 2c: O/E for 'all u-slices u <= U fail' with LEAVE-ONE-OUT marginals in cells
(p mod MOD) x chi_p(l) for l in EXTRA. Also pairwise failure correlations within cells for u,v <= 8.
Usage: file MOD l1,l2,..."""
import sys, collections
fn = sys.argv[1]; MOD = int(sys.argv[2]); EXTRA = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 and sys.argv[3] else []
rows = []
for l in open(fn):
    p, s = l.split(); p = int(p)
    cell = (p % MOD,) + tuple(pow(p, (q - 1) // 2, q) == 1 for q in EXTRA)
    rows.append((p, cell, s))
cnt = collections.Counter(c for _, c, _ in rows)
for U in (4, 8, 16, 32, 64):
    fails = collections.defaultdict(lambda: [0] * U)
    for p, cell, s in rows:
        for u in range(U):
            if s[u] == '0': fails[cell][u] += 1
    O = 0; E = 0.0; used = 0
    for p, cell, s in rows:
        n = cnt[cell] - 1
        if n < 20: continue
        used += 1
        pr = 1.0
        for u in range(U): pr *= (fails[cell][u] - (s[u] == '0')) / n
        E += pr
        if '1' not in s[:U]: O += 1
    print(f'MOD={MOD} extra={EXTRA} U={U:3d} used={used} cells={len(cnt)} O={O} E={E:.2f} O/E={O/E if E else float("nan"):.2f}')
