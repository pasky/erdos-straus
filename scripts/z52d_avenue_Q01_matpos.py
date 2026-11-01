# Z0083: (4/n) I = X^-1 + Y^-1 + Z^-1, X,Y,Z in M2(Z) with all entries >= 1, invertible
from fractions import Fraction as F
import itertools, sys
E=int(sys.argv[2]); n=int(sys.argv[1])
mats=[]
for a,b,c,d in itertools.product(range(1,E+1),repeat=4):
    D=a*d-b*c
    if D: mats.append(((a,b,c,d),(F(d,D),F(-b,D),F(-c,D),F(a,D))))
t=F(4,n); found=[]
for i,(X,Xi) in enumerate(mats):
    for (Y,Yi) in mats[i:]:
        S=(t-Xi[0]-Yi[0], -Xi[1]-Yi[1], -Xi[2]-Yi[2], t-Xi[3]-Yi[3])
        D=S[0]*S[3]-S[1]*S[2]
        if D==0: continue
        Z=(S[3]/D, -S[1]/D, -S[2]/D, S[0]/D)
        if all(z.denominator==1 and z>=1 for z in Z):
            found.append((X,Y,tuple(int(z) for z in Z)))
            if len(found)>=3: break
    if len(found)>=3: break
print(n, len(mats), found)
