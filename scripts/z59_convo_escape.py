# For given n, list rho = 3 mod 4 (< R) with Jacobi(n/rho) = -1, factorization of N=(n+rho)/4, and whether -1 in ratio set.
import sys
from sympy import factorint, jacobi_symbol, divisors
def works(N,rho):
    D=divisors(N)
    return any((a+b)%rho==0 for a in D for b in divisors(N//a))
for n in map(int,sys.argv[1:]):
    R=120 if n!=4545 else 60
    esc=[];ok=[]
    for rho in range(3,R,4):
        from math import gcd
        if gcd(rho,n)!=1: continue
        N=(n+rho)//4; w=works(N,rho)
        if w: ok.append(rho)
        if jacobi_symbol(n,rho)==-1: esc.append((rho,dict(factorint(N)),w))
    print(n,"working rho<%d:"%R,ok)
    for e in esc[:8]: print("   NR rho",e[0],"N=",e[1],"works" if e[2] else "FAILS")
