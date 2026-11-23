"""Exhaust the two generators {2,n} in the signed divisor-ratio box.
Tag 0: 2^j=-1; L: n*2^j=-1; R: n=-2^j, modulo k (j>=0).
Run in repo root; exact factor verification including >64-bit primes.
"""
from fractions import Fraction
from functools import cache
from math import gcd, prod
from pathlib import Path
from sympy import factorint

@cache
def factors(n):
    f = {int(k): int(v) for k, v in factorint(n).items()}
    assert prod(q**a for q,a in f.items()) == n
    for q in f:
        assert prime(q)
    return f

@cache
def prime(n):
    if n <= 3:
        return n >= 2
    # Lucas/Pocklington with the complete proven factorization of n-1.
    return all(any(pow(a,n-1,n) == 1 and gcd(pow(a,(n-1)//q,n)-1,n) == 1
                   for a in range(2,min(n,1002))) for q in factors(n-1))

def divisors(n):
    ds=[1]
    for p,e in factors(n).items():
        old=ds[:]
        for j in range(1,e+1):
            ds.extend(a*p**j for a in old)
    return ds

def windows(n,M):
    hits={}
    for j in range((3*n//M).bit_length()):
        t=2**j
        for tag,N in [('0',t+1),('L',n*t+1),('R',n+t)]:
            for k in divisors(N):
                if k>2*n or (k+n)%M or gcd(k,n)!=1:
                    continue
                x=(n+k)//M
                if x%2 or x%t: continue
                # Actual rectangle for the residual M/n - 1/x = k/(nx).
                B=n*x
                A,C={'0':(t,1),'L':(n*t,1),'R':(n,t)}[tag]
                d=B*A//C
                assert B*A%C==0 and B*B%d==0
                e=B*B//d
                assert (d+B)%k == (e+B)%k == 0
                y,z=(d+B)//k,(e+B)//k
                assert Fraction(M,n)==sum(Fraction(1,u) for u in (x,y,z))
                hits.setdefault(k,set()).add((j,tag))
    return hits

if __name__=='__main__':
    hard=[2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929]
    star=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and s[0].isdigit()]
    controls=[25,49,121,105,1465,3865,4545,10305,12145,39361,67425,17401609]
    print('n M #k least_k least(j,tag) all_k_when_count<=4')
    records=[1590284203561,6955940568721]
    for M,ns in [(4,star+hard+records+controls),(8,[11,17,131,241]+records)]:
        for n in ns:
            hits=windows(n,M)
            k=min(hits,default=0)
            print(n,M,len(hits),k,min(hits[k]) if k else '-',sorted(hits) if len(hits)<=4 else '...')
