"""R176: cross-check the Type I slice criterion used in review_dd_slices.c against the direct ET definition.
Direct: a>=1, f=4acd-p>0, f | 4a^2 d+1 (e=(4a^2d+1)/f, b=ce-a>=1)."""
from sympy import primerange, divisors
cs=[(1,1),(1,2),(1,3),(1,6),(2,1),(2,3),(3,1),(3,2),(6,1)]
bad=0; n=0
for p in primerange(5,700):
    for c,d in cs:
        M=4*c*d
        crit=any((f+p)%M==0 for f in divisors(p*p+4*c*c*d))
        direct=False
        for a in range(1,(p*p+4*c*c*d+p)//M+2):
            f=4*a*c*d-p
            if f>0 and (4*a*a*d+1)%f==0:
                e=(4*a*a*d+1)//f; b=c*e-a
                assert b>=1 and 4*a*b*d==p*e+1 and a+b==c*e
                direct=True; break
        n+=1; bad+= crit!=direct
print("slice tests",n,"criterion mismatches",bad)
