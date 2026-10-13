"""R176 from scratch: (1) for Type II pairs (f,f') of primes p<P, the algebra B_T, T=[[f,1],[1,f']],
B_T = (-f, -f*detT) is ramified exactly at {p} (finite places);  (2) pairs with G >= 2 sqrt(h) but 4h !| g^2,
and B_T ramified exactly at p (=> exist on a supersingular curve, show the 'G >= 2 sqrt h' reading is only necessary);
(3) Type I tuples: does p | e ever happen?"""
import sys
from math import gcd, isqrt
from sympy import factorint, primerange

def vq(x,q):
    v=0
    while x%q==0: x//=q; v+=1
    return v,x
def leg(a,q): # q odd prime, a unit
    r=pow(a%q,(q-1)//2,q); return 1 if r==1 else -1
def hilb(a,b,q):
    al,u=vq(a,q); be,w=vq(b,q)
    if q!=2:
        s = (-1)**(al*be*((q-1)//2))
        return s*(leg(u,q)**be)*(leg(w,q)**al)
    eps=lambda x: ((x-1)//2)%2
    om=lambda x: ((x*x-1)//8)%2
    e = eps(u)*eps(w) + al*om(w) + be*om(u)
    return -1 if e%2 else 1
def ram(a,b):
    qs=set(factorint(abs(a)))|set(factorint(abs(b)))|{2}
    return sorted(q for q in qs if hilb(a,b,q)==-1)
