# R104 from-scratch: sanity of Lemma harm2 (a),(b) — ratios should stay bounded.
import math
from sympy import totient, factorint, divisor_count
def phi_table(n):
    ph=list(range(n+1))
    for i in range(2,n+1):
        if ph[i]==i:
            for j in range(i,n+1,i): ph[j]-=ph[j]//i
    return ph
Y=600; ph=phi_table(2*Y+2)
for m in [4,6,30,210,2310,7]:
    S=0.0
    for e in range(1,2*Y+1):
        if math.gcd(e,m)!=1: continue
        for a in range(1,Y+1):
            if math.gcd(a,e)!=1: continue
            b0=(-a)%e or e
            for b in range(b0,Y+1,e):
                if math.gcd(a,b)==1: S+=1/(ph[a]*ph[b])
    L=math.log(Y); bound=(ph[m]/m if m<len(ph) else totient(m)/m)*L**3+L**2
    print("(a) m=%d Y=%d sum=%.2f  sum/bound=%.3f"%(m,Y,S,S/float(bound)))
def tau3(u): 
    f=factorint(u); r=1
    for v in f.values(): r*=(v+1)*(v+2)//2
    return r
for m in [4,10,101,1000]:
    U=4000 if m<1000 else 3000
    S=sum(tau3(u)/int(totient(m*u-1)) for u in range(1,U+1))
    print("(b) m=%d U=%d m*sum=%.2f  log^3U=%.1f  ratio=%.3f"%(m,U,m*S,math.log(U)**3,m*S/(math.log(U)**3+m**0.02)))
