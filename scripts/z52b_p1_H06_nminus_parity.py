"""Z2030: parity of N_-(n) = #{(t,u,v) >= 1 : tuv - u - v = n, chi(w) = (-(tu-1)/n) = -1} (SIGN_IDENTITY notation),
for primes n = p ≡ 1 (4). The involution (t,u,v) -> (t,v,u) preserves chi (AA* = tn+1 ≡ 1 mod n), so N_- ≡ #{u = v, chi = -1}."""
import sys
from sympy import primerange, jacobi_symbol
P=int(sys.argv[1]); odd=[]; cnt=0
for p in primerange(5,P):
    if p%4!=1: continue
    Nm=0
    for u in range(1,p+2):
        for t in range(1,p+3):
            A=t*u-1
            if A<=0: continue
            if A*1-u > p: break           # v >= 1: tuv-u-v = A v - u >= A - u
            if (p+u)%A==0:
                v=(p+u)//A
                if v>=1 and jacobi_symbol((-A)%p,p)==-1: Nm+=1
    cnt+=1
    if Nm%2: odd.append((p,Nm))
print('primes p≡1(4) <',P,':',cnt,' with N_- odd:',odd[:10])
