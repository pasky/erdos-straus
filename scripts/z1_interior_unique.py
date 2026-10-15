"""z1: do isometric path lattices with all letters >= 2 have the same word up to reversal? (odd n < N)"""
import sys
from cf_lib import words
from ce_classes import canon
N = int(sys.argv[1]); bad = 0; multi = 0; tot = 0
for n in range(3, N, 2):
    cls = {}
    for w in words(n):
        if min(w) < 2: continue
        t, u, v = w
        cls.setdefault(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]), set()).add(w)
    for k, ws in cls.items():
        tot += 1
        reps = {min(w, (w[0], w[2], w[1])) for w in ws}
        if len(reps) > 1:
            bad += 1
            if bad <= 5: print('n', n, ws)
print('interior classes', tot, 'with >1 word up to reversal', bad)
