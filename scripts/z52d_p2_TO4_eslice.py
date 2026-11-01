# z52d pass2 TO4 (Z1606): e-slice test literal: for e ≡ -p (mod 4), e ≥ 1, N=(p+e)/4 (Type II) — exists a,b ≥1 with
# ab | N, gcd(b,e)=1, and a*b^{-1} ≡ -1 (mod e).   Compare with C-form (sufficient, proved) on p ≤ PM.
import sys, math
from sympy import primerange, divisors
PM=int(sys.argv[1]); E=int(sys.argv[2])
def eslice(p, E):
    for e in range(1, E+1):
        if (e+p)%4: continue
        N=(p+e)//4
        if N<1 or e<2: continue
        if math.gcd(N,e)==0: continue
        dv=divisors(N)
        for a in dv:
            for b in dv:
                if (a*b)%1==0 and N % (a*b)==0 and math.gcd(b,e)==1:
                    if (a*pow(b,-1,e)-(-1))%e==0 and e>1:
                        return e
    return None
def cform(p):
    from sympy import factorint
    for C in range(1,400):
        N=4*C*p+1; m=4*C; f=factorint(N); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        if any(a>1 and a%m==m-1 for a in divs): return C
    return None
out=[]
for p in [193,409,577,2521]:
    out.append((p,'e_min(II)=',eslice(p,E),'cform C_min=',cform(p)))
for p,a,b,c,d in out: print(p,a,b,c,d)
agree=0; dis=[]
ps=[p for p in primerange(5,PM) if p%4==1][:120]
for p in ps:
    e=eslice(p,E); c=cform(p)
    if (e is not None)==(c is not None): agree+=1
    else: dis.append((p,e,c))
print("agree",agree,"of",len(ps),"disagreements (p,e_min,C_min):",dis[:10])
