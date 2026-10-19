#!/usr/bin/env python3
"""Exact positive pivot components. Run with uv; use external memory/CPU limits.
No denominator/depth truncation. A timeout is CENSORED, never a trap.
Each coordinate fibre is expanded once at its first (shortest) discovery.
"""
import argparse
from collections import Counter, deque
from functools import lru_cache
from math import gcd, prod
import json
from pathlib import Path
import signal
import time
import sympy as sp

MORDELL = {1,121,169,289,361,529}
STAR = [409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
TRAPS2 = [1321,6121,8641,12241,14281,17041,19441,19801,27361,29401,30241,31081,43321,47881,49201,51481,52321,61561,65521,72481,92041]
BOARD = [5209,15289,104161,210169,287281,291481,305761,357169,365569,400009,428401,437809,443689]

class Censored(Exception):
    pass

def alarm(*_):
    raise Censored('per-prime timeout')

@lru_cache(maxsize=20000)
def prime_cert(n):
    """Deterministic 64-bit Miller–Rabin; full Lucas n-1 certificate above.
    Use SymPy's documented seven bases explicitly, bypassing factor_cache and
    the optional GMPY BPSW shortcut. Heuristics only propose factors.
    """
    if n < 2**64:
        assert n == 2 or (n > 2 and n % 2 and sp.ntheory.primetest.mr(
            n, [2,325,9375,28178,450775,9780504,1795265022])), n
        return True
    fs = {int(r):int(e) for r,e in sp.factorint(n-1).items()}
    assert prod(r**e for r,e in fs.items()) == n-1
    for r in fs:
        prime_cert(r)
        a = 2
        while not (pow(a,n-1,n)==1 and gcd(pow(a,(n-1)//r,n)-1,n)==1):
            a += 1
    return True

@lru_cache(maxsize=10000)
def factor(n):
    f = tuple((int(r),int(e)) for r,e in sp.factorint(n).items())
    assert prod(r**e for r,e in f) == n
    for r,e in f:
        assert e > 0
        prime_cert(r)
    return f

def divisors_square(n):
    fs = factor(n)
    def rec(i,d):
        if i == len(fs):
            yield d
        else:
            r,e = fs[i]
            for _ in range(2*e+1):
                yield from rec(i+1,d)
                d *= r
    yield from rec(0,1)

def splits(num,den):
    if num <= 0:
        return
    g=gcd(num,den); a=num//g; b=den//g
    for d in divisors_square(b):
        if d > b or (d+b)%a:
            continue
        c=b*b//d
        assert (c+b)%a == 0
        y,z=(b+d)//a,(b+c)//a
        assert num*y*z == den*(y+z)
        yield y,z

def all_solutions(n,k=4):
    for x in range(n//k+1,3*n//k+1):
        for y,z in splits(k*x-n,n*x):
            if x <= y:
                yield (x,y,z)

def valid(t,n,k=4):
    x,y,z=t
    return 0 < x <= y <= z and k*x*y*z == n*(x*y+x*z+y*z)

def explore(p,q=3,k=4,max_vertices=200000,store=False):
    start=time.process_time()
    seeds=sorted(tuple(p*x for x in t) for t in all_solutions(q,k))
    dist={t:0 for t in seeds}; parent={t:None for t in seeds}
    todo=deque(seeds); expanded=set(); hit=None
    while todo:
        t=todo.popleft()
        if all(x%q==0 for x in t) and (hit is None or dist[t]<dist[hit]):
            hit=t
        for x in t:
            if x in expanded:
                continue
            expanded.add(x)
            for y,z in splits(k*x-q*p,q*p*x):
                u=tuple(sorted((x,y,z)))
                assert valid(u,q*p,k)
                if u not in dist:
                    dist[u]=dist[t]+1; parent[u]=t; todo.append(u)
                    if len(dist)>max_vertices:
                        raise Censored('vertex budget')
    path=[]; t=hit
    while t is not None:
        path.append(t); t=parent[t]
    path.reverse()
    result=dict(p=p,q=q,k=k,status='HIT' if hit else 'TRAP',depth=dist[hit] if hit else None,
                vertices=len(dist),fibres=len(expanded),layers=dict(sorted(Counter(dist.values()).items())),
                targets=sum(all(x%q==0 for x in t) for t in dist),path=path,
                cpu_seconds=round(time.process_time()-start,6))
    if store:
        result['states']=sorted(dist)
    return result

def flags(p):
    A=(3*p+1)//4; B=(p+3)//4; C=(p+1)//2; K=B+1
    return dict(A_prime=bool(sp.isprime(A)),B_prime=bool(sp.isprime(B)),C_prime=bool(sp.isprime(C)),
                no7=not any(r%2 and pow(r,3,7)==6 for r,e in factor(K)))

def candidates(mode):
    if mode=='baseline':
        ps=set(int(p) for p in sp.primerange(5,30000) if p%840 in MORDELL)
        ps.update(BOARD+STAR+[193,2521,66529,3361,5101441])
        # Reconstruct Astra's entire 17-prime early adversarial sample.
        for p in sp.primerange(5,200001):
            p=int(p)
            if p%840 in MORDELL and sp.isprime((p+3)//4) and sp.isprime((3*p+1)//4) and flags(p)['no7']:
                ps.add(p)
        for p in sorted(ps): yield p,{'group':'baseline'}
    elif mode=='q2':
        for p in TRAPS2: yield p,{'group':'q2-fixture'}
    elif mode=='adversarial':
        # Exhaust all Mordell primes below 10**7 satisfying the strongest filters.
        # Further decades use reproducible arithmetic progressions, not a census.
        for exponent, count in [(5,0),(6,0),(7,80),(8,80),(9,40),(10,20)]:
            lo=max(443690,10**exponent); hi=10**(exponent+1)
            got=0
            for p in sp.primerange(lo,hi):
                p=int(p)
                if p%840 not in MORDELL or not sp.isprime((p+3)//4): continue
                if not sp.isprime((3*p+1)//4): continue
                f=flags(p)
                if not f['no7']: continue
                yield p,dict(group='AB-no7',**f)
                got+=1
                if count and got>=count: break
    elif mode=='shadow':
        for exponent in range(6,10):
            got=0
            for p in sp.primerange(10**exponent,10**(exponent+1)):
                p=int(p)
                if p%840 not in MORDELL or not sp.isprime((p+1)//2): continue
                if not sp.isprime((3*p+1)//4): continue
                f=flags(p)
                yield p,dict(group='AC-shadow',**f)
                got+=1
                if got==50: break
    elif mode=='near':
        for exponent in range(3,6):
            got=0
            for m in range(10**exponent,10**exponent+20000,2):
                p=m*m-3
                if p%840 in MORDELL and sp.isprime(p):
                    yield p,dict(group='square-minus3',m=m)
                    got+=1
                    if got==10: break
    elif mode=='trend':
        for exponent in range(4,11):
            got=0
            for p in sp.primerange(10**exponent,2*10**exponent):
                p=int(p)
                if p%840 in MORDELL:
                    yield p,{'group':'trend'}
                    got+=1
                    if got==80: break

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['baseline','q2','adversarial','shadow','near','trend','one'])
    ap.add_argument('--p',type=int); ap.add_argument('--q',type=int,default=3); ap.add_argument('--seconds',type=int,default=30)
    ap.add_argument('--cpu-budget',type=int,default=1000); ap.add_argument('--out',required=True)
    args=ap.parse_args(); signal.signal(signal.SIGALRM,alarm)
    start=time.process_time(); rows=candidates(args.mode) if args.mode!='one' else [(args.p,{'group':'one'})]
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    with open(args.out,'w') as out:
        for p,meta in rows:
            if time.process_time()-start>args.cpu_budget:
                out.write(json.dumps({'status':'BUDGET_STOP','next_p':p,'cpu_seconds':time.process_time()-start})+'\n'); out.flush(); break
            t=time.process_time()
            signal.alarm(args.seconds)
            try:
                prime_cert(p)
                r=explore(p,2 if args.mode=='q2' else args.q)
            except Censored as e:
                r=dict(p=p,q=2 if args.mode=='q2' else args.q,status='CENSORED',reason=str(e),cpu_seconds=time.process_time()-t)
            finally:
                signal.alarm(0)
                factor.cache_clear(); prime_cert.cache_clear()
            r.update(meta); out.write(json.dumps(r)+'\n'); out.flush()
            print(p,r['status'],r.get('depth'),r.get('vertices'),flush=True)
    print('CPU',time.process_time()-start,flush=True)

if __name__=='__main__': main()
