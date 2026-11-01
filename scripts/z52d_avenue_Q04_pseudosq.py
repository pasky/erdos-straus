"""z52d avenue Q04 Z0762: R(n) (ordered (u,B,C), 4uBC-u-B=n) at Lehmer pseudosquares vs nearby n = 1 (8) non-squares.
EVIDENCE only. Pseudosquare list = OEIS A002189 (first terms)."""
import numpy as np, math, random, sys
def R(n):
    tot=0; u=1
    while 4*u-u-1<=n:
        Bmax=(n+u)//(4*u-1)+1
        B=np.arange(1,Bmax+1,dtype=np.int64)
        num=n+u+B; den=4*u*B
        ok=(num%den==0)&(num//den>=1)
        tot+=int(ok.sum()); u+=1
        if 4*u-1>n+u: break
    return tot
ps=[73,241,1009,2641,8089,18001,53881,87481,117049,515761,1083289,3206641]
random.seed(1)
for n in ps:
    r=R(n)
    ctrl=[]
    m=n
    while len(ctrl)<8:
        m+=8
        if math.isqrt(m)**2!=m: ctrl.append(R(m))
    L=math.log(n)
    print(n, 'R=',r, ' ctrl mean=%.1f min=%d'%(np.mean(ctrl),min(ctrl)), ' R/L^2=%.3f ctrl/L^2=%.3f'%(r/L/L,np.mean(ctrl)/L/L), flush=True)
