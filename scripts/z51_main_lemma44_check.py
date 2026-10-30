from fractions import Fraction as F
from sympy import isprime, factorint
import random, itertools, math
random.seed(7)
ok=0
for S in ([3,7],[3,7,11],[3,11,19],[7,19]):
    P=math.prod(S)
    ells=[l for l in range(4*P-1,4*P*400,4*P) if isprime(l)][:15]
    for l in ells:
        A=(l+1)//4
        for a in itertools.product(range(4),repeat=len(S)):
            Q=math.prod(s**e for s,e in zip(S,a)); D=Q*Q
            r0=(-4*D)%l
            for k in range(6):
                n=r0+l*random.randrange(1,10**6)
                if n%2==0 or math.gcd(n,P)>1: continue
                V=(n+4*D)//l; assert (n+4*D)%l==0
                x=(n+V)//4; assert (n+V)%4==0
                y=n*A; z=F(n*x*A,D)
                assert F(4,n)==F(1,x)+F(1,y)+1/z
                r=math.prod(s**max(0,e-factorint(A).get(s,0)) for s,e in zip(S,a))
                assert z.denominator==r*r, (S,l,a,n)
                ok+=1
print("ok",ok)
