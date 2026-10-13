"""R181: control for review_dr_kpow — (P/f)_k for true Type II P vs random monic P of same degree (q = 7)."""
import random
from review_dr_ff import FF, jacobi
random.seed(5); F=FF(7); cnt={}
for _ in range(500):
    A=F.norm([random.randrange(7)]+[1]); a=F.norm([random.randrange(7),1]); d=(1,); c=(1,)
    b=F.norm([random.randrange(7),1])
    if F.gcd(a,b)!=(1,): continue
    E=F.add(a,b); Aad=F.mul(A,F.mul(a,d)); P=F.sub(F.mul(Aad,b),E); f=F.sub(F.mul(Aad,c),(1,))
    Pr=F.norm(list(P[:-1])[:0]+[random.randrange(7) for _ in range(len(P)-1)]+[1])
    if F.gcd(Pr,f)!=(1,): continue
    for k in (2,3,6):
        cnt[(k,'true',jacobi(F,P,f,k))]=cnt.get((k,'true',jacobi(F,P,f,k)),0)+1
        cnt[(k,'rand',jacobi(F,Pr,f,k))]=cnt.get((k,'rand',jacobi(F,Pr,f,k)),0)+1
print(sorted(cnt.items()))
