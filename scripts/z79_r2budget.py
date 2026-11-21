"""Inject round-2 envelope rows into the R1 union/conditional ledger. All costs exact."""
from z79_pbudget import *
from z78_pack import interval,fixed,tsum
rd=base/'r2'; grid={}
for l in [s for f in ('shift.txt','wide.txt') for s in (rd/f).read_text().splitlines()]:
    r,k,*cs=map(int,l.split());v=spbig.setdefault((r,k),[])
    for j,c in enumerate(cs):
        if j<len(v):v[j]=min(v[j],c)
        else:v.append(c)
for l in (rd/'qbound.txt').read_text().splitlines() if (rd/'qbound.txt').exists() else []:
    r,z=map(int,l.split());qLocal[r]=min(z,qLocal.get(r,r**5))
for f in list((rd/'layers').glob('*.txt'))+[rd/'runs.txt']:
    for l in f.read_text().splitlines():
        r,k,j,*cs=map(int,l.split());g=grid.setdefault((r,k),{});
        for i,c in enumerate(cs):g[j+i]=min(c,g.get(j+i,c))
for rk,g in grid.items():
    j,cs=fine.get(rk,(0,[]))
    for i,c in enumerate(cs):g[j+i]=min(c,g.get(j+i,c))
    a=min(g);fine[rk]=(a,[g.get(j,rk[0]**((rk[1]+1)//2)) for j in range(a,max(g)+1)])
for l in (rd/'high.txt').read_text().splitlines() if (rd/'high.txt').exists() else []:
    b,j,c=map(int,l.split());t,cs=layers.get(b,(j,[]));a=min(j,t);h=max(j+1,t+len(cs));arr=[1<<b]*(h-a);arr[t-a:t-a+len(cs)]=cs;arr[j-a]=min(arr[j-a],c);layers[b]=(a,arr)
# A small sieve cap at E remains available as a prefix of ANY longer cut;
# add a bound for disjoint annuli, not the entire unsieved short prefix.
seeds={r**k:(r,k,v) for (r,k),v in spbig.items()}
@lru_cache(None)
def short(n,j):
    s=sh(n,j)
    if n not in seeds:return s
    r,k,v=seeds[n];m=(n+(1<<j))//4
    if j<len(v):s=min(s,v[j])
    if j==0:return s
    s=min(s,short(n,j-1)+fixed(n,j)-fixed(n,j-1))
    for i in range(max(0,j-9),j):
        s=min(s,short(n,i)+interval(n,i,j))
        if 1<<(3*i)>=m:s=min(s,short(n,i)+4*tsum(n,m,ceildiv((1<<j)-(1<<i),4)))
    return s
import z79_pbudget as old
old.sh=short
if __name__=='__main__':
    import sys
    for r in (map(int,sys.argv[1:]) if sys.argv[1:] else sorted(r for r in small if 17<=r<=283)):
        x,p,t,q,pt,qt=row(r);margin=x-sum(p)-q-pt-qt
        print(r,x,*(ppm(z) for z in [p[0],p[1],sum(p[2:]),q,pt,qt]),margin*1000000//1,*t[:3],flush=True)
