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
def typeII(n):
    out=[]
    a=1
    while 4*a*a<=n+2*a:
        d=1
        while a*(4*a*d-1)<=n+a:
            b=a
            while b*(4*a*d-1)<=n+a:
                e=4*a*b*d-n
                if e>0 and (a+b)%e==0:
                    c=(a+b)//e; out.append((4*a*c*d-1,4*b*c*d-1,c))
                b+=1
            d+=1
        a+=1
    return out
P=int(sys.argv[1])
bad=0; tot=0
for p in primerange(3,P):
    for f,g,c in typeII(p):
        tot+=1
        r=ram(-f,-f*(f*g-1))
        if r!=[p]: bad+=1; print("ram mismatch",p,f,g,r)
print(f"(1) Type II pairs p<{P}: {tot}, ramification != {{p}}: {bad}")
# (2) counterexamples to 'G >= 2 sqrt h suffices'
ex=0
for p in primerange(3,200):
    for h in range(1,60):
        N=1+p*h
        for f in range(1,isqrt(N)+1):
            if N%f: continue
            g2=N//f; G=gcd(f+1,g2+1); gg=gcd(h,G)
            if G*G>=4*h and (gg*gg)%(4*h)!=0 and ram(-f,-f*(N-1))==[p]:
                ex+=1
                if ex<=5: print("  example: p",p,"f,f'",f,g2,"h",h,"G",G,"gcd(h,G)",gg)
print(f"(2) pairs with G>=2sqrt(h), 4h !| gcd(h,G)^2, B_T ramified exactly at p (p<200,h<60): {ex}")
