# Lorenzini's family n = 2^m - 2 (m odd): search a covering of odd m by fixed-pair families.
# Family (d,c): n = c (mod d)  <=>  2^m = c+2 (mod d).  With d = 2^s d' (d' odd): need m >= s and c+2 = 0 (mod 2^s)
# [for m >= s, 2^m = 0 mod 2^s], and 2^m = c+2 (mod d') -> m in a set of classes mod ord_{d'}(2).
import sys
from math import gcd
D=int(sys.argv[1]); L=int(sys.argv[2])
def ordmod(d):
    if d==1: return 1
    k,v=1,2%d
    while v!=1:
        v=v*2%d; k+=1
        if k>L: return None
    return k
ordc={}
fams=[]  # (L-periodic set of m classes)
def add(d,c):
    s=0; dd=d
    while dd%2==0: dd//=2; s+=1
    if (c+2)%(2**s)!=0: return
    o=ordc.get(dd)
    if o is None: o=ordc[dd]=ordmod(dd) or 0
    if o==0 or L%o: return
    t=(c+2)%dd
    ms=[m for m in range(o) if pow(2,m,dd)==t]
    if ms: fams.append((d,o,ms))
for x in range(2,D):
    for y in range(2,D):
        d=x*y-1
        if d>D: break
        add(d,(-x)%d)
    for z in range(x,D):
        d=x*z
        if d>D: break
        add(d,(-(x+z))%d)
cov=[False]*L
for d,o,ms in fams:
    for m0 in ms:
        for m in range(m0,L,o): cov[m]=True
unc=[m for m in range(1,L,2) if not cov[m]]
print("D=%d L=%d families=%d uncovered odd m mod L: %d"%(D,L,len(fams),len(unc)), unc[:20])
