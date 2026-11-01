# z52d pass2 TO4 lint-fix B: Z1025 (target-matched), Z1053 (pretentious distance), Z1057 (walk vs exact reachability),
# Z1299 (coefficient residues of winner counts), Z1301/Z1300 (Lambert-series identity), Z1286 (conic fibration sections),
# Z1675/Z1676 (singular fibres of conic bundle y=tz), Z1677 (node distances), Z1152 (braid refactorisation),
# Z1304 (Brandt/class numbers), Z1178 (x=(p+k)/4 bounded-k residual two-term test)
import math, statistics, sys, itertools
from collections import defaultdict, Counter
from fractions import Fraction
from sympy import primerange, factorint, divisors, symbols, Poly, factor, Matrix, simplify, cancel, legendre_symbol, jacobi_symbol
import sympy as sp
rows={}
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); rows[t[0]]=set(t[2:2+t[1]])
P24=[p for p in sorted(rows) if p%24==1 and 10**4<=p<=10**6]
# ---- Z1025 target-matched: P(win(C)|win(C1),win(C2)) vs P(win(C)) for the same C
for name,op in [("C1*C2",lambda x,y:x*y),("lcm",lambda x,y:x*y//math.gcd(x,y))]:
    a=b=0; exc_num=0; exc_den=0
    margin=defaultdict(lambda:[0,0])
    for p in P24:
        W=rows[p]
        for C1 in range(1,21):
            for C2 in range(C1+1,21):
                C=op(C1,C2)
                if C>400 or C in (C1,C2): continue
                if C1 in W and C2 in W:
                    a+=1; b+= (C in W)
    base_C=statistics.mean((sum(1 for p in P24 if C in rows[p])/len(P24)) for C in range(1,401))
    print("Z1025 %s: n=%d  P(win(C)|win(C1),win(C2))=%.3f  vs unconditional mean over C-values of P(win(C))=%.3f"%(name,a,b/a,base_C))
# ---- Z1053: pretentious distance of factor-sign pattern (q/p), q≤100, to a library of Kronecker characters
def kron(D,q):
    from sympy.ntheory import jacobi_symbol as J
    if q==2:
        if D%2==0: return 0
        return 1 if D%8 in (1,7) else -1
    return J(D % q, q) if D%q else 0
library=[-4,8,-8,-3,5,-7,12,-11,13,-15,17,-19,21,-23,24,-20,28,-24,-31,33]
Qs=[q for q in primerange(3,101)]
dists={}
sample=[p for p in P24[:4000]]
rowsD=[]
for p in sample:
    sig={q: (1 if legendre_symbol(p%q,q)==1 else -1) for q in Qs}  # (p/q) = (q/p) up to reciprocity; this is the factor-sign pattern
    best=(1.0,None)
    for D in library:
        agree=sum(1 for q in Qs if kron(D,q)==sig[q])/len(Qs)
        best=min(best,(1-agree,D))
    rowsD.append((best[0],best[1],p))
dd=[r[0] for r in rowsD]
print("Z1053 p≡1 mod 24 (n=%d): min disagreement with library of Kronecker chars, median %.3f ; fraction with ≤0.10: %.3f"%(len(dd),statistics.median(dd),sum(1 for x in dd if x<=0.10)/len(dd)))
# correlation of pretentiousness with win count
wc=[len(rows[p]) for _,_,p in rowsD]
import numpy as np
print("Z1053 corr(min disagreement, #wins C≤400) = %.3f"%np.corrcoef(dd,wc)[0,1])
# ---- Z1057 (UNRESTRICTED version; superseded by z52d_p2_TO4_fix_C.py which restricts to -1 in <gens>): unrestricted walk vs exact reachability for C-form failures with -1 in generated group
def walk_mass_at_minus1(gens, m, steps=60):
    G=[a for a in range(1,m) if math.gcd(a,m)==1]
    idx={g:i for i,g in enumerate(G)}
    S=set()
    for g in gens: S.add(g%m); S.add(pow(g,-1,m))  # symmetric steps (inverses included)
    S=list(S)
    v=np.zeros(len(G)); v[idx[1%m]]=1.0
    T=np.zeros((len(G),len(G)))
    for g in G:
        for s in S:
            T[idx[g*s%m], idx[g]]+=1.0/len(S)
    for _ in range(steps): v=T@v
    return v[idx[(m-1)%m]], 1.0/len(G)
gaps=[]; reach_no=0; n=0
for p in primerange(5,8001):
    if p%24!=1: continue
    for C in range(1,41):
        N=4*C*p+1; m=4*C
        f=factorint(N)
        divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        if any(a>1 and a%m==m-1 for a in divs): continue
        gens=[q%m for q in f if math.gcd(q,m)==1]
        if len(f)<3: continue
        n+=1
        mass,unif=walk_mass_at_minus1(gens,m)
        gaps.append((mass,unif))
        reach_no+=1  # exact reachability: -1 not a divisor class (no winner) -> exact reach 0 for this divisor set
print("Z1057 failures (no winner; p≡1 mod 24 ≤8000, C≤40, ω≥3; n=%d): walk (60 steps, inverses included) mass at -1: median %.4f; exact divisor-reachability of -1: 0 in all %d"%(n, statistics.median([g[0] for g in gaps]), reach_no))
print("Z1057 fraction of failures where walk mass at -1 exceeds 1/10: %.3f"%(sum(1 for g in gaps if g[0]>0.1)/len(gaps)))
# ---- Z1299: residues of winner counts r(p,C)=#{a|N: a≡-1 mod 4C} (ordered) mod 2 and mod 4
res=Counter(); sq=0
for p in primerange(5,20001):
    if p%24!=1: continue
    for C in range(1,41):
        N=4*C*p+1; m=4*C
        f=factorint(N); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        r=sum(1 for a in divs if a>1 and a%m==m-1)
        is_sq = math.isqrt(N)**2==N
        res[(r%4, is_sq)]+=1
print("Z1299 distribution of r(p,C) mod 4 by (N square?):", dict(res))
# ---- Z1301/Z1300: Lambert identity sum_{X,Y≡-1 (4C), X,Y≥1} q^{XY} ; coefficient at 4Cp+1 = ordered winner count
def coeffs(C, Nmax):
    c=[0]*(Nmax+1)
    for X in range(4*C-1, Nmax+1, 4*C):
        for Y in range(4*C-1, Nmax//X+1, 4*C):
            c[X*Y]+=1
    return c
ok=True; checks=[]
for C in (1,2,3,4):
    Nmax=4*C*200+1
    c=coeffs(C,Nmax)
    for p in [5,13,17,29,37,41,53,61,73,89,97,101]:
        n=4*C*p+1
        if n>Nmax: continue
        f=factorint(n); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        r=sum(1 for a in divs if a>1 and a%(4*C)==4*C-1)
        if c[n]!=r: ok=False
        checks.append((C,p,c[n]))
print("Z1301 Lambert coefficient at 4Cp+1 equals ordered winner count (C≤4, small p):", ok, "examples", checks[:6])
# ---- Z1286: conic fibration y=t·z of ES surface; integral sections; count ES solutions with y/z=a/b (small a,b)
def es_sols_with_ratio(p, a, b, zmax):
    out=[]
    # y=a k, z=b k  (y/z=a/b);  4xyz=p(xy+yz+zx) ⇒ solve for x: x(4yz - p(y+z)) = p y z
    for k in range(1, zmax//max(a,b)+1):
        y=a*k; z=b*k
        den=4*y*z-p*(y+z)
        if den==0: continue
        num=p*y*z
        if num%den==0:
            x=num//den
            if x>0: out.append((x,y,z))
    return out
tot=0; per={}
for p in [409,577,1009,1321,2521]:
    cnt=0
    for a in range(1,7):
        for b in range(1,7):
            if math.gcd(a,b)!=1: continue
            cnt+=len(es_sols_with_ratio(p,a,b,4*p*p))
    per[p]=cnt
print("Z1286 integer points on the pencil y/z=a/b (a,b≤6, coprime) via section x=pyz/(4yz-p(y+z)): ", per)
# ---- Z1675/Z1676: conic bundle of the cubic 4xyz=p(xy+yz+zx)w along the pencil of planes y=t z (through line y=z=0)
t,x,z,w=symbols('t x z w')
p_=sp.symbols('p')
F=4*x*(t*z)*z - p_*(x*(t*z)*w + (t*z)*z*w + z*x*w)   # F with y=t z, homogenised with w
F=sp.factor(sp.expand(F))
conic=sp.factor(F/z)
print("Z1675 residual conic on y=tz (after dividing the line z=0):", conic)
Mc=sp.hessian(sp.expand(conic),(x,z,w))/2
dis=sp.factor(sp.simplify(Mc.det()))
print("Z1675 determinant of conic matrix (degenerate fibres at roots):", dis)
for pv in [409,577,1009]:
    dpoly=sp.Poly(sp.expand(dis.subs(p_,pv)),t)
    fl=sp.factor_list(dpoly.as_expr())
    print("Z1676 p=%d: degenerate-fibre polynomial in t factors over Q as"%pv, fl)
# (Z1677 node-chart analysis: see z52d_p2_TO4_fix_D.py)
# ---- Z1152 (trivial-commutation version; superseded by fix_C nontrivial braid count): braid refactorisation L(a)U(b)L(c) = U(c')L(b')U(a') over Z: count integral partners in small box
def mul(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def L(a): return [[1,0],[a,1]]
def U(a): return [[1,a],[0,1]]
bad=0; tot=0; examples=[]
B=12
partner={}
for a,b,c in itertools.product(range(-B,B+1),repeat=3):
    M=mul(mul(L(a),U(b)),L(c))
    partner.setdefault(tuple(map(tuple,M)),[]).append((a,b,c))
integral_partners=0; total=0
for key,lst in partner.items():
    total+=1
    if len(lst)>1: integral_partners+=1
print("Z1152 matrices L(a)U(b)L(c) (|·|≤12): %d distinct, %d with >1 factorisation (nontrivial refactorisation); example:"%(total,integral_partners), next((lst for lst in partner.values() if len(lst)>1),None))
# ---- Z1304: Brandt/Eichler class number of maximal order in B_{p,∞}: h = (p-1)/12 + (1/4)(1-(-4/p)) + (1/3)(1-(-3/p))
hs=[]
for p in primerange(5,2001):
    h=Fraction(p-1,12)+Fraction(1,4)*(1-legendre_symbol((-4)%p,p) if p>2 else 0)+Fraction(1,3)*(1-legendre_symbol((-3)%p,p) if p>3 else 0)
    hs.append((p,h))
print("Z1304 Eichler class number h(B_{p,∞}) examples:", [(p,str(h)) for p,h in hs if p in (409,577,1009,1321,2521,1993)])
# ---- Z1178: x=(p+k)/4, residual 4k/(p(p+k)) ; for bounded k, is it two-term? (divisor condition with a=numerator ≤4k)
def two_term_exists(num,den):
    g=math.gcd(num,den); a=num//g; b=den//g
    for e in divisors(b*b):
        f=(b*b)//e
        if (e+b)%a==0 and (f+b)%a==0: return True
    return False
res178={}
for k in range(1,9):
    ok=0; tot=0
    for p in primerange(1000,6000):
        if p%4!=1 or (p+k)%4!=0: continue
        tot+=1
        if two_term_exists(4*k, p*(p+k)): ok+=1
    res178[k]=(ok,tot)
print("Z1178 x=(p+k)/4 (k≤8): primes with two-term residual 4k/(p(p+k)) :", res178)
