# z52d P2 TO8 batch C: Z3131 (window Jacobi/forced nonresidues), Z3160 (single-character reduction of M_BM), Z3163 (U_n reductions mod q),
# Z3053 (hit structure over (t,u)), Z3067 (restricted counts over L-smooth divisors)
import math, statistics as st
from math import gcd
from sympy import factorint, primerange, legendre_symbol as lsym
D = 'data/z52b/pass2/TO8/'
def divisors(n):
    ds=[1]
    for q,e in factorint(n).items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
# ---- Z3131: windows e ≡3 mod 4, e<=200 prime-ish; p≡1 mod 4 primes 1e3<p<=2e4 with (p/e) = -1 (Jacobi (p/e)) ; N_e=(p+e)/4
rows=[]; nodd=0; nwin=0; cert=0; forced=0
ps=[p for p in primerange(1001, 20000) if p%4==1]
for p in ps:
    for e in range(3, 201, 4):
        if gcd(e,p)!=1: continue
        # Jacobi symbol (p/e): product over prime factors of e
        J=1
        for q,ex in factorint(e).items(): J*= lsym(p%q,q)**ex
        if J!=-1: continue
        N=(p+e)//4
        if N<=0 or N%1: continue
        nwin+=1
        f=factorint(N)
        # forced nonresidue: a prime factor q of N with (q/e)-Jacobi = -1
        def jac(a,n):
            r=1; a%=n
            for q,ex in factorint(n).items():
                r*= lsym(a%q,q)**ex
            return r
        nr=[q for q in f if q!=e and gcd(q,e)==1 and jac(q,e)==-1]
        if nr: forced+=1
        # window certificate: divisor d of N with d ≡ -1 mod e
        if any((d % e)==e-1 for d in divisors(N)): cert+=1
print(f"Z3131: windows with (p/e)=-1 (Jacobi, e≤200, 1e3<p≤2e4): {nwin}; with a prime factor q|N_e having Jacobi (q/e)=-1: {forced} ({forced/nwin:.3f}); with a divisor ≡-1 mod e (window certificate): {cert} ({cert/nwin:.3f})")
# ---- Z3160: which single character explains M_BM/M0 (data mbm_le1e5.txt): regress M/M0 on (ℓ/p) for small ℓ
rows=[l.split() for l in open(D+'mbm_le1e5.txt')]
data=[(int(a),float(c),float(d)) for a,b,c,d in rows if int(a)>1000]
best=[]
for l in primerange(3,60):
    xs=[legendre_symbol(l,p) if False else (1 if pow(l,(p-1)//2,p)==1 else -1) for p,M,M0 in data]
    ys=[M/M0 for p,M,M0 in data]
    mx,my=st.mean(xs),st.mean(ys)
    cov=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/len(xs)
    r2=cov*cov/(st.pvariance(xs)*st.pvariance(ys))
    best.append((round(r2,4),l))
best.sort(reverse=True)
print("Z3160: R^2 of M_BM/M0 on the single Legendre symbol (l/p), top 6 ℓ:", best[:6], "; overall spread of M/M0: mean", round(st.mean(M/M0 for p,M,M0 in data),3), "min", round(min(M/M0 for p,M,M0 in data),3))
print("   smallest M_BM/L² among primes: ", sorted(((M/math.log(p)**2),p) for p,M,M0 in data)[:4])
# ---- Z3163: reductions of solutions of 4xyz = n(xy+yz+zx) mod q vs U_n(Z/q)
def sols(n):
    out=[]
    for x in range(-(-n//4), (3*n)//4+1):
        # 4/n-1/x = (4x-n)/(nx) = 1/y+1/z
        a=4*x-n; b=n*x
        if a<=0: continue
        g=gcd(a,b); aa=a//g; bb=b//g
        for d in divisors(bb*bb):
            if (d+bb)%aa==0 and ((bb*bb//d)+bb)%aa==0:
                y=(d+bb)//aa; z=(bb*bb//d+bb)//aa
                out.append((x,y,z))
    return out
for q in [3,5,7]:
    tot=0; cov=set(); U=set()
    for n in [5,13,29,37,53,61,73,89,97,101,113,137,149,157,173,181,193]:
        S=sols(n)
        for (x,y,z) in S:
            cov.add((x%q,y%q,z%q))
        tot+=len(S)
    for x in range(1,q):
        for y in range(1,q):
            for z in range(1,q):
                pass
    Uq=set()
    for x in range(q):
        for y in range(q):
            for z in range(q):
                pass
    print(f"Z3163 q={q}: distinct residues of solutions over 17 n’s (n≡1 mod 4 primes): {len(cov)} from {tot} solutions; residues with some coordinate 0 (mod q) present: {sum(1 for c in cov if 0 in c)}")
# ---- Z3053: hit structure over (t,u): hits = divisors d=tu-1 of p+u (level t=C, u); fraction of (t,u) with tu<=200 hit, hard vs control
def hits(p,T=200):
    H=set()
    for t in range(1,T+1):
        for u in range(1,T//t+1):
            m=t*u-1
            if m<1: continue
            if (p+u)%m==0 and (p+u)//m>=1: H.add((t,u))
    return H
for p in [409,577,5569,9601,1009,10009]:
    H=hits(p)
    print(f"Z3053 p={p}: hits (t,u) with tu<=200: {len(H)}; hits with t=1: {sorted(u for t,u in H if t==1)[:6]}")
