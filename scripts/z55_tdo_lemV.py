# z55 TDO: numeric check of Lemma V: sup_theta |S_m(theta)| / sqrt(hU), S_m(theta)=sum_{r in (2U,4U], r^2-4m>=1} e(h sqrt(r^2-4m) - theta r)
import numpy as np, sys
rng=np.random.default_rng(1)
out=[]
for U in [20,50,100,200,400]:
    worst=0
    for h in [1,2,3,5,8]:
        for m in rng.integers(U*U+1,4*U*U+1,size=12):
            r=np.arange(2*U+1,4*U+1); r=r[r*r-4*m>=1]
            if len(r)==0: continue
            ph=h*np.sqrt((r*r-4*m).astype(float))
            th=np.linspace(0,1,4096,endpoint=False)
            # S(theta) for all theta via exp matrix in chunks
            best=0
            for c in range(0,len(th),512):
                M=np.exp(2j*np.pi*(ph[None,:]-th[c:c+512,None]*r[None,:]))
                best=max(best,np.abs(M.sum(1)).max())
            worst=max(worst,best/np.sqrt(h*U))
    out.append((U,worst)); print(U,round(worst,3),flush=True)
