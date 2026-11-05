# Construction of Thm 7.7: p = Q t + 1 with Q = lcm(24, rho(rho+1) : rho in F); if p and all P_rho = 1 + (Q/(rho+1)) t
# are prime then every rho in F fails. Find such t for F = {3,7,...,R}, and verify min rho > R by brute force.
import sys
from math import lcm
from sympy import isprime, divisors
R=int(sys.argv[1]); cnt=int(sys.argv[2])
F=list(range(3,R+1,4)); Q=24
for r in F: Q=lcm(Q,r*(r+1))
print("R",R,"Q",Q)
def works(N,rho):
    D=divisors(N); return any((a+b)%rho==0 for a in D for b in divisors(N//a))
found=0; t=0
while found<cnt:
    t+=1; p=Q*t+1
    if not isprime(p): continue
    if all(isprime(1+(Q//(r+1))*t) for r in F):
        m=next(rho for rho in range(3,4*p,4) if works((p+rho)//4,rho))
        print("t",t,"p",p,"min rho",m, "OK" if m>R else "CONTRADICTION"); found+=1
