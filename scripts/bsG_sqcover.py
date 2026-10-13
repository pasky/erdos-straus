# Can finitely many fixed-pair families cover all odd squares?  Families (Lemma 3.2 of HJ_DEEP):
#   (x,y) fixed: n = -x (mod xy-1)   [z=(n+x)/(xy-1)];  (y,z) symmetric;  (x,z) fixed: n = -(x+z) (mod xz).
# For modulus M, take all families whose modulus divides M; report uncovered residues m mod M (n=m^2), m odd.
import sys, math
from sympy import divisors
M=int(sys.argv[1])
cls=set()   # (d, c): n = c mod d
for d in divisors(M):
    if d<3: continue
    for x in divisors(d+1):          # (x,y) with xy-1=d
        if 2<=x<=(d+1)//2: cls.add((d,(-x)%d))
    for x in divisors(d):            # (x,z) with xz=d
        if 2<=x and d//x>=2: cls.add((d,(-(x+d//x))%d))
cov=bytearray(M)  # covered residues n mod M
for d,c in cls:
    for r in range(c,M,d): cov[r]=1
unc=[m for m in range(1,M,2) if not cov[(m*m)%M]]
print("M=",M,"families",len(cls),"odd m mod M uncovered:",len(unc),"of",M//2, "fraction %.4g"%(len(unc)/(M//2)), "first:",unc[:12])
