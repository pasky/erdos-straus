"""Independent arithmetic audits of the new graded/finite-box claims.
Run with ulimit -v 2000000; timeout 180 uv run --with python-flint python ...
Existing z45 toy already independently covers the four numerator-8 BFS profiles.
This adds finite-box composite minima, factorwise weighted distances, and cap separation.
"""
import csv
import gzip
import json
from math import gcd
from fractions import Fraction
from z46_overflow_delta_scan import OUT, fac, divisors, window, distance

BIG = 10**9


def weighted_distance(fs,m,target):
    """Factor-at-a-time min-plus convolution, not multi-generator BFS.
    Each factor offers e free multiplications, then unit-cost forward steps.
    Two sweeps around each permutation cycle solve its directed distance transform.
    """
    cost=[BIG]*m
    cost[1 % m]=0
    for p,e in fs:
        seed=[BIG]*m
        for r,c in enumerate(cost):
            if c == BIG: continue
            v=r
            for j in range(e+1):
                seed[v]=min(seed[v],c)
                v=v*p % m
        visited=bytearray(m)
        for r in range(m):
            if visited[r]:continue
            cycle=[];v=r
            while not visited[v]:
                visited[v]=1;cycle.append(v);v=v*p % m
            # Twice traversing a whole cycle propagates every candidate to every point.
            for _ in range(2):
                for v in cycle:
                    w=v*p % m
                    if seed[v]+1 < seed[w]:seed[w]=seed[v]+1
        cost=seed
    c=cost[target % m]
    return None if c==BIG else c


def actual_typeII(n,limit=None):
    """Direct Y,Z denominator search; independent of divisor residues."""
    for m in range((-n)%4 or 4,(n if limit is None else limit)+1,4):
        K=(n+m)//4
        if gcd(K,n)!=1:continue
        for Y in range(K//m+1,2*K//m+1):
            den=m*Y-K
            if K*Y % den==0:
                Z=K*Y//den
                assert Z>=Y
                return m,K,Y,Z
    return None


def at_m_direct(n,m):
    K=(n+m)//4
    for Y in range(K//m+1,2*K//m+1):
        if K*Y % (m*Y-K)==0:return True
    return False


def cap_reachable(K,m,e=None):
    S={1}
    for p,b in fac(K):
        A={pow(p,j,m) for j in range(2*b+1)}
        if p!=2:
            # e=None means every even exponent; m! is unnecessary: phi(m)<=m.
            A.update(pow(p,2*b+2*j,m) for j in range(1,(m if e is None else e)+1))
        S={r*a%m for r in S for a in A}
    return -K % m in S


def main():
    report={}
    prime_rows=[]
    for name in ['primes.csv.gz','prime_samples.csv.gz']:
        with gzip.open(OUT/name,'rt') as f:prime_rows.extend(list(csv.DictReader(f)))
    for row in prime_rows:
        n,q,d=int(row['p']),int(row['first_forced_q']),int(row['delta_at_q'])
        K=(n+q)//4;fs=[(p,2*b) for p,b in fac(K)]
        assert weighted_distance(fs,q,-K)==d
        assert at_m_direct(n,int(row['first_zero_m']))
    report['prime_distances_and_zero_witnesses']=len(prime_rows)
    with gzip.open(OUT/'composites.csv.gz','rt') as f:comps=list(csv.DictReader(f))
    nonzero=0
    for r in comps:
        n,d,m=int(r['n']),int(r['delta_box']),int(r['witness_m'])
        if d==0:
            assert at_m_direct(n,m)
        else:
            nonzero+=1
            assert actual_typeII(n) is None
            K=(n+m)//4;fs=[(p,2*b) for p,b in fac(K)]
            assert weighted_distance(fs,m,-K)==d
            if d>1:
                # Independent lower bound: no divisor of K^2 times one prime of K hits.
                for t in range((-n)%4 or 4,n+1,4):
                    L=(n+t)//4
                    if gcd(L,n)!=1:continue
                    ff=fac(L)
                    ds=divisors([(p,2*b) for p,b in ff])
                    assert all((a*p+L)%t for a in ds for p,b in ff)
    report['composite_minima']=len(comps)
    report['complete_typeII_failures']=nonzero
    # Independent min=1 verification in every nonempty non-kernel PW15 exception.
    with gzip.open(OUT/'failures.json.gz','rt') as f:
        controls=json.load(f)
    tested=0
    for r in controls:
        if r['minimum']!=1:continue
        n,k=r['n'],r['k']
        row=next(x for x in r['rows'] if x['delta']==1)
        a,b,x=row['a'],row['b'],row['x']
        fs=fac(b);ds=divisors([(p,2*e) for p,e in fs])
        assert not any((d+b)%a==0 for d in ds)
        witness=next(d*p for d in ds for p,e in fs if (d*p+b)%a==0)
        y=(b+witness)//a;z=Fraction(b*y,witness)
        assert Fraction(k,n)==Fraction(1,x)+Fraction(1,y)+1/z
        assert int(fac(z.denominator)[0][1])==1 and len(fac(z.denominator))==1
        # The existing independent z45 classification excludes every delta-zero fibre.
        old=json.loads((OUT.parent/'z45_prime_t1_dual'/f'full{k}_{n}.json').read_text())
        assert all(t['kind'] in ('quadratic','higher','budget') for t in old)
        tested+=1
    report['real_failures_with_verified_minimum_one']=tested
    # The new counterexample: prime 2113, odd K, delta one but square cap infinite.
    n,m,K=2113,43,539
    assert fac(n)==[(2113,1)] and n % 24==1
    assert weighted_distance([(7,4),(11,2)],43,-539)==1
    assert not cap_reachable(K,m,None)
    assert pow(7,3,43)==42 and pow(11,7,43)==1
    assert Fraction(4,2113)==Fraction(1,539)+Fraction(1,9111256)+Fraction(7,185944)
    # A forced window can have odd overflow too, but its cap is finite.
    assert window(31121,43)==1 and cap_reachable(7791,43,1)
    report['parity_separation']={'n':n,'m':m,'K':K,'delta':1,'cap':'inf'}
    # Rank-one exact distance formula, independently computed over residue orders.
    toy=[]
    for m in [3,7,11,19,43,67]:
        for p in [2,3,5,7,11,13]:
            if gcd(p,m)>1:continue
            order=next(j for j in range(1,m) if pow(p,j,m)==1)
            for b in range(1,9):
                pred=None if order%2 else max(0,order//2-b)
                got=distance([(p,2*b)],m,-pow(p,b,m))
                assert pred==got
                toy.append([m,p,b,got])
    report['rank_one_toy_checks']=len(toy)
    (OUT/'verify.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
