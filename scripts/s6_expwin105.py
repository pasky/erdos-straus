# Exponential window classes for n_s = 4^s + k (default k=105): windows m = 4^j*c - k, so
# K = (n_s+m)/4 = 4^{min(s,j)-1} * (algebraic number). Cap-0 test with KNOWN divisors only
# (2-power, small primes by trial division, algebraic factors 2^{2g}+1, Aurifeuillean halves); every hit is
# rebuilt as an exact ES solution and checked with Fractions. Usage: s6_expwin105.py k S JMAX C...
import sys, math
from fractions import Fraction as F
from sympy import primerange
k=int(sys.argv[1]); S=int(sys.argv[2]); JMAX=int(sys.argv[3]); CS=[int(c) for c in sys.argv[4:]] or [1]
SMALL=list(primerange(3,3000))
def atoms_of(X, extra):
    # coprime basis of X from small primes + gcd refinement with extra factors
    at={}
    for l in SMALL:
        while X%l==0: X//=l; at[l]=at.get(l,0)+1
    parts=[X]
    for f in extra:
        new=[]
        for P in parts:
            g=math.gcd(P,f)
            if 1<g<P: new+= [g,P//g]
            else: new.append(P)
        parts=new
    # merge equal / refine pairwise until coprime
    changed=True
    while changed:
        changed=False
        for i in range(len(parts)):
            for j2 in range(i+1,len(parts)):
                g=math.gcd(parts[i],parts[j2])
                if g>1:
                    a,b=parts[i],parts[j2]; parts=[p for t,p in enumerate(parts) if t not in(i,j2)]+[g,a//g,b//g]; changed=True; break
            if changed: break
    for P in parts:
        if P>1: at[P]=at.get(P,0)+1   # P may be composite; treated as an atom (multiplicity counted crudely)
    return at
def alg_factors(r):
    fs=[]
    for g in range(1,r+1):
        if r%g==0 and (r//g)%2==1: fs.append(4**g+1)
        if r%g==0 and (r//g)%2==1 and g%2==1:
            h=2**((g+1)//2); fs+= [2**g-h+1,2**g+h+1]
    return fs
def try_window(n,m,K):
    if math.gcd(K,n)!=1: return None
    t=0; Kp=K
    while Kp%2==0: Kp//=2; t+=1
    # Kp = c*... + ... ; extra algebraic factors only for the c=1 shape
    return t,Kp
def cap0(n,m,K,atoms):
    # BFS over residues of d1/d2 with |delta| <= mult; want -1 mod m
    reach={1:(1,1)}
    for a,b in atoms.items():
        ai=pow(a,-1,m) if math.gcd(a,m)==1 else None
        if ai is None: continue
        new=dict(reach)
        for r,(d1,d2) in reach.items():
            for dl in range(1,b+1):
                for sgn in (1,-1):
                    rr=r*pow(a if sgn>0 else ai,dl,m)%m
                    if rr not in new: new[rr]=(d1*a**dl,d2) if sgn>0 else (d1,d2*a**dl)
        reach=new
        if (m-1) in reach: break
    return reach.get(m-1)
def check(n,m,K,d1,d2):
    d=K*d1//d2; assert (K*d1)%d2==0 and (K+d)%m==0
    A=(K+d)//m; x=K; y=n*A; z=F(n*K*A,d)
    assert F(4,n)==F(1,x)+F(1,y)+1/z and z.denominator==1 and z>0
    return True
cov=0; un=[]
for s in range(5,S+1):
    n=4**s+k; hit=None
    for c in CS:
        for j in range(1,JMAX+1):
            m=4**j*c-k
            if m<=0 or j==s: continue
            K=(n+m)//4
            if math.gcd(K,n)!=1: continue
            a=min(s,j)-1; r=abs(s-j)
            X=K//4**a
            extra=alg_factors(r) if c==1 else []
            at=atoms_of(X,extra)
            if a>0: at[2]=2*a
            res=cap0(n,m,K,at)
            if res: check(n,m,K,*res); hit=(j,c); break
        if hit: break
    if hit: cov+=1
    else: un.append(s)
print("k",k,"s<=",S,"covered",cov,"of",S-4,"uncovered:",un[:60],len(un))
