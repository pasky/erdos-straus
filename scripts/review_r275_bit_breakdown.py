import numpy as np, collections
from math import isqrt
PB=200000
B=collections.defaultdict(lambda:[0,0])
for p in range(5,PB+1,8):
    if not all(p%r for r in range(3,isqrt(p)+1,2)): continue
    m=np.arange(1,(p+1)//3+2,dtype=np.int64); g=(-p)%(4*m)
    ok=(g>0)&((m+1)%np.where(g>0,g,1)==0)
    for mm,gg in zip(m[ok].tolist(),g[ok].tolist()):
        d=(p+gg)//(4*mm); c=(mm+1)//gg; w=4*c*d-1
        assert (w*mm-1)%p==0 and (w*mm-1)//p==c
        t=pow(2*w,(p-1)//4,p)==1
        key=('m=2' if mm==2 else 'm<=100' if mm<=100 else 'd<=40' if d<=40 else 'mid')
        B[key][0 if t else 1]+=1
        B['c=%s'%min(c,4)][0 if t else 1]+=1
for k,(a,b) in sorted(B.items()): print(k,a,b,'%.2f%%'%(100*a/(a+b)),'z=%.1f'%((a-b)/(a+b)**.5))
