# Word-level checks for Z2803, Z2839, Z2847, Z2817, Z2871.
# ES word at prime/integer n: (t,u,v) with t,u,v>=2 and t*u*v - u - v = n. A := t*u-1 = (n+u)/v, A* := t*v-1 = (n+v)/u.
# sign s(w) := (A/n) = (uv/n) (Legendre/Jacobi), equal to (A*/n) since A*A ≡ 1 (mod n)... (checked numerically)
import math, sys
from fractions import Fraction
import numpy as np
def words(n, tmin=2):
    out=[]
    for u in range(2, n+2):
        if u*u>n*4 and u>2: pass
        for v in range(2, n+2):
            if u*v*tmin - u - v > n: 
                if v*u*tmin > n+u+v: break
                continue
            s=n+u+v
            if s % (u*v)==0:
                t=s//(u*v)
                if t>=tmin: out.append((t,u,v))
    return out
def leg(a,n):
    # Jacobi symbol (a/n), n odd positive
    a%=n; res=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): res=-res
        a,n=n,a
        if a%4==3 and n%4==3: res=-res
        a%=n
    return res if n==1 else 0
def v2(x):
    e=0
    while x%2==0: x//=2; e+=1
    return e
def ordv2(a,p):
    # v2 of multiplicative order of a mod prime p
    m=p-1
    x=pow(a,m>>v2(m),p)  # odd part removed
    j=0
    while x!=1:
        x=x*x%p; j+=1
    return j
def stern(x: Fraction):
    # Minkowski ?(x) for rational x in [0,1]
    if x<=0 or x>=1:
        return Fraction(0) if x<=0 else Fraction(1)
    # continued fraction
    cf=[]; a,b=x.numerator,x.denominator
    while b:
        q=a//b; cf.append(q); a,b=b,a-q*b
    # ?(x) = 2*sum_{k} (-1)^k 2^{-(a1+..+ak)} ... use standard formula
    cf=cf
    if len(cf)==1: return Fraction(1,1)*0+Fraction(1,2)  # unreachable for 0<x<1 with a0=0
    # x=[0;a1,a2,...]
    a=cf[1:] if cf[0]==0 else cf
    s=Fraction(0); total=0
    for i,ai in enumerate(a):
        total+=ai
    # ?(x) = 2 * sum_{k=1}^{m} (-1)^{k+1} 2^{-(a1+...+ak)} + boundary correction (Minkowski)
    val=Fraction(0); acc=0
    for k,ak in enumerate(a):
        acc+=ak
        val+= Fraction((-1)**(k), 2**acc)
    # standard: ?(x)=2*sum_{k>=1}(-1)^{k+1} 2^{-(a1+..+ak)} for [0;a1,...,am]  (last term with am-1 convention)
    res=2*sum(Fraction((-1)**(k), 2**sum(a[:k+1])) for k in range(len(a)))
    return -res if False else res*(-1)*(-1)
primes=[p for p in range(5,1200) if all(p%d for d in range(2,int(p**0.5)+1))]
def run():
    # Z2871: identity (A/n)=(A*/n) and sign=(uv/n) for all words at primes 5<=p<1200
    bad=0; tot=0
    for p in primes:
        for (t,u,v) in words(p):
            A=t*u-1; As=t*v-1; tot+=1
            if p%4!=1: continue
            if leg(A,p)!=leg(As,p) or leg(A,p)!=leg(u*v,p): bad+=1
            assert A*As % p == 1 % p
    print("Z2871 words checked",tot,"identity violations",bad)
    # Z2803: v2(ord_p A) vs v2(p-1) on words, p ≡ 1 mod 8
    cnt_full=0; cnt_words=0; p_with=0; p_tot=0
    for p in primes:
        if p%8!=1: continue
        p_tot+=1; ws=words(p); full=False
        for (t,u,v) in ws:
            A=(t*u-1)%p
            cnt_words+=1
            if ordv2(A,p)==v2(p-1): cnt_full+=1; full=True
        p_with+= full
    print(f"Z2803 p≡1(8) primes {p_tot}: primes with some word A full-2-order {p_with}; words {cnt_words}, fraction full {cnt_full/cnt_words:.3f}")
    # Z2817: signed count N+ - N- over words per prime
    diffs=[]
    for p in primes:
        if p%4!=1 or p<50: continue
        ws=words(p)
        s=sum(leg(u*v,p) for (t,u,v) in ws)
        diffs.append((p,len(ws),s))
    print("Z2817 sample (p, #words, N+-N-):", diffs[:12])
    # Z2839: Minkowski ?(A/p) for words at p ≡ 1 mod 8: QR vs QNR classes of A
    qr=[];qnr=[]
    for p in primes:
        if p%8!=1 or p<100: continue
        for (t,u,v) in words(p):
            A=(t*u-1)%p
            if A==0: continue
            x=Fraction(A,p)
            val=stern(x)
            (qr if leg(A,p)==1 else qnr).append(float(val))
    if qr and qnr:
        print(f"Z2839: ?(A/p) mean QR {np.mean(qr):.4f} (n={len(qr)}), QNR {np.mean(qnr):.4f} (n={len(qnr)}); dyadic denominators check: sample ",[str(stern(Fraction(a,11))) for a in range(1,6)])
run()
