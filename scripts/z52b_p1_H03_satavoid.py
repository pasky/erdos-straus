# Z1376: the proposed SAT instance ("p ≡ 1 mod 840, no (u,C) ≤ K certificate") is a pure CRT avoidance system:
# each (u,C) forbids one class p ≡ -u mod 4uC-1. p ≡ 1 mod lcm(all moduli) always satisfies it (since 4uC-1 > u+1),
# so the instance is never UNSAT. Here: least primes satisfying it for K = 20, 40, and their full R(p).
import subprocess
from sympy import isprime
for K in (20,40):
    mods=[(u,4*u*C-1) for u in range(1,K+1) for C in range(1,K+1)]
    found=[]
    p=1
    while len(found)<3:
        p+=840
        if all((p+u)%m for u,m in mods) and isprime(p):
            R=len(subprocess.run(['/tmp/h03certs',str(p)],capture_output=True,text=True).stdout.splitlines())
            found.append((p,R))
    print('K',K,'least avoiders (p, R(p)):',found)
