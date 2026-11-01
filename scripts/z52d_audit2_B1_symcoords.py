# Z0980: ES in symmetric coordinates s1=x+y+z, s2=xy+yz+zx, s3=xyz, 4 s3 = p s2.
# (a) enumerate all solutions x<=y<=z of 4/p for primes p≡1(4) <= PMAX, record min s1 / p^{3/2}, s2 mod stuff, disc.
# (b) for tiny p, a direct (s1,s2) box search for cubics T^3 - s1 T^2 + s2 T - p s2/4 with 3 positive integer roots reproduces (a).
import sys, math
from sympy import primerange, divisors
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 3000
def sols(p):
    out=[]
    for x in range(p//4+1, 3*p//4+1):           # 1/x >= 4/(3p)
        a=4*x-p; b=p*x                           # 1/y+1/z = a/b
        if a<=0: continue
        # y in [b/a, 2b/a]; (a y - b)(a z - b) = b^2
        for d in divisors(b*b):
            if d*d> b*b: break
            if (d+b)%a==0 and (b*b//d+b)%a==0:
                y=(d+b)//a; z=(b*b//d+b)//a
                if y>=x: out.append((x,y,z))
    return out
worst=[]
for p in primerange(5,PMAX):
    if p%4!=1: continue
    S=sols(p)
    s1min=min(sum(s) for s in S)
    disc_sq=all(True for s in S)
    worst.append((s1min/p**1.5,p,len(S),s1min))
    for (x,y,z) in S:
        s1=x+y+z; s2=x*y+y*z+z*x; s3=x*y*z
        assert 4*s3==p*s2 and s2%4==0
worst.sort()
print('min over p of (min s1)/p^1.5:',worst[:5]); print('max:',worst[-3:])
# (b) box search for p=5,13
for p in (5,13,17):
    S=set(tuple(s) for s in sols(p)); found=set()
    B=max(sum(s) for s in S)
    for s1 in range(3,B+1):
        # integer root x of T^2(T-s1)+s2(T-p/4): s2 = 4x^2(s1-x)/(4x-p) for x>p/4
        for x in range(p//4+1,s1):
            num=4*x*x*(s1-x); den=4*x-p
            if num%den: continue
            s2=num//den
            # remaining quadratic T^2-(s1-x)T + (s2 - x(s1-x))
            q1=s1-x; q2=s2-x*q1; D=q1*q1-4*q2
            if D<0: continue
            r=math.isqrt(D)
            if r*r!=D or (q1+r)%2: continue
            y,z=(q1-r)//2,(q1+r)//2
            if y>=x and y>0: found.add((x,y,z))
    print(p,'box search reproduces enumeration:',found==S,len(S))
