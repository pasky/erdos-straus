"""Composite-shift exact check; finite simultaneous-trap audits; nested-seed probe."""
from fractions import Fraction
from itertools import product
from math import gcd
from sympy import divisors, isprime
from z73_orbit_audit import ROOT, audit
from z74_orbit_search import other


def composite():
    p,q,r,c=3117161329,2729,285559,715
    assert all(isprime(n) for n in (p,q,r))
    K=q*r; v=p*K;assert 4*K-p==c and gcd(c,v)==1
    for m in [55,65,143,715]:
        hits=[(i,j) for i,j in product(range(-1,2),repeat=2) if pow(q,i,m)*pow(r,j,m)%m==m-1]
        print('ratio hits',m,hits);assert bool(hits)==(m!=715)
    ds=divisors(v*v);assert len(ds)==27 and not any((v+d)%c==0 for d in ds)
    print('full fixed-K candidates',len(ds),'hits 0')
    for n,triple in [(p,(779290335,221553301293526860,68016863497112746020)),(101641,(25413,240279324,10332010932))]:
        assert sum(Fraction(1,x) for x in triple)==Fraction(4,n)


def closures():
    a=audit(101641,(101641,)*4,ROOT/'closed101641O.csv')
    b=audit(101641,other(101641),ROOT/'closed101641T.csv');assert a.isdisjoint(b)
    audit(1009,other(1009),ROOT/'closed1009T.csv')

def nested_audit():
    import json
    from z73_four_orbit import merges
    for n,tr in json.loads((ROOT/'nested_paths.json').read_text()).items():
        p=int(n);a=(p+3)//4;q=p*a;b=(q+2)//3
        assert tr[0]==sorted([a,b,q*b,q*b]) and merges(tr[-1])
        for t in tr: assert min(t)>0 and sum(Fraction(1,d) for d in t)==Fraction(4,p)
        for s,t in zip(tr,tr[1:]):
            keep=list(s)
            for d in t:
                if d in keep:keep.remove(d)
            assert len(keep)==2
        print('verified nested path',p,len(tr)-1)


def nested(p,cap=10000,depth=12):
    from z74_first_trap import step,merges
    a=(p+3)//4;q=p*a;b=(q+2)//3; s=tuple(sorted([a,b,q*b,q*b]));assert sum(Fraction(1,x) for x in s)==Fraction(4,p)
    cur={s}; seen={s:None}
    for d in range(1,depth+1):
        nxt=set()
        for t in sorted(cur):
            for v in step(t): # skips too-large pair-sum denominators; positives only
                if v not in seen:
                    seen[v]=t;nxt.add(v)
                    if merges(v):
                        path=[v]
                        while seen[path[-1]] is not None:path.append(seen[path[-1]])
                        return 'hit',path[::-1]
                    if len(seen)>cap:return 'state-cap',d
        cur=nxt
        if not cur:return 'pruned-exhaustion',(d,len(seen))
    return 'depth-cap',(depth,len(seen))

if __name__=='__main__':
    import sys
    composite();closures();nested_audit()
    if '--nested' in sys.argv:
        for p in [1009,14281,101641]:print('nested',p,*nested(p),flush=True)
