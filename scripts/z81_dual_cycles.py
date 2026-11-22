"""Two independent full enumerators of alternating returns (no prime filters).
Also a small scan of the positive fibres with exactly prescribed q,c congruences.
"""
from math import gcd
from sympy import divisors, primerange

def by_a(M,n):
    p=n; r=(-n)%M
    assert r and p*p%M==1
    A=(p*r+M*p+1)//(r*M*M)
    for a in range(1,A+1):
        for c in divisors(p*p+M*a):
            if (p+c)%(M*a): continue
            q=(p+c)//(M*a)
            if c%M!=r or q%M!=r or (p*q+1)%(M*c): continue
            yield (c,q)

def by_q(M,n):
    # q(M²ab-p)=Mbp+1 and b<= (p q+1)/(M c), c=Maq-p.
    # When q>=2p, c>=M*q-p>= (M-1/2)*q, so b<=p +1 and
    # q<=M(p+1)*p+1. Use for independent SMALL-n verification only.
    r=(-n)%M
    for q in range(r,M*(n+1)*n+2,M):
        for c in divisors((n*q+1)//M):
            if (n+c)%(M*q)==0: yield c,q

if __name__=='__main__':
    import sys
    B=int(sys.argv[1]) if len(sys.argv)>1 else 2000
    for M in [4,8]:
        for n in list(range(5,30,4))+[11,17]:
            assert set(by_q(M,n))==set(by_a(M,n))
    print('independent full check passed',flush=True)
    for p in primerange(5,B+1):
        if p%4==1:
            C=list(by_a(4,int(p))); print(p,len(C),C[:3],flush=True)
