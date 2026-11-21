"""Replay the relative measure certificate. Costs live in Q, not ppm."""
from z79_r2budget import *
D=Path('data/z80/crush')
def readrows(name):return [list(map(int,s.split())) for s in (D/name).read_text().splitlines()]
for f in ('shift.txt','shift31.txt','prefix.txt'):
 for r,k,*cs in readrows(f):
    if f=='prefix.txt':j=cs.pop(0);assert len(cs)==j+1
    v=spbig.setdefault((r,k),[]);seeds[r**k]=r,k,v
    for i,c in enumerate(cs):
        if i<len(v):v[i]=min(v[i],c)
        else:v.append(c)
for r,k,j,*cs in readrows('runs.txt'):
    t,oldcs=fine[r,k]; a=min(t,j); end=max(t+len(oldcs),j+len(cs));g=[r**((k+1)//2)]*(end-a);g[t-a:t-a+len(oldcs)]=oldcs
    for i,v in enumerate(cs):g[j+i-a]=min(g[j+i-a],v)
    fine[r,k]=a,g
# Join the certified small-shift prefix to the complementary CF count.
for r,c in readrows('cf.txt'):
 j=29;k=9;g0,cs=fine[r,k];assert g0<=j<g0+len(cs);cs[j-g0]=min(cs[j-g0],c)
qsh={r:e+2*f for r,e,f in readrows('qs.txt')}
for r,k,E,T,w,s,v,c in readrows('qboth.txt'):
 assert k==5 and E==T==rootup(r**k,3)**2;qLocal[r]=min(qLocal.get(r,r**5),c+qsh[r])
if __name__=='__main__':
 for r in sorted(r for r in small if 17<=r<=283):
    x,p,t,q,pt,qt=row(r);margin=x-sum(p)-q-pt-qt
    print(r,*(ppm(z) for z in [p[0],p[1],sum(p[2:]),q,pt,qt]),margin*1000000//1,flush=True)
