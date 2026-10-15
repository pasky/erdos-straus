# Hybrid adaptive covering of exponents s for n_s = 4^s + k: z8_adaptive's ET/divisor classes PLUS the exponential
# window classes of s6_cover105 (window m_j = 4^j - k, K = 4^{j-1}(4^r+1), r = s - j, d = K*d1/d2 with d1/d2 a
# ratio of 2^i and algebraic factors G = 4^g+1, A± (g = r/e)).  Exp classes are predicates on s mod 2*e*ord_{m_j}(2).
# Usage: PYTHONPATH=scripts uv run python scripts/s6_hybrid105.py k L0 Mmax0 Mmax LCAP JMAX EMAX
import sys, functools
from math import lcm, gcd
import mordell_lib as ML, ec_cover as EC
from ec_screen import admissible_prime_powers
from sympy import n_order, factorint, isprime
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
c0=1; k, L, Mmax0, Mmax, LCAP, JMAX, EMAX = map(int, sys.argv[1:8]); GMAX=60
@functools.lru_cache(None)
def LM(M):
    out=1
    for q,e in factorint(M).items():
        if q!=2: out=lcm(out,n_order(4,q**e))
    return out
def nval(s,M):
    S=s+64*LM(M) if s<64 else s
    return (c0*pow(4,S,M)+k)%M
WIN={}
for j in range(1,JMAX+1):
    m=4**j-k
    if m>1: WIN[j]=(m,n_order(2,m),[q for q in factorint(m)])
def expfire(s,j,e):
    m,o,pm=WIN[j]; P=2*e*o; s=s%P+P*(1+ (j+64)//P)   # representative, r>0
    r=s-j
    if r%e: return False
    if any((pow(4,r,l)+1)%l==0 for l in pm): return False
    g=r//e; G=(pow(4,g,m)+1)%m; pairs=[(1,G),(G,1)]
    if g%2:
        h=pow(2,(g+1)//2,m); t=pow(2,g,m); Am=(t-h+1)%m; Ap=(t+h+1)%m
        pairs+=[(1,Am),(Am,1),(1,Ap),(Ap,1),(Ap,Am),(Am,Ap)]
    return any((pow(2,i,m)*U+V)%m==0 for U,V in pairs for i in range(-(2*j-2),2*j-1))
classes=[]   # ('ET',M,R) or ('EXP',j,e,P)
def incls(s,c):
    if c[0]=='ET': return nval(s,c[1]) in c[2]
    return expfire(s,c[1],c[2])
def period(c): return LM(c[1]) if c[0]=='ET' else c[3]
# seed exactly as z8_adaptive
sets=[]
for q,Q in admissible_prime_powers(4,L,QMAX=Mmax0):
    if q>2:
        st={x for x in range(L) if nval(x,q)==0}
        if st: sets.append((q,('D',(q,)),st))
for M in EC.candidate_moduli(c0,4,k,L,Mmax0):
    if M%4 and M%4!=3: continue
    W=ML.residue_table(M); cv={}
    for x in range(L):
        r=nval(x,M)
        if r in W: cv.setdefault(W[r],set()).add(x)
    for cls,st in cv.items(): sets.append((M,cls,st))
unc=set().union(*[st for _,_,st in sets]) if sets else set()
while unc:
    M,cls,st=max(sets,key=lambda t:(len(unc&t[2]),-t[0])); unc-=st
    fam,P=cls; R={0} if fam=='D' else set(ML.cls_modulus_residues(fam,P)[1]); classes.append(('ET',M,R))
U=[x for x in range(L) if not any(incls(x,c) for c in classes)]
Ms=sorted([M for M in range(3,Mmax+1) if M%4 in (0,3)]); primes=[q for q in range(3,20000) if isprime(q)]
it=0
while U:
    print('iter %d L=%d classes=%d uncovered=%d density=%.3g'%(it,L,len(classes),len(U),len(U)/L),U[:10],flush=True); it+=1
    cands={}
    for u in U[:12]:
        for q in primes:
            if nval(u,q)==0: cands[('ET',q,frozenset({0}))]=1
        for M in Ms:
            W=ML.residue_table(M); r=nval(u,M)
            if r in W: cands[('ET',M,frozenset({r}))]=1
        for j in WIN:
            for e in range(1,EMAX+1,2):
                if expfire(u,j,e): cands[('EXP',j,e,2*e*WIN[j][1])]=1
    best=None
    for c in cands:
        g=lcm(L,period(c))//L
        if g>GMAX or g*len(U)>400000: continue
        cov=sum(1 for u in U for x in range(u,u+g*L,L) if incls(x,c))
        key=(-cov/g,g)
        if best is None or key<best[0]: best=(key,c)
    if best is None: print('no candidate'); sys.exit(1)
    c=best[1]; classes.append(c); g=lcm(L,period(c))//L
    U=[x for u in U for x in range(u,u+g*L,L) if not incls(x,c)]; L*=g
    print('  add',c[:2] if c[0]=='ET' else c,'-> L=%d'%L,flush=True)
    if L>LCAP: print('L cap exceeded'); sys.exit(1)
print('COVERED: final L',L,'classes',len(classes)); print([c[:2] if c[0]=='ET' else c for c in classes])
