"""Round 2. No SE/ZL libm count/table as input to the new finite-range test.
Inputs: native exact sets L1/P3/Q3/P5, integer z77/z78 arithmetic. Count
P7 first on union of WHOLE depth-3 live parents; Q>=5 subtracted en bloc."""
from z78_pack import packed
from z78_r2tail import coef
from z78_r2qtail import qnorm,geom
from z76_lift import ceildiv,rootup
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
from pathlib import Path
Z=Path('data/z78');R=Z/'r2'
def rows(p):return [list(map(int,s.split())) for s in p.read_text().splitlines()]
def cat(p):return [v for f in p.glob('*.txt') for v in rows(f)]
scale={v[0]:(v[2],coef(v)) for v in rows(R/'scale.txt')}
layers={n.bit_length()-1:(c,v) for n,c,*v in cat(Z/'layer')+cat(R/'layer')};Q=dict(cat(R/'q'))
ss7={r:v for r,*v in cat(R/'p7')};s7base={r:v for r,*v in cat(Z/'p7')}
spbig={}
for r,k,*v in cat(R/'p9'):
    old=spbig.setdefault((r,k),[])
    for i,x in enumerate(v):
        if i<len(old):old[i]=min(old[i],x)
        else:old.append(x)
@lru_cache(None)
def sh(n,j):return packed(n,j)
small={r:(a//r**2,b//r,c,d) for r,a,b,c,d in [list(map(int,s.split())) for s in (Z/'exact/union.tsv').read_text().splitlines()[1:]]}
local={(r,k):(j,v) for r,k,j,*v in cat(R/'local')}
ex7={r:c for r,E,d,h,c in cat(R/'exact7')};qLocal=dict(cat(R/'qLocal'))
if (R/'qSpecial/bound.txt').exists():
    for r,z in rows(R/'qSpecial/bound.txt'):qLocal[r]=min(qLocal.get(r,z),z)
cf7={r:(E,c) for r,E,T,c,dep,raw in cat(R/'cfrows')}
if (Z/'r2exact'/'rows.tsv').exists():
    for l in (Z/'r2exact'/'rows.tsv').read_text().splitlines():
        if l and l[0].isdigit():r,*v=map(int,l.split());small[r]=tuple(v)

def ppm(x):return ceildiv(x.numerator*1000000,x.denominator)
def lowerexp(x,k,N):return F(x,rootup(N,k)-1) if N>1 else F(x)
@lru_cache(None)
def globalP(n):
    return min([F(1<<1000)]+[a*F(1<<(20+g),max(1,rootup((n**g)<<(20*B),B)-1)) for B,(g,a) in scale.items() if n>=1<<B])

def budget(r):
    A,B,C,D=small[r];initial=F((r-1)//2-A,r)-F(B,r*r)-F(C+D,r**3)
    lv=initial;p=[];q=F(0);charges=[]
    for k in range(7,2000,2):
        n=r**k;b=n.bit_length();depth=(k+1)//2;W=r**depth
        if n>=1<<320:
            G,A=scale[320];pt=globalP(n)*geom(r,G,320)/isqrt(r);break
        # simple cap: one unit of mass when there is no better input
        old=min(F(1),globalP(n)/isqrt(r));sp=[]
        if b in layers:
            j,cs=layers[b];sp=[(1<<(j+i),sh(1<<b,j+i),c) for i,c in enumerate(cs)]
        if (r,k) in local:
            j,cs=local[r,k];sp.extend((1<<(j+i),sh(n,j+i),c) for i,c in enumerate(cs))
        if k==7 and r in ex7:old=min(old,F(ex7[r],W))
        if (r,k) in spbig:
            sums=spbig[r,k];sp=[(E,min(s,sums[E.bit_length()-1]) if E.bit_length()<=len(sums) else s,c) for E,s,c in sp]
        if k==7 and r in s7base:
            sp=[(E,min(s,s7base[r][E.bit_length()-1]) if E.bit_length()<=len(s7base[r]) else s,c) for E,s,c in sp]
        if k==7 and r in ss7:
            for j,s in enumerate(ss7[r]):
                E=r**3<<j; c0=min([W]+[c for t,_,c in sp if t<=E]);
                if r in cf7 and E>=cf7[r][0]:c0=min(c0,cf7[r][1])
                sp.append((E,s,c0))
        # Extend even if bound currently fails: compute independent nonnegative
        # cost for each remaining level, not a zero loss after live mass gone.
        cost=old
        for E,s,c in sp:
            T=(n//E+1)//2;per=2*ceildiv(T,W//r)
            cost=min(cost,F(s+c,W),F(s,W)+min(F(1),F(per,r))*max(F(0),lv)) if lv>0 else min(cost,F(s+c,W))
        p.append(cost);lv-=cost
    for k in range(5,1000,2):
        f=r**k;b=f.bit_length()
        if b>=80:qt=qnorm(f)*geom(r,1,4);break
        q+=min(F(1),F(Q.get(b,f),f),F(qLocal[r],f) if k==5 and r in qLocal else F(1))
    return initial,p,q,pt,qt
if __name__=='__main__':
    import sys
    for r in sorted(small) if len(sys.argv)==1 else map(int,sys.argv[1:]):
        if r<17 or r>=919:continue
        a,p,q,t,u=budget(r);res=sum(p)+q+t+u
        print(r,a,ppm(a),ppm(p[0]),ppm(p[1]),ppm(sum(p[2:])),ppm(q),ppm(t+u),ppm(res),int(res<a),flush=True)
