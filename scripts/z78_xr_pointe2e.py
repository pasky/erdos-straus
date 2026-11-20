"""Cross-review: end-to-end test of the three-index size theorem + engines (own and
author's z78_point.search) at small depth for several r, (p,q) in the theorem set,
against complete own data dumps (z78_xr_pdump). Run from root with PYTHONPATH=scripts."""
import subprocess, math, io, contextlib
from z78_xr_point import MODES, Xcut
from z78_point import search
tot=0;cases=0
for r in (19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103):
  for K in ((5,7) if r<60 else (5,)):
    L=(K+1)//2;W=r**L;N=W*W//r
    if W<1000:continue
    E=4*math.isqrt(r**K)+1
    out=subprocess.run(['/tmp/xr_pdump',str(r),str(K),str(E)],capture_output=True,text=True,check=True).stdout
    D={tuple(map(int,l.split()[:4])) for l in out.splitlines()}
    X=Xcut(W)
    for p,q in ((1,5),(5,1),(1,3),(3,1),(1,2),(2,1),(1,4),(4,1)):
      want={v for v in D if (p*v[0]+q*v[1])%W==0}
      got=set()
      for m in ('Ha','Hd','J'):got|=MODES[m](r,L,p,q,X,1,X,W)
      assert got==want,(r,K,p,q,got^want)
      if (p,q) in ((1,5),(5,1),(1,3),(3,1)):
        a=set()
        for m in ('Ha','Hd','J'):
          s=io.StringIO()
          with contextlib.redirect_stdout(s):search(r,L,p,q,m,1,10**9)
          a|={tuple(map(int,l.split()[-4:])) for l in s.getvalue().splitlines() if l.startswith('hit')}
        assert a==want,(r,K,p,q,'author',a^want)
      tot+=len(want);cases+=1
print('e2e cases',cases,'total hits matched (own engine; author engine on 4 theorem pairs)',tot)
