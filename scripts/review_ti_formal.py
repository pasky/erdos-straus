# R31 from-scratch formal ck_min at an H-generic residue point (independent of typei_formal.py).
# Point: p = a_l (mod l^e_l) for prescribed l; p = 1 (mod l^E) (E huge) for all other primes l <= B.
# For each slice (c,k), ck<=X, s=sf(c) not in {1,2,3,6}: forcedness from Legendre symbols fixed by the point;
# fixed B-part f of N=p^2+4ck^2 from valuations (checked determined); target class -p mod 4ck (checked determined);
# formal M = 2*#{D | f : D = -p (mod 4ck)}.
# Usage: review_ti_formal.py X B l:a:e ...
import sys
from sympy import factorint, primerange, isprime
X,B=int(sys.argv[1]),int(sys.argv[2])
pres={}
for t in sys.argv[3:]:
    l,a,e=map(int,t.split(':')); assert isprime(l) and a%l
    pres[l]=(a%l**e,e)
def leg_p(q):  # (q/p) at the point, p = 1 mod 4 assumed and checked
    if q==2:
        a,e=pres.get(2,(1,99)); assert e>=3; return 1 if a%8 in (1,7) else -1
    a,e=pres.get(q,(1,99)); r=pow(a%q,(q-1)//2,q); return 1 if r==1 else -1
# hard + n_p
a2,e2=pres.get(2,(1,99)); a3,e3=pres.get(3,(1,99))
assert e2>=3 and a2%8==1 and a3%3==1, "point not p=1 (24)"
q=2
while leg_p(q)==1: q+=1
npf=q
def sf(c):
    s=1
    for qq,e in factorint(c).items():
        if e%2: s*=qq
    return s
def val(n,l):
    v=0
    while n%l==0: n//=l; v+=1
    return v
def pmod(m):  # p mod m, m | 4X, determined?
    res=0; mod=1
    for l,v in factorint(m).items():
        if l in pres:
            a,e=pres[l]; assert v<=e, ("target class not fixed",l,m); r=a%l**v
        else: r=1%l**v
        # CRT
        L=l**v; t=((r-res)*pow(mod,-1,L))%L; res+=mod*t; mod*=L
    return res
nall=nuse=nunf=0; best=None; maxroots_needed=0
for m in range(1,X+1):
    for k in range(1,m+1):
        if m%k: continue
        c=m//k; nall+=1
        s=sf(c)
        if s in (1,2,3,6): continue
        nuse+=1
        chi=1
        for qq in factorint(s): chi*=leg_p(qq)
        if chi==1: continue   # forced: M=0 by notes Thm 48.1, no determinacy needed
        nunf+=1
        h=4*c*k; pm=pmod(h)
        # fixed part f
        f=1; A=1+4*c*k*k
        for l,v in factorint(A).items():
            if l<=B and l not in pres: f*=l**v
        for l,(a,e) in pres.items():
            if l>B: continue
            if (c*k)%l==0 or l==2: continue
            v=val(a*a+4*c*k*k,l); assert v<e, ("valuation not fixed",l,c,k,v,e); f*=l**v
        # divisors of f in class -p mod h
        ds=[1]
        for l,v in factorint(f).items(): ds=[d*l**i for d in ds for i in range(v+1)]
        hits=[D for D in ds if (D+pm)%h==0]
        if hits and best is None:
            best=(m,c,k,sorted(hits)[:4],dict(factorint(f)),nunf)
    if best: break
print(f"point n_p={npf}; slices ck<=X: all={nall}, s∉{{1,2,3,6}}={nuse}, unforced={nunf}")
print("formal ck_min:", best if best else f">{X}")
print("B>=2*unforced+2:",B>=2*nunf+2," B>=2*nuse+2:",B>=2*nuse+2," B>=2*all+2:",B>=2*nall+2)
