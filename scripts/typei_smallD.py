"""O31 (POINTWISE_TYPEI.md §6, EVIDENCE): for hard p in (1e5,X) with n_p=r, least ck of an unforced slice
witnessed by a target divisor D<=Dmax (search ck<=C). Usage: typei_smallD.py r X Dmax C"""
import sys, collections
from sympy import primerange, factorint, legendre_symbol
sys.path.insert(0,'scripts')
from typei_ratio import divs_from_fac, sf, chi_minus_s
r=int(sys.argv[1]); X=int(sys.argv[2]); Dmax=int(sys.argv[3]); C=int(sys.argv[4])
from sympy import isprime
worst=[]; Dused=collections.Counter(); unc=0; tot=0
for p in primerange(10**5, X):
    if p%24!=1: continue
    if any(legendre_symbol(l,p)!=1 for l in primerange(5,r)) or legendre_symbol(r,p)!=-1: continue
    tot+=1; found=None
    for P in range(r, C+1):
        for c in range(1,P+1):
            if P%c: continue
            k=P//c; s=sf(c)
            if s in (1,2,3,6) or chi_minus_s(s,p)==1: continue
            h=4*c*k; N=p*p+4*c*k*k
            # small target divisors only
            for D in range(h-p%h, Dmax+1, h):
                if N%D==0: found=(P,c,k,D); break
            if found: break
        if found: break
    if found: Dused[found[3]]+=1; worst.append((found[0],p))
    else: unc+=1
worst.sort()
print(f"r={r}: {tot} primes; uncovered (no slice ck<={C} with target D<={Dmax}): {unc}; max w={worst[-5:]}")
print("D used:", Dused.most_common(20))
