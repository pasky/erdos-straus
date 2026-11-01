import sys; sys.path.insert(0,'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
from sympy import isprime, primerange
# Z0832 inheritance for 4/p^2
import time
out=[]
for p in [3,5,7,11,13]:
    s=sols(4,p*p)
    inh=[t for t in s if all(v%p==0 for v in t)]
    out.append((p,len(s),len(inh)))
print('Z0832 small', out)
t=time.time()
res=[]
for p in primerange(3,174):
    s=sols(4,p*p); inh=[t_ for t_ in s if all(v%p==0 for v in t_)]
    res.append((p,len(s),len(inh)))
print(time.time()-t)
print(res[:12], 'fraction inherited total', sum(r[2] for r in res)/sum(r[1] for r in res))
print('all with inherited count 0?', [r for r in res if r[2]==0])
