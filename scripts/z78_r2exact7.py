"""P7 exact union from two complementary shift enumerators. No storage of cell universe.
All small-shift tuples checked in the engine, CF at e>=E (inclusive) then remove
all already-covered native centres after projection. Print raw oriented count,
distinct after squares, newly covered mod r^4. 17 validated against stored p7."""
from math import isqrt
from tempfile import TemporaryDirectory
from pathlib import Path
import subprocess,sys
base=Path('data/z78/exact');dst=Path('data/z78/r2/exact7');dst.mkdir(exist_ok=True);bin=dst.parent
for r in map(int,sys.argv[1:]):
    n=r**7;E=max(2,isqrt(n)//3);T=(n//E+1)//2;hits=set();cnt=0
    for b,args in [('exact7.bin',[r,E])]+[('cf.bin',[r,7,E,a,min(a+99999999,T)]) for a in range(1,T+1,100000000)]:
        p=subprocess.run([bin/b,*map(str,args)],check=True,text=True,capture_output=True,timeout=1200)
        for l in p.stdout.splitlines():
            x,y=map(int,l.split());assert x*y%r**4==1
            if pow(x%r,(r-1)//2,r)==r-1:hits.update([x,y]);cnt+=2
    if r==17:
        expect={v for l in Path('data/m17b/p7.txt').read_text().splitlines() for a,b,c,d in [map(int,l.split())] for u in (a,b) for v in [(1-4*u*c*d)%r**4] if pow(v,8,17)==16};assert hits==expect
    if r<=211:
        fam=lambda f:set(map(int,(base/f'r{r}_{f}.txt').read_text().split()));old=[fam('p1')|fam('q1'),fam('p3'),fam('q3')|fam('p5')]
    else:
        with TemporaryDirectory(dir=dst) as tmp:
            pre=Path(tmp)/'box';subprocess.run([bin/'depth3.bin',str(r),'--dump-prefix',pre],check=True,capture_output=True,timeout=1200)
            fam=lambda f:set(map(int,Path(f'{pre}.{f}.tsv').read_text().splitlines()[1:]));old=[fam('L1'),fam('P3'),fam('Q3')|fam('P5')]
    new={x for x in hits if all(x%r**j not in t for j,t in enumerate(old,1))};(dst/f'{r}.txt').write_text(f'{r} {E} {cnt} {len(hits)} {len(new)}\n');print(r,E,cnt,len(hits),len(new),flush=True)
