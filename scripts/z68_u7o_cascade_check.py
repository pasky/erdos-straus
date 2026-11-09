# independent brute-force check of m(p) (min letter of a U7 word) for primes p = 1 (8) <= N
import sys
from sympy import primerange
N=int(sys.argv[1]); out=[]
for p in primerange(17,N+1):
    if p%8!=1: continue
    best=None
    for x in range(1,2*p+3):
        for y in range(1,(2*p+2)//x+2):
            if (x*y)%8: continue
            f=x*y-1
            if f<1 or f>2*p+1: 
                if f>2*p+1: break
                continue
            if (p+x)%f==0:
                z=(p+x)//f; m=min(x,y,z)
                if best is None or m<best: best=m
    out.append((p,best))
for p,m in out: print(p,m)
