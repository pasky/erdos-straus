"""bsB_root_number_parity: is the parity of W(p) (Type I slice a=1) predictable from local data?
Tabulate P(W(p) odd) by p mod 120 classes and by (p mod 8, Legendre symbols at 3,5,7). usage: Wfile LO HI"""
import sys, numpy as np
from collections import defaultdict
from sympy import primerange, legendre_symbol as L
W=np.fromfile(sys.argv[1],dtype=np.uint32); lo,hi=int(sys.argv[2]),int(sys.argv[3])
D=defaultdict(lambda:[0,0])
for p in primerange(lo,hi):
    if p%4!=1: continue
    k=(p%8,L(p%3,3),L(p%5,5),L(p%7,7),L(p%11,11)); D[k][0]+=1; D[k][1]+=int(W[p])&1
fr=[v[1]/v[0] for v in D.values()]
print("classes",len(D),"P(odd) min/max over local classes:",round(min(fr),3),round(max(fr),3),
      "overall",round(sum(v[1] for v in D.values())/sum(v[0] for v in D.values()),3))
