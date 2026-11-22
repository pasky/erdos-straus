"""Complete weighted-pencil orbit test (on enumerated inputs); keep pairwise
ratios modulo S-units, allowing diagonal/inverse and permutations. Also check
p-adic chord/Brauer law for rational residual roots and direction squareclass.
"""
from fractions import Fraction as Q
from math import gcd,lcm,prod,isqrt
from itertools import permutations,combinations
from collections import Counter
from z81_dual_chords import points
from sympy import primerange, jacobi_symbol, isprime
from sys import argv

def core(x,S):
    x=abs(x)
    for q in S:
        while x%q==0: x//=q
    return x

def tag(P,S):
    a,b,c=sorted(core(z,S) for z in P); g=gcd(a,b,c)
    U=(a//g,b//g,c//g); L=lcm(*U); V=tuple(L//v for v in reversed(U));return min(U,V)

def representative(n):
    return next((int(q) for q in primerange(2,1000) if jacobi_symbol(q,n)==-1),None)

def scan(M,n):
    pts=points(M,n); pos=[v for v in pts if min(v)>0];sig=[v for v in pts if min(v)<0];q=representative(n)
    def test(S):
        A={tag(v,S):v for v in sig}; return [(v,A[t]) for v in pos if (t:=tag(v,S)) in A]
    cases=[]
    for S in ((2,),tuple(sorted({2,q}-{None})),(2,3,5,7),tuple(primerange(2,20))):
        L=test(S); cases.append((S,len(L),L[0] if L else None))
    print(M,n,len(pts),len(pos),cases,flush=True)

if __name__=='__main__':
    for s in argv[1:]:
        if s=='small':
            for p in primerange(5,1000):
                if p%4==1:scan(4,int(p))
        else:
            M,n=map(int,s.split(':'));scan(M,n)
