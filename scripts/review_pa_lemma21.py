"""R265 from-scratch check of PARITY_AUDIT Lemma 2.1: |R|, M(p), R(p), U-version."""
import math, numpy as np, sys
def R_div(p):
    # R(p) = #{(u,f): f | p+u, f = -1 mod 4u}  (all u)
    c=0
    for u in range(1,(p+1)//3+1):
        n=p+u; m=4*u
        # f = m*C-1 <= n
        f=np.arange(m-1,n+1,m,dtype=np.int64)
        c+=int(np.count_nonzero(n%f==0))
    return c
def RM(p,U=None):
    Umax=(p+1)//3 if U is None else min(U,(p+1)//3)
    size=0;M=0.0
    for u in range(1,Umax+1):
        X=(p+u+1)//(4*u)
        C=np.arange(1,X+1,dtype=np.float64)
        size+=X; M+=float(np.sum(1.0/(4*u*C-1)))
    return size,M
for p in (10007,100003,1000003,10000019):
    L=math.log(p); s,M=RM(p)
    r=R_div(p) if p<2_000_000 else None
    print(p,"|R|/(p/4 log p)=%.3f"%(s/(p/4*L)),"|R|-(p/4)log p=%.3f p"%((s-p/4*L)/p),"M=%.3f"%M,"L^2/8=%.3f"%(L*L/8),"M-L^2/8=%.3f (L=%.2f)"%(M-L*L/8,L),"R=",r)
    for U in (10,100):
        s,MU=RM(p,U); lu=math.log(U)
        print("   U=%d |R_U|/(p/4 logU)=%.3f M_U=%.3f formula=%.3f"%(U,s/(p/4*lu),MU,lu*L/4-lu*lu/8))
