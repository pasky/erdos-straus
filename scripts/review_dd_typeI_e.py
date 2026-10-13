"""R176: Type I tuples (a<=b) of primes p<P: check e <= (p+1)^2+1 (Prop 1.3), whether p | e ever occurs, and
4dm-1 = pe (m=ab). Loop: a d <= (p+1)/2, f | 4a^2 d+1, f = -p (4ad), c=(f+p)/4ad, e=(4a^2d+1)/f, b=ce-a."""
import sys
from sympy import primerange, divisors
P=int(sys.argv[1]); tot=0; pe=0; big=0; ratio=0
for p in primerange(5,P):
    for a in range(1,(p+1)//2+1):
        for d in range(1,(p+1)//(2*a)+2):
            for f in divisors(4*a*a*d+1):
                if (f+p)%(4*a*d): continue
                c=(f+p)//(4*a*d); e=(4*a*a*d+1)//f; b=c*e-a
                if b<a: continue
                assert 4*a*b*d==p*e+1 and a+b==c*e
                tot+=1; pe+= e%p==0; big+= e>(p+1)**2+1; ratio=max(ratio,e/p**2)
print(f"Type I tuples p<{P}: {tot}; with p|e: {pe}; e>(p+1)^2+1: {big}; max e/p^2 = {ratio:.3f}")
