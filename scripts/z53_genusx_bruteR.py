import sys
from sympy import factorint
def sqf(x): return all(e==1 for e in factorint(x).values())
from math import gcd
n,U0,U1,Y,X=map(int,sys.argv[1:])
R=0
for u in range(U0+1,U1+1):
    if u%4!=1 or not sqf(u) or gcd(u,n)>1: continue
    for w in range(Y+1,X+1,2):
        if (n+u+2*w)%(8*u*w)==0 and sqf(w) and gcd(w,u*n)==1: R+=2
print("bruteR",R)
