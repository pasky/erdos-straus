"""Exact CRT union via signed intersections. Natural height=max(q,product of fixed blocks)."""
from fractions import Fraction
from math import gcd,lcm,prod
from collections import defaultdict
from functools import lru_cache
import sys
from z80_square_span import fac,primes_to,jac

@lru_cache(None)
def phi(m):return prod(p**(a-1)*(p-1) for p,a in fac(m))

def crt(m,a,t,b):
    h=gcd(m,t)
    if (a-b)%h:return None
    return (lcm(m,t),(a+m*(((b-a)//h)*pow(m//h,-1,t//h)%(t//h)))%lcm(m,t))

def atoms(T):
    out=set();neutral=0
    for q in primes_to(T):
        if q<7 or q%4!=3:continue
        for g in range(q-1,T+1,q):out.add((4*g,-q%(4*g)))
        Q=(q-1)//2;k=0
        while 3**k<Q:k+=1
        for h in range(2,q):
            if pow(h,Q,q)!=1 or any(pow(h,Q//l,q)==1 for l,_ in fac(Q)):continue
            def dfs(i,G,r):
                nonlocal neutral
                if i==k:
                    neutral+=1
                    for b in range(1,q):
                        if jac(b,q)<0:out.add(crt(4*G,-q,q,b))
                    return
                for g in range(r,T//G+1,q):dfs(i+1,G*g,r**3%q)
            dfs(0,1,h)
    return sorted(out),neutral

def density(T,a,brute=False):
    E,k=atoms(T);avoid={(840,a):1}
    for m,b in E:
        ch=defaultdict(int)
        for (M,R),c in avoid.items():
            t=crt(m,b,M,R)
            if t:ch[t]-=c
        for t,c in ch.items():
            avoid[t]=avoid.get(t,0)+c
            if not avoid[t]:del avoid[t]
    d=1-sum(Fraction(c*phi(840),phi(m)) for (m,b),c in avoid.items())
    if brute:
        F=[(m,b) for m,b in E if crt(m,b,840,a)]
        P=lcm(840,*(m for m,b in F));assert P<=10**8
        h=tot=0
        for r in range(a,P,840):
            if gcd(r,P)==1:tot+=1;h+=any(r%m==b for m,b in F)
        assert d==Fraction(h,tot)
    return d,k,len(E)
if __name__=='__main__':
    for T in map(int,sys.argv[1:]):
        for a in (1,121,169,289,361,529):
            d,k,e=density(T,a,T<=16);print(T,a,d,k,e,flush=True)
