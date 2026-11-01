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

# All products of subsets of the symbols below (reviewer: balanced marginals do not exclude product laws).
import itertools
syms={'(2/p)':leg(2,p),'(3/p)':leg(3,p),'(5/p)':leg(5,p),'(7/p)':leg(7,p),'(11/p)':leg(11,p),'(13/p)':leg(13,p),
      '(2/p)4':np.where(p%8==1,np.where(pow_mod(2,(p-1)//4,p)==1,1,-1),1),'(-1/p)4':np.where(p%8==1,1,-1)}
sgn=1-2*h  # +1 if R/2 even
names=list(syms); best=[]
for k in range(1,len(names)+1):
    for S in itertools.combinations(names,k):
        prod=np.ones(len(p),dtype=np.int64)
        for s_ in S: prod=prod*syms[s_]
        best.append((abs(np.mean(sgn*prod)),'*'.join(S)))
best.sort(reverse=True)
print('products tested:',len(best),' max |E[(-1)^(R/2) * product]| = %.4f (%s); 1/sqrt(n) = %.4f'%(best[0][0],best[0][1],1/np.sqrt(len(p))))
