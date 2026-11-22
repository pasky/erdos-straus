"""Actual alternating prime-factor walk. Bounded runs are not traps unless the
queue exhausts without censoring; edges above the two-cycle bound may be dropped
only in the separate bounded graph, not to assert anything about the full walk.
"""
from functools import cache
from math import gcd, isqrt
from sympy import factorint, jacobi_symbol, primerange, divisors, isprime
from collections import deque
from pathlib import Path
from sys import argv

@cache
def factor(X): return tuple((int(q),int(a)) for q,a in factorint(X).items())

def tests(M,n,c,side,onlyneg):
    X=((n*c+1) if side=='I' else (n+c))//M
    assert (M*X==n*c+1 if side=='I' else M*X==n+c)
    f=factor(X)
    succ=[q for q,_ in f if q%M==(-n)%M and gcd(n,q)==1 and (not onlyneg or jacobi_symbol(q,n)==-1)]
    # Ratio test: two divisors of X opposite mod c; divide their gcd if necessary.
    box={1%c}
    for q,a in f:
        box={v*pow(q,i,c)%c for v in box for i in range(a+1)}
    hit=any((-r)%c in box for r in box)
    return succ,hit

def walk(M,n,c,onlyneg,H=10**7,budget=128):
    assert n*n%M==1 and gcd(c,n)==1
    Q=deque([('II',c)]);seen=set(Q);hist=[];hit=None;cross=None;high=0
    while Q and len(hist)<budget and not (cross and hit):
        typ,e=Q.popleft(); succ,h=tests(M,n,e,typ,onlyneg); hist.append((typ,e))
        if h and hit is None:hit=(typ,e)
        for q in succ:
            # A return edge in the unrestricted graph even when q/e have opposite signs.
            a,b=(e,q) if typ=='II' else (q,e)
            if (n+a)%(M*b)==0 and (n*b+1)%(M*a)==0 and not cross:cross=(a,b)
            if q>H:high+=1;continue
            p=('II' if typ=='I' else 'I',q)
            if p not in seen:Q.append(p);seen.add(p)
    return hist,hit,cross,high,len(Q)

def table():
    Z=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if not s.startswith('#')]
    C=[105,1465,3865,4545,10305,12145,39361,67425,17401609,25,49,121]
    P=sorted(set(Z+[2521,3361,113035442521,1590284203561,6955940568721]))
    for M,n in [(4,n) for n in P+C]+[(8,n) for n in (11,17,131,241,1590284203561,6955940568721)]:
        start=next(c for c in primerange(2,1000) if c%M==(-n)%M and gcd(c,n)==1)
        neg=next((q for q in primerange(2,1000) if q%M==(-n)%M and jacobi_symbol(q,n)==-1),None)
        for c in sorted({start, neg}-{None}):
            for filt in (True,False):
                h,hit,cy,hi,un=walk(M,n,c,filt);print(M,n,c,int(filt),len(h),hit,cy,hi,un,'prefix',h[:5],flush=True)
    factor.cache_clear()

if __name__=='__main__':table()
