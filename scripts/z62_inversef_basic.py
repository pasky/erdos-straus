# Verify reformulations of R(n) and look at structure of the 14 zero primes.
# R(n) = #{(u,B,C): 4uBC-u-B = n}
# Claim A: R(n)=0 iff for all r>=1, n+r has no divisor d == -1 (mod 4r).
# Claim B: R(n)=0 iff for all C>=1, 4Cn+1 has no divisor == -1 (mod 4C).
import sys
from sympy import factorint, divisors, jacobi_symbol, isprime
def R_direct(n):
    cnt=0
    for u in range(1,n+1):
        for B in range(1,n+1):
            if 4*u*B > n+u+B: break
            if (n+u+B) % (4*u*B)==0: cnt+=1
    return cnt
def R_A(n):
    cnt=0
    for r in range(1,n+1):
        for d in divisors(n+r):
            if d%(4*r)==4*r-1: cnt+=1
    return cnt
def R_B(n):
    cnt=0
    for C in range(1,n+1):
        for d in divisors(4*C*n+1):
            if d%(4*C)==4*C-1: cnt+=1
    return cnt
if __name__=="__main__":
    for n in range(1,400,4):
        a,b,c=R_direct(n),R_A(n),R_B(n)
        assert a==b==c,(n,a,b,c)
    print("reformulations A,B verified for n=1(4), n<400")
