"""O147 brainstorm: does non-abelian Frobenius data of p correlate with ES Type II abundance?
Statistic W(p) = #{(e,a,b): e<=E0, e≡-p (4), ab | N=(p+e)/4, e | a+b} (ordered a,b), a fixed-window
Type II count (Lemma 1.2 of CONDITIONAL_ES).  Strata: Frobenius of p in non-abelian fields.
Usage: bs_nonab_frob.py PMAX E0"""
import sys, math
import numpy as np
PMAX=int(sys.argv[1]); E0=int(sys.argv[2])
M=(PMAX+E0)//4+2
spf=np.zeros(M+1,dtype=np.int64)
for i in range(2,int(M**0.5)+1):
    if spf[i]==0:
        s=spf[i*i::i]; s[s==0]=i
spf_l=spf.tolist()
def divisors(n):
    ds=[1]
    while n>1:
        q=spf_l[n] or n; k=0
        while n%q==0: n//=q; k+=1
        ds=[d*q**j for d in ds for j in range(k+1)]
    return ds
def W(p):
    tot=0; emin=None
    for e in range((-p)%4 or 4,E0+1,4):
        N=(p+e)//4; ds=divisors(N); c=0
        for a in ds:
            for b in divisors(N//a):
                if (a+b)%e==0: c+=1
        if c and emin is None: emin=e
        tot+=c
    return tot,emin
def isprime(n):
    if n<2: return False
    r=int(n**0.5)
    for q in range(2,r+1):
        if n%q==0: return False
    return True
def is_quartic(a,p): return pow(a,(p-1)//4,p)==1
def is_cubic(a,p): return pow(a,(p-1)//3,p)==1
def rep_x2_32y2(p):
    y=0
    while 32*y*y<=p:
        x2=p-32*y*y; x=math.isqrt(x2)
        if x*x==x2: return True
        y+=1
    return False
sq840={r*r%840 for r in range(840) if math.gcd(r,840)==1}
from sympy import primerange
rows=[]
for p in primerange(1000,PMAX):
    if p%24!=1: continue
    w,em=W(p)
    rows.append((p,w,em,p%840 in sq840,is_quartic(2,p),rep_x2_32y2(p),is_cubic(2,p),is_quartic(3,p),p%16==1))
names=['sqclass840','2quartic','x2+32y2','2cubic','3quartic','p=1(16)']
def stats(sel,lab):
    xs=[r[1]/math.log(r[0])**3 for r in sel]
    if not xs: return
    m=sum(xs)/len(xs); sd=(sum((x-m)**2 for x in xs)/len(xs))**.5
    print(f"  {lab:28s} n={len(xs):6d} mean W/log^3p={m:.4f} ±{sd/len(xs)**.5:.4f}  min={min(xs):.4f}  frac(emin>E0/4)={sum(1 for r in sel if r[2] is None or r[2]>E0//4)/len(sel):.3f}")
print(f"PMAX={PMAX} E0={E0} primes p≡1(24) in [1000,PMAX): {len(rows)}")
for univ,ul in [(rows,'all p≡1(24)'),([r for r in rows if r[3]],'square classes mod 840')]:
    print(ul)
    for k,nm in enumerate(names[1:],start=4):
        stats([r for r in univ if r[k]],nm+'=T'); stats([r for r in univ if not r[k]],nm+'=F')
