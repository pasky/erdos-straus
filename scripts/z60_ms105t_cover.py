# Residue-class (Mordell-type) coverage for the family n = 4uBC - u - B, modulus M.
# Covered: n = -k mod d (d|M, d=3 mod 4, k|(d+1)/4) or n = -u-k mod 4uk (4uk | M).
# Prints fraction of admissible residues (n=1 mod 4, gcd(n,105)=1) NOT covered, and a few of them.
import sys, numpy as np
from math import gcd
from sympy import divisors
M=int(sys.argv[1])
cov=np.zeros(M,dtype=bool)
for d in divisors(M):
    if d%4==3:
        for k in divisors((d+1)//4):
            cov[(-k)%d::d]=True
for m in divisors(M):
    if m%4==0:
        for u in divisors(m//4):
            k=m//4//u; cov[(-u-k)%m::m]=True
idx=np.arange(M)
adm=(idx%4==1)&(idx%3!=0)&(idx%5!=0)&(idx%7!=0)
unc=adm&~cov
print(M, 'admissible',adm.sum(),'uncovered',unc.sum(),'frac %.4f'%(unc.sum()/adm.sum()))
sq=np.zeros(M,dtype=bool); sq[(idx*idx)%M]=True
print(' uncovered that are squares mod M:', (unc&sq).sum(), ' non-square uncovered:', (unc&~sq).sum())
if len(sys.argv)>2: print(' first non-square uncovered:', idx[unc&~sq][:20].tolist())
if len(sys.argv)>3:   # consistency check: every listed zero >= M must be uncovered
    Z=[int(l.split()[0]) for l in open(sys.argv[3]) if l.split()[1]=='NS' and l.split()[2]=='g105=1']
    bad=[n for n in Z if n>=M and cov[n%M]]
    print(' zeros >= M checked:', sum(1 for n in Z if n>=M), ' covered (would refute Thm 4.1):', bad)
