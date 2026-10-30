"""Sanity checks for claims used in free_fable items (small ranges)."""
from sympy import primerange, factorint, divisors
def typeII_direct(p, B):
    # x=pX,y=pY, z = pXY/(4XY-X-Y); X<=Y
    sols=set()
    for X in range(1,B):
        for Y in range(X,B):
            den=4*X*Y-X-Y
            if den<=0: continue
            if (p*X*Y)%den==0: sols.add((X,Y))
    return sols
def wins_C(p,C):
    N=4*C*p+1
    return any(d%(4*C)==4*C-1 for d in divisors(N))
def typeI_direct(p,B):
    # x=pX, (4X-1)/(pX) = 1/y+1/z  -> y,z: (4X-1)y - pX  | (pX)^2 ... brute: y from ceil(pX/(4X-1)) up
    sols=set()
    for X in range(1,B):
        a=4*X-1; m=p*X
        # 1/y+1/z = a/m -> (a y - m)(a z - m) = m^2
        for d in divisors(m*m):
            if d>m: break
            if (d+m)%a==0 and (m*m//d+m)%a==0:
                sols.add(X)
    return sols
bad=0; c1=0; c1crit=0
for p in primerange(5,1500):
    if p%4!=1: continue
    t2=len(typeII_direct(p,60))>0
    w=any(wins_C(p,C) for C in range(1,60))
    if t2!=w: print("mismatch TypeII vs C-criterion",p,t2,w); bad+=1
    # C=1 criterion
    N=4*p+1
    crit=any(q%4==3 for q in factorint(N))
    if wins_C(p,1)!=crit: print("C=1 crit mismatch",p); bad+=1
    if wins_C(p,1): c1+=1
print("done, mismatches:",bad, "C=1 wins fraction:", c1, "of primes 1 mod 4 <1500")
# gcd lemma: gcd(4Cp+1,4C'p+1) | 4(C'-C)
import math
ok=all(( (4*(C2-C1)) % math.gcd(4*C1*p+1,4*C2*p+1) )==0 for p in [13,17,29,1009] for C1 in range(1,30) for C2 in range(C1+1,30))
print("gcd lemma:",ok)
# T1: odd squares uncovered by C-criterion for C<100
print("odd squares uncovered C<100:", all(not any(wins_C(m*m,C) for C in range(1,100)) for m in range(3,40,2)))
# subgroup vs subset product disagreement (gate G4)
from itertools import combinations
def subset_products(fs,m):
    S={1}
    for q,e in fs.items():
        S={ (s*pow(q,k,m))%m for s in S for k in range(e+1)}
    return S
dis=0;tot=0
for p in primerange(5,3000):
    if p%4!=1: continue
    for C in range(1,40):
        m=4*C; N=4*C*p+1; fs=factorint(N)
        S=subset_products(fs,m)
        # subgroup generated
        G={1}; frontier=[1]
        gens=[q%m for q in fs]
        while frontier:
            x=frontier.pop()
            for g in gens:
                y=(x*g)%m
                if y not in G: G.add(y); frontier.append(y)
        a=(m-1) in S; b=(m-1) in G
        tot+=1
        if a!=b: dis+=1
print("G4 disagreements (subgroup has -1 but subset-products don't):",dis,"of",tot)

# --- later additions (run separately; see BRAINSTORM/z52b_free_fable.md header) ---
# (a) C-form exceptions below 20000: 409, 577, 5569, 9601 (no certificate for C <= 60000)
# (b) every C-form divisor a has jacobi(a,p) = -1 (1798 certificates, p<3000, C<80)
# (c) rich failures (Omega>=5, p<6000, C<150): 4182 total, 1651 subgroup-type (39%)
# (d) Type I c=1 exceptions below 20000 (d<1500): [2521]; 409,577,5569,9601 certified by (d,f)=(11,75),(5,3),(17,7),(67,851)
# (e) reparametrisation verified: C-form certificate (C,a=4Cu-1) <-> a | p+u, a = -1 mod 4u  (p<800 existence; p=1009 bijection)
# (f) 409: no u<=60000 with a divisor of 409+u congruent to -1 mod 4u; expected count sum tau(4*409*C+1)/phi(4C), C<=60000 = 51.8
