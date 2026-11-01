# z52d Pass 2 NC0 — verify S-lines (solutions) exactly with Fractions, sample per file.
import sys, random, glob
from fractions import Fraction as F
random.seed(1)
tot=bad=0
for fn in sorted(glob.glob('data/z52b/pass2/NC0/exist/m*_p1e7.txt')):
    m=int(fn.split('/m')[-1].split('_')[0])
    S=[l.split() for l in open(fn) if l.split()[1]=='S']
    smp=random.sample(S,min(300,len(S)))
    for r in smp:
        N,x,y,z=int(r[0]),int(r[2]),int(r[3]),int(r[4])
        tot+=1
        if not (F(m,N)==F(1,x)+F(1,y)+F(1,z) and 1<=x<=y<=z):
            bad+=1; print('BAD',fn,r)
print('checked',tot,'bad',bad)
