# z69 TWIST round 2: exact checks of the two structure lemmas for G_d(p) (d = 1, 3, 5).
#  Lemma CS (complement swap): if 4ad | p - 1 and (a,b,c) is a solution with A = 4acd - 1, e = (p + 4a^2 d)/A, then
#     e == -1 (4ad), (a, b', c') with 4ac'd - 1 = e is a solution, and  class[A,4ad,de] * class[e,4ad,dA] = T_d := class[d,0,p].
#     Hence T_d * g lies in G for every g of such a fibre (G is inversion-closed).
#  Lemma DL (divisor lattice): if A and l*A are divisors of p + 4a^2 d, both == -1 (4ad) (l prime, l == 1 mod 4ad), then
#     class(l*A) = class(A) * class of the prime ideal (l, 2ad + sqrt(-dp)).
# Output per window: O(T_d) summed, the part predicted by CS, and the number of violations (must be 0).
import sys
sys.path.insert(0,'scripts')
from sympy import divisors, primerange, isprime
from z69_twist_i17 import reduce, compose_std
from z69_twist_i17b import Grp
def sols(p,d):
    out=[]; e=3; emax=(p+4*d)//(4*d-1)
    while e<=emax:
        if (p+e)%(4*d)==0:
            x=(p+e)//(4*d)
            for a in divisors(x):
                b=x//a
                if (a+b)%e==0: out.append((a,b,(a+b)//e,e))
        e+=4
    return out
d=int(sys.argv[1]); P0=int(sys.argv[2]); P1=int(sys.argv[3])
tot=dict(n=0,k=0,OT=0,cs=0,viol=0,dl=0,dlviol=0,allcs=0,stab=0)
for p in primerange(P0,P1):
    if p%8!=1: continue
    S=sols(p,d)
    if len(S)<2: continue
    D=-4*d*p; G=Grp(D); cls={}
    for (a,b,c,e) in S: cls[(a,b,c)]=G.coords[reduce(4*a*c*d-1,4*a*d,d*e)]
    X=set(cls.values()); T=G.coords[reduce(d,0,p)] if d>1 else G.one
    tot['n']+=1; tot['k']+=len(X)
    OT=sum(1 for x in X if G.add(x,T) in X) if d>1 else 0; tot['OT']+=OT
    csset=set()
    for (a,b,c,e) in S:
        g=cls[(a,b,c)]
        if (p-1)%(4*a*d)==0:
            A=4*a*c*d-1
            ok=(e+1)%(4*a*d)==0
            if ok:
                c2=(e+1)//(4*a*d); b2=(p+A)//(4*a*d)
                ok = (p+A)%(4*a*d)==0 and (a,b2,c2) in cls and G.add(g,cls[(a,b2,c2)])==T
            if not ok: tot['viol']+=1
            csset.add(g); csset.add(G.negd[g])
        # DL
        Na=p+4*a*a*d; A=4*a*c*d-1
        for l in (q for q in divisors(Na//A) if q>1 and isprime(q) and q%(4*a*d)==1):
            c3=(l*A+1)//(4*a*d)
            key=[k for k in cls if k[0]==a and k[2]==c3]
            if not key: tot['dlviol']+=1; continue
            Lc=G.coords[reduce(l,(4*a*d)%(2*l),(( (4*a*d)%(2*l))**2+4*d*p)//(4*l))]
            tot['dl']+=1
            if G.add(g,Lc)!=cls[key[0]]: tot['dlviol']+=1
    if d>1:
        tot['cs']+=sum(1 for x in X if x in csset and G.add(x,T) in X)
        if X<=csset: tot['allcs']+=1
        if all(G.add(x,T) in X for x in X): tot['stab']+=1
print(f"d={d} primes p==1(8) in [{P0},{P1}) with >=2 solutions: {tot['n']}; sum|G|={tot['k']}; sum O(T_d)={tot['OT']}, of which in CS fibres (4ad | p-1): {tot['cs']}; "
      f"CS violations: {tot['viol']}; primes with all classes in CS fibres: {tot['allcs']}, primes with T_d*G = G: {tot['stab']}; DL instances checked: {tot['dl']}, violations: {tot['dlviol']}")
assert tot['viol']==0 and tot['dlviol']==0
