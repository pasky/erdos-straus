# z52d_thinfamily_xcheck.py — cross-check of the k-loop of z52d_thinfamily_menuA.py (Thm 5) against direct divisor
# enumeration, c0 in {3, 15, 63, 255}, odd u < 400, p in {3,5,7}, N <= 10^30.  Usage: uv run --with cypari2 --with gmpy2 python scripts/z52d_thinfamily_xcheck.py
import sys, runpy
sys.argv=['x','15','1']
g=runpy.run_path('scripts/z52d_thinfamily_menuA.py')
from math import isqrt
import cypari2
pari=g['pari']
bad=0;tot=0
for c0 in (3,15,63,255):
    F=c0+1
    g['F']=F
    for u in range(1,400,2):
      for p in (3,5,7):
        c=c0*u**p-1; E=(c&-c).bit_length()-1; co=c>>E; N=F+c
        if N>10**30: continue
        direct=sorted((X,N//X) for X in (int(t) for t in pari.divisors(N)) if ((F+X)*(1+N//X))%co==0)
        # k-loop
        kl=[]; k=1
        while True:
            Q=2*F*(k+2**E)
            if k*k*co>Q+(Q*Q+1)//2 or k*co>F*N+2*F+1: break
            D=co*(k*k*co-4*F*(k+2**E))
            if D>=0:
                W=isqrt(D)
                if W*W==D:
                    for sg in (1,-1):
                        a2=k*co-2*F+sg*W; b2=k*co-2*F-sg*W
                        if a2>0 and a2%2==0 and b2>0 and b2%(2*F)==0:
                            X,Xp=a2//2,b2//(2*F)
                            if X*Xp==N: kl.append((X,Xp))
            k+=1
        tot+=1
        if sorted(set(kl))!=direct: bad+=1; print('MISMATCH',c0,u,p,direct,sorted(set(kl)))
print('checked',tot,'mismatches',bad)
