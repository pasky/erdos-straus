"""Paired-window controls. Default checks the saved certificates with stdlib.
--search uses SymPy as composite filter and PARI primecert for ECPP.
"""
import argparse
from math import gcd, isqrt, prod
from pathlib import Path
import json

DB = Path('data/z81/geom_comb/smooth.json')


def td(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def lucas(n):
    from sympy import factorint
    if n<10**6: return None
    fac = list(factorint(n-1).items())
    g=next(a for a in range(2,n) if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,b in fac))
    return [g,[[int(q),int(b),lucas(int(q))] for q,b in fac]]


def search():
    from sympy import isprime, primerange
    from cypari2 import Pari
    from random import Random
    pari=Pari(); pari.allocatemem(128000000)
    neutral=[q for q in primerange(2,100000) if q%31==1]
    rng=Random(31081); cases=[]
    for b in (1,3):
        for tries in range(2000000):
            Q=sorted(rng.sample(neutral,32)); x=11**b*prod(Q); p=8*x-31
            if p%840!=1 or not isprime(p): continue
            cert=pari(p).primecert(); assert cert.primecertisvalid()==1
            ec=cert.python(); n,t,s,a,pt=ec[-1]; tail=(n+1-t)//s
            cases.append(dict(b=b,Q=Q,p=p,ec=ec,tailproof=lucas(tail)));break
        else: raise ValueError('budget exhausted')
    DB.write_text(json.dumps(cases,indent=1)+'\n')


def check_lucas(n,P):
    if P is None:
        assert n<10**6 and td(n); return
    a,fac=P
    assert len({q for q,b,W in fac})==len(fac) and all(q>=2 and b>=1 for q,b,W in fac)
    assert prod(q**b for q,b,W in fac)==n-1 and pow(a,n-1,n)==1
    for q,b,W in fac:
        check_lucas(q,W); assert gcd(pow(a,(n-1)//q,n)-1,n)==1


def add(P,Q,n,a):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%n==0:return None
    if P==Q:t=(3*x*x+a)*pow(2*y,-1,n)%n
    else:t=(v-y)*pow(u-x,-1,n)%n
    w=(t*t-x-u)%n
    return w,(t*(x-w)-y)%n


def mul(k,P,n,a):
    R=None
    while k:
        if k%2:R=add(R,P,n,a)
        P=add(P,P,n,a);k//=2
    return R


def ec_check(p,rows,tailproof):
    for n,t,s,a,(x,y) in rows:
        assert n==p and n>3 and gcd(6,n)==1 and s>0
        b=(y*y-x*x*x-a*x)%n
        assert gcd(4*a**3+27*b*b,n)==1
        m=n+1-t; q,r=divmod(m,s)
        # Hasse + least prime divisor <=sqrt(n); rounded up deliberately.
        assert r==0 and (isqrt(isqrt(n))+2)**2 < q < n
        P=mul(s,(x%n,y%n),n,a);assert P is not None and mul(q,P,n,a) is None
        p=q
    check_lucas(p,tailproof)


def check():
    for row in json.loads(DB.read_text()):
        b,Q,p=row['b'],row['Q'],row['p']; x=prod(Q)*11**b
        assert len(set(Q))==32 and all(td(q) and q%31==1 for q in Q)
        assert p==8*x-31 and p%840==1 and max(Q)**27<p
        ec_check(p,row['ec'],row['tailproof'])
        assert pow(11,(p-1)//2,p)==p-1
        for m in (8,4):
            r={pow(p,j,31)*pow(11,i,31)*pow(2,h,31)%31 for j in (-1,0,1) for i in range(-b,b+1) for h in range(-int(m==4),int(m==4)+1)}
            assert (30 in r)==(b==3 and m==4)
            print('p',p,'m',m,'v11',b,'largest',max(Q),'omega',len(Q)+1+int(m==4),'residue_count',len(r),'hit',30 in r)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--search',action='store_true');args=ap.parse_args()
    if args.search:search()
    check()
