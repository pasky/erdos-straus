"""Z52D_HYPERBOLA.md Cor 4 illustration (EVIDENCE): relative class spread of the pair-product model M_q(r) on the sharp block
(U,2U]^2 for q = 7, 16 and U = 50, 200, 800.  Usage: uv run --with numpy python scripts/z52d_hyperbola_cor4check.py"""
import numpy as np
from math import gcd
def phi_table(N):
    ph=np.arange(N+1); 
    for i in range(2,N+1):
        if ph[i]==i: ph[i::i]-=ph[i::i]//i
    return ph
for q in (7,16):
  for U in (50,200,800):
    ph=phi_table(2*U+1)
    u=np.arange(U+1,2*U+1); UU,BB=np.meshgrid(u,u,indexing='ij')
    g=np.gcd(UU,BB); adm=(g==1)&((UU+BB)%2==1)
    w=np.where(adm,1.0/(4.0*ph[UU]*ph[BB]),0.0)
    G=np.gcd(4*UU*BB,q); phG=np.vectorize(lambda x:int(phi_table(q)[x]))(G)
    res=[]
    for r in range(1,q):
        if gcd(r,q)!=1: continue
        res.append(float((w*phG*((r+UU+BB)%G==0)).sum()))
    res=np.array(res); print(q,U,np.round(res/res.mean(),4), 'spread',round(float(res.max()/res.min()-1),4))
