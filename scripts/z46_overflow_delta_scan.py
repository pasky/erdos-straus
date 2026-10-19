"""Overflow distances. Run under ulimit -v 2000000 and timeout; no dense products.
Primary invariant: positive-exponent l1 overflow of divisors of K^2 mod m.
Secondary full residual fibres use exactly the same function, with N=b^2.
"""
import argparse
import csv
import gzip
import json
from collections import Counter, deque
from math import gcd, isqrt
from pathlib import Path
from random import Random
from flint import fmpz

OUT = Path('data/z46_overflow_delta')


def fac(n):
    return [(int(p), int(e)) for p, e in fmpz(n).factor()]


def divisors(fs):
    ds = [1]
    for p, e in fs:
        old = ds[:]
        z = 1
        for _ in range(e):
            z *= p
            ds.extend(d*z for d in old)
    return ds


def residues(fs, m):
    S = {1 % m}
    for p, e in fs:
        old = S
        S = set()
        z = 1
        for _ in range(e+1):
            S.update(r*z % m for r in old)
            z = z*p % m
    return S


def distance(fs, m, target):
    """Exact multi-source BFS, at most m states; None denotes infinity."""
    target %= m
    fs = [(p,e) for p,e in fs if gcd(p,m) == 1]
    S = residues(fs,m)
    if target in S:
        return 0
    seen = set(S)
    layer = S
    d = 0
    while layer:
        d += 1
        nxt = {r*p % m for r in layer for p,_ in fs} - seen
        if target in nxt:
            return d
        seen.update(nxt)
        layer = nxt
    return None


def window(n, m):
    K = (n+m)//4
    assert (n+m) % 4 == 0 and gcd(m,n) == 1
    fs = fac(K)
    return distance([(p,2*e) for p,e in fs],m,-K)


def hit(n,m):
    K = (n+m)//4
    if gcd(K,n) != 1:
        return None
    fs = fac(K)
    ds = divisors([(p,2*e) for p,e in fs])
    for d in ds:
        if (d+K) % m == 0:
            A = (K+d)//m
            assert K*A % d == 0
            Y,Z = A,K*A//d
            assert 4*K*Y*Z == n*Y*Z + K*(Y+Z)
            return [m,K,d]
    return None


