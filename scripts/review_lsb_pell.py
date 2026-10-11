# R136 from-scratch: F2 claims. For each Type II quadruple (a,b,c,d) of p (4abcd=a+b+pc):
# (1) check T^2 - D'(2c)^2 = 1, T=2cd(a+b)-1, D'=d^2(a-b)^2+dp;  (2) is any power eps^k (k>=2) again the unit of
# ANY Type II quadruple of p (any c',d')? A unit is determined by T (U^2 D' = T^2-1), so compare T_k with the T-set.
# (3) log eps vs log p.
import math
from sympy import primerange
def quads(d,n):
    out=[]; a=1
    while 4*a*d-1<=n+a:
        for b in range(1,(n+a)//(4*a*d-1)+1):
            t=4*a*b*d-n
            if t>0 and (a+b)%t==0: out.append((a,b,(a+b)//t,d))
        a+=1
    return out
bad=0; hits=0; maxratio=0; nq=0
for p in primerange(5,1500):
    Q=[q for d in range(1,(p+3)//4+1) for q in quads(d,p)]
    Ts={}
    for (a,b,c,d) in Q:
        T=2*c*d*(a+b)-1; Dp=d*d*(a-b)**2+d*p
        if T*T-Dp*4*c*c!=1: bad+=1
        Ts[T]=(a,b,c,d)
    for T in Ts:
        Tk_1,Tk=1,T
        for k in range(2,6):
            Tk_1,Tk=Tk,2*T*Tk-Tk_1
            if Tk in Ts: hits+=1; print("power hit",p,Ts[T],k,Ts[Tk])
        maxratio=max(maxratio, math.log(2*T)/math.log(p)); nq+=1
print("quadruples",nq,"identity failures",bad,"power hits (k=2..5)",hits,"max log(2T)/log p",round(maxratio,3))
