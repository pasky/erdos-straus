# hit rate of (*) level C=q when q | 4p+1 vs baseline at same q
from sympy import primerange, factorint
import random
def hit(p,C):
    N=4*C*p+1; m=4*C
    # divisors d of N with d ≡ -1 mod m, d <= sqrt(N)
    f=factorint(N); ds=[1]
    for q,e in f.items():
        ds=[d*q**k for d in ds for k in range(e+1)]
    return any(d%m==m-1 for d in ds)
P=[p for p in primerange(10**5,4*10**5) if p%24==1]
cond=[0,0]; base=[0,0]
random.seed(1)
for p in P:
    f=factorint(4*p+1)
    for q in f:
        if q<=500:
            cond[0]+=1; cond[1]+=hit(p,q)
            p2=random.choice(P)
            while (4*p2+1)%q==0: p2=random.choice(P)
            base[0]+=1; base[1]+=hit(p2,q)
print('cond (q|4p+1):',cond, cond[1]/cond[0]); print('base same q:',base, base[1]/base[0])
