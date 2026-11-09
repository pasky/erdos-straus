#!/usr/bin/env python3
"""Checks for Z68_U7F: (a) Prop 3.2 family covers all odd (u,v) classes mod 8 with m odd;
(b) Prop 3.6 for R=4, y=5 on primes p = 1 (mod M) up to 2e9."""
from sympy import isprime, factorint, divisors
from math import gcd, log, floor
# (a)
cls=set()
for A in range(8):
    u,v,m=A*A+A-1,2*A+1,A*A+A+1
    assert u*u+v*v-1==m*m and m%2==1
    for su in (1,-1):
        for sv in (1,-1):
            for (a,b) in ((u,v),(v,u)):
                cls.add(((su*a)%8,(sv*b)%8))
odd={(a,b) for a in (1,3,5,7) for b in (1,3,5,7)}
print("Prop3.2 classes covered:",len(cls&odd),"of 16 ->", "OK" if odd<=cls else "FAIL")
# (b)
R,y=4,5
M=1
for q in (2,3,5):
    e=floor(log(8*R*(R+1))/log(q))+1; M*=q**e
print("M =",M)
def smooth_part(n):
    s=1
    for q in (2,3,5):
        while n%q==0: n//=q; s*=q
    return s
def has_word_with_letter(p,r):
    # pairs (x,r): x | p+r, x = -p mod r, x+r = 7 mod 8
    return [x for x in divisors(p+r) if (x+p)%r==0 and (x+r)%8==7]
bad=0; tested=0
p=1+M
while p<2*10**9:
    if isprime(p):
        tested+=1
        for r in range(1,R+1):
            L=8*r//gcd(8,r); s=smooth_part(p+r); Q=(p+r)//s
            assert s==1+r, (p,r,s)
            assert Q%L==1, (p,r,Q%L)
            xs=has_word_with_letter(p,r)
            if xs:
                if isprime(Q): bad+=1; print("COUNTEREXAMPLE",p,r,xs)
                for x in xs:
                    g=x//gcd(x,1+r)  # rough part of x
                    # check x = e*g with e | 1+r, 1<g<Q proper divisor of Q
                    e=x//g
                    assert (1+r)%e==0 and Q%g==0 and 1<g<Q, (p,r,x)
                print(f"p={p} r={r}: Q composite={not isprime(Q)}, words x={xs}")
    p+=M
print("tested primes:",tested,"violations:",bad)
