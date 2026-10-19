#!/usr/bin/env python3
"""Static audit of saved trap certificates and streamed experiment summaries.
Does not import either explorer. Rejects factors >=2**64 (none in traps).
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from math import gcd, prod, log
from pathlib import Path
import json
import hashlib
import sympy as sp

ROOT=Path('data/z47_q3_pivot')

def prime64(n):
    assert 1 < n < 2**64
    return n == 2 or (n % 2 and sp.ntheory.primetest.mr(
        n, [2,325,9375,28178,450775,9780504,1795265022]))

def components(states):
    index=defaultdict(set)
    for v in states:
        for x in v: index[x].add(v)
    unseen=set(states); groups=[]
    while unseen:
        v=min(unseen); unseen.remove(v); group={v}; todo=[v]
        while todo:
            t=todo.pop()
            for x in t:
                for u in index[x]:
                    if u in unseen: unseen.remove(u); group.add(u); todo.append(u)
        groups.append(group)
    return sorted(groups,key=lambda s:(-len(s),min(s)))

def audit(c):
    p,q=c['p'],c['q']; n=p*q
    assert prime64(p)
    states={tuple(t) for t in c['states']}
    assert len(states)==c['vertices']
    seeds={(p,4*p,12*p),(p,6*p,6*p),(2*p,2*p,3*p)}
    assert seeds <= states
    for x,y,z in states:
        assert 0<x<=y<=z and 4*x*y*z==n*(x*y+x*z+y*z)
        assert any(t%3 for t in (x,y,z))
    assert {f['x'] for f in c['closure_fibres']}=={x for t in states for x in t}
    largest=0
    for f in c['closure_fibres']:
        x,a,b=f['x'],f['a'],f['b']
        g=gcd(4*x-n,n*x)
        assert a==(4*x-n)//g and b==n*x//g and a>0
        fs={int(r):e for r,e in f['factors'].items()}
        assert prod(r**e for r,e in fs.items())==b
        ds=[1]
        for r,e in fs.items():
            assert e>0 and prime64(r)
            largest=max(largest,r)
            ds=[d*r**i for d in ds for i in range(2*e+1)]
        good=sorted(d for d in ds if d<=b and (b+d)%a==0)
        assert good==f['divisors']
        for d in good:
            assert (b+b*b//d)%a==0
            assert tuple(sorted((x,(b+d)//a,(b+b*b//d)//a))) in states
    gs=components(states)
    assert all(g&seeds for g in gs)
    x,y,z=c['ES']['solution']
    assert 4*x*y*z==p*(x*y+x*z+y*z)
    return dict(p=p,vertices=len(states),edges=c['edges'],fibres=len(c['closure_fibres']),
                components=[len(g) for g in gs],
                component_seed_counts=[len(g&seeds) for g in gs],
                layers=c['layers'],q_divisible_slots=dict(Counter(sum(x%q==0 for x in t) for t in states)),
                max_denominator=max(max(t) for t in states),largest_factor=largest,
                side_factors=c['side_factors'],ES=c['ES'],
                states_sha256=hashlib.sha256(json.dumps(sorted(states)).encode()).hexdigest())

def aggregate(rows):
    ok=[r for r in rows if r['status'] in ['HIT','TRAP']]
    hits=[r for r in ok if r['status']=='HIT']
    return dict(attempts=len(rows),complete=len(ok),hits=len(hits),
                traps=[r['p'] for r in ok if r['status']=='TRAP'],
                censored=[r['p'] for r in rows if r['status']=='CENSORED'],
                p_range=[min(r['p'] for r in rows),max(r['p'] for r in rows)] if rows else None,
                depth_hist=dict(sorted(Counter(r['depth'] for r in hits).items())),
                mean_depth=sum(r['depth'] for r in hits)/len(hits) if hits else None,
                mean_vertices=sum(r['vertices'] for r in ok)/len(ok) if ok else None,
                max_vertices=max((r['vertices'] for r in ok),default=None),
                cpu_seconds=sum(r.get('cpu_seconds',0) for r in rows))

def main():
    v=json.loads((ROOT/'verification.json').read_text())
    result={'trap_audits':[audit(c) for c in v['trap_certificates']],
            'reference_validation':dict(Counter(r['status'] for r in v['validation'])),
            'cohorts':{},'trend_decades':{},'hardest':[]}
    unique={}
    for name in ['baseline','adversarial','shadow','near','trend']:
        rows=[json.loads(s) for s in (ROOT/(name+'.jsonl')).read_text().splitlines()]
        stops=[r for r in rows if r['status']=='BUDGET_STOP']
        rows=[r for r in rows if 'p' in r]
        result['cohorts'][name]=aggregate(rows)
        result['cohorts'][name]['budget_stops']=stops
        for r in rows:
            if r['status'] in ['HIT','TRAP']:
                assert sum(r['layers'].values()) == r['vertices']
            if r['status']=='HIT':
                p=r['p']; path=r['path']
                assert len(path)==r['depth']+1
                assert tuple(path[0]) in {(p,4*p,12*p),(p,6*p,6*p),(2*p,2*p,3*p)}
                assert all(x%3==0 for x in path[-1])
                for x,y,z in path:
                    assert 0<x<=y<=z and 4*x*y*z==3*p*(x*y+x*z+y*z)
                assert all(set(t)&set(u) for t,u in zip(path,path[1:]))
            prev=unique.get(r['p'])
            if prev and prev['status']!='CENSORED' and r['status']!='CENSORED':
                assert (prev['depth'],prev['vertices'])==(r['depth'],r['vertices'])
            if not prev or prev['status']=='CENSORED': unique[r['p']]=r
        if name=='trend':
            for decade in sorted({len(str(r['p']))-1 for r in rows}):
                result['trend_decades'][decade]=aggregate([r for r in rows if len(str(r['p']))-1==decade])
    result['unique']=aggregate(list(unique.values()))
    hits=[r for r in unique.values() if r['status']=='HIT']
    maxdepth=max(r['depth'] for r in hits)
    result['hardest']=[r for r in hits if r['depth']==maxdepth]
    result['top_depths']=[{k:r[k] for k in ['p','depth','vertices','group']} for r in sorted(hits,key=lambda r:(-r['depth'],r['p']))[:25]]
    (ROOT/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
