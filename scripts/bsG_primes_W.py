# (W) at primes p = 1 (mod 4), p >= 13, by two fixed-pair families; and the ES sign of the (3,t,4) word for p = 5 (mod 12).
from sympy import primerange, jacobi_symbol
bad=0;cnt=0
for p in primerange(13,2*10**6):
    if p%4!=1: continue
    cnt+=1
    if p%3==1: x,y,z=2,2,(p+2)//3
    else: x,y,z=3,(p+7)//12,4
    if x*y*z-x-z!=p or min(x,y,z)<2: bad+=1
    if p%12==5 and jacobi_symbol(y*x-1,p)!=-1: bad+=1   # A = t*u - 1 with middle t = y, outer u = x = 3: A = (p+3)/4
    if p%12==1 and (jacobi_symbol(3,p)!=1 or jacobi_symbol(2*z-1,p)!=1): bad+=1
print("primes p=1(4), 13<=p<2e6:",cnt,"failures",bad)
