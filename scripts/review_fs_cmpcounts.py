#!/usr/bin/env python3
"""R217: compare exact Case B pattern counts (review_fs_count.c output) with the Lemma 1.6 route minimum
(review_fs_exact.routes, R217's own implementation). Tuples with deg w = a <= deg C = b are compared with the pattern bound.
usage: review_fs_cmpcounts.py p count_file"""
import sys
from collections import Counter
sys.path.insert(0, 'scripts')
from review_fs_exact import routes
p = int(sys.argv[1]); cnt = Counter()
for line in open(sys.argv[2]):
    if line.startswith('P '):
        s, a, z, y, t = map(int, line.split()[1:])
        b = s - a - z
        assert y + t == max(a, b)
        if a <= b: cnt[(s, a, z, y, t)] += 1
viol = 0; worst = 0.0; tight = 0
for (s, a, z, y, t), c in sorted(cnt.items()):
    B = min(routes(p, s, a, z, y, t).values())
    if c > B: viol += 1; print('VIOLATION', s, a, z, y, t, c, B)
    worst = max(worst, c / B); tight += (c == B)
print(f'p={p}: {len(cnt)} nonempty patterns, {sum(cnt.values())} tuples (a<=b), violations={viol}, max count/bound={worst:.4f}, attained={tight}')
