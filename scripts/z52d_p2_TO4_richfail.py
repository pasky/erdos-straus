# z52d pass2 TO4 (Z1598-Z1600): for p ≡ 1 (mod 4) prime ≤ PMAX and C ≤ CMAX with NO C-form winner
# (no divisor a of N=4Cp+1 with a ≡ -1 mod 4C), test whether the prime-factor classes generate a subgroup of
# (Z/4C)^× containing -1. Also tabulate by omega(N). Exact (sympy factorint). Bounded ranges (see summary).
import sys, math
from sympy import factorint, primerange
from collections import Counter
PMAX=int(sys.argv[1]); CMAX=int(sys.argv[2])
def gen_subgroup(gens, m):
    H={1%m}
    for g in gens:
        new=set(H)
        frontier=list(H)
        # close under multiplication by g (finite group: closure = <H,g>)
        cur=set(H)
        mult=g%m
        changed=True
        S=set(H)
        # generate closure of S ∪ {g}
        Q=set(S); elems=set(S)
        todo=[g%m]
        while todo:
            x=todo.pop()
            if x in elems: continue
            elems.add(x)
            for y in list(elems): 
                z=(x*y)%m
                if z not in elems: todo.append(z)
        H=elems
    return H
def has_winner(f, m, N):
    # divisor a of N with a ≡ -1 mod m: enumerate divisors from factorization
    divs=[1]
    for q,e in f.items():
        divs=[d*q**j for d in divs for j in range(e+1)]
    return any(a>1 and a%m==m-1 for a in divs)
stats=Counter(); examples=[]
for p in primerange(5,PMAX+1):
    if p%4!=1: continue
    for C in range(1,CMAX+1):
        N=4*C*p+1; m=4*C
        f=factorint(N)
        if has_winner(f,m,N): continue
        gens=[q%m for q in f if math.gcd(q,m)==1]
        # also account for q dividing m (none: N coprime to 4C since N ≡1 mod 4C)
        H=gen_subgroup(gens,m) if m>2 else {1}
        neg=(m-1)%m in H
        omega=len(f)
        stats[(min(omega,6), 'gen∋-1' if neg else 'gen∌-1')]+=1
        if neg and len(examples)<8: examples.append((p,C,dict(f)))
print("failures (no winner) by omega and subgroup type:")
for k in sorted(stats): print(" ",k,stats[k])
print("examples gen∋-1 but no winner (p,C,factorization):",examples)