def first_hit(n, limit):
    # m <= (n+4)/3 at a cap-zero witness, proved in the memo.
    for m in range((-n) % 4 or 4, min(limit,(n+4)//3)+1,4):
        w = hit(n,m)
        if w is not None:
            return w
    return None


def minimum(n,limit):
    # Zero search first: no BFS at large moduli on the common successful case.
    w = first_hit(n,limit)
    if w:
        return 0,w[0],w
    best,bm = None,None
    for m in range((-n) % 4 or 4, min(limit,n)+1,4):
        if gcd(m,n) != 1:
            continue
        d = window(n,m)
        if d is not None and (best is None or d < best):
            best,bm = d,m
            if d == 1:
                break
    return best,bm,None


def sieve(N):
    s=bytearray(b'\1')*(N+1)
    s[:2]=b'\0\0'
    for p in range(2,isqrt(N)+1):
        if s[p]:
            s[p*p::p]=b'\0'*((N-p*p)//p+1)
    return s


def hist(values):
    return dict(sorted(Counter('inf' if v is None else str(v) for v in values).items()))


def scan():
    OUT.mkdir(parents=True,exist_ok=True)
    isp=sieve(1_000_000)
    ps=[p for p in range(25,1_000_001,24) if isp[p]]
    qs=[q for q in range(3,1001,4) if isp[q]]
    rows=[]
    for p in ps:
        q=next(q for q in qs if pow(p % q,(q-1)//2,q)==q-1)
        d=window(p,q)
        zero=first_hit(p,1000)
        assert zero is not None
        rows.append([p,0,zero[0],q,d])
    with gzip.open(OUT/'primes.csv.gz','wt') as f:
        w=csv.writer(f); w.writerow(['p','delta_box','first_zero_m','first_forced_q','delta_at_q']); w.writerows(rows)
    rng=Random(46031)
    samples=set()
    for lo,hi in [(1_000_000,10_000_000),(10_000_000,100_000_000)]:
        while len([p for p in samples if lo <= p < hi]) < 500:
            p=rng.randrange((lo+23)//24,(hi-1)//24)*24+1
            if fmpz(p).is_prime(): samples.add(p)
    sample_rows=[]
    for p in sorted(samples):
        zero=first_hit(p,1000)
        assert zero is not None
        q=next(q for q in qs if pow(p % q,(q-1)//2,q)==q-1)
        sample_rows.append([p,0,zero[0],q,window(p,q)])
    with gzip.open(OUT/'prime_samples.csv.gz','wt') as f:
        w=csv.writer(f);w.writerow(['p','delta_box','first_zero_m','first_forced_q','delta_at_q']);w.writerows(sample_rows)
    comp_rows=[]
    for n in range(3,20001,2):
        if isp[n] or isqrt(n)**2 == n: continue
        # Exhaust all cap-zero windows if the small menu fails; full-box min is then exact.
        d,m,w=minimum(n, min(1000,n))
        if d != 0:
            zero=first_hit(n,n)
            if zero: d,m,w=0,zero[0],zero
            elif d != 1: d,m,w=minimum(n,n)
        comp_rows.append([n,d,m])
    with gzip.open(OUT/'composites.csv.gz','wt') as f:
        w=csv.writer(f);w.writerow(['n','delta_box','witness_m']);w.writerows(comp_rows)
    # Independently test the character killing both Type-I/II shapes at squares.
    checks=0
    for a in range(3,1000,2):
        n=a*a
        for m in range(3,1001,4):
            if gcd(n,m)!=1: continue
            for K in [(n+m)//4,(n*m+1)//4]:
                for p,e in fac(K):
                    # chi_{-m}(p) = Jacobi(p/m), since m=3 mod4.
                    assert int(fmpz(p).jacobi(m)) == 1
                checks+=1
    fixtures=[]
    for n in [193,409,577,2521,3361,5569,9601,23929,66529,83449,102001,329617,712321,1134241,1724209,1726201,5101441,5212561,8813281,8803369]:
        d,m,w=minimum(n,1000)
        fixtures.append(dict(n=n,delta=d,m=m,witness=w))
    # Matched near-square subset is a deterministic census stratum, not independent evidence.
    near=[r for r in rows if min(r[0]-isqrt(r[0])**2,(isqrt(r[0])+1)**2-r[0]) <= 24]
    hard=[r for r in rows if r[0]%840 in (1,121,169,289,361,529)]
    result=dict(primes_count=len(rows),prime_min_hist=hist(r[1] for r in rows),
        forced_hist=hist(r[4] for r in rows),forced_max=max(rows,key=lambda r:r[4]),
        first_zero_max=max(rows,key=lambda r:r[2]),sample_count=len(sample_rows),
        sample_min_hist=hist(r[1] for r in sample_rows),sample_forced_hist=hist(r[4] for r in sample_rows),
        sample_forced_max=max(sample_rows,key=lambda r:r[4]),sample_first_zero_max=max(sample_rows,key=lambda r:r[2]),
        composite_count=len(comp_rows),composite_hist=hist(r[1] for r in comp_rows),
        composite_nonzero=[r for r in comp_rows if r[1]!=0],square_count=499,square_character_checks=checks,
        fixtures=fixtures,near_square_count=len(near),near_forced_hist=hist(r[4] for r in near),
        hard_count=len(hard),hard_forced_hist=hist(r[4] for r in hard))
    (OUT/'scan.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


def controls():
    OUT.mkdir(parents=True,exist_ok=True)
    # Recompute arithmetic from m,n,x rather than trusting the stored classifications.
    pw=[1,2,3,4,8,16,17,19,23,31,34,47,53,61,79,113,122,137,151,197,226,233,271,541,1103,1171,1367,4201,6301,12601,16831,20521]
    results=[]
    for k,ns in [(8,[11,17,131,241]),(15,pw)]:
        for n in ns:
            rows=[]
            for x in range(n//k+1,3*n//k+1):
                g=gcd(k*x-n,n*x);a=(k*x-n)//g;b=n*x//g
                fs=[(p,2*e) for p,e in fac(b)]
                d=distance(fs,a,-b)
                assert d != 0
                rows.append(dict(x=x,a=a,b=b,delta=d))
            finite=[r['delta'] for r in rows if r['delta'] is not None]
            results.append(dict(k=k,n=n,hist=hist(r['delta'] for r in rows),minimum=min(finite) if finite else None,rows=rows))
            print(k,n,results[-1]['hist'],flush=True)
    with gzip.open(OUT/'failures.json.gz','wt') as f:
        json.dump(results,f,indent=2)
        f.write('\n')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['scan','controls']);args=ap.parse_args()
    {'scan':scan,'controls':controls}[args.mode]()
