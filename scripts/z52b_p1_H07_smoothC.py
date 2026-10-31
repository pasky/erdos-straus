# Z2582: smoothness of C (and of 4uB) in (★) solutions 4uBC-u-B=p at sample primes.
# R(p) counts ordered (u,B,C); here enumerate all ordered (u,B) via B | p+u, B ≡ -(p+u) mod 4u.
import sys, math, random
from sympy import divisors, factorint, isprime, nextprime
def Pplus(n):
    return max(factorint(n)) if n>1 else 1
def sols(p):
    out=[]
    u=1
    while 4*u-u-1<=p:
        for B in divisors(p+u):
            if (p+u+B)%(4*u*B)==0:
                C=(p+u+B)//(4*u*B); out.append((u,B,C))
        u+=1
        if 4*u*1-u-1>p: break
        if u*u>p: # need 4uB-u-B<=p with B>=1 always true for u<=p/3; but B|p+u large u still possible
            pass
    return out
def sols_fast(p):
    # ordered (u,B): 4uB C = p+u+B >= 4uB  => (4u-1)B <= p+u. enumerate both u<=B via u<=sqrt and swap.
    out=set()
    u=1
    while (4*u-1)*u <= p+u:
        for B in divisors(p+u):
            if B>=u and (p+u+B)%(4*u*B)==0:
                C=(p+u+B)//(4*u*B); out.add((u,B,C)); out.add((B,u,C))
        u+=1
    return sorted(out)
random.seed(1)
hard=[409,577,5569,9601,23929,83449,102001,329617,712321,8813281]
rows=[]
for p in [p for p in hard]+[nextprime(random.randrange(10**k,2*10**k)) for k in (6,7,8,9) for _ in range(3)]:
    if p%4!=1:
        while p%4!=1: p=nextprime(p)
    S=sols_fast(p); L=math.log(p)
    if not S: print(p,"R=0"); continue
    Cs=[c for (_,_,c) in S]
    sm=lambda y: sum(1 for c in Cs if Pplus(c)<=y)/len(Cs)
    fr01=sm(p**0.1); frL2=sm(L*L); frC1=sum(1 for c in Cs if c==1)/len(Cs)
    print(f"p={p} R={len(S)} R/L^2={len(S)/L/L:.3f} frac P+(C)<=p^0.1: {fr01:.2f}  <=log^2p: {frL2:.2f}  C=1: {frC1:.2f}  maxC={max(Cs)}",flush=True)
