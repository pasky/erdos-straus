import math, random
from sympy import isprime, sqrt_mod
bad=0;cnt=0
for p in [13,17,29,37,41,53,193,2521]:
    for k in range(1,6):
        N=4*k*k*p+1
        for g in range(3,N+1,4):
            if N%g or (g+1)%(4*k): continue
            rho=pow(2*k,-1,g); assert (rho*rho+p)%g==0
            s=(2*k*rho-1)//g; m=N//g
            z=complex(-rho,math.sqrt(p))/g
            w=(g*z+rho)/(-2*k*z-s)
            w2=complex(-2*k*p,math.sqrt(p))/m
            cnt+=1
            if abs(w-w2)>1e-9*max(1,abs(w2)): bad+=1
print(cnt,bad)
