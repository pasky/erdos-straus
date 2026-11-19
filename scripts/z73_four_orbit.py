"""Four-unit pair-move BFS. Only a drained frontier certifies closed-no-merge."""
import csv
from functools import lru_cache
from itertools import combinations
from math import gcd
from pathlib import Path
from sympy import factorint, primerange

ROOT=Path(__file__).resolve().parents[1]/'data/z72/counter_tail'

def dsq(n):
    ds=[1]
    for q,v in factorint(n).items():
        ds=[d*q**i for d in ds for i in range(2*v+1)]
    return ds

@lru_cache(maxsize=16384)
def alternatives(a,b):
    g=gcd(a+b,a*b); u=(a+b)//g; v=a*b//g
    if v.bit_length()>90: raise OverflowError
    out=[]
    for d in dsq(v):
        if d<=v and (v+d)%u==0:
            e=v*v//d
            assert (v+e)%u==0
            x,y=(v+d)//u,(v+e)//u
            assert (x+y)*v==x*y*u
            out.append((int(x),int(y)))
    assert (a,b) in out
    return sorted(out)

def moves(s):
    for i,j in combinations(range(4),2):
        for a,b in alternatives(s[i],s[j]):
            yield tuple(sorted([s[k] for k in range(4) if k not in (i,j)]+[a,b]))

def merges(s):
    return any(a*b%(a+b)==0 for a,b in combinations(s,2))

def orbit(p,depth=16,ncap=6000,start=None):
    if start is None: start=(p,)*4
    current={start}; seen=set(current); even=None; cert=None
    def row(status,d): return [p,status,d,len(seen),even,cert]
    for d in range(depth+1):
        for s in sorted(current):
            if even is None and any(x%2==0 for x in s): even=d
            if merges(s) and cert is None: cert=d
        if cert is not None and even is not None: return row('hit',d)
        if d==depth: return row('depth-cap',d)
        nxt=set()
        for s in sorted(current):
            try:
                for t in moves(s):
                    if t not in seen: nxt.add(t)
                    if len(nxt)+len(seen)>ncap: return row('state-cap',d)
            except OverflowError: return row('bit-cap',d)
        if not nxt: return row('closed',d)
        seen.update(nxt); current=nxt
    assert False

if __name__=='__main__':
    with (ROOT/'four_orbit.csv').open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['p','status','last_full_depth','states','first_even','first_merge'])
        for p in primerange(2,20000):
            if p%840 not in {1,121,169,289,361,529}: continue
            row=orbit(p)
            if row[1]=='state-cap': row=orbit(p,ncap=20000)
            w.writerow(row); f.flush(); print(row,flush=True)
