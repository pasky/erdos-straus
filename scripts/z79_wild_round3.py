"""Round-3 finite checks: cubic sign detector, cancellation and terminal primes."""
from math import gcd, isqrt
from collections import Counter
from z79_wild_round2 import prime, jac


def radical_odd_valuation(n):
    k=1; p=2
    while p*p<=n:
        inv=False
        while n%p==0: n//=p; inv=not inv
        if inv: k*=p
        p+=1
    return k*n


def run():
    for a,b,c,d in [(1,0,1,1),(1,0,-3,7),(2,3,-5,11),(1,1,0,0),(1,3,3,1)]:
        P=b*b-3*a*c; J=2*b**3-9*a*b*c+27*a*a*d; disc=(4*P**3-J*J)//(27*a*a)
        counts=Counter()
        for v in range(1,10):
            for u in range(1,26):
                if gcd(u,v)>1: continue
                w=4*P**3*v*v-(J*v+27*a*a*u)**2
                if w and P:
                    n=w if disc else 2*J*v+27*a*a*u
                    s=radical_odd_valuation(abs(n))
                    assert gcd(s,u*v)==gcd(gcd(s,u*v),abs(6*a*(disc or J)))
                for l in range(5,121):
                    if not prime(l) or 3*a*v%l==0: continue
                    nr=sum(((a*i**3+b*i*i+c*i+d)*v+u)%l==0 for i in range(l))
                    sign=jac(3*w,l)
                    if sign<0: assert nr==1
                    if sign>0: assert nr in (0,3)
                    if not P and l%3==2: assert nr==1
                    counts[sign]+=1
        print('F',a,b,c,d,'P/disc',P,disc,'sign counts -/0/+',*(counts[i] for i in [-1,0,1]))
    ok=no=0
    for f in range(11,6000):
        if not prime(f): continue
        real=any((f+1)%u==0 and jac(-u,f)<0 for u in range(2,(f+1)//2+1))
        predicted=f%8!=1 or any(prime(q) and q%4==3 and (f+1)%q==0 for q in range(3,f,4))
        assert real==predicted
        ok+=real; no+=not real
    print('prime terminal criterion [11,6000):',ok,no)

if __name__=='__main__': run()
