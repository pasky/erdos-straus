"""Round-2 exact identity and divisor-depth checks; no analytic input."""
from itertools import combinations
from math import gcd, isqrt, prod
from z79_es_engine import jac, triple


def prime(x):
    return x >= 2 and all(x%i for i in range(2,isqrt(x)+1))


def small_mr(x):
    # Sorenson-Webster, Math. Comp. 86 (2017), psi_12 > 10^23.
    assert 37<x<10**23 and x%2
    s,d=0,x-1
    while d%2==0: s,d=s+1,d//2
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        w=pow(a,d,x)
        if w==1 or w==x-1: continue
        for _ in range(s-1):
            w=w*w%x
            if w==x-1: break
        else: return False
    return True


def check(n,u,A):
    assert (n+u)%A == (A+1)%u == 0
    v,t=(n+u)//A,(A+1)//u
    assert min(t,u,v)>=2 and n==t*u*v-u-v and jac(A,n)==-1
    if u%4==0:
        w=u//4; f=t*v-1
        triple(n,(w*f,t*n*w,t*n*w*f))
    else:
        assert t%4==0
        w=t//4; triple(n,(u*v*w,n*v*w,n*u*w))


def main():
    for z in (210,1050,1890):
        b=z*(4*z+1); u=4*z*z-3*z+1; t=4*z*z+5*z+2
        A=b*b-b+1
        for e in range(3,55,6):
            n=(u+1)*b**e+1
            assert t*u==A+1 and n%840==1
            check(n,u,A)
    print('F: 27 growing-base instances; all triple and character tests pass')
    # A small exact depth-3 packet: shrink the ambient modulus for replay.
    u=72; r=u+1; d=3
    g=next(g for g in range(u) if pow(g,d,u)==u-1 and g!=u-1 and gcd(g,u)==1)
    pp=[q for q in range(g,4000,u) if prime(q) and q>2*u]
    neutral=[a for a in range(1+2*u,4000,u) if prime(a)][:2]
    v=pp[0]*prod(neutral); s=v+1; K=r*s*s*u
    assert gcd(r,s)==1 and gcd(u,v)==1 and s%8==0
    bb=[q for q in pp[1:] if K%q!=0 and q not in neutral][:d-1]; B=prod(bb); T=r*v*B
    l0=(-pow(B,-1,K))%K
    L=next(l0+i*K for i in range(10000) if l0+i*K>T and small_mr(l0+i*K))
    n=T*L-u; h=(B*L+1)//K
    assert n==1+r*s*((r-1)*(s-1)*r*s*h-1) and gcd(r*s,(n-1)//(r*s))==1
    got=[]; primes=[pp[0]]+bb+neutral+[r]
    for i in range(len(primes)+1):
        for inds in combinations(primes,i):
            A=prod(inds)
            if (A+1)%u==0:
                assert set(primes[:d])<=set(inds)
                check(n,u,A); got.append(A)
    assert len(set(got))==2**(len(neutral)+1) and min(got)==prod(primes[:d])
    print('G small packet: u,g,r,small factors:',u,g,r,primes)
    print('G exact hits below the cofactor:',len(got),'least',min(got),'largest',max(got))
    # Counter-row, same programmed product, a single-prime shortcut in L.
    b=next(q for q in range(2*u-1,10000,u) if prime(q) and gcd(q,T*K)==1)
    L2=b*((l0*pow(b,-1,K))%K); n2=T*L2-u
    check(n2,u,b)
    assert n2%(T*K)==n%(T*K)
    print('G unsifted same class: depth-one shortcut',b)

if __name__=='__main__': main()
