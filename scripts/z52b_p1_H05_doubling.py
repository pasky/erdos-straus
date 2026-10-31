# Z1915: doubling K=|Q·Q|/|Q| of divisor quotient sets Q = {a b^{-1} mod 4C : ab | N}, N=4Cp+1 (signed set; -1∈Q iff a level-C
# certificate... note Q is the e-slice ratio set), versus the GAP bound 3^ω and |<Q>| (subgroup generated).
import sys, math
from sympy import factorint, divisors
from collections import Counter
def stats(p,Cmax):
    out=[]
    for C in range(1,Cmax+1):
        m=4*C; N=m*p+1; D=[d%m for d in divisors(N)]
        inv={d:pow(d,-1,m) for d in set(D)}
        Q={a*inv[b]%m for a in set(D) for b in set(D)}
        QQ={x*y%m for x in Q for y in Q}
        H={1}; fr=[1]
        while fr:
            x=fr.pop()
            for g in Q:
                y=x*g%m
                if y not in H: H.add(y); fr.append(y)
        w=len(factorint(N))
        out.append((C,w,len(Q),len(QQ)/len(Q),len(H),(m-1) in Q,(m-1) in H))
    return out
for p in [409,577,8813281, 409+12*4+1-1 if False else 433, 8813281+48]:
    s=stats(p,200)
    Ks=[r[3] for r in s]
    smallK=[r for r in s if r[3]<=1.5 and r[2]>2]
    print(p,"mean K",round(sum(Ks)/len(Ks),2),"max K",round(max(Ks),2),
          "#levels -1∈Q",sum(r[5] for r in s),"#levels -1∈<Q>",sum(r[6] for r in s),
          "#levels K<=1.5,|Q|>2:",len(smallK),"of which -1∈<Q> but ∉Q:",sum(1 for r in smallK if r[6] and not r[5]))
