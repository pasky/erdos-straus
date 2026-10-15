# O240: hybrid covering of n_s = c*b^s + k (b = 2^beta) by ET/divisor classes + exponential window rules.
# Rule (shape, j, t, e): window m = c*2^j*w - k, w = t^4 (SG, needs S-j == 2 mod 4) or t^e (CY_e, e odd, e | S-j), S = beta*s,
# K = (n+m)/4 = c*2^(j-2)*(2^(S-j) + w), atoms: 2 (mult j-2), primes of c, algebraic factors of 2^(S-j)+w (mult 1).
# Cap-0 Lemma-1.1: d = prod atoms^x, x <= 2*mult, d == -K (mod m), gcd(K, m) = 1.  Validity depends on S mod (4|e)*ord_m(2).
# Usage: z15_hybrid_exp.py c k beta L Mmax JMAX TMAX EMAX
import sys, math, itertools, functools
from fractions import Fraction as F
import mordell_lib as ML, ec_cover as EC
from ec_screen import admissible_prime_powers
from sympy import n_order, factorint, cyclotomic_poly, symbols, Poly
ML.residue_table=functools.lru_cache(maxsize=None)(ML.residue_table)
c,k,beta,L,Mmax,JMAX,TMAX,EMAX=map(int,sys.argv[1:9]); b=2**beta
Us=symbols('U')
@functools.lru_cache(None)
def cyc(f): co=Poly(cyclotomic_poly(2*f,Us),Us).all_coeffs()[::-1]; return [int(a) for a in co]
def psi(f,U,t,mod):
    co=cyc(f); dg=len(co)-1
    return sum(a*pow(U,i,mod)*pow(t,dg-i,mod) for i,a in enumerate(co))%mod
CF=factorint(c)
def rule_ok(S,rule):
    shape,j,t,e=rule; w=t**4 if shape=='SG' else t**e; m=c*2**j*w-k
    if m<=0 or j<2 or S-j<6: return None
    r=S-j
    if shape=='SG':
        if r%4!=2: return None
        X=pow(2,(r-2)//4,m); fac=[(2*X*X+2*X*t+t*t)%m,(2*X*X-2*X*t+t*t)%m]
    else:
        if r%e: return None
        U=pow(2,r//e,m); fac=[psi(f,U,t,m) for f in range(1,e+1,2) if e%f==0]
    at=([(2,j-2)] if j>2 else [])+[(p%m,v) for p,v in CF.items()]+[(x,1) for x in fac]
    K=(c*pow(2,S,m)+k+m)*pow(4,-1,m)%m
    if math.gcd(K,m)!=1 or any(math.gcd(a,m)!=1 for a,_ in at): return None
    tgt=(-K)%m
    for ex in itertools.product(*[range(2*v+1) for _,v in at]):
        d=1
        for (a,_),x in zip(at,ex): d=d*pow(a,x,m)%m
        if d==tgt: return ex
    return None
def exact(s,rule,ex):
    shape,j,t,e=rule; S=beta*s; w=t**4 if shape=='SG' else t**e; m=c*2**j*w-k; n=c*b**s+k; r=S-j
    if shape=='SG':
        X=2**((r-2)//4); fac=[2*X*X+2*X*t+t*t,2*X*X-2*X*t+t*t]
    else:
        U=2**(r//e); fac=[]
        for f in range(1,e+1,2):
            if e%f==0:
                co=cyc(f); dg=len(co)-1; fac.append(sum(a*U**i*t**(dg-i) for i,a in enumerate(co)))
    at=([2] if j>2 else [])+list(CF.keys())+fac
    d=1
    for a,x in zip(at,ex): d*=a**x
    K=(n+m)//4; assert 4*K==n+m and (K*K)%d==0
    A=F(K+d,m); z=F(n*K*A,d)
    return A.denominator==1 and z.denominator==1 and F(4,n)==F(1,K)+F(1,n*A)+1/z
# ---- ET/divisor sets mod L (as in z15_cert_proth_make)
@functools.lru_cache(None)
def LM(M):
    out=1
    for q,ee in factorint(M).items():
        if q!=2: out=math.lcm(out,n_order(b,q**ee))
    return out
def nval(s,M):
    S=s+64*LM(M)*L if s<64 else s
    return (c*pow(b,S,M)+k)%M
target=set(range(L)); sets=[]
for q,Q in admissible_prime_powers(b,L,QMAX=Mmax):
    if q>2 and c%q:
        st={x for x in target if nval(x,q)==0}
        if st: sets.append((('D',q),st))
for M in EC.candidate_moduli(c,b,k,L,Mmax):
    if M%4 and M%4!=3: continue
    W=ML.residue_table(M); cv={}
    for x in target:
        r=nval(x,M)
        if r in W: cv.setdefault(W[r],set()).add(x)
    for cls,st in cv.items(): sets.append((('ET',M,cls),st))
etall=set().union(*[st for _,st in sets]) if sets else set()
R=sorted(target-etall)
print("c=%d k=%d b=%d L=%d Mmax=%d: ET/divisor-uncoverable residues (%d): %s"%(c,k,b,L,Mmax,len(R),R[:24]),flush=True)
# ---- rules: those whose validity is periodic mod L (P | beta*L)
rules=[]
for shape,e in [('SG',4)]+[('CY',e) for e in range(3,EMAX+1,2)]:
    for j in range(2,JMAX+1):
        for t in range(1,TMAX+1,2):
            w=t**4 if shape=='SG' else t**e; m=c*2**j*w-k
            if m<=1 or math.gcd(m,2)==0: continue
            P=(4 if shape=='SG' else e)*n_order(2,m)
            if (beta*L)%P: continue
            rules.append((shape,j,t,e))
rsets=[]
for rule in rules:
    st={}
    for x in range(L):
        s=x+L*(10+JMAX)        # large representative
        ex=rule_ok(beta*s,rule)
        if ex is not None: st[x]=ex
    if st: rsets.append((rule,st))
ruleall=set().union(*[set(st) for _,st in rsets]) if rsets else set()
print("rules periodic mod L:",len(rules),"firing:",len(rsets),"; residual after ET+rules:",sorted(target-etall-ruleall)[:24],flush=True)
# greedy: rules first on R, then ET for the rest
unc=set(R); used=[]
while unc & ruleall:
    rule,st=max(rsets,key=lambda t:len(unc&set(t[1])))
    used.append((rule,{x:st[x] for x in unc&set(st)})); unc-=set(st)
for rule,st in used:
    for x,ex in list(st.items())[:3]:
        s=x+L*(10+JMAX); assert exact(s,rule,ex), ('exact fail',rule,x)
    print(" rule",rule,"m=%d"%(c*2**rule[1]*(rule[2]**4 if rule[0]=='SG' else rule[2]**rule[3])-k),"covers",len(st),"of R; e.g.",list(st.items())[:3],flush=True)
print("LEFT (needs more):",sorted(unc)[:30],"of",len(R))
