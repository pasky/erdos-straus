"""Opus cross-review experiment (NOT a certificate): z80_crush.py plus prefix/CF rows at 59..83
from data/z80/xreview/xr_{prefix,cf}_lo.txt (author z80_pshift.c and reviewer z80_xr_cf.c)."""
import sys
sys.argv=sys.argv[:1]
from z79_r2budget import *
D=Path('data/z80/crush');X=Path('data/z80/xreview')
def readrows(p):return [list(map(int,s.split())) for s in p.read_text().splitlines()]
for p in (D/'shift.txt',D/'shift31.txt',D/'prefix.txt',X/'xr_prefix_lo.txt'):
 for r,k,*cs in readrows(p):
    if 'prefix' in p.name:j=cs.pop(0);assert len(cs)==j+1
    v=spbig.setdefault((r,k),[]);seeds[r**k]=r,k,v
    for i,c in enumerate(cs):
        if i<len(v):v[i]=min(v[i],c)
        else:v.append(c)
for r,k,j,*cs in readrows(D/'runs.txt'):
    t,oldcs=fine[r,k]; a=min(t,j); end=max(t+len(oldcs),j+len(cs));g=[r**((k+1)//2)]*(end-a);g[t-a:t-a+len(oldcs)]=oldcs
    for i,v in enumerate(cs):g[j+i-a]=min(g[j+i-a],v)
    fine[r,k]=a,g
for p in (D/'cf.txt',X/'xr_cf_lo.txt'):
 for r,c in readrows(p):
  j=29;k=9;g0,cs=fine[r,k]
  while g0+len(cs)<=j:cs.append(r**5)  # pad with trivial W
  assert g0<=j;cs[j-g0]=min(cs[j-g0],c)
qsh={r:e+2*f for r,e,f in readrows(D/'qs.txt')}
for r,k,E,T,w,s,v,c in readrows(D/'qboth.txt'):qLocal[r]=min(qLocal.get(r,r**5),c+qsh[r])
for r in (59,61,67,71,73,79,83,89):
 x,p,t,q,pt,qt=row(r);margin=x-sum(p)-q-pt-qt
 print(r,*(ppm(z) for z in [p[0],p[1],sum(p[2:]),q,pt,qt]),margin*1000000//1,*t[:3],flush=True)
