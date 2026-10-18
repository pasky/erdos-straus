"""z35 checks: (1) b=1 line divisor form <-> least-residue (m,g) form; (2) Burde's law;
(3) quartic decomposition (w/p)_4 (g/p)_4 = (2/p)(d/p)_4 for b=1 certificates.  Tiny output."""
import sys
from sympy import primerange, divisors
def rep(p):
    a=1
    while a*a<p:
        b2=p-a*a; b=int(round(b2**.5))
        if b*b==b2 and b%2==0: return a,b
        a+=2
def leg(x,p):
    r=pow(x%p,(p-1)//2,p); return 0 if r==0 else (1 if r==1 else -1)
def b1_div(p):
    S=set()
    for d in range(1,(p+3)//8+1):
        n=p+4*d
        for w in divisors(n):
            if w<n and w%(4*d)==4*d-1: S.add((d,w))
    return S
def b1_res(p):
    S=set()
    for m in range(1,(p+1)//3+2):
        g=(-p)%(4*m)
        if g and (m+1)%g==0:
            d=(p+g)//(4*m); c=(m+1)//g; S.add((d,4*c*d-1))
    return S
N=int(sys.argv[1]) if len(sys.argv)>1 else 20000
mis=0;np=0
for p in primerange(5,N):
    if p%4!=1: continue
    np+=1
    if b1_div(p)!=b1_res(p): mis+=1
print("(1) b=1 divisor form vs least-residue form, p=1(4) <",N,":",np,"primes, mismatches",mis)
P=[p for p in primerange(5,800) if p%4==1]; bad=0; tot=0
for p in P:
    for q in P:
        if p==q or leg(p,q)!=1: continue
        a,b=rep(p); c,d=rep(q); tot+=1
        q4=lambda x,r: 1 if pow(x,(r-1)//4,r)==1 else -1
        if q4(p,q)*q4(q,p)!=leg(a*c-b*d,q): bad+=1
print("(2) Burde (p/q)_4(q/p)_4=((ac-bd)/q), (p/q)=1, p,q<800:",tot,"pairs, violations",bad)
bad=0;tot=0
for p in primerange(5,5000):
    if p%4!=1: continue
    e=(p-1)//4
    for d,w in b1_div(p):
        g=(p+4*d)//w; tot+=1
        if pow(w,e,p)*pow(g,e,p)%p != pow(2,2*e,p)*pow(d,e,p)%p: bad+=1
        if leg(w,p)!=-1: bad+=1
print("(3) quartic decomposition + (w/p)=-1 on",tot,"certificates p<5000: violations",bad)
