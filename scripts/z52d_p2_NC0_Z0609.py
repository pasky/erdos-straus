# z52d Pass 2 NC0, item Z0609 — composite sporadic failures vs prime-factor families ("scaling compatibility").
# Data: data/z52b/raw/var_all_3000.txt (all n<=3000; family k at col 2+k, names as in z52b_fingerprint_variants_an.py).
# For composite n: F_empty(n) = families with zero solutions at n. Compare with the families empty at its prime factors.
import numpy as np
from sympy import factorint
A=np.loadtxt('data/z52b/raw/var_all_3000.txt',dtype=np.int64)
N=A[:,0]; cnt={int(n):A[i,2:] for i,n in enumerate(N)}
names=['0 even','1 even','2 even','3 all even','primitive','x,y|z','x|y','isosceles','all squarefree','z<=n^2','z<=n^1.5','some power of 2','x or y prime','some coprime pair','no denom div 3','some denom div 4']
sporadic=[105,2961]          # the in-range members of the listed sporadic set (others > 3000)
def empty(n): return {names[k] for k in range(16) if cnt[n][k]==0}
rows=[]
comp_total=0; comp_with_empty=0; incompat=0; sample=[]
for n in range(4,3001):
    f=factorint(n)
    if len(f)<2: continue
    comp_total+=1
    e=empty(n)
    if not e: continue
    comp_with_empty+=1
    primes=list(f)
    # family empty at n but nonempty at every prime factor: composite-specific emptiness (scaling-incompatible)
    spec={k for k in e if all(k not in empty(q) for q in primes if q in cnt)}
    if spec:
        incompat+=1
        if len(sample)<6: sample.append((n,sorted(spec)))
print('composite n in [4,3000]:',comp_total,'with >=1 empty family:',comp_with_empty,'with a family empty only at n (not at any prime factor):',incompat)
print('sample:',sample)
for n in sporadic:
    print('sporadic',n,factorint(n),'empty families:',sorted(empty(n)),'prime factors empty:',{q:sorted(empty(q)) for q in factorint(n)})
