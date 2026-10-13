"""Type II certificates at primes p = 1 mod 4: ff' - 4c^2 d p = 1, f = f' = -1 (mod 4cd).
Check the Gamma_0(4)-conjugate theta multiplier sign (p/f') = (f'/p) = -1 on every certificate.
usage: python bsB_typeII_mult.py PMAX"""
import sys
from sympy import primerange, divisors, jacobi_symbol as J
P=int(sys.argv[1]); cnt=bad=0
for p in primerange(5,P):
    if p%4!=1: continue
    for c in range(1,p):
        for d in range(1,p):
            b=4*c*c*d; N=b*p+1; q=4*c*d
            if q>N: break
            for f in divisors(N):
                ff=N//f
                if (f+1)%q==0 and (ff+1)%q==0:
                    cnt+=1
                    if J(p,ff)!=-1 or J(ff%p,p)!=-1: bad+=1
        if 4*c*c*p+1<16*c*c: break
print(f"certificates={cnt} violations={bad}")
