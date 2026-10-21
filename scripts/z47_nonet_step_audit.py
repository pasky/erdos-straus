#!/usr/bin/env python3
"""Independent image audit, exact candidate checks, and census summaries.
Run: uv run python scripts/z47_nonet_step_audit.py /tmp/z47_nonet_brute
"""
import json
import resource
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
from z47_nonet_step_search import witnesses, brute, representations, factor

resource.setrlimit(resource.RLIMIT_AS,(1_500_000_000,1_500_000_000))
resource.setrlimit(resource.RLIMIT_CPU,(600,600))
ROOT=Path('data/z47_nonet_step')
rows=[json.loads(s) for s in (ROOT/'census.jsonl').read_text().splitlines()]
gs=['baseline','repair','greedy','ratio','core','split']


def c_fibre(k,n):
    text=subprocess.check_output([sys.argv[1],str(k),str(n)],text=True,timeout=120)
    return {tuple(map(int,s.split())) for s in text.splitlines()}


def rat(x,y):
    g=gcd(x,y)
    return tuple(sorted((x//g,y//g)))


def independent_pool(C,w,split):
    D=set(w)
    for u in w:
        for v in w:
            D.update([u*v,gcd(u,v),u*v//gcd(u,v),u//gcd(u,v)])
    D.add(gcd(gcd(w[0],w[1]),w[2]))
    D.add(w[0]*w[1]//gcd(w[0],w[1])*w[2]//gcd(w[0]*w[1]//gcd(w[0],w[1]),w[2]))
    if split:
        for u in w:
            D.update([u+1,u*(u+1)])
    P=set(C)
    for u in D:
        for v in C:
            P.update([u*v,gcd(u,v),u*v//gcd(u,v)])
            if u%v==0: P.add(u//v)
            if v%u==0: P.add(v//u)
    return P


audits=[]
fixtures={25,169,289,193,409,577,2521,3361,5569,9601}
for row in rows:
    n,k,a,b=row['n'],row['k'],row['a'],row['b']
    if k!=4 or n not in fixtures: continue
    target=c_fibre(k,n)
    Q={a,b,a+b,a-b}-{1}
    sources={q:brute(k,q) for q in Q}
    assert all(sources[q]==set(witnesses(k,q)) for q in Q)
    ratios={rat(w[i],w[j]) for ws in sources.values() for w in ws for i,j in combinations(range(3),2)}
    ratio_image={w for w in target if any(rat(w[i],w[j]) in ratios for i,j in combinations(range(3),2))}
    greedy_image={w for w in target if any(w[t]==n//k+1 and rat(w[(t+1)%3],w[(t+2)%3]) in ratios for t in range(3))}
    C={1,2,k,a,b,a+b,a-b,a*a,b*b,a*b,2*a*b,n}
    images={'core':set(),'split':set(),'ratio':ratio_image,'greedy':greedy_image}
    for ws in sources.values():
        for win in ws:
            for name,sp in [('core',False),('split',True)]:
                P=independent_pool(C,win,sp)
                images[name].update(w for w in target if w[0] in P and w[1] in P and w[1]<=10*n*n)
    for name,img in images.items():
        assert len(img)==row['counts'][name]['solutions'],(n,name,len(img),row['counts'][name])
        assert sum(gcd(n,*w)==1 for w in img)==row['counts'][name]['primitive_target']
        if row['square']:
            assert sum(any(d%isqrt(n) for d in w) for w in img)==row['counts'][name]['nonscaling']
    audits.append({'n':n,'target_solutions':len(target),'image_counts':{g:len(v) for g,v in images.items()}})

# Independent controls include the two outside the norm domain.
controls={str(n):len(c_fibre(8,n)) for n in [11,17,131,241]}
assert not any(controls.values())
# Every stored example independently satisfies the rational identity.
examples=0
for row in rows:
    for ex in row['examples'].values():
        assert sum(F(1,v) for v in ex['output'])==F(row['k'],row['n'])
        if ex.get('input'):
            assert sum(F(1,v) for v in ex['input'])==F(row['k'],ex['q'])
        examples+=1

# Infinite-family toy: m=16t^2+1, a=m-2,b=8t, 3 does not divide t.
family=0
for t in range(1,1001):
    if t%3==0: continue
    m=16*t*t+1; a=m-2; b=8*t; n=m*m
    win=(4*t*t,4*t*t*m,2*t*t*a*m)
    assert a*a+b*b==n
    assert sum(F(1,v) for v in win)==F(4,a)
    X=(n+3)//4; h=m*(m+1)*(n+3)//12
    out=(X,h,m*h)
    assert sum(F(1,v) for v in out)==F(4,n)
    assert gcd(X,n)==1 and gcd(h//m,m)==1
    family+=1
# Nontrivial source dependence at the first example: another valid witness
# at the same coordinate fails the SAME first-pair greedy rule.
w=(4,84,210); n=289
assert sum(F(1,v) for v in w)==F(4,15)
r,s=rat(w[0],w[1]); h=F(n*(r+s)*(n+3),12*r*s)
assert h.denominator!=1

exposure=[]
for n,a,b in [(169,12,5),(289,15,8),(1369,35,12)]:
    p=isqrt(n)
    ratios={rat(w[i],w[j]) for q in {a,b,a+b,a-b}-{1}
            for w in witnesses(4,q) for i,j in combinations(range(3),2)}
    exposed=sorted([list(rs) for rs in ratios if rs[0]*rs[1]%p==0])
    exposure.append({'n':n,'ratio_count':len(ratios),'exposed':exposed})

summary={'valuation_exposure':exposure,'independent_image_audits':audits,'numerator8':controls,
         'examples_rechecked':examples,'family_toy_cases':family,
         'replacement_witness_gate':str(h),'rows':len(rows),
         'operations':dict(sum((Counter(x['operations']) for x in rows),Counter())),
         'maxpool':max(x['maxpool'] for x in rows),
         'cpu_seconds_search':sum(x['cpu_seconds'] for x in rows)}
cohorts={
 'square_representations':[x for x in rows if x['square']],
 'prime_squares':[x for x in rows if x['square'] and factor(isqrt(x['n']))=={isqrt(x['n']):1}],
 'all_primes':[x for x in rows if x['k']==4 and not x['square']],
 'mordell_under_100000':[x for x in rows if x['k']==4 and not x['square'] and x['mordell'] and x['n']<100000],
 'primes_under_10000':[x for x in rows if x['k']==4 and not x['square'] and x['n']<10000],
 'near_square_gap_le16':[x for x in rows if x['k']==4 and not x['square'] and x['near_square_gap']<=16]}
summary['cohorts']={}
for name,rs in cohorts.items():
    summary['cohorts'][name]={'size':len(rs),
      'hit':{g:sum(x['counts'][g]['solutions']>0 for x in rs) for g in gs},
      'nonscaling_hit':{g:sum(x['counts'][g]['nonscaling']>0 for x in rs) for g in gs},
      'primitive_target_hit':{g:sum(x['counts'][g]['primitive_target']>0 for x in rs) for g in gs},
      'union_hit':sum(any(x['counts'][g]['solutions'] for g in gs) for x in rs),
      'source_witnesses':sum(x['operations']['source_witnesses'] for x in rs),
      'source_hits':{g:sum(x['source_coverage'][g] for x in rs) for g in ['repair','greedy','ratio','core','split']}}
summary['union_failures']=[x['n'] for x in cohorts['all_primes'] if not any(x['counts'][g]['solutions'] for g in gs)]
(ROOT/'audit.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2,sort_keys=True))
