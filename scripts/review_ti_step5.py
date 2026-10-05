# R31: check the H-step identity: if N=p^2+4ck^2 = f*R, f = B-smooth part, R prime > B, then
# M_{c,k}(p) = 2*#{D | f : D = -p (mod 4ck)}  (real factorisation, random p)
import random
from sympy import isprime, factorint, divisors, nextprime
random.seed(1); B=60; n=0; bad=0
for _ in range(3000):
    p=nextprime(random.randrange(10**6,10**9))
    for c in range(1,8):
        for k in range(1,6):
            h=4*c*k; N=p*p+4*c*k*k; f=1; R=N
            for l,v in factorint(N, limit=B+1).items():
                if l<=B: f*=l**v; R//=l**v
            if R<=B or not isprime(R): continue
            n+=1
            Mreal=sum(1 for D in divisors(N) if (D+p)%h==0)
            Mf=2*sum(1 for D in divisors(f) if (D+p)%h==0)
            if Mreal!=Mf: bad+=1; print("BAD",p,c,k)
print("cases",n,"bad",bad)
