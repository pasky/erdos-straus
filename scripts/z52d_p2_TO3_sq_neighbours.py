import numpy as np, math
F=np.loadtxt('data/z52b/raw/f4_all_30000.txt',dtype=np.int64)
U=dict(zip(F[:,0].tolist(),F[:,1].tolist()))
def nonsq(k): return math.isqrt(k)**2!=k
res={'a_samepar_nonsq_pm20':[], 'b_all_nonsq_pm10':[], 'c_pm1':[], 'd_samepar_nonsq_pm40': []}
for m in range(3,174,2):
    n2=m*m
    if n2>30000: break
    u=U[n2]
    nbA=[U[k] for k in range(max(2,n2-40),n2+41) if k!=n2 and k%2==1 and nonsq(k) and k<=30000]
    nbA20=[U[k] for k in range(max(2,n2-20),n2+21) if k!=n2 and k%2==1 and nonsq(k) and k<=30000]
    nbB=[U[k] for k in range(max(2,n2-10),n2+11) if k!=n2 and nonsq(k)]
    nbC=[U[k] for k in (n2-1,n2+1)]
    res['a_samepar_nonsq_pm20'].append(u/np.median(nbA20))
    res['b_all_nonsq_pm10'].append(u/np.median(nbB))
    res['c_pm1'].append(u/np.mean(nbC))
    res['d_samepar_nonsq_pm40'].append(u/np.median(nbA))
for k,v in res.items(): print(k, round(float(np.median(v)),3), round(float(np.mean(v)),3), len(v))
# parity lemma check for primes p=3 mod 4 and 1 mod 4: number of even denominators in all solutions
import sys; sys.path.insert(0,'scripts')
from z52d_p2_TO3_lib import sols
from sympy import primerange
h={}
for p in primerange(3,200):
    for t in sols(4,p):
        k=sum(1 for v in t if v%2==0); h[(p%4,k)]=h.get((p%4,k),0)+1
print('parity hist (p mod 4, #even denominators):', h)
