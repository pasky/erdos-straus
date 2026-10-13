"""bsB_orthant_sign: the sign-blind set D*(n) of GI Prop 4.1 = integral points of ONE cubic
X_n: cfg - c - f = n, fg = 1 (mod 4), g >= 1, in the two orthants c,f >= 1 (class -1) and c,f <= -1 (class +1).
Check: (i) counts agree with D*(n) class counts; (ii) Jacobi((cg-1)/n) = sign(c) on X_n points (n = 1 mod 4).
usage: python bsB_orthant.py NMAX"""
import sys
from sympy import jacobi_symbol as J, divisors
N=int(sys.argv[1]); bad=0; tot=[0,0]
for n in range(5,N+1,4):
    pos=neg=0
    for g in range(1,n+3):
        for s in (1,-1):                       # s = sign of (c,f)
            # g n + 1 = (cg-1)(fg-1)  with c,f of sign s
            T=g*n+1
            for A in divisors(T):
                for sa in ((1,) if s==1 else (-1,)):
                    m2=A if s==1 else -A        # m'' = cg-1
                    m=T//m2
                    if (m2+1)%g or (m+1)%g: continue
                    c=(m2+1)//g; f=(m+1)//g
                    if c==0 or f==0 or (c>0)!=(s>0) or (f>0)!=(s>0): continue
                    if (f*g)%4!=1: continue
                    if J(m2%n,n)!=s*(-1): bad+=1       # (m''/n) = -sign(c)?  m''=cg-1
                    if s==1: pos+=1
                    else: neg+=1
    # D*(n) class counts
    cp=cm=0
    for t in range(3,n+3,4):
        T=t*n+1
        for m2 in divisors(T):
            if m2==1 or (T//m2)%4: continue
            if (m2-1)%t==0: cp+=1
            elif (m2+1)%t==0: cm+=1
    if (pos,neg)!=(cm,cp): bad+=1
    tot[0]+=pos; tot[1]+=neg
print(f"positive-orthant pts={tot[0]} negative-orthant pts={tot[1]} violations={bad}")
