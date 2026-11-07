import sys
sys.path.insert(0,'scripts')
from z62_parityf_master import master
from collections import Counter
for p in map(int, sys.argv[1:]):
    rows = master(p)
    cnt = Counter()
    ex = {}
    for xyz, m in rows:
        g,a,b,c,eps = m
        marked = tuple(sorted(v for v,e in zip((a,b,c),eps) if e == p))
        unmarked = tuple(sorted(v for v,e in zip((a,b,c),eps) if e != p))
        key = ('I' if len(marked)==2 else 'II', 'markedmin=%d' % min(marked))
        cnt[key] += 1
        ex.setdefault(key, (xyz, g, a, b, c, eps))
    print(p, dict(cnt))
    for k,v in ex.items(): print("   ", k, v)
