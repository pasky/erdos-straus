from cf_lib import *
from sympy import isprime
bad=0; tot=0
for n in range(3,1200,2):
    for w in words(n):
        t,u,v=w
        if t*v-1==0: continue
        A=t*u-1
        if gcd(A,n)!=1: continue
        R=ram_set(w)
        c=chi(w,n)
        tot+=1
        if isprime(n):
            # predict: chi=-1 <=> ram at n
            if (c==-1)!=(n in R): bad+=1; print("prime mismatch",n,w,c,R)
        # 2-adic ramification vs cell
print(tot,bad)
