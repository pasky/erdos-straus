"""Composite-divisor walk, shortest hit <= 6. Starts are both faces separately.
Report a miss only in the stated bounded depth, and distinguish empty boundary.
Seed q=least QNR only when q == -n mod M; q* is the least eligible QNR prime.
"""
from math import gcd,isqrt
from collections import deque,Counter
from functools import lru_cache
from sympy import divisors, jacobi_symbol, primerange,isprime
from pathlib import Path
import sys
@lru_cache(80000)
def ds(N):return tuple(map(int,divisors(N)))

def walk(M,n,q,side):
    C=deque([(q,0,(q,))]);seen={(q,0)};frontier=0
    while C:
        z,j,path=C.popleft(); i=bool(side^(j%2));X=(n*z+1 if i else n+z)//M
        D=ds(X); res={d%z:d for d in D};
        for a in D:
            if (-a)%z in res:
                b=res[-a%z]; g=gcd(a,b);a//=g;b//=g
                assert (a+b)%z==0 and X%(a*b)==0
                return j,path,(a,b),len(seen),frontier
        for d in D:
            if d%M!=(-n)%M or gcd(d,n)>1 or (d,1-j%2) in seen:continue
            if j==6:frontier+=1;continue
            seen.add((d,1-j%2));C.append((d,j+1,path+(d,)))
    return -1,(),(),len(seen),frontier

def row(M,n,output=True):
    q0=next((q for q in primerange(2,2000) if jacobi_symbol(q,n)==-1),None)
    if not q0:
        assert isqrt(n)**2==n, 'least QNR search exhausted'
        return print('square',M,n) if output else None
    q=next(q for q in primerange(2,2000) if q%M==(-n)%M and jacobi_symbol(q,n)==-1)
    W=[walk(M,n,int(q),i) for i in (0,1)]
    if output:print(M,n,'q',q0,'eligible',q,'II,I',W,flush=True)
    return W,q0==q

if __name__=='__main__':
    f4=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if not s.startswith('#')]
    if sys.argv[1:] == ['panel']:
        # Deterministic proof that the three linear forms in the permanent
        # dual trap are prime at the recorded instance, independent of factorint.
        for value in (9189181,183783601,174594421):
            assert all(value%d for d in range(2,isqrt(value)+1))
        for n in sorted(set(f4+[2521,3361,113035442521,183783601,1590284203561,6955940568721,25,49,121,105,1465,3865,4545,10305,12145,39361,67425,17401609])):row(4,n)
        for n in (11,17,131,241,1590284203561,6955940568721):row(8,n)
    else:
        H=int(sys.argv[1]);freq=Counter();boundary=Counter();bad=[]
        for p in range(841,H+1,840):
            if isprime(p):
                W,ok=row(4,p,False);best=min((w[0] for w in W if w[0]>=0),default=-1);freq[ok,best]+=1
                if best==-1:
                    bad.append(p); boundary[ok,any(w[4] for w in W)]+=1
        print('H',H,'counts',sorted(freq.items()),'misses',bad)
        print('misses by (literal seed?, boundary nonempty?)',sorted(boundary.items()))
