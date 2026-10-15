# O240: list exponential window rules firing at given exponents s of c*b^s + k (b = 2^beta), with their s-periods.
# Usage: z15_rules_at.py c k beta JMAX TMAX EMAX s1,s2,...
import sys, math
import z15_winlib as W
from sympy import n_order
c,k,beta,JMAX,TMAX,EMAX=map(int,sys.argv[1:7]); W.setup(c,k,beta)
for s in map(int,sys.argv[7].split(',')):
    out=[]
    for shape,e in [('SG',4)]+[('CY',e) for e in range(3,EMAX+1,2)]:
        for j in range(2,JMAX+1):
            for t in range(1,TMAX+1,2):
                w=t**4 if shape=='SG' else t**e; m=c*2**j*w-k
                if m<=1 or m%2==0: continue
                ex=W.rule_ok(beta*s,(shape,j,t,e))
                if ex is not None and W.exact(s,(shape,j,t,e),ex):
                    P=(4 if shape=='SG' else e)*n_order(2,m); out.append((shape,j,t,e,m,P//math.gcd(P,beta)))
    print(s,len(out),sorted(out,key=lambda r:r[5])[:6],flush=True)
