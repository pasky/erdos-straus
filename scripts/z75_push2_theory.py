"""Exact one-prime repair thresholds, and independent brute on the floor pencil."""
from math import gcd,isqrt,factorial
from fractions import Fraction

def prime(q):return q>=2 and all(q%i for i in range(2,isqrt(q)+1))

def permitted(n,q,m):
    if gcd(q,n*(n+1))!=1:return False
    a=m;k=q
    while a%q==0:a//=q;k*=q
    return pow(-n,(q-1)//gcd(q-1,m),q)==1 and pow(-n,q-1,k)==1

def qmin(n,k,m):return next(q for q in range(k-1,50000,k) if prime(q) and permitted(n,q,m))

def test_local(n,k,m,q):
    b=(n+1)*q**(m-1);C=(1+q)//k;u=Fraction(n+b,k*b*C-1)
    assert k*u*b*C==n+u+b and gcd(u.denominator*u.numerator,q)==1
    # Direct m-th power test on the actual u' in the finite unit group, not on -n.
    mod=q**2;a=m
    while a%q==0:mod*=q;a//=q
    order=mod//q*(q-1);val=u.numerator*pow(u.denominator,-1,mod)%mod
    assert pow(val,order//gcd(m,order),mod)==1

def brutefibre(n,c):
    # a<=b, (4ac*d-1)b=nc+a; a(4ac-1)<=nc+a.
    for a in range(1,isqrt(n)+2):
        if a*(4*a*c-1)>n*c+a:break
        for d in range(1,(n*c+2*a)//(4*a*a*c)+1):
            if (n*c+a)%(4*a*c*d-1)==0:return True
    return False

if __name__=='__main__':
    for n,k in [(4545,4),(131,8),(241,8),(13,4),(137,8)]:
        print('qmin',n,k,[(m,qmin(n,k,m)) for m in (2,4,6,12,60,120,720,5040,40320,3628800,factorial(16))]);
        for m in (2,4,6,12,60,120):test_local(n,k,m,qmin(n,k,m))
        for B in (32,128):
            Q=[q for q in range(k-1,B+1,k) if prime(q)]
            j=2
            while any(permitted(n,q,factorial(j)) for q in Q):j+=1
            print('cap',n,k,B,'first factorial with no q',j)
    for j in range(16,65):
        delta=4-j%4;a=(j+delta)//4;cut=(4*a*a+j)//delta
        assert any(brutefibre(j*cut+r,cut) for r in range(j))
        for c in range(cut+1,cut+4):assert not any(brutefibre(j*c+r,c) for r in range(j))
    print('fixed-fibre cutoff attained and next 3 rows empty j=16..64')
