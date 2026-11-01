"""z52d avenue Q04 Z0276: check that every ES solution of 4/p with all denominators Eisenstein norms
(a^2+ab+b^2: primes = 2 mod 3 to even power) has v3(x)=v3(y)=v3(z)>=1. EVIDENCE check of a PROVED valuation lemma."""
from fractions import Fraction
from sympy import factorint, primerange
def isnorm(n):
    return all(e%2==0 for q,e in factorint(n).items() if q%3==2)
def v3(n):
    k=0
    while n%3==0: n//=3; k+=1
    return k
def sols(p):
    out=[]; t=Fraction(4,p)
    for x in range(p//4+1, 3*p//4+1):
        r=t-Fraction(1,x)
        if r<=0: continue
        a,b=r.numerator,r.denominator
        # 1/y+1/z=a/b, y<=z: (a y - b)(a z - b)=b^2
        B2=b*b
        for d,e in [(d,B2//d) for d in divisors(B2)]:
            if d>e: continue
            if (d+b)%a or (e+b)%a: continue
            y=(d+b)//a; z=(e+b)//a
            if y>=x: out.append((x,y,z))
    return out
from sympy import divisors
bad=0; surv=0
for p in primerange(5,700):
    S=[s for s in sols(p) if all(isnorm(v) for v in s)]
    if S:
        surv+=1
        for s in S:
            vs=[v3(v) for v in s]
            if not (vs[0]==vs[1]==vs[2]>=1): bad+=1; print('COUNTEREX',p,s,vs)
print('primes with Eisenstein-norm solution:',surv,' violations:',bad)
