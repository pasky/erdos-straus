import numpy as np, collections
from math import isqrt
PB=200000
B=collections.defaultdict(lambda:[0,0])
for p in range(5,PB+1,8):
    if not all(p%r for r in range(3,isqrt(p)+1,2)): continue
    for mm in range(3,101):
        gg=(-p)%(4*mm)
        if gg and (mm+1)%gg==0:
            d=(p+gg)//(4*mm); c=(mm+1)//gg; w=4*c*d-1
            t=pow(2*w,(p-1)//4,p)==1
            B[mm][0 if t else 1]+=1
for k,(a,b) in sorted(B.items()):
    if a+b>100: print(k,a,b,'%.1f%%'%(100*a/(a+b)),'z=%.1f'%((a-b)/(a+b)**.5))
