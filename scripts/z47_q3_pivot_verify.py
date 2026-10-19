#!/usr/bin/env python3
"""Independent Fable BFS vs new explorer; static full closure certificates.
All factor proposals from Fable's independent Pollard-rho implementation are
certified prime and checked to reconstruct the input. Reproducible random seed.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction
from math import gcd, prod
from pathlib import Path
import json
import random
import signal
import time
import z47_q3_pivot_search as new
import z47_q3_pivot_fable as old

random.seed(47)
raw_factor=old.factor
maxfactor=0

def checked_factor(n):
    global maxfactor
    fs=raw_factor(n)
    assert prod(r**e for r,e in fs.items())==n
    for r in fs:
        new.prime_cert(r)
        maxfactor=max(maxfactor,r)
    return fs
old.factor=checked_factor

def reference(p,q,k=4):
    assert k==4
    seeds=old.solve3(4,q)
    dist={tuple(p*x for x in t):0 for t in seeds}
    todo=deque(sorted(dist)); edges=set()
    while todo:
        t=todo.popleft()
        for x in t:
            for y,z in old.pivots(p*q,x):
                u=tuple(sorted((x,y,z)))
                assert sum((Fraction(1,c) for c in u),Fraction())==Fraction(4,p*q)
                if u!=t: edges.add(tuple(sorted((t,u))))
                if u not in dist:
                    dist[u]=dist[t]+1; todo.append(u)
    hits=[dist[t] for t in dist if all(c%q==0 for c in t)]
    return dist, min(hits) if hits else None, len(edges)

def first_es(p):
    # Independent Type II window construction: d|K², d ≡ -K mod m.
    for m in range(3,10000,4):
        K=(p+m)//4
        if gcd(m,K)>1: continue
        for d in old.divisors(old.factor(K*K)):
            if (d+K)%m==0:
                t=tuple(sorted((K,p*(K+d)//m,p*(K+K*K//d)//m)))
                assert sum((Fraction(1,c) for c in t),Fraction())==Fraction(4,p)
                return dict(window=m,divisor=d,solution=t)
    raise AssertionError('no ES witness in test range')

def certificate(p,q):
    r=new.explore(p,q,store=True)
    dist,depth,edges=reference(p,q)
    assert sorted(dist)==[tuple(t) for t in r['states']]
    assert depth==r['depth']
    assert dict(Counter(dist.values()))==r['layers']
    r['edges']=edges
    r['independent_match']=True
    r['ES']=first_es(p)
    r['side_factors']={name:checked_factor(n) for name,n in [('A',(3*p+1)//4),('B',(p+3)//4),('C',(p+1)//2),('K',(p+7)//4)]}
    # A small independently checkable closure table: factorizations of reduced b,
    # and the complete admissible divisors d <= b of b² for every coordinate.
    fibres=[]
    for x in sorted({x for t in dist for x in t}):
        num=4*x-q*p; den=q*p*x; g=gcd(num,den); a=num//g; b=den//g
        fs=checked_factor(b)
        ds=sorted(d for d in old.divisors({s:2*e for s,e in fs.items()}) if d<=b and (d+b)%a==0)
        fibres.append(dict(x=x,a=a,b=b,factors=fs,divisors=ds))
        assert {tuple(sorted((x,(b+d)//a,(b+b*b//d)//a))) for d in ds} <= set(dist)
    r['closure_fibres']=fibres
    return r

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='data/z47_q3_pivot/verification.json'); ap.add_argument('--quick',action='store_true')
    args=ap.parse_args(); signal.signal(signal.SIGALRM,new.alarm)
    start=time.process_time(); out={'trap_certificates':[], 'validation':[]}
    for p in [7909441,8604961]:
        signal.alarm(90)
        r=certificate(p,3); out['trap_certificates'].append(r)
        signal.alarm(0)
        print('TRAP VERIFIED',p,r['vertices'],r['edges'],r['ES'],flush=True)
    rows=[]
    for name in ['q2','baseline']:
        rows.extend(json.loads(s) for s in Path('data/z47_q3_pivot/'+name+'.jsonl').read_text().splitlines())
    if args.quick: rows=[r for r in rows if r['p'] in [1321,14281,5209,104161]]
    for r in rows:
        p,q=r['p'],r['q']; signal.alarm(90)
        try:
            dist,depth,edges=reference(p,q)
            assert depth==r['depth'] and len(dist)==r['vertices']
            assert dict(Counter(dist.values()))=={int(d):v for d,v in r['layers'].items()}
            out['validation'].append(dict(p=p,q=q,vertices=len(dist),depth=depth,edges=edges,status='MATCH'))
        except new.Censored:
            out['validation'].append(dict(p=p,q=q,status='CENSORED'))
        finally: signal.alarm(0)
        print('VALIDATION',out['validation'][-1],flush=True)
    out['largest_reference_prime_factor']=maxfactor
    out['cpu_seconds']=time.process_time()-start
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    print('CPU',out['cpu_seconds'],flush=True)

if __name__=='__main__': main()
