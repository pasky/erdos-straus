"""Certify minimality among Mordell classes: need only one path, from either seed."""
import csv,heapq,json
from itertools import combinations
from math import gcd
from fractions import Fraction
from sympy import primerange
from z74_orbit_search import other
from z73_four_orbit import ROOT,merges, alternatives

def priority(t):
    # Favor a small reduced numerator and even denominators. No negative
    # conclusions are drawn from this ordering or the caps.
    return (all(x%2 for x in t),min((a+b)//gcd(a+b,a*b) for a,b in combinations(t,2)),t[-1].bit_length())

def step(t):
    v=set()
    for i,j in combinations(range(4),2):
        try: rows=alternatives(t[i],t[j])
        except OverflowError: continue
        tail=[t[k] for k in range(4) if k not in (i,j)]
        for x,y in rows:v.add(tuple(sorted([x,y,*tail])))
    return v-{t}

def path(p,cap,breadth=False):
    seen={x:None for x in ((p,)*4,other(p))}; q=[((0,),0,s) for s in seen];heapq.heapify(q)
    for _ in range(cap):
        if not q:break
        _,d,t=heapq.heappop(q)
        for v in sorted(step(t)):
            if v in seen:continue
            seen[v]=t
            if merges(v):
                out=[v]
                while seen[out[-1]] is not None:out.append(seen[out[-1]])
                return out[::-1]
            pr=priority(v);order=(d,pr) if breadth else (pr[0],d//3,pr[1],pr[2]);heapq.heappush(q,(order,d+1,v))
        if len(seen)>25000:break
    return None

HARD={1,121,169,289,361,529}
FIRST=101641

def audit(paths):
    missing=[]
    for p in primerange(2,FIRST):
        if p%840 not in HARD:continue
        tr=paths.get(str(p))
        if not tr:missing.append(p);continue
        assert tuple(tr[0]) in ((p,)*4,other(p)) and merges(tr[-1])
        for t in tr:assert min(t)>0 and sum(Fraction(1,x) for x in t)==Fraction(4,p)
        for s,t in zip(tr,tr[1:]):
            ls=list(s);n=0
            for x in t:
                if x in ls:ls.remove(x);n+=1
            assert n==2
    return missing

if __name__=='__main__':
    import sys
    fn=ROOT/'pretrap_paths.json'
    paths=json.loads(fn.read_text()) if fn.exists() else {}
    if sys.argv[1:]!=['--audit']:
        for p in audit(paths):
            tr=path(p,int(sys.argv[1]) if len(sys.argv)>1 else 600, '--breadth' in sys.argv)
            if tr:paths[str(p)]=tr;fn.write_text(json.dumps(paths,separators=(',',':'))+'\n')
    missing=audit(paths);print('certified earlier escapes',len(paths),'uncertified',len(missing),missing,flush=True)
