#!/usr/bin/env python3
"""z66 HSTARF §5: certify, for all Type II solutions with p <= PMAX, the necessary conditions
   (ab/p) = -1,  (q1/p) = -1 with q1 = 4acd-1,  (j*d/p) = -1 with j = (a+b)/c,
and tabulate R-(p) = #TypeII (a<=b) vs R+(p) = #{4abcd + a + b = p, a<=b} (the mirror class q = +1 mod 4ad).
usage: uv run scripts/z66_hstarf_jacobi.py PMAX"""
import sys
from sympy import primerange, jacobi_symbol
def type2(p):
    out=[]; a=1
    while 4*a*a<=p+2*a:
        d=1
        while 4*a*a*d<=p+2*a:
            n=4*a*d; N=4*a*a*d+p; q=n-1
            while q<=N:
                if N%q==0:
                    c=(q+1)//n; b=(a+p*c)//q; out.append((a,b,c,d))
                q+=n
            d+=1
        a+=1
    return out
def plus(p):  # 4abcd + a + b = p, a<=b
    out=[]; a=1
    while 4*a*a+2*a<=p:
        for m in range(1, (p-2*a)//(4*a)+1):   # m = cd
            if (p-a)%(4*a*m+1)==0:
                b=(p-a)//(4*a*m+1)
                if b>=a:
                    # count factorisations m = c*d
                    nf=sum(1 for c in range(1,m+1) if m%c==0)
                    out.append((a,b,m,nf))
        a+=1
    return out
pmax=int(sys.argv[1]); bad=0; tot=0; rows=[]
for p in primerange(5,pmax+1):
    if p%4!=1: continue
    T=type2(p); tot+=len(T)
    for (a,b,c,d) in T:
        assert 4*a*b*c*d==a+b+p*c
        j=(a+b)//c
        if jacobi_symbol(a*b,p)!=-1 or jacobi_symbol(4*a*c*d-1,p)!=-1 or jacobi_symbol(j*d,p)!=-1:
            bad+=1; print("VIOLATION",p,(a,b,c,d))
    P=plus(p); rows.append((p,len(T),sum(nf for *_,nf in P)))
print("solutions checked:",tot,"violations:",bad)
print("p, R-(p) [TypeII a<=b], R+(p) [4abcd+a+b=p, a<=b, weighted by #(c,d)]:")
for r in rows[:12]+rows[-6:]: print("  ",r)
import statistics
print("mean R-:",statistics.mean(r[1] for r in rows),"mean R+:",statistics.mean(r[2] for r in rows),"#p with R+=0:",sum(1 for r in rows if r[2]==0))
