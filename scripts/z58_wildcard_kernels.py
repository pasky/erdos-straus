# z58 WILDCARD: squarefree-kernel profile of zero sets (is the hard composite set made of twisted squares s*m^2, s small?)
# Usage: uv run --with sympy python scripts/z58_wildcard_kernels.py
import math, sys
from sympy import factorint
from collections import Counter
def kernel(n):
    s=1; m=1
    for q,e in factorint(n).items():
        if e%2: s*=q
        m*=q**(e//2)
    return s,m
def load_census(fns):
    Z=[]
    for fn in fns:
        for l in open('data/z58/wildcard/'+fn):
            if l.startswith('ZERO'): t=l.split(); Z.append((int(t[1]),t[2]))
    return Z
sets={'(★) composite zeros <=8e6':[(int(l.split()[0]),'C') for l in open('data/z58/screens/composite_zeros_le8e6.txt') if not l.startswith('#')],
 'K=4 coprime <=1e8':load_census(['census_K4cop_1e8.txt']),
 'K=8 <=1e9':load_census(['census_K8_1e7.txt','census_K8_1e7_1e8.txt','census_K8_1e8_1e9.txt']),
 'K=12 <=1e8':load_census(['census_K12_1e8.txt']),'K=16 <=1e8':load_census(['census_K16_1e8.txt'])}
for name,Z in sets.items():
    comp=[n for n,t in Z if t=='C']
    ks=[kernel(n) for n in comp]
    sq=[n for n,(s,m) in zip(comp,ks) if m>1]  # has a square factor
    c=Counter(s for s,m in ks if m>1)
    big=[(n,s,m) for n,(s,m) in zip(comp,ks) if n>=max(comp)//100] if comp else []
    frac_sm=lambda S: sum(1 for s,m in ks if s<=S and m>1)
    print(f'## {name}: composites {len(comp)}; with square factor m>1: {len(sq)}; kernel s<=15: {frac_sm(15)}, s<=105: {frac_sm(105)}')
    print('   most common kernels (m>1):',c.most_common(8))
    top=sorted(comp)[-8:]
    print('   largest 8:',[(n,)+kernel(n) for n in top])
