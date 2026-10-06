"""LS7 Prop 5.1 spot check: (a,D) class a=pq, D=l has large H* (mod pql) but residue -4l mod p (EVIDENCE)."""
from math import gcd
def hstar(b,G,Hmax):
    best=None
    for s in range(1,Hmax+1):
        if gcd(s,G)!=1: continue
        r=(-b*s)%G   # b = -r/s  => r = -b s mod G
        h=max(r,s)
        if best is None or h<best: best=h
        if s>best: break
    return best
for (p,ap,l) in [(101,103,7),(1009,1013,11),(10007,10009,13)]:
    G=p*ap*l; a=p*ap
    # class: x = -4l mod a, x = -a mod l
    x=[y for y in range(-4*l % a, G, a) if (y+a)%l==0][0]
    print(p,ap,l,"G",G,"H*",hstar(x,G,10**6),"res mod p",x%p,(-4*l)%p)
