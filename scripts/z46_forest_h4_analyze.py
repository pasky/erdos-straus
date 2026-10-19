#!/usr/bin/env python3
"""Stream summaries and independently audit every saved stopping time.
No large arrays: at most the set of distinct primes and 80 records per heap.
"""
import csv
import gzip
import heapq
import json
import math
from itertools import chain
from collections import defaultdict
from pathlib import Path
from sympy import factorint, isprime, primerange

OUT = Path('data/z46_forest_h4')

def sign(a, p):
    x = pow(a % p, (p-1)//2, p)
    return -1 if x == p-1 else x

def independent(p, cap):
    # Use mutual divisibility and Legendre colours, NOT the five slot test.
    for v in range(2, cap+1):
        u = (-p) % v
        if u and (p+v) % u == 0 and sign(u*v,p) == -1:
            return v
    return 0

def denominator_check(p,u,v,t):
    if t % 4 == 0:
        d=t//4; ds=(u*v*d,p*v*d,p*u*d)
    else:
        for a,b in ((u,v),(v,u)):
            A,B=t*a-1,t*b-1
            if a%4==0:
                d=a//4; ds=(B*d,B*t*d*p,t*d*p);break
            if A%4==0:
                d=A//4; ds=(B*d*p,b*d,B*b*d);break
        else: raise AssertionError('no slot')
    x,y,z=ds
    assert 4*x*y*z == p*(x*y+x*z+y*z)

def amin(p):
    for m in range(3,2004,4):
        K=(p+m)//4
        if K%p==0: continue
        S={1}
        for q,e in factorint(K).items():
            q=int(q); e=int(e)
            T={pow(q,j,m) for j in range(-e,e+1)}
            S={a*b%m for a in S for b in T}
        if m-1 in S or (-p)%m in S:return m
    raise AssertionError('window cutoff')

def main():
    groups=defaultdict(lambda: {'n':0,'sum_H':0,'sum_ratio':0,'max_ratio':-1,'max_H':0,'equal_r':0})
    buckets=defaultdict(lambda: {'n':0,'sum_H_over_r':0,'sum_ratio':0,'max_ratio':0,'max_H_over_r':0,'equal_r':0})
    seen=set(); top=[]; firstpositive=0; total=0
    with gzip.open(OUT/'census.csv.gz','rt') as f, gzip.open(OUT/'hunt.csv.gz','rt') as f2, gzip.open(OUT/'qnr.csv.gz','rt') as f3:
        for row in chain(csv.DictReader(f),csv.DictReader(f2),csv.DictReader(f3)):
            p,h,u,t,r=(int(row[k]) for k in ('p','H','u','t','r'))
            assert h and h>=r and t*u*h-u-h==p
            assert isprime(p)
            assert independent(p,h)==h
            assert sign(r,p)==-1 and all(sign(q,p)==1 for q in primerange(2,r))
            denominator_check(p,u,h,t)
            total+=1; ratio=h/math.log(p)**2
            g=groups[row['family']];g['n']+=1;g['sum_H']+=h;g['sum_ratio']+=ratio;g['equal_r']+=h==r
            if ratio>g['max_ratio']:g['max_ratio']=ratio;g['record']=[p,h,u,t,r]
            g['max_H']=max(g['max_H'],h)
            if p in seen:continue
            seen.add(p)
            firstpositive+=sign(h,p)==1
            entry=(ratio,p,h,u,t,r)
            if len(top)<80:heapq.heappush(top,entry)
            else:heapq.heappushpop(top,entry)
            b=buckets[r]; b['n']+=1;b['sum_H_over_r']+=h/r;b['sum_ratio']+=ratio;b['max_ratio']=max(b['max_ratio'],ratio);b['max_H_over_r']=max(b['max_H_over_r'],h/r);b['equal_r']+=h==r
    top.sort(reverse=True)
    for row in top[:20]:print('TOP',row,flush=True)
    special=sorted({int(g['record'][0]) for g in groups.values()}|{r[1] for r in top[:20]}|{193,409,577,2521,3361,5569,9601,23929,66529,5101441,59929,8803369,9257329})
    windows={p:amin(p) for p in special}
    result={'rows':total,'distinct_primes':len(seen),'larger_endpoint_QR':firstpositive,'groups':dict(groups),'by_r':dict(sorted(buckets.items())),'top':top,'selected_amin':windows,'audit':'All rows: sympy primality, distinct Legendre/mutual-divisibility minimum, least QNR, integer fraction identity.'}
    (OUT/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ROWS',total,'UNIQUE',len(seen),'QR_ENDPOINT',firstpositive)
    for family,g in groups.items():print(family,g['n'],g['max_H'],round(g['max_ratio'],6),g['record'],flush=True)

if __name__=='__main__':main()
