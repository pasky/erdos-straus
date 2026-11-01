# z52d pass2 TO4 corrections: (i) Z1397 threshold: exists solution with max(y,z) ≤ p^{3/2}  <=>  min(max(y,z))/p ≤ sqrt(p)
#  (ii) Z1555 zero-fraction restricted to p≡1 (mod 24) (hard class) (iii) Z1605 (c,d)=(2,1) Type II for C-form exceptions ≤1e6
import math, statistics, sys
from sympy import primerange
exec(open('scripts/z52d_p2_TO4_residual.py').read().split('# ---- Z0996')[0])
exec(open('scripts/z52d_p2_TO4_forms.py').read().split('if __name__')[0])
ok=0; tot=0; vals=[]
for p in primerange(1000,3000):
    if p%24!=1: continue
    best=None
    for x in range(p//4+1,(3*p)//4+1):
        a,b=reduce(4*x-p,p*x)
        if a<=0: continue
        for (y,z) in two_term(a,b):
            m=max(y,z)
            if best is None or m<best: best=m
    tot+=1
    if best is None: continue
    vals.append(best/p)
    if best <= p**1.5: ok+=1
print("Z1397 (x-fixed two-term solutions only) p≡1 mod 24, 1000≤p<3000: n=%d, exists solution with max(y,z)≤p^{3/2}: %d; median min max/p %.1f ; sqrt(p) median %.1f"%(len(vals), ok, statistics.median(vals), statistics.median([math.sqrt(p) for p in primerange(1000,3000) if p%24==1])))
rows=[]
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); rows.append((t[0],t[2:2+t[1]]))
for lo,hi in [(10**3,10**5),(10**5,10**7)]:
    for K in (25,100,400):
        s=[(p,w) for p,w in rows if lo<=p<hi and p%24==1]
        z=sum(1 for p,w in s if not any(c<=K for c in w))
        print("Z1555 p≡1(24) in [%g,%g) K=%d zero-fraction %.5f (%d/%d)"%(lo,hi,K,z/len(s),z,len(s)))
ex=[p for p,w in rows if not w and p<=10**6]
print("Z1605 C-form exceptions (K=400 zero, p≤1e6, of which full-C-verified exceptions are a subset):")
for p in ex:
    print("   p=%d  Type II (c,d)=(2,1) solutions: %d ; (1,d) with d≤60: %s"%(p, len(typeII(p,2,1)), [d for d in range(1,61) if typeII(p,1,d)][:3]))
