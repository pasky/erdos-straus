# For each zero prime: least prime QNR l(p); smallest-modulus identity class (c,D) containing p (D up to DMAX, any family);
# also whether p is covered at modulus 840 (Mordell) and at 840*l(p).
import sys
from sympy import primerange, legendre_symbol, divisors
from math import gcd
from z62_inversef_cover import classes, is_square_class
ZEROS=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
DMAX=int(sys.argv[1]) if len(sys.argv)>1 else 400
# all classes with modulus D<=DMAX: use classes(lcm)?? simpler: generate per D by calling classes(D) and keeping modulus==D
allcl=[]
for D in range(3,DMAX+1):
    if D%4 in (0,3):
        allcl+=[x for x in classes(D) if x[1]==D]
print("classes with D<=",DMAX,":",len(allcl))
for p in ZEROS:
    l=next(q for q in primerange(3,1000) if legendre_symbol(q,p)==-1)
    hits=sorted((D,c,f) for c,D,f in allcl if p%D==c)
    inM=is_square_class(p%840,840)
    Ml=840*l
    cov_l=any(p%D==c for c,D,f in classes(Ml))
    print(f"p={p}: least QNR prime l={l}; in Mordell M? {inM}; covered at 840*l={Ml}? {cov_l}; smallest classes: {hits[:4]}")
