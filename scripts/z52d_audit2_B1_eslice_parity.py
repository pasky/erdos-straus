# Z2430: prime e-slices (Type II, N = (p+e)/4, e ≡ -p ≡ 3 mod 4 for p ≡ 1 mod 4).
# -1 in H=<prime factors of N mod e>  <=>  |H| even  <=>  (v2(e-1)=1) some factor is a QNR mod e.
# Compare with -1 in Q = {ab^-1 : ab | N} (the actual slice event) and with the reciprocity-forced case (e/p) = -1.
import random
from sympy import primerange, factorint, legendre_symbol, n_order
random.seed(2)
def Qset(F,e):
    S={1}
    for l,a in F.items():
        g=l%e; mult={pow(g,c,e) for c in range(a+1)}|{pow(g,-c,e) for c in range(a+1)}
        S={(s*m)%e for s in S for m in mult}
    return S
hard=[p for p in primerange(10**6,3*10**6) if p%840 in (1,121,169,289,361,529)]
ps=random.sample(hard,300)
tab={}
for p in ps:
    for e in primerange(3,400):
        if (p+e)%4: continue
        N=(p+e)//4; F=factorint(N)
        if any(l%e==0 for l in F): continue
        H_has=any(n_order(l%e,e)%2==0 for l in F) if True else None
        qnr=any(legendre_symbol(l%e,e)==-1 for l in F)
        assert H_has==qnr
        hit=(e-1) in Qset(F,e)
        forced=(legendre_symbol(e%p,p)==-1)
        if forced: assert H_has
        k=(forced,H_has,hit); tab[k]=tab.get(k,0)+1
tot=sum(tab.values())
print('slices',tot)
for k,v in sorted(tab.items()): print(' (e/p)=-1:%s  -1∈H:%s  hit:%s  %6d  %.3f'%(k[0],k[1],k[2],v,v/tot))
H=sum(v for k,v in tab.items() if k[1]); A=sum(v for k,v in tab.items() if k[1] and not k[2])
print('P(-1∈H)=%.3f  P(hit)=%.3f  P(no hit | -1∈H)=%.3f'%(H/tot,sum(v for k,v in tab.items() if k[2])/tot,A/H))
