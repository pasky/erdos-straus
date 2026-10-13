"""bsB_sterile_pretentious: correlate W(p) (Type I slice a=1, from bsB_wcount output) at primes p = 1 mod 4
with the truncated L(1, chi_p) = prod_{l<=y} (1 - (l/p)/l)^{-1} (pretentiousness of chi_p to 1).
usage: python bsB_pretend.py Wfile LO HI y"""
import sys, numpy as np, math
from sympy import primerange, legendre_symbol as L
W=np.fromfile(sys.argv[1],dtype=np.uint32); lo,hi,y=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
ls=list(primerange(3,y+1)); xs=[];ws=[]
for p in primerange(lo,hi):
    if p%4!=1: continue
    Lv=1/(1-1/2) if p%8==1 else 1/(1+1/2)        # (2/p)
    for l in ls: Lv*= 1/(1-L(p%l,l)/l) if p%l else 1
    xs.append(math.log(Lv)); ws.append(W[p]/math.log(p)**2)
xs=np.array(xs); ws=np.array(ws)
print("n=",len(xs),"corr(log L_y, W/log^2 p)=",round(np.corrcoef(xs,ws)[0,1],3))
q=np.quantile(xs,[0.1,0.9]); print("mean W/log^2: bottom decile L:",round(ws[xs<=q[0]].mean(),3)," top decile L:",round(ws[xs>=q[1]].mean(),3), " min W:",int((ws*np.log(np.arange(1)+1)).sum()) if 0 else "")
