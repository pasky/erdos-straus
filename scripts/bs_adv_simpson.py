"""O154(b): re-check of O142 truncated L(1,chi_p) correlation by residue class mod 24 (Simpson effect). Input /tmp/fII_1e8.bin."""
import numpy as np
A=np.fromfile('/tmp/fII_1e8.bin',dtype=np.uint32).reshape(-1,3).astype(np.int64)
p,f=A[:,0],A[:,1].astype(float); m=(p>=2**20)&(p<=3*10**7); p,f=p[m],f[m]
k=np.floor(np.log2(p)).astype(int)
def resid(x,Q):
    out=np.zeros(len(x))
    for kk in np.unique(k):
        mm=k==kk; u,inv,c=np.unique(p[mm]%Q,return_inverse=True,return_counts=True); out[mm]=x[mm]-(np.bincount(inv,weights=x[mm])/c)[inv]
    return out
def primes_upto(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]
logL=np.zeros(len(p))
for l in primes_upto(300):
    l=int(l)
    if l==2: chi=np.where((p%8==1)|(p%8==7),1.0,-1.0)
    else:
        qr=np.zeros(l,bool); qr[(np.arange(1,l)**2)%l]=True; leg=np.where(qr[p%l],1.0,-1.0)
        sign=np.where(((l-1)//2)*((p-1)//2)%2==1,-1.0,1.0); chi=leg*sign
    logL+=-np.log1p(-chi/l)
x=np.log(f)
print('all classes: within mod-24 cells', np.corrcoef(resid(x,24),resid(logL,24))[0,1])
for r in (1,13,5,7,11,17,19,23):
    mm=p%24==r; print('p=%d mod 24: corr'%r, np.corrcoef(resid(x,24)[mm],resid(logL,24)[mm])[0,1])
