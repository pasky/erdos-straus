"""z52d avenue Q05 Z1510: is the parity of R(p)/2 ((★) solution count up to the u<->B symmetry) governed by simple
symbols? Primes p = 1 (4) <= N, R from scripts/z52b_p1_H04_rstar.c (uint16 array). EVIDENCE only."""
import numpy as np, sys
R=np.fromfile(sys.argv[1],dtype=np.uint16); N=len(R)-1
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
p=np.nonzero(s)[0]; p=p[(p%4==1)&(p>100)]
r=R[p].astype(np.int64)
print('all R even:', bool(np.all(r%2==0)))
h=(r//2)%2
print('P(R/2 odd) overall: %.4f  (n=%d)'%(h.mean(),len(p)))
def leg(a,p): return np.where(pow_mod(a,(p-1)//2,p)==1,1,-1)
def pow_mod(a,e,m):
    res=np.ones_like(m); b=np.full_like(m,a)%m; e=e.copy()
    while np.any(e>0):
        odd=(e&1)==1; res=np.where(odd,(res*b)%m,res); b=(b*b)%m; e>>=1
    return res
for name,mask in [('p=1(8)',p%8==1),('p=5(8)',p%8==5),('p=1(16)',p%16==1),('p=9(16)',p%16==9),('p=1(24)',p%24==1),
                  ('(3/p)=1',leg(3,p)==1),('(3/p)=-1',leg(3,p)==-1),('(5/p)=1',leg(5,p)==1),('(5/p)=-1',leg(5,p)==-1),
                  ('(7/p)=1',leg(7,p)==1),('(7/p)=-1',leg(7,p)==-1),('2 quartic res (p=1(8))',(p%8==1)&(pow_mod(2,(p-1)//4,p)==1)),
                  ('2 not quartic (p=1(8))',(p%8==1)&(pow_mod(2,(p-1)//4,p)!=1))]:
    print('%-26s P(R/2 odd)=%.4f n=%d'%(name,h[mask].mean(),mask.sum()))
