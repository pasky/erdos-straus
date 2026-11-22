"""Finite, exhaustive signed-sector/chord study on the ordinary affine ES model.
The chord scan uses the inverse direction: start from every positive point and every
signed point (coordinate permutations via symmetry) and check for signed co-inputs.
"""
from itertools import permutations, combinations_with_replacement
from fractions import Fraction
from math import gcd, prod, isqrt
from collections import Counter
from functools import cache
import sys

@cache
def divisors_square(b):
    from sympy import factorint
    ds = [1]
    for p, k in factorint(b).items():
        ds = [d * int(p)**e for d in ds for e in range(2*int(k)+1)]
    return ds

def points(M,n):
    assert n%M
    S=set()
    for v in range(1,3*n//M+1):
        for x in (v,-v):
            h=Fraction(M,n)-Fraction(1,x); a,b=h.as_integer_ratio()
            for e in divisors_square(b):
                for d in (e,-e):
                    Z=b+b*b//d; Y=b+d
                    if Y and Z and Y%a==Z%a==0:
                        y,z=Y//a,Z//a
                        if v<=min(abs(y),abs(z)):
                            S.add(tuple(sorted((x,y,z))))
    divisors_square.cache_clear()
    return sorted(S)

def chord(M,n,P,Q):
    # P != Q, return only finite *integral* residual intersection on a proper line.
    V0=[y-x for x,y in zip(P,Q)]; g=gcd(*V0)
    if not g or 0 in V0: return None
    u,v,w=(v//g for v in V0); a,b,c=P
    den=M*u*v*w
    num=n*(u*v+v*w+w*u)-M*(a*v*w+b*w*u+c*u*v)
    if num%den: return None
    k=num//den-g
    R=(a+k*u,b+k*v,c+k*w)
    assert M*prod(R)==n*(R[0]*R[1]+R[1]*R[2]+R[0]*R[2])
    return R

def scan(M,n):
    S=points(M,n); pos=[P for P in S if min(P)>0]
    neg=sorted({A for P in S if min(P)<0 for A in permutations(P)})
    counts=Counter(); good=[]
    for P in pos:
        for Q in neg:
            R=chord(M,n,P,Q)
            if R is None or 0 in R or min(R)>0 or R==Q: continue
            if Q>R: continue
            counts[(sum(x<0 for x in Q),sum(x<0 for x in R))]+=1
            good.append((P,Q,R))
    print(M,n,'positive',len(pos),'signed-sorted',len(S)-len(pos),'chords',sorted(counts.items()),'example',min(good,default=None),flush=True)

if __name__=='__main__':
    for row in sys.argv[1:]:
        M,n=map(int,row.split(':')); scan(M,n)
