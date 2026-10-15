# O240 (MENU_STERILITY §4.2): Type II families with CONSTANT a, c for n = phi(U) = C*U^3 + 1 (cube-root menu).
# Classification: n + 4a^2 d = e f, f = 4acd - 1 with a, c constant  <=>  h := mu*e - kappa divides phi + nu,
# nu = kappa/mu, kappa = 4a^2, mu = 4ac.  For phi + nu = C(U^3 + t^3) (nu = C t^3 - 1 > 0) and h = lam*(U + t) (case 1)
# or h = lam*(U^2 - tU + t^2) (case 2) or h = lam (window).  Test validity on the class through U* = (RHO at odd l, 0 at 2).
# Usage: z15_acconst_root.py C RHO H
import sys, math, itertools
from fractions import Fraction as Fr
C=int(sys.argv[1]); ANY=(sys.argv[2]=='any'); RHO=Fr(1) if ANY else Fr(sys.argv[2]); H=int(sys.argv[3])
def ev(co,u): return sum(c*u**i for i,c in enumerate(co))
def padd(p,q):
    n=max(len(p),len(q)); return [ (p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)]
def psc(p,s): return [s*x for x in p]
def pmul(p,q):
    r=[Fr(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r
rats=sorted({Fr(p,q) for q in range(1,H+1) for p in range(1,H*H+1) if math.gcd(p,q)==1 and Fr(p,q)<=H})
def classpoint(polys):
    T=8
    for p in polys:
        for c in p: T=math.lcm(T,c.denominator)
    T*=8; t2=1
    while T%(2*t2)==0: t2*=2
    To=T//t2
    if RHO.denominator!=1 and math.gcd(RHO.denominator,To)!=1: return None
    r=(RHO.numerator*pow(RHO.denominator,-1,To))%To if To>1 else 0
    g=(r*t2*pow(t2,-1,To))%T if To>1 else 0
    return g,T
hits=0; tested=0
for t in rats:
    nu=C*t**3-1
    if nu<=0: continue
    for case in (1,2):
        for lam in rats:
            for a in rats:
                kappa=4*a*a; mu=kappa/nu; c=a/nu
                if case==1:
                    h=[lam*t,lam]; dpol=padd(psc([t*t,-t,Fr(1)],C/lam),[1/mu])
                else:
                    h=[lam*t*t,-lam*t,lam]; dpol=padd(psc([t,Fr(1)],C/lam),[1/mu])
                e=psc(padd(h,[kappa]),1/mu)
                f=padd(psc(dpol,4*a*c),[Fr(-1)])
                b=padd(psc(e,c),[-a])
                ps=[[a],b,[c],dpol,e,f]
                if any(p[-1]<=0 for p in ps): continue
                tested+=1
                cp=classpoint(ps)
                if cp is None: continue
                g,T=cp
                gl=[g]
                if ANY:
                    if T>4096: continue
                    gl=range(T)
                for g in gl:
                  ok=True
                  for k in range(40,44):
                    u=g+T*k; n=C*u**3+1
                    vals=[ev(p,u) for p in ps]
                    if any(v.denominator!=1 or v<=0 for v in vals) or n%4!=1: ok=False;break
                  if not ok: continue
                  A,B,Cc,D,E,F=[int(ev(p,g+T*50)) for p in ps]; u=g+T*50; n=C*u**3+1
                  assert Fr(4,n)==Fr(1,A*B*D)+Fr(1,A*Cc*D*n)+Fr(1,B*Cc*D*n)
                  hits+=1
                  if hits<=12: print("HIT case",case,"t",t,"lam",lam,"a",a,"T",T,"g",g,"e",e,"d",dpol,flush=True)
print("C",C,"RHO",RHO,"tested",tested,"hits",hits)
