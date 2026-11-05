# For each prime zero p, and k=1..K: factor p+k, list prime residues mod 4k, and check that no sub-multiset product is -1 mod 4k.
from sympy import factorint
from itertools import product
zeros=[5569,9601,83449,102001,712321,1724209,1726201,5212561,8813281]
K=8
for p in zeros:
    print(f"p={p}  p mod 840={p%840}")
    for k in range(1,K+1):
        N=p+k; f=factorint(N); m=4*k
        # all sub-multiset products mod m of the odd part coprime to k
        prods={1}
        for q,e in f.items():
            if m%q==0: continue
            new=set()
            for r in prods:
                v=r
                for _ in range(e):
                    v=v*q%m; new.add(v)
            prods|=new
        has=(m-1) in prods
        fs=" ".join(f"{q}^{e}" if e>1 else f"{q}" for q,e in f.items())
        res=" ".join(f"{q%m}" for q in f if m%q)
        print(f"  k={k:2d} 4k={m:3d}  p+k={fs:30s} residues mod 4k: {res:20s} hit={has}")
