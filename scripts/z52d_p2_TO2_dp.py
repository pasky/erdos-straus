# Z0673: Type I witnesses (a,d) for prime p: f | 4a^2 d + 1, f ≡ -p (mod 4ad), and f <= p/2 (so that b>=a holds; exact).
# Test the claim "(d/p) = -1 is needed": count witnesses with (d/p) = +1.
import math, numpy as np
def divisors(n):
    ds=[1]; x=n; f=2
    while f*f<=x:
        if x%f==0:
            e=0
            while x%f==0: x//=f; e+=1
            ds=[d*f**k for d in ds for k in range(e+1)]
        f+=1
    if x>1: ds=ds+[d*x for d in ds]
    return ds
def leg(a,p): 
    r=pow(a%p,(p-1)//2,p); return 1 if r==1 else (-1 if r==p-1 else 0)
primes=[p for p in range(10000,100000) if all(p%q for q in range(2,int(p**0.5)+1)) and p%24==1]
tot=0; pos=0; hits_by_d={}
DIV={}
for a in range(1,51):
    for d in range(1,51):
        DIV[(a,d)]=divisors(4*a*a*d+1)
for p in primes:
    for (a,d),ds in DIV.items():
        q=4*a*d; M=4*a*a*d+1
        for f in ds:
            if f>p//2 or math.gcd(f,q)!=1: continue
            if (f+p)%q: continue
            # f = q c - p with c=(f+p)/q; e=M/f; b = c e - a >= a required
            c=(f+p)//q; e=M//f
            if c*e-a < a: continue
            tot+=1
            l=leg(d,p)
            if l==1: pos+=1; hits_by_d[d]=hits_by_d.get(d,0)+1
print('primes',len(primes),'Type-I witnesses (a,d<=50,f<=p/2,b>=a):',tot,' with (d/p)=+1:',pos, ' examples of d with +1:', sorted(hits_by_d.items())[:10])
