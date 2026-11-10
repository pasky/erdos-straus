# z69 TWIST triage, I10 / IDEAA #10: every Type I point (a,d,f): f | 4a^2 d + 1, f == -p (mod 4ad), f>0
# has Jacobi (d/p) = -1 (Lemma T10).  Hence no Type I point has p | 4a^2 d + 1 (negative-Pell substitution, any d).
import sys
from sympy import primerange, jacobi_symbol, divisors
P=int(sys.argv[1]); AD=int(sys.argv[2])
npts=0; bad=0; pellpts=0
for p in primerange(5,P):
    if p%4!=1: continue
    for a in range(1,AD+1):
        for d in range(1,AD//a+1):
            N=4*a*a*d+1; m=4*a*d
            for f in divisors(N):
                if (f+p)%m==0:
                    npts+=1
                    if jacobi_symbol(d,p)!=-1: bad+=1; print("VIOLATION",p,a,d,f)
                    if N%p==0: pellpts+=1
print(f"primes p==1(4) < {P}, a*d <= {AD}: Type I points {npts}, with (d/p) != -1: {bad}, with p | 4a^2d+1: {pellpts}")
sys.exit(1 if (bad or pellpts) else 0)
