"""Z2025: dispersion of D_C(p) = #{d | 4Cp+1 : d ≡ -1 (mod 4C)} over C <= X at fixed p.
E_C = 2*tau3(N)/phi(4C), tau3 = #{d | N : d ≡ 3 (mod 4)} (genus-corrected uniform model).
Reports X, R_X = sum D, M_X = sum E, Disp = sum (D-E)^2, and the Cauchy–Schwarz ratio X*Disp/M_X^2 (need << 1)."""
import sys, math
from sympy import factorint, totient
from itertools import product
def divisors_from(f):
    ps=list(f.items()); ds=[1]
    for q,e in ps: ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def run(p, Xs):
    Xmax=max(Xs); R=M=Disp=0.0; out=[]; Ds=[]
    for C in range(1,Xmax+1):
        N=4*C*p+1; ds=divisors_from(factorint(N)); m=4*C
        D=sum(1 for d in ds if d%m==m-1); t3=sum(1 for d in ds if d%4==3)
        E=2*t3/int(totient(m)); R+=D; M+=E; Disp+=(D-E)**2; Ds.append(D)
        if C in Xs: out.append((C,R,round(M,2),round(Disp,2),round(C*Disp/M**2,2) if M else None, sum(1 for x in Ds if x>0)))
    return out
for p in map(int, sys.argv[1:]):
    print('p=',p,'log p=%.1f'%math.log(p))
    for row in run(p,[10,30,100,300,1000,3000,10000]): print('  X=%d R_X=%d M_X=%s Disp=%s X*Disp/M^2=%s #C with D>0=%d'%row)
