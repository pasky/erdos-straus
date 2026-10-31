# Z1696: parity of R(p)/2 (unordered (★) triples) for primes p≡1 mod 4 < N
import sys
from sympy import primerange, divisors
N=int(sys.argv[1])
odd=even=0; zero=[]
for p in primerange(5,N):
    if p%4!=1: continue
    R=0
    for C in range(1,(p+1)//2+1):
        n=4*C*p+1; m=4*C
        R+=sum(1 for d in divisors(n) if d%m==m-1)
    h=R//2
    if R==0: zero.append(p)
    if h%2: odd+=1
    else: even+=1
print("odd",odd,"even",even,"R=0 at",zero)
