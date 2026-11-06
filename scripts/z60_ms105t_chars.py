# EVIDENCE: for C <= X split #{a | 4Cn+1 : a = -1 mod 4C} into principal-character part tau/phi(4C),
# quadratic part -sum_{a|N}(n/a)/phi(4C) and the remainder E (all other characters).
import sys
from sympy import divisors, totient, jacobi_symbol
X=int(sys.argv[1])
for n in map(int,sys.argv[2:]):
    M=Q=R=0.0
    for C in range(1,X+1):
        N=4*C*n+1; ds=divisors(N); ph=int(totient(4*C))
        M+=len(ds)/ph; Q+=sum(jacobi_symbol(n,a) for a in ds)/ph
        R+=sum(1 for a in ds if a%(4*C)==4*C-1)
    print(n, 'X=%d  main=%.3f  quad=%.3f  main-quad=%.3f  R_X=%d  E=%.3f'%(X,M,Q,M-Q,R,R-(M-Q)))
