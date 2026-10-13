"""bsB_rayclass_norm_pullback check: for K=Q(sqrt(-tp)) (t=3 mod 4 squarefree, p=1 mod 4 prime, t,p coprime),
every m >= 1 coprime to tp all of whose prime factors split in K (= a norm of an ideal coprime to tp) with
m = eps (mod t), eps = +-1, has (m/p) = eps  (genus product formula; GI Prop 4.1 is the case m | tp+1).
usage: python bsB_genus_pullback.py TRIALS"""
import sys, random
from sympy import jacobi_symbol as J, isprime, primerange, factorint
random.seed(1); T=int(sys.argv[1]); bad=0; tested=0
sqf=lambda t: all(e==1 for e in factorint(t).values())
ps=[p for p in primerange(5,3000) if p%4==1]
for _ in range(T):
    t=random.choice([x for x in range(3,300,4) if sqf(x)]); p=random.choice(ps)
    if t%p==0: continue
    D=-t*p
    split=[l for l in primerange(3,400) if (t*p)%l and J(D%l,l)==1]
    m=1
    for _ in range(random.randint(1,5)): m*=random.choice(split)
    if m%t in (1,t-1):
        eps=1 if m%t==1 else -1; tested+=1
        if J(m%p,p)!=eps: bad+=1
print(f"tested={tested} violations={bad}")
