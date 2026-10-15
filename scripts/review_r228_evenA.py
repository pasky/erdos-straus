"""R228: even-A chi=-1 words at predicted sign-clean levels (examples with n PRIME), by hand-rolled enumeration."""
import sys
from math import gcd
from sympy import isprime, divisors, legendre_symbol
def tab(t,u,v,A,As): return -1 if any(z%4==0 for z in (t,u,v,A,As)) else 1
def run(k, side, M, mmax, show=3):
    b = k+M if side=='u' else M*k+1
    cnt=0; lit=0; ex=[]
    for m in range(1, mmax+1):
        n=m*m+k
        if n%4!=1 or not isprime(n): continue
        g=gcd(m,b)
        while g%2==0: g//=2
        if g!=1: continue
        N = n+M if side=='u' else M*n+1
        for A in divisors(N):
            if A%2 or (A+1)%M: continue
            if side=='u': u,t,v=M,(A+1)//M,N//A
            else: t,u=M,(A+1)//M; v=(N//A+1)//M
            As=t*v-1; assert t*u*v-u-v==n
            chi=legendre_symbol(A%n,n); assert chi==tab(t,u,v,A,As)
            if chi==-1:
                cnt+=1; lit += gcd(m,b)==1
                if len(ex)<show: ex.append((m,n,(t,u,v),A,'N=%d'%N))
    print(f"k={k} {side}={M}: even-A chi=-1 words at prime n, m<={mmax}: {cnt} (of which literal-generic m: {lit}); e.g. {ex}")
for k,side,M in [(1,'t',3),(1,'t',35),(9,'t',11),(9,'t',75),(9,'u',3),(9,'u',39),(9,'u',99),(1,'u',8),(24,'u',3),(24,'u',51),(8,'u',1),(16,'u',9)]:
    run(k,side,M,int(sys.argv[1]))
