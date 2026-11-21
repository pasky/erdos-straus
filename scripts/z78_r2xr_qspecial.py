"""Round-2 review (Claude Opus): reconstruct data/z78/r2/qSpecial/bound.txt, for which the
author committed no generator.  bound = min over j,l in 0..3 of
   smallE[j] + 2*smallF[l] + qlarge(F, cut<<j, cut<<l),   cut=ceil(F^(1/3))^2, F=r^5,
smallE/smallF from qSpecial/shifts.txt (z78_r2q5shift.c); the factor 2 is z77 §5's inversion
factor for the a<=b-oriented small-f range.  Usage: r"""
import sys;sys.path.insert(0,'scripts')
from z78_qcap import qlarge
r=int(sys.argv[1]);F=r**5;z=1
while z**3<F:z+=1
cut=z*z
row=[list(map(int,l.split())) for l in open('data/z78/r2/qSpecial/shifts.txt') if int(l.split()[0])==r][0]
e,f=row[1:5],row[5:9]
best=min((e[j]+2*f[l]+qlarge(F,cut<<j,cut<<l),j,l) for j in range(4) for l in range(4))
print(r,best[0],'argmin j,l =',best[1],best[2])
