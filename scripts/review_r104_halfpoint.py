# R104 from-scratch: exact m-representability of primes p via x-loop + divisor
# parametrisation (Ay-B)(Az-B)=B^2 (independent of the author's PW-criterion scanner).
# Usage: m L  -> proportion of representable primes p in (e^L/2, e^L], p∤m (all primes).
import sys, math
from sympy import primerange, factorint
from fractions import Fraction
def two_unit(A,B):
    # does A/B (reduced) = 1/y+1/z ? need divisor D of B^2 with D ≡ -B (mod A), y=(B+D)/A
    f=factorint(B); ps=list(f.items()); divs=[1]
    for p,e in ps:
        divs=[d*p**k for d in divs for k in range(2*e+1)]
    t=(-B)%A
    return any(D%A==t for D in divs)
def rep(m,p):
    for x in range(p//m+1, 3*p//m+1):
        fr=Fraction(m,p)-Fraction(1,x)
        if fr<=0: continue
        if two_unit(fr.numerator,fr.denominator): return True
    return False
m=int(sys.argv[1]); L=float(sys.argv[2]); N=int(math.exp(L))
ps=[p for p in primerange(N//2+1,N+1) if m%p][::int(sys.argv[3]) if len(sys.argv)>3 else 1]
r=sum(rep(m,p) for p in ps)
print("m=%d L=%.2f N=%d primes=%d rho_rep=%.3f"%(m,L,N,len(ps),r/len(ps)))
