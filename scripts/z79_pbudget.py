"""Integer certificate for long shifts: split off all b/a<=H by w=c*c*d.
The remaining 1-4t list has about half the former length for large H.
At the certified primes the determinant rather than this split wins.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from functools import lru_cache
from z78_r2ledger import (small,ex7,ss7,spbig,local,layers,sh,globalP,scale,
    qnorm,geom,Q,qLocal,ceildiv,ppm,rootup)
from z77_bound import tau_major
from z78_qcap import qlarge
base=Path('data/z79');fine={(r,k):(j,cs) for f in (base/'layer').glob('*.txt') for line in f.read_text().splitlines() for r,k,j,*cs in [list(map(int,line.split()))]}
for file in (base/'p7new').glob('[0-9]*.txt'):
    r,count=map(int,file.read_text().split());ex7[r]=count
for l in (base/'q5shift.txt').read_text().splitlines():
    r,e0,e1,f0,f1=map(int,l.split());n=r**5;t=rootup(n,3)**2
    v=min(e+2*f+qlarge(n,t<<j,t<<i) for j,e in enumerate([e0,e1]) for i,f in enumerate([f0,f1]))
    qLocal[r]=min(qLocal.get(r,n),v)
low={int(l.split()[0]):list(map(int,l.split()[1:])) for l in (base/'low/rows.txt').read_text().splitlines() if l[0].isdigit()}
@lru_cache(None)
def tau(V):
    return min(ceildiv(rootup(V,k)*v,u) for k in range(3,13) for _,v,u in [tau_major(k)])

def cost(r,k,live):
    n=r**k; W=r**((k+1)//2);b=n.bit_length()
    ans=min(live,globalP(n)/isqrt(r));tag='global'
    if k==7 and r in ex7 and F(ex7[r],W)<ans:ans,tag=F(ex7[r],W),'exact'
    sp={}
    for N,grid in [(1<<b,layers.get(b)),(n,local.get((r,k))),(n,fine.get((r,k)))]:
        if grid:
            j,cs=grid
            for i,c in enumerate(cs):
                E=1<<(j+i);s=sh(N,j+i)
                if E in sp:s=min(s,sp[E][0]);c=min(c,sp[E][1])
                sp[E]=s,c
    for E,s in ([(r**3<<j,s) for j,s in enumerate(ss7.get(r,[]))] if k==7 else [])+[(1<<j,s) for j,s in enumerate(spbig.get((r,k),[]))]:
        sp[E]=min(sp.get(E,(W,W))[0],s),min([W]+[c for t,(_,c) in sp.items() if t<=E])
    for E,(s,c) in sp.items():
        if F(s,W)>=ans:continue
        y=F(s+c,W)
        if y<ans:ans,tag=y,'det'
        for H in (1,8,64,512,4096):
            w=(n+E)*(H+1)**2//(4*H*E**2)
            # both oriented keys are positive divisors of 4wn+1
            cbal=w*tau(4*w*n+1) if H>1 and w else 0
            T=(n+E)*(H+1)//(4*E*H)
            # All live parents at previous depth; inverse pairing used globally
            y=F(s+cbal,W)+live*min(F(1),F(2*ceildiv(T,W//r),r))
            if y<ans:ans,tag=y,f'split:{E}:{H}'
    return ans,tag

def row(r):
    A,B,C,D=small[r];init=F((r-1)//2-A,r)-F(B,r*r)-F(C+D,r**3);live=init;parts=[];tags=[]
    for k in range(7,2001,2):
        n=r**k
        if n>=1<<320:
            g,_=scale[320];assert all(gg*320>=bb*g for bb,(gg,_) in scale.items() if 1<<bb<=n)
            pt=globalP(n)*geom(r,g,320)/isqrt(r);break
        p,tag=cost(r,k,live)
        if r in low and k in (7,9):
            p7,p9,q5,over,alive5=low[r];p=F(p7,r**4) if k==7 else F(p9+q5-over,r**5);tag='exact-union';assert k==7 or live-p==F(alive5,r**5)
        live-=p;parts.append(p);tags.append(tag)
    q=0
    for k in range(5,1000,2):
        f=r**k;b=f.bit_length()
        if b>=80:qt=qnorm(f)*geom(r,1,4);break
        if not(k==5 and r in low):q+=min(F(1),F(Q.get(b,f),f),F(qLocal.get(r,f),f) if k==5 else F(1))
    return init,parts,tags,q,pt,qt
if __name__=='__main__':
    import sys
    for r in (map(int,sys.argv[1:]) if sys.argv[1:] else sorted(r for r in small if 17<=r<=283)):
        x,p,t,q,pt,qt=row(r);margin=x-sum(p)-q-pt-qt
        print(r,x,*(ppm(z) for z in [p[0],p[1],sum(p[2:]),q,pt,qt]),margin*1000000//1,*t[:3],flush=True)
