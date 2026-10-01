# Independent brute-force engine for the signed graph G_p (no project code used)
from fractions import Fraction as Fr
from math import gcd
from collections import defaultdict, deque
import sys

def factor(n):
    n=abs(n); f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1 if d==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f

def divisors_from(f):
    ds=[1]
    for pr,e in f.items():
        ds=[d*pr**k for d in ds for k in range(e+1)]
    return ds

def fibre(p,z):
    """all vertices containing z (as sorted tuples)"""
    R=Fr(4,p)-Fr(1,z)
    r,s=R.numerator,R.denominator
    out=set()
    if r==0: return out
    f=factor(s); f2={k:2*v for k,v in f.items()}
    for d in divisors_from(f2):
        for D in (d,-d):
            if D==-s: continue
            if (s+D)%r: continue
            y=(s+D)//r; w2=s+s*s//D
            if w2%r: continue
            w=w2//r
            if y==0 or w==0: continue
            assert Fr(1,z)+Fr(1,y)+Fr(1,w)==Fr(4,p)
            out.add(tuple(sorted((z,y,w))))
    return out

def all_vertices(p):
    V=set()
    for z in range(1,3*p//4+1):
        V|=fibre(p,z)
    return V

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def vp(n,p):
    k=0
    while n%p==0: n//=p;k+=1
    return k
