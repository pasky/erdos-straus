import sys
from math import gcd
from m13c_witness import witness_all
from m13d_wit import Engine
E=Engine(); bad=0; n=0
for L in map(int, sys.argv[1:]):
    for x in range(1, L):
        if gcd(x, L) != 1: continue
        c=set(E.query(x,L,all=True)); p=set(witness_all(x,L,first=False)); n+=1
        if c!=p: bad+=1; print("MISMATCH",x,L,sorted(c-p),sorted(p-c)) if bad<5 else None
print("units",n,"bad",bad)
