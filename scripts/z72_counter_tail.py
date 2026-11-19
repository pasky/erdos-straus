"""Exact bounded, all-shift z72 search above 10^18. Run via uv; see lane README."""
from collections import Counter
import csv
from itertools import combinations
from math import gcd, lcm, prod
from pathlib import Path
from subprocess import run
import sys

from sympy import isprime, primerange

ROOT = Path(__file__).resolve().parents[1] / 'data/z72/counter_tail'
L = 4*lcm(*range(1, 26))
BATCH = 32768


def candidates(start, ts):
    # p=1+Lk; both p,h prime. For every additional t require
    # 1+(p-1)/(4t) prime. Sieve the linear forms before exact primality.
    coeff = [L,L//2] + [L//(4*t) for t in ts]
    assert all(L%(4*t)==0 for t in ts)
    sieve = [(r, {(-pow(a,-1,r))%r for a in coeff if a%r}) for r in primerange(2,1000)]
    k0 = (start-1)//L+1
    while True:
        buf = bytearray(b'\x01')*BATCH
        for r, roots in sieve:
            for z in roots:
                j=(z-k0)%r
                buf[j::r]=bytes(len(range(j,BATCH,r)))
        for j,v in enumerate(buf):
            if v:
                k=k0+j
                assert L*k+1 < 2**64
                if all(isprime(1+a*k) for a in coeff):
                    yield L*k+1
        k0+=BATCH


def control(p):
    # Next in exactly the same 840-class with prime h; not conditioned on shifts.
    q=p+840
    while not (isprime(q) and isprime((q+1)//2)):
        q+=840
    assert q<p+L and q<2**64
    return q


def fact_many(ns):
    text=run(['factor'],input='\n'.join(map(str,ns)),capture_output=True,text=True,check=True).stdout
    rows=text.splitlines()
    assert len(rows)==len(ns)
    for n,row in zip(ns,rows):
        k,fs=row.split(':')
        fs=list(map(int,fs.split()))
        assert int(k)==prod(fs)==n and all(isprime(q) for q in set(fs))
        yield Counter(fs)


def hit(fs,c):
    # Distinct primes can be on one side together, or one prime on each.
    powers=[[q**i for i in range(1,v+1)] for q,v in fs.items()]
    for row in powers:
        for a in row:
            if (1+a)%c==0: return 1,a
    for left,right in combinations(powers,2):
        for a in left:
            for b in right:
                if (a+b)%c==0: return min(a,b),max(a,b)
                if (1+a*b)%c==0: return 1,a*b
    return None


def scan(ps,cap):
    live=list(ps); out={}
    for c in range(3,cap+1,4):
        if not live: break
        ks=[(p+c)//4 for p in live]
        keep=[]
        for p,k,fs in zip(live,ks,fact_many(ks)):
            ab=hit(fs,c)
            if not ab: keep.append(p); continue
            a,b=ab
            assert gcd(a,b)==1 and k%(a*b)==(a+b)%c==0
            d,e=k//(a*b),(a+b)//c
            y,z=p*a*d*e,p*b*d*e
            assert 4*k*y*z==p*(k*y+k*z+y*z)
            out[p]=(c,a,b,k,y,z)
        live=keep
    return out


def stage(name,start,ts,count,cap):
    from itertools import islice
    ps=list(islice(candidates(start,ts),count)); ctr=[control(p) for p in ps]
    assert len(set(ps+ctr))==2*count
    ROOT.mkdir(exist_ok=True,parents=True)
    result=scan(ps+ctr,cap)
    with (ROOT/(name+'.csv')).open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['pair','arm','p','first_c','A','B','x','y','z'])
        for i,(p,q) in enumerate(zip(ps,ctr)):
            for arm,n in [('target',p),('control',q)]:
                w.writerow([i,arm,n,*result.get(n,('',)*6)])
    for arm in (ps,ctr):
        vals=sorted(result[n][0] if n in result else cap+4 for n in arm)
        print(name,len(arm),'p50,p90,p99,max',[vals[(len(vals)*u-1)//100] for u in (50,90,99,100)],'missing',sum(n not in result for n in arm),flush=True)

def progression_controls():
    # Match the progression itself too. Do not reject a control for passing a
    # shift filter. Report any overlap/reuse in this particular finite cohort.
    with (ROOT/'cluster.csv').open() as f:
        targets=[int(r['p']) for r in csv.DictReader(f) if r['arm']=='target']
    ctr=[]
    for p in targets:
        q=p+L
        while not (isprime(q) and isprime((q+1)//2)): q+=L
        assert q<2**64
        ctr.append(q)
    res=scan(sorted(set(ctr)),2047)
    with (ROOT/'progression_controls.csv').open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['pair','arm','p','first_c','A','B','x','y','z'])
        for i,q in enumerate(ctr): w.writerow([i,'L-control',q,*res.get(q,('',)*6)])
    vals=sorted(res[n][0] for n in ctr)
    print('L-controls ranks:',[vals[(len(vals)*u-1)//100] for u in (50,90,99,100)],'unique',len(set(ctr)),'also targets',len(set(ctr)&set(targets)))


if __name__=='__main__':
    if sys.argv[1]=='controls':
        progression_controls(); sys.exit()
    stage(*{'pilot':('pilot',10**18,[],512,1023),
            'cluster':('cluster',2*10**18,[1,2,3],2048,2047)}[sys.argv[1]])
