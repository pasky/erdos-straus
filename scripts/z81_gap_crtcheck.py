"""Check the discrete transfer mechanism, independently of an asymptotic sieve.
Full period, three genuinely different overlapping-at-a-prime window tests.
Counts exact integer CRT allocations in two ways, under both ordinary and unit laws.
"""
from fractions import Fraction
from itertools import product
from math import gcd,prod
W=(3,7,11);P=(13,17,19,23);Q=prod(P)

def hit(k,rs):
    # positive divisors, not the abstract subgroup
    R={1}
    for r in rs:R.update([d*r%k for d in R])
    return any((-d)%k in R for d in R)

def sig(colors):
    return sum(hit(k,[p for p,c in zip(P,colors) if c==j])<<j for j,k in enumerate(W))

def check(unit):
    observed=[0]*8;haar=[0]*8;cache={C:sig(C) for C in product(range(-1,3),repeat=4)}
    for t in range(Q):
        n=4*t+1
        if unit and gcd(n,Q)>1:continue
        C=tuple(next((j for j,k in enumerate(W) if (n+k)%r==0),-1) for r in P)
        observed[cache[C]]+=1
    for C,mask in cache.items():haar[mask]+=prod(r-unit-3 if c<0 else 1 for r,c in zip(P,C))
    assert observed==haar;den=sum(haar)
    # negative association for all-success products, then for all-failure
    for reverse in (False,True):
        counts=[Fraction(sum(c for mask,c in enumerate(haar) if (((mask^7) if reverse else mask)&m)==m),den) for m in range(8)]
        for m in range(8):assert counts[m]<=prod(counts[1<<j] for j in range(3) if m>>j&1)
    print('unit?',unit,'period',Q,'all-fail',haar[0], 'law size',den,'hist',haar)
if __name__=='__main__':
    check(False);check(True)
    from z81_gap_audit import gap,isprime,genus,factor
    p,b,r=4063936801,13,26050877
    assert all(isprime(t) for t in (p,b,r)) and p==12*b*r-11 and p%11==1 and b%11==2
    q,kg=genus(p);g,triple=gap(p);assert kg==11 and g==55
    for ks in range(3,kg+1,4):
        H={1}
        for a in [p]+[u for u,_ in factor((p+ks)//4)]:
            powers={1};w=a%ks
            while w not in powers:powers.add(w);w=w*a%ks
            H={v*w%ks for v in H for w in powers}
        if ks-1 in H:break
    assert ks==kg and ks-1 in H
    print('starved primitive generator control',p,'x11=3*',b,'*',r,'Kgen=Ksub=',ks,'g=',g,'triple',triple)
