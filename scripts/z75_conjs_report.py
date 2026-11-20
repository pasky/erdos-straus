from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json
D=Path('data/z75/conjs')
for tag in ('W1','W2','F1','F2','F3','F4'):
    rows=[json.loads(s) for s in (D/(tag+'.jsonl')).read_text().splitlines()]
    def summary(rows):
        gd={r['n'] for r in rows if r['G']}
        print('pairs',len(rows),'active',sum(bool(r['G']) for r in rows),'inputs/eligible',len({r['n'] for r in rows}),len(gd),'T',sum(r['T'] for r in rows),end=' ')
        hits=set()
        for i in range(3):
            rs=[s for r in rows for s in r['out'][i]]; ns={r['n'] for r in rows if any(s[1] for s in r['out'][i])}; hits|=ns
            e=sum(Q(s[2],s[3]) for s in rs); print(f'| {len(ns)}/{sum(any(s[1] for s in r["out"][i]) for r in rows)} {len(rs)} {sum(s[1] for s in rs)}:{e}',end=' ')
        print('| all',len(hits),'first eligible miss',min(gd-hits,default=None))
    print(tag); summary(rows)
    for d in sorted({r['d'] for r in rows}): print(' ',d,end=' ');summary([r for r in rows if r['d']==d])
    for n in (4545,3361,2094481,85664329):
        if any(r['n']==n for r in rows): print(' ',n,end=' ');summary([r for r in rows if r['n']==n])
