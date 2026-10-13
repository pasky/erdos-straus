# Profinite sterile set of (W): nu in Zhat is "covered" if some fixed-pair family contains it:
#   (x,y): nu = -x (mod xy-1);  (x,z): nu = -(x+z) (mod xz)   [x,y,z >= 2; size conditions ignored].
# U_M = classes mod M not covered by families with modulus | M.  Sterile set S has pi_m(S) = cap_{M'} pi_m(U_{M'}).
# Prints |U_M| and its projections to small moduli m | M.
import sys, numpy as np
from sympy import divisors
M=int(sys.argv[1]); ms=[int(a) for a in sys.argv[2:]] or [4,3,8,9,5,7,12,24,72,16,32]
cov=np.zeros(M,dtype=bool)
nf=0
for d in divisors(M):
    if d<3: continue
    cs=set()
    for x in divisors(d+1):
        if 2<=x<=(d+1)//2: cs.add((-x)%d)
    for x in divisors(d):
        if x>=2 and d//x>=2: cs.add((-(x+d//x))%d)
    for c in cs: cov[c::d]=True; nf+=1
U=np.nonzero(~cov)[0]
print("M=%d families=%d |U_M|=%d (%.3g%%)"%(M,nf,len(U),100*len(U)/M))
for m in ms:
    if M%m==0: print("  mod %d: uncovered residues"%m, sorted(set((U%m).tolist())))
# single-prime deviations: uncovered nu with nu = -1 mod (M / l^k)
from sympy import factorint
for l,k in factorint(M).items():
    Q=M//l**k
    dev=[int(u) for u in U if (u+1)%Q==0]
    print("  deviations at prime %d (nu=-1 mod %d): nu mod %d ="%(l,Q,l**k), sorted(set(u%(l**k) for u in dev))[:40])
# how far is U from -1: distribution of gcd(nu+1, M)
from collections import Counter
from math import gcd
c=Counter(gcd(int(u)+1,M) for u in U)
print("  top gcd(nu+1,M):",c.most_common(12))
