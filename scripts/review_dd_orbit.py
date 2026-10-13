"""R176 from scratch: bsC_valence_borcherds numerics. For slices (c,d) in {(1,1),(1,2),(1,3)} and primes 5<=p<P:
#certificate pairs (f<=f', f|1+4c^2dp, f=-1 mod 4cd) / h(D), D=-16c^2 d p, h = # reduced primitive forms."""
import sys
from math import gcd, isqrt
from sympy import primerange, divisors
def h(D):  # D<0, D=0,1 mod 4: count reduced primitive forms (a,b,c), |b|<=a<=c, b>=0 if |b|=a or a=c
    n=0; a=1
    while 3*a*a<=-D:
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a): continue
            c=(b*b-D)//(4*a)
            if c<a or (c==a and b<0): continue
            if gcd(gcd(a,abs(b)),c)!=1: continue
            n+=1
        a+=1
    return n
P=int(sys.argv[1]); worst=(0,None)
for p in primerange(5,P):
    for c,d in ((1,1),(1,2),(1,3)):
        M=4*c*d; N=1+4*c*c*d*p
        k=sum(1 for f in divisors(N) if f*f<=N and (f+1)%M==0)
        r=k/h(-16*c*c*d*p)
        if r>worst[0]: worst=(r,(p,c,d,k))
print("max certificate/h ratio, p<%d:"%P, worst)
