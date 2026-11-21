"""Opus cross-review of R17_WALK (NOT a certificate): which route/grid supplies the P11..P15 charge at 73, 83."""
import sys;sys.argv=sys.argv[:1]
import z80_budget2 as B
from fractions import Fraction as F
for r in (73,83):
  for k in (11,13,15):
    n=r**k;W=r**((k+1)//2);b=n.bit_length();src=[]
    for name,grid in [('layers',B.layers.get(b)),('local',B.local.get((r,k))),('fine',B.fine.get((r,k)))]:
        if grid:j,cs=grid;src.append((name,j,j+len(cs)-1))
    p,tag=B.cost(r,k,F(1))
    print(r,k,'grids(j range)',src,'spbig len',len(B.spbig.get((r,k),[])),'cost ppm',B.ppm(p),'route',tag,flush=True)
