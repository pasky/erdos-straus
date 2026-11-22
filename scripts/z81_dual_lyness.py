"""Enumerate off-neighbour positive words on small-seed autonomous Lyness
fibres from the factored residual identity; independent direct check on small
inputs. Polynomial test for a non-neighbour, high-height family.
"""
from math import gcd,isqrt
from sympy import divisors, isprime, jacobi_symbol
from itertools import combinations_with_replacement
from fractions import Fraction as F
import sys

def sameslice(n,e,b,u,v):
    return (e+1)*(b+1)*(n+e+b)*u*v==(u+1)*(v+1)*(n+u+v)*e*b

def primitive_good(n,u,v,t):return n%4==1 and gcd(u,v)==1 and any(z%4==0 for z in (t,u,v,t*u-1,t*v-1))

def exceptional(e,b):
    V=e*b;W=(e+1)*(b+1);L=e+b+1;H=max(e,b)
    for u in range(1,8*(H+1)+1):
        A=L*u-V
        R=W*L*(u-e)*(u-b)
        if R==0:continue
        if A==0:
            # D=-V(u+1), and t>0 forces v<e+b-u
            tests=range(u,e+b-u)
        else:
            tests=set()
            for k in divisors(abs(R)):
                for d in (int(k),-int(k)):
                    v,r=divmod(d+V*(u+1),A)
                    if r==0 and v>=u:tests.add(v)
        for v in tests:
            D=A*v-V*(u+1)
            if not D:continue
            t,r=divmod(W*(u+v-e-b),D)
            if r or t<1:continue
            n=t*u*v-u-v
            if n<1:continue
            assert sameslice(n,e,b,u,v)
            if u not in (e,b) and v not in (e,b):yield n,u,v,t

def main(H):
    # In the small box the literal candidate words are enumerated independently.
    for e,b in combinations_with_replacement(range(1,9),2):
        seen=set(exceptional(e,b));direct=set()
        for u in range(1,41):
            for v in range(u,101):
                for t in range(1,13):
                    n=t*u*v-u-v
                    if n>0 and not ({u,v}&{e,b}) and sameslice(n,e,b,u,v):direct.add((n,u,v,t))
        assert {z for z in seen if z[1]<=40 and z[2]<=100 and z[3]<=12}==direct
    print('small independent check passed')
    biggest=[(0,)]*4;num=[0]*4
    for e,b in combinations_with_replacement(range(1,H+1),2):
        for n,u,v,t in exceptional(e,b):
            good=primitive_good(n,u,v,t)
            for j,yes in enumerate([True,good,good and n%840 in (1,121,169,289,361,529),good and n%840 in (1,121,169,289,361,529) and isprime(n)]):
                if yes:
                    num[j]+=1;biggest[j]=max(biggest[j],(n,e,b,u,v,t))
    print('seed bound',H,'counts/maxima (multiplicity over seed,word pairs)',list(zip(num,biggest)))

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 12)
