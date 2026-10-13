from cf_lib import *
from itertools import product
from collections import defaultdict
def K(t,u,v): return t*u*v-u-v
D=defaultdict(set)
for t,u,v in product(range(1,33),repeat=3):
    n=K(t,u,v)
    if n<1 or n%2==0: continue
    w2=(u,v,t); n2=K(*w2)
    if n2<1 or n2%2==0: continue
    D[(t%8,u%8,v%8)].add(chi((t,u,v),n)*chi(w2,n2))
print(all(len(s)==1 for s in D.values()))
for (t,u,v),s in D.items():
    pred = -1 if (t%2 and u%2 and v%2 and (t-u)%4) else 1
    assert s=={pred}, (t,u,v,s)
print("rotation law asserted on", len(D), "cells mod 8")
# test candidate laws: product == (-1/n)(-1/n')^? or (-1)^{(n-n')/2 * something}
ok={}
for key,s in D.items():
    t,u,v=key; f=list(s)[0]
    n=K(t,u,v)%8; n2=K(u,v,t)%8
    ok[key]=(f,n%4,n2%4,t%4,u%4,v%4)
from collections import Counter
C=Counter((x[1],x[2],x[3],x[4],x[5],x[0]) for x in ok.values())
for k in sorted(C): print(k,C[k])
