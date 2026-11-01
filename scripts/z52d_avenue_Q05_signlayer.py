"""z52d avenue Q05 Z1501: check the Type I sign layer — a Type I certificate at (c,d) (f | p^2+4c^2 d, f = -p mod 4cd)
occurs only when (d/p) = -1 (p = 1 mod 4 prime). Brute force, small ranges. EVIDENCE check of the T1_TEMPLATE lemma."""
from sympy import primerange, divisors, legendre_symbol, gcd
viol=0; hits=0
for p in primerange(5,1500):
    if p%4!=1: continue
    for d in range(1,25):
        for c in range(1,25):
            N=p*p+4*c*c*d; m=4*c*d
            ok=any((f+p)%m==0 for f in divisors(N) if f%p)
            if ok:
                hits+=1
                if d%p and legendre_symbol(d%p,p)==1: viol+=1; print('VIOLATION',p,c,d)
print('certificates found:',hits,' violations of (d/p)=-1:',viol)
