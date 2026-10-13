"""O169 §4.3 probe: genus split of HJ lengths in C0={A=0 mod 4}; min length per Jacobi class (primes and odd squares = 1 mod 4, <= 6000)."""
import sys
sys.path.insert(0,'scripts')
from dk_dict import hj
from math import gcd, isqrt
from collections import Counter
from sympy import isprime, jacobi_symbol
# genus constancy per (length, A mod 4) cylinder at n=1 mod 4
C=Counter(); M=Counter()
for n in range(5,6001,4):
    sq = isqrt(n)**2==n
    if not (sq or isprime(n)): continue
    mins={}
    for A in range(4,n,4):
        if gcd(A,n)>1: continue
        b=hj(n,A); r=len(b)
        if r<=6 and not sq: C[(r,jacobi_symbol(A,n))]+=1
        mins[jacobi_symbol(A,n)]=min(mins.get(jacobi_symbol(A,n),99),r)
    M[('sq' if sq else 'p', mins.get(1), mins.get(-1))]+=1
print(sorted(C.items())); print(sorted(M.items(), key=str))
