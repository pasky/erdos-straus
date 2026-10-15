# Covering of s mod L for n_s = 4^s + k by (a) exponential window classes (windows m_j = 4^j - k, K = 4^{j-1}(4^r+1),
# r = s - j, atoms 2^i, G = 4^g+1, A± = 2^g ∓ 2^{(g+1)/2} + 1 with g = r/e, e odd), (b) divisor classes l | n_s (l prime < PL).
# Usage: s6_cover105.py k L JMAX PL [dump]
import sys, math, numpy as np
from sympy import n_order, primerange, divisors
k=int(sys.argv[1]); L=int(sys.argv[2]); JMAX=int(sys.argv[3]); PL=int(sys.argv[4])
cov=np.zeros(L,dtype=np.uint8)   # 1 = exp class, 2 = divisor class
nexp=0; classes=[]
for j in range(1,JMAX+1):
    m=4**j-k
    if m<=1: continue
    o=n_order(2,m); P0=2*o
    pm=[l for l in divisors(m) if l>1 and all(l%q for q in range(2,int(l**.5)+1))]
    for e in divisors(L):
        if e%2==0 or L%(e*P0): continue
        P=e*P0
        for g in range(P0):
            r=e*g   # representative of r mod P
            # gcd(K, m) = 1  <=>  no prime l | m divides 4^r + 1
            if any((pow(4,r,l)+1)%l==0 for l in pm): continue
            G=(pow(4,g,m)+1)%m; pairs=[(1,G,'1/G'),(G,1,'G/1')]
            if g%2==1:
                h=pow(2,(g+1)//2,m); t=pow(2,g,m); Am=(t-h+1)%m; Ap=(t+h+1)%m
                pairs+=[(1,Am,'1/A-'),(Am,1,'A-/1'),(1,Ap,'1/A+'),(Ap,1,'A+/1'),(Ap,Am,'A+/A-'),(Am,Ap,'A-/A+')]
            hit=None
            for U,V,nm in pairs:
                for i in range(-(2*j-2),2*j-1):
                    if (pow(2,i,m)*U+V)%m==0: hit=(i,nm); break
                if hit: break
            if hit:
                s0=(j+r)%P
                if not cov[s0::P].all(): classes.append((j,e,g,P,hit))
                cov[s0::P]|=1; nexp+=1
print("exp-covered residues:",int((cov>0).sum()),"of",L, "classes used",len(classes))
for l in primerange(3,PL):
    if k%l==0: continue
    o=n_order(4,l)
    if L%o: continue
    # solve 4^s = -k mod l
    t=(-k)%l; x=1
    for s in range(o):
        if x==t: cov[s::o]|=2
        x=x*4%l
unc=np.nonzero(cov==0)[0]
print("after divisor classes (l <",PL,"): uncovered",len(unc), "density %.3g"%(len(unc)/L), "first:",unc[:30].tolist())
if len(sys.argv)>5: np.save(sys.argv[5],unc)
