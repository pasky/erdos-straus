# For primes p = 1 mod 8: claim: witnesses g>p exist iff (p+1)/2 has a prime factor = 3 mod 4; and all such g are g = p+a (BN) with a | p+1, (p+1)/a = 3 mod 4.
from sympy import isprime, factorint
def wit_big(p):
    out=[]
    for g in range(p+2, 2*p+2, 4):
        if g%4!=3: continue
        Q=(g+1)//4; r=g-p%g
        if Q%r==0: out.append(("BN",g,r))
        i4=pow(4,-1,g); r2=(-p*i4)%g
        if r2 and Q%r2==0: out.append(("B4",g,r2))
    return out
bad=0
for p in range(17, 6000, 8):
    if not isprime(p): continue
    W=wit_big(p); u=(p+1)//2
    has3=any(q%4==3 for q in factorint(u))
    if (len(W)>0)!=has3: print("MISMATCH",p,W,has3); bad+=1
    for (b,g,r) in W:
        if b!="BN" or (p+1)%(g-p) or ((p+1)//(g-p))%4!=3: print("SHAPE",p,b,g,r); bad+=1
print("bad",bad)
