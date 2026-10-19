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

THRESHOLDS = (16, 32, 64, 128, 256, 512, 1024)

def tally():
    return {'rows': 0, 'censored': 0, 'max_H': 0, 'at_256': 0,
            'tails': [0]*len(THRESHOLDS), 'cap': None}

def observe(counts, row):
    status, cap = row['status'], int(row['cap'])
    assert status in ('HIT', 'CENSORED') and cap > 0
    assert counts['cap'] in (None, cap)
    counts['cap'] = cap
    counts['rows'] += 1
    cut = status == 'CENSORED'
    counts['censored'] += cut
    if cut:
        assert row['H'] == '' and int(row['u']) == int(row['t']) == 0
    else:
        h = int(row['H'])
        assert 2 <= h <= cap
        counts['max_H'] = max(counts['max_H'], h)
        counts['at_256'] += h == 256
    for j, bound in enumerate(THRESHOLDS):
        counts['tails'][j] += cap >= bound if cut else h > bound

def log_fields(line):
    return dict(token.split('=', 1) for token in line.split() if '=' in token)

def audit_hunt_counts(text, counts):
    assert {k for k in counts if k.startswith('hunt_')} <= {'hunt_0', 'hunt_1'}
    logs = [log_fields(line) for line in text.splitlines()]
    assert len(logs) == 2 and [int(d['band']) for d in logs] == [0, 1]
    for band, d in enumerate(logs):
        s = counts.get(f'hunt_{band}', tally())
        primes, kept, cut, cap = (int(d[k]) for k in ('primes', 'kept', 'censored', 'cap'))
        tails = list(map(int, d['tails16,32,64,128,256,512,1024'].split(',')))
        assert len(tails) == len(THRESHOLDS)
        assert 0 <= cut <= kept <= primes
        assert kept == s['rows'] and cut == s['censored']
        assert s['cap'] in (None, cap)
        assert int(d['maxH_complete']) == (cut == 0)
        assert int(d['tails_exact_through']) == (cap if cut else 2**64-1)
        assert all(0 <= b <= a <= primes for a, b in zip(tails, tails[1:]))
        # Retained hits include H=256, whereas tails use strict >.
        assert kept == tails[4] + s['at_256'] + (cut if cap < 256 else 0)
        assert tails[4:] == s['tails'][4:]
        assert all(a >= b for a, b in zip(tails[:4], s['tails'][:4]))
        if kept > cut:
            assert int(d['maxH']) == s['max_H']
        else:
            assert 0 <= int(d['maxH']) < 256
        assert int(d['maxH']) <= cap
    return logs

def audit_full_counts(text, counts, name):
    lines = text.splitlines()
    assert len(lines) == 1 and lines[0].split()[0] == name
    d = log_fields(lines[0])
    assert int(d['evaluated']) == counts['rows']
    assert int(d['censored']) == counts['censored']
    assert counts['cap'] in (None, int(d['cap']))
    if name == 'qnr97':
        assert int(d['prime_hits']) == counts['rows'] <= int(d['candidates'])
    return d

def main():
    groups=defaultdict(lambda: {'n':0,'sum_H':0,'sum_ratio':0,'max_ratio':-1,'max_H':0,'equal_r':0})
    buckets=defaultdict(lambda: {'n':0,'sum_H_over_r':0,'sum_ratio':0,'max_ratio':0,'max_H_over_r':0,'equal_r':0})
    seen=set(); top=[]; firstpositive=0; total=0
    counts=defaultdict(tally); cuts=[]
    with gzip.open(OUT/'census.csv.gz','rt') as f, gzip.open(OUT/'hunt.csv.gz','rt') as f2, gzip.open(OUT/'qnr.csv.gz','rt') as f3:
        rows = chain((("census", row) for row in csv.DictReader(f)),
                     ((row['family'], row) for row in csv.DictReader(f2)),
                     (("qnr97", row) for row in csv.DictReader(f3)))
        for source,row in rows:
            observe(counts[source], row)
            p,u,t,r=(int(row[k]) for k in ('p','u','t','r'))
            assert p % 24 == 1 and isprime(p)
            assert sign(r,p)==-1 and all(sign(q,p)==1 for q in primerange(2,r))
            if row['status'] == 'CENSORED':
                assert independent(p, min(int(row['cap']), p+2)) == 0
                cuts.append({'family': row['family'], 'p': p, 'cap': int(row['cap'])})
                continue
            h=int(row['H'])
            assert h>=r and t*u*h-u-h==p and 0<u<h
            assert independent(p,h)==h
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
    logs = {
        'census': audit_full_counts((OUT/'census_counts.txt').read_text(), counts['census'], 'census'),
        'hunt': audit_hunt_counts((OUT/'hunt_counts.txt').read_text(), counts),
        'qnr': audit_full_counts((OUT/'qnr_counts.txt').read_text(), counts['qnr97'], 'qnr97'),
    }
    top.sort(reverse=True)
    for row in top[:20]:print('TOP',row,flush=True)
    special=sorted({int(g['record'][0]) for g in groups.values()}|{r[1] for r in top[:20]}|{193,409,577,2521,3361,5569,9601,23929,66529,5101441,59929,8803369,9257329})
    windows={p:amin(p) for p in special}
    distinct = len(seen | {row['p'] for row in cuts})
    result={'rows':total+len(cuts),'hit_rows':total,'distinct_primes':distinct,'larger_endpoint_QR':firstpositive,'groups':dict(groups),'by_r':dict(sorted(buckets.items())),'top':top,'selected_amin':windows,'audit':'All rows: SymPy primality and least QNR. Hits: independent Legendre/mutual-divisibility minimum and fraction identity. Censored: independent absence through cap. All retained-row counts reconciled against aggregate logs; low hunt tails require the separate full replay.'}
    result.update(censored_rows=len(cuts), censored_primes=cuts,
                  saved_max_complete=not cuts, count_audit=logs)
    (OUT/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ROWS',total+len(cuts),'UNIQUE',distinct,'QR_ENDPOINT',firstpositive,'CENSORED',len(cuts))
    for family,g in groups.items():print(family,g['n'],g['max_H'],round(g['max_ratio'],6),g['record'],flush=True)

if __name__=='__main__':main()
