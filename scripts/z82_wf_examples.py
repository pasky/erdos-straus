"""Finite check of the forced first-miss family, and small-closure bound.
Primes/factorizations only accepted below 2^64 (SymPy's deterministic range).
"""
from math import gcd,isqrt
from sympy import primerange,isprime,factorint


def crt(a,m,b,l):
    return (a+m*((b-a)*pow(m,-1,l)%l))%(m*l),m*l


def controls():
    q,s,v=73,101,1487
    a,m=crt(1,840,-q,s);a,m=crt(a,m,-s,v)
    ps=list(primerange(11,q)); qr={l:{i*i%l for i in range(1,l)} for l in ps+[q]}
    for p in range(a,2**64,m):
        if any(p%l not in qr[l] for l in ps) or p%q in qr[q]|{0} or not isprime(p):continue
        f=factorint((p+q)//2); assert all(isprime(l) for l in f)
        if any(l%4!=1 for l in f):continue
        assert (p+q)%s==0 and (t:=(p+s+v)//(s*v))*s*v==p+s+v
        assert pow(s,(p-1)//2,p)==p-1 and pow(v,(p-1)//2,p)==1
        print('norm family example',p,'odd part factors',f,'q s t v',q,s,t,v);break
    else:raise ValueError('outside deterministic range')
    N=10**9;V=[1]
    for r in (2,3,5,7):
        V += [v*r**j for v in V for j in range(1,N.bit_length()) if v*r**j<=N]
    L=[d for d in V if d<=isqrt(N)]
    print('smooths',len(V),'short',len(L),'reduced ratios',sum(gcd(a,b)==1 for a in L for b in L))
if __name__=='__main__': controls()
