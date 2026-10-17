import sys, math
sys.path.insert(0,'.')
from review_r270_checks import *
X=10**12
for Mod in (24, 1800, 176400, 64033200):
    ps=[]; k=X//Mod+1
    while len(ps)<300:
        q=1+Mod*k
        if isprime(q): ps.append(q)
        k+=1
    n1=[c for _,c in eng("count",ps)]; nc=[c for _,c in eng("count",ps,line=2)]
    L2=sum(math.log(q)**2 for q in ps)/len(ps)
    print(f"p=1 mod {Mod} near 1e12 (300 primes): N1/L^2={sum(n1)/len(n1)/L2:.3f}  Nc1/L^2={sum(nc)/len(nc)/L2:.3f}  min N1 {min(n1)}")
