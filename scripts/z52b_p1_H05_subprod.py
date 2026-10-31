# Z1904: per-level hit probability P(-1 ∈ divisor classes of N=4Cp+1 mod 4C) vs random subset-product models.
# Model A: k iid uniform units mod m=4C. Model B: same, conditioned on product ≡ 1 (since N ≡ 1 mod m).
# Empirical: primes p≡1 (4) in [X, X+W), squarefree N, grouped by (C, k=ω(N)).
import sys, random, math
from sympy import factorint, primerange
from collections import defaultdict
X=int(sys.argv[1]); W=int(sys.argv[2]); Cs=[1,2,3,5,6,7,10,15]
random.seed(0)
def units(m): return [a for a in range(1,m) if math.gcd(a,m)==1]
def hit(m, gs):
    S={1}
    for g in gs: S|={s*g%m for s in S}
    return (m-1) in S
def model(m,k,cond,T=20000):
    U=units(m); h=n=0
    while n<T:
        gs=[random.choice(U) for _ in range(k)]
        if cond and math.prod(gs)%m!=1: continue
        n+=1; h+=hit(m,gs)
    return h/n
emp=defaultdict(lambda:[0,0])
for p in primerange(X,X+W):
    if p%4!=1: continue
    for C in Cs:
        m=4*C; f=factorint(m*p+1)
        if any(e>1 for e in f.values()): continue
        k=len(f); r=emp[(C,k)]; r[1]+=1; r[0]+=hit(m,[q%m for q in f])
print("C k  n_emp  emp   modelA  modelB(prod=1)")
for (C,k),(h,n) in sorted(emp.items()):
    if n<40: continue
    print(C,k,n,round(h/n,3),round(model(4*C,k,False),3),round(model(4*C,k,True),3))
