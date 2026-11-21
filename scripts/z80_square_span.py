"""Interior-word endpoint products in Q*/Q*2. Exact small-prime experiment."""
from math import isqrt
from functools import lru_cache
from collections import Counter
import sys


def primes_to(b):
    a = bytearray(b'\x01') * (b + 1)
    a[:2] = b'\x00\x00'
    for i in range(2, isqrt(b) + 1):
        if a[i]:
            a[i*i::i] = b'\x00' * ((b-i*i)//i+1)
    return [i for i in range(2,b+1) if a[i]]


def jac(a,n):
    assert n > 0 and n%2
    s=1
    while a:=a%n:
        while not a%2:
            a//=2
            if n%8 in (3,5): s=-s
        if n%4==a%4==3: s=-s
        a,n=n,a
    return s if n==1 else 0


@lru_cache(200000)
def fac(n):
    d=2; f=[]
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e: f.append((d,e))
        d=3 if d==2 else d+2
    if n>1: f.append((n,1))
    return tuple(f)


def divs(n):
    out=[1]
    for d,e in fac(n):
        out += [x*d**k for k in range(1,e+1) for x in out]
    return out


def words(n):
    # At least one letter <= cubic root of n up to an additive constant.
    w=set(); k=2
    while k**3-2*k <= n:
        for A in divs(n+k):
            if (A+1)%k==0:
                t=(A+1)//k; v=(n+k)//A
                if min(t,v)>=k: w.add((k,t,v))
        for A in divs(k*n+1):
            if (A+1)%k==0:
                u=(A+1)//k; v=((k*n+1)//A+1)//k
                if k<=u<=v: w.add((u,k,v))
        k+=1
    return {(min(u,v),t,max(u,v)) for u,t,v in w}


def test(n,ps):
    q=next(l for l in ps if jac(l,n)==-1)
    coords={}; piv={}
    def vec(v):
        b=0
        for l,e in fac(v):
            if e%2: b^=1<<coords.setdefault(l,len(coords))
        return b
    def reduce(b):
        while b and (j:=b.bit_length()-1) in piv: b^=piv[j]
        return b
    W=words(n); direct=False; simple=False
    for u,t,v in sorted(W):
        assert t*u*v-u-v==n
        z=vec(u)^vec(v)
        direct|=z==vec(q)
        simple|= q in (u,v)
        z=reduce(z)
        if z:piv[z.bit_length()-1]=z
    return q,len(W),len(piv),int(reduce(vec(q))==0),int(direct),int(simple)

if __name__=='__main__':
    b=int(sys.argv[1]); ps=primes_to(b); cnt=Counter(); first={}
    for n in ps:
        if n%840!=1:continue
        q,m,r,span,direct,simple=test(n,ps)
        for k,v in [('all',1),('least_prime_spanned',span),('single_row',direct),('endpoint',simple)]:cnt[k]+=v
        if (span,direct,simple) not in first:first[span,direct,simple]=(n,q,m,r)
    print(b,cnt,sorted(first.items()))
