# z52d Pass 2 NC0, item Z0651 — are the record-setters near-squares (p = m² + k with small k)? Normalised distance k/(2√p) for the
# record primes vs the hard-class population in [5e7, 5.01e7).
from math import isqrt
import numpy as np, statistics as st
def k(p):
    m=isqrt(p); return min(p-m*m,(m+1)*(m+1)-p)
recs=[(53049049,2814),(393858721,3092),(486915361,2451),(596814241,2044),(172652089,1810),(201760441,1774)]
for p,s in recs: print(p,'s=',s,'k=',k(p),'k/(2sqrt p)=',round(k(p)/(2*p**0.5),3))
L,H=50000000,50100000
sv=np.ones(H-L,bool); r=int(H**0.5)+2
base=np.ones(r+1,bool); base[:2]=False
for i in range(2,int(r**0.5)+1):
    if base[i]: base[i*i::i]=False
for q in np.nonzero(base)[0]:
    q=int(q); s0=max(q*q,((L+q-1)//q)*q); sv[s0-L::q]=False
idx=np.arange(L,H); pr=idx[sv&(idx>1)]
hard=pr[np.isin(pr%840,[1,121,169,289,361,529])]
vals=[k(int(p))/(2*int(p)**0.5) for p in hard]
print('hard primes in [5e7,5.01e7):',len(hard),' median k/(2sqrt p)=',round(st.median(vals),3),' fraction <0.05:',round(sum(v<0.05 for v in vals)/len(vals),3))
