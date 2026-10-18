"""z35 shared helpers: SPF sieve, divisors, Gaussian representation, quartic symbols."""
import numpy as np
def spf_sieve(n):
    s=np.zeros(n+1,dtype=np.int32); s[1]=1
    for i in range(2,int(n**.5)+1):
        if s[i]==0:
            blk=s[i*i::i]; blk[blk==0]=i
    idx=np.nonzero(s==0)[0]; s[idx]=idx
    return s
def factor(n,spf):
    f={}
    while n>1:
        q=int(spf[n]); f[q]=f.get(q,0)+1; n//=q
    return f
def divisors_from(f):
    ds=[1]
    for q,e in f.items():
        ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def primes_upto(n,spf):
    return [int(i) for i in np.nonzero(spf[:n+1]==np.arange(n+1))[0] if i>=2]
def rep2(p):
    """p=a^2+b^2, a odd, b even, both >0 (Cornacchia)."""
    # sqrt(-1) mod p
    c=2
    while pow(c,(p-1)//2,p)!=p-1: c+=1
    x=pow(c,(p-1)//4,p)
    r0,r1=p,x
    import math
    lim=math.isqrt(p)
    while r1>lim: r0,r1=r1,r0%r1
    a=r1; b=math.isqrt(p-a*a)
    if a%2==0: a,b=b,a
    return a,b
def b1_witnesses(p,D,spf):
    """b=1 line certificates (d,w) with d<=D: w | p+4d, w = -1 mod 4d, w < p+4d."""
    out=[]
    for d in range(1,D+1):
        n=p+4*d; t=4*d
        for w in divisors_from(factor(n,spf)):
            if w<n and w%t==t-1: out.append((d,w))
    return out
