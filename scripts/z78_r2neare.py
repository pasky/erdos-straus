"""Supplement near-P search at 17 in the specifically bounded shift slice e<=2^17.
Use full divisor allocations; not a claim about all larger shifts."""
from pathlib import Path
import subprocess,sys
from itertools import groupby
for L in map(int,sys.argv[1:]):
    N=17**(2*L-1);es=[e for e in range(1,1<<17) if (N+e)%4==0 and e%17];out=Path(f'data/z78/r2/near/E{L}.txt').open('w');best=0
    for g in range(0,len(es),4000):
        bloc=es[g:g+4000];ms=[(N+e)//4 for e in bloc];lines=subprocess.run(['factor'],input='\n'.join(map(str,ms))+'\n',text=True,capture_output=True,check=True,timeout=120).stdout.splitlines();assert len(lines)==len(ms)
        for m,e,line in zip(ms,bloc,lines):
            lh,rs=line.split(':');assert int(lh)==m;ds=[1]
            for p,items in groupby(map(int,rs.split())):
                base=ds[:];q=1
                for _ in items:q*=p;ds.extend(z*q for z in base)
            assert max(ds)==m
            for a in ds:
                if a*a>m:continue
                for b in ds:
                    if b<a or (a+b)%e or m%(a*b):continue
                    c=(a+b)//e;d=m//(a*b)
                    if c%17==0 or d%17==0:continue
                    for o,z in enumerate((a+5*b,b+5*a)):
                        v=0
                        while z%17==0:z//=17;v+=1
                        if v>=2:print(L,v,o,a,b,c,d,e,file=out)
    out.close()
