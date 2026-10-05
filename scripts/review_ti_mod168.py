# R31: is any Type-I (15d) certificate (c,k,F), decided mod 168, valid on a hard class p≡1 (24) with p a non-residue mod 7?
from sympy import divisors, factorint
def sf(c):
    s=1
    for q,e in factorint(c).items():
        if e%2: s*=q
    return s
hits=[]
for m in divisors(42):
    for k in divisors(m):
        c=m//k
        for F in (1,3,7,21):
            from math import gcd
            if gcd(F,4*c*k)!=1: continue
            for p in range(168):
                if p%24!=1 or p%7 not in (3,5,6): continue
                if (p+F)%(4*c*k)==0 and (p*p+4*c*k*k)%F==0: hits.append((c,k,F,p,sf(c)))
print(hits)
