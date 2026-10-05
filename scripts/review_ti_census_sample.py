# R31: independent recomputation of a random sample + the stated records of the author's census file.
import gzip, random, sys
sys.path.insert(0,'scripts')
from review_ti_ckmin import ckmin, np_
from sympy import primerange
rows=[tuple(map(int,l.split())) for l in gzip.open('data/pointwise_typei/ckmin_np_1e7.txt.gz','rt')]
d={p:(n,c) for p,n,c in rows}
# completeness: all hard primes < 1e7 present
hard=[p for p in primerange(25,10**7) if p%24==1]
print("hard primes:",len(hard),"file rows:",len(rows),"same set:",set(hard)==set(d))
from collections import defaultdict
mx=defaultdict(int)
for p,(n,c) in d.items(): mx[n]=max(mx[n],c)
print("per-n_p max (file):",dict(sorted(mx.items())))
random.seed(31); sample=random.sample(rows,150)+[r for r in rows if r[0] in (12289,92401,414241,9033649)]
bad=0
for p,n,c in sample:
    n2=np_(p); c2=ckmin(p,c+1)   # all slices incl. forced, up to stated value
    if (n2,c2)!=(n,c): bad+=1; print("MISMATCH",p,n,c,n2,c2,flush=True)
print("sample",len(sample),"mismatches",bad)
