# z53 HCHYP: model prediction of X*(p) = least X with S(X) = sum_{x in C, x<=X} 2*P_x >= log p,
# P_x = c * E[min(1,(2^k-1)/phi(x))], k ~ Poisson(log log p) (Theorem M bracket: c in [1/2,1]).
# Prints X*, X*/log p and the local exponent d log X*/d log log p; asymptotically -> 2 log 2 = 1.386.
import math
from z53_hchyp_model import phi
def Ufun(lam,n):
    # E[min(1,(2^k-1)/n)] with k ~ Poisson(lam), computed stably
    s=0.0; logp=-lam
    for k in range(0,int(lam*12+60)):
        if k>0: logp+=math.log(lam)-math.log(k)
        s+=math.exp(logp)*min(1.0,(2.0**k-1)/n) if k<1000 else 0
    return s
C=[x for x in range(4,10**7) if x%4==0 or x%8==7]
PHI={}
def xstar(L,c):
    lam=math.log(L); S=0.0
    for x in C:
        if x not in PHI: PHI[x]=phi(x)
        S+=2*c*Ufun(lam,PHI[x])
        if S>=L: return x
    return None
for c in (1.0,0.5):
    prev=None
    print(f"c={c}")
    for L in [18.4,27.6,50,100,200,400,800,1600]:
        x=xstar(L,c)
        loc= (math.log(x/prev[1])/math.log(L/prev[0])) if prev else float('nan')
        print(f"  log p={L:7.1f}  X*={x:8d}  X*/logp={x/L:6.2f}  local exponent={loc:.3f}")
        prev=(L,x)
