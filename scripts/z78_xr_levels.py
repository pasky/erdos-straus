import z78_deep as Z
from z78_deep import *
r=929
# instrument: replicate loop printing per-level choice
parts=budget2(r)
lv0=F(r-1,2*r)-sum(parts[:4])
lv=lv0
print('alive after P5 (author)',float(lv*10**6))
for k in range(7,801,2):
    n=r**k;b=n.bit_length()
    if b>800:break
    D=(k+1)//2;W=r**D
    old=F(bound(P,n),W)
    splits=[]
    if b in layers:
        cut,v=layers[b];splits=[(1<<(cut+i),packed(1<<b,cut+i),c) for i,c in enumerate(v)]
    splits+=local.get((r,k),[])
    if k==7 and r in p7:
        splits=[(E,min(s,p7[r][E.bit_length()-1]) if E.bit_length()-1<len(p7[r]) else s,c) for E,s,c in splits]
    N=n;best=(lv-old,'table');
    for E,s,c in splits:
        T=(N//E+1)//2; per=2*ceildiv(T,W//r)
        for val,tag in ((lv-F(s+c,W),'sc'),(lv*(1-F(min(per,r),r))-F(s,W),'per')):
            if val>best[0]:best=(val,f'{tag} E=2^{E.bit_length()-1} s={s} c={c} per={per}')
    x=max(F(0),best[0]);loss=lv-x
    if loss*10**6>=1: print(k,b,'loss_ppm',round(float(loss*10**6),1),'table_ppm',round(float(old*10**6),1),best[1])
    lv=x
