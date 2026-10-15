# O240: two-level hybrid covering of c*b^s + k: ET/divisor classes at L0, then the residual lifted to Lstar (L0 | Lstar)
# is attacked by exponential window rules with period | Lstar and by ET/divisor classes at Lstar.
# Usage: z15_tree.py c k beta L0 Lstar Mmax JMAX TMAX EMAX
import sys, math, functools
import mordell_lib as ML, ec_cover as EC
from ec_screen import admissible_prime_powers
from sympy import n_order, factorint
import z15_winlib as W
ML.residue_table=functools.lru_cache(maxsize=None)(ML.residue_table)
c,k,beta,L0,Ls,Mmax,JMAX,TMAX,EMAX=map(int,sys.argv[1:10]); b=2**beta; W.setup(c,k,beta)
assert Ls%L0==0
@functools.lru_cache(None)
def LM(M):
    out=1
    for q,ee in factorint(M).items():
        if q!=2: out=math.lcm(out,n_order(b,q**ee))
    return out
def etcover(L,target):
    def nval(s,M):
        S=s+64*L if s<64 else s
        return (c*pow(b,S,M)+k)%M
    cov=set()
    for q,Q in admissible_prime_powers(b,L,QMAX=Mmax):
        if q>2 and c%q: cov|={x for x in target if nval(x,q)==0}
    for M in EC.candidate_moduli(c,b,k,L,Mmax):
        if M%4 and M%4!=3: continue
        Wt=ML.residue_table(M)
        cov|={x for x in target if nval(x,M) in Wt}
    return cov
R0=sorted(set(range(L0))-etcover(L0,set(range(L0))))
print("level 0: L0=%d residual %s"%(L0,R0),flush=True)
lifts={r+L0*i for r in R0 for i in range(Ls//L0)}
rules=[]
for shape,e in [('SG',4)]+[('CY',e) for e in range(3,EMAX+1,2)]:
    for j in range(2,JMAX+1):
        for t in range(1,TMAX+1,2):
            w=t**4 if shape=='SG' else t**e; m=c*2**j*w-k
            if m<=1 or m%2==0: continue
            P=(4 if shape=='SG' else e)*n_order(2,m)
            if (beta*Ls)%P==0: rules.append((shape,j,t,e))
left=set(lifts); used=[]
for rule in rules:
    hit={x for x in left if W.rule_ok(beta*(x+Ls*(4+JMAX)),rule) is not None}
    if hit:
        x0=next(iter(hit)); ex=W.rule_ok(beta*(x0+Ls*(4+JMAX)),rule)
        assert W.exact(x0+Ls*(4+JMAX),rule,ex)
        used.append((rule,len(hit))); left-=hit
print("level 1: Lstar=%d lifts %d, rules periodic %d, used %s, left after rules %d"%(Ls,len(lifts),len(rules),used,len(left)),flush=True)
left-=etcover(Ls,left)
print("left after ET at Lstar:",len(left),sorted(left)[:20])
