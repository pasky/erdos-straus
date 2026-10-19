#!/usr/bin/env python3
"""Small algebra/control checks not covered by the board-component validation."""
import json
from fractions import Fraction
from pathlib import Path
import signal
import time
import z47_q3_pivot_search as s

signal.signal(signal.SIGALRM,s.alarm)
out={'controls':[],'spines':[]}
for p,q,k in [(11,7,8),(17,7,8),(131,7,8),(241,7,8),(9,3,4),(25,3,4)]:
    signal.alarm(30)
    try:
        r=s.explore(p,q,k)
    except s.Censored as e:
        r=dict(p=p,q=q,k=k,status='CENSORED',reason=str(e))
    finally: signal.alarm(0)
    out['controls'].append(r)
for p in [5,13,5209,104161,7909441,8604961]:
    B=(p+3)//4
    path=[(p,4*p,12*p),(p,12*B,4*p*B),(4*B,12*B,p*B)]
    path=[tuple(sorted(t)) for t in path]
    assert all(s.valid(t,3*p) for t in path)
    assert all(set(t)&set(u) for t,u in zip(path,path[1:]))
    for e in s.divisors_square(B):
        t=tuple(sorted((3*(B+e),3*(B+B*B//e),p*B)))
        assert s.valid(t,3*p) and set(t)&set(path[-1])
    out['spines'].append(dict(p=p,B=B,divisors_checked=sum(1 for _ in s.divisors_square(B))))
# Explicit correction: not all B-spine exits are Type II.
p=13; B=4; K=5; m=7
assert not any((d+K)%m==0 for d in s.divisors_square(K))
exit_path=[(13,52,156),(13,48,208),(16,48,52),(15,52,60),(15,30,390)]
assert all(s.valid(tuple(sorted(t)),39) for t in exit_path)
assert all(set(t)&set(u) for t,u in zip(exit_path,exit_path[1:]))
out['typeI_not_typeII']={'p':13,'x':5,'window':7,'path':exit_path,'ES':[5,10,130]}
Path('data/z47_q3_pivot/toys.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
