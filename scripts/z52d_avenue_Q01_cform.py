# z52d avenue Q01: Z1630 (square-multiple closure of (★)-zeros), Z1605 (c=2,d=1 line at the 14 (★) zeros), Z1606 (least e-slice)
# run: uv run --with sympy --with numpy python scripts/z52d_avenue_Q01_cform.py
import numpy as np, math
N=10**5
hit=np.zeros(N+1,dtype=bool)
u=1
while 4*u-u-1<=N:
    B=1
    while 4*u*B-u-B<=N:
        s=4*u*B-u-B
        hit[s::4*u*B]=True
        B+=1
    u+=1
odd=[n for n in range(5,N+1,4) if not hit[n]]
sq=lambda n: math.isqrt(n)**2==n
ns=[n for n in odd if not sq(n)]
print("C-form zeros n≡1(4) ≤1e5 non-square:",len(ns), ns[:60])
# closure under odd square multiples
bad=[(n,m) for n in ns for m in (3,5,7) if n*m*m<=N and math.gcd(n,m)==1 and hit[n*m*m]]
print("square-multiple closure violations (n,m) with n*m^2 having solution:",bad[:20], len(bad))
print("409*9 hit?",hit[409*9], "409*25",hit[409*25], "577*9",hit[577*9])

import math
from sympy import divisors
# Z1605: smallest c such that cp has C-form cert with C=cd (Type II with parameter c)
# Z1606: smallest e-slice e (Type II: N=(p+e)/4; Type I: N=(pe+1)/4) with -1 in {a/b mod e: ab|N}
def typeii_c(p,cmax=20,dmax=2000):
    for c in range(1,cmax+1):
        for d in range(1,dmax+1):
            M=4*c*c*d*p+1; m=4*c*d
            for f in divisors(M):
                if f*f>M: break
                if f%m==m-1 and (M//f)%m==m-1: return c,d,f
    return None
def eslice(p,emax=400):
    out={}
    for typ in ('II','I'):
        for e in range(3,emax,4):  # e ≡ -p ≡ 3 mod 4
            N=(p+e)//4 if typ=='II' else (p*e+1)//4
            if typ=='II' and (p+e)%4: continue
            if typ=='I' and (p*e+1)%4: continue
            ds=divisors(N); ok=False
            for a in ds:
                if math.gcd(a,e)!=1: continue
                for b in ds:
                    if (N//a)%b==0 and math.gcd(b,e)==1 and (a+b)%e==0: ok=True;break
                if ok: break
            if ok: out[typ]=e;break
    return out
for p in [409,577,5569,9601,23929]:
    print(p, typeii_c(p), eslice(p))

for p in [409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]:
    M=16*p+1; print("c=2,d=1", p, [f for f in divisors(M) if f*f<M and f%8==7 and (M//f)%8==7][:3])
