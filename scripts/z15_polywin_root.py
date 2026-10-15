# O240 (MENU_STERILITY §4): POLYNOMIAL-WINDOW Type II families for n = phi(U) = C*U^E + 1:
#   x = K = (n + m(U))/4,  delta | K^2 (product of irreducible factors of K, exponent <= 2*mult, times lam in Q),
#   m(U) | K + delta in Q[U],  A = (K + delta)/m,  y = n*A,  z = n*K*A/delta (must be a polynomial).
# Every Type II family has this shape (x = abd, 4x = n + e, m := e); constant m = CAP_DOWN Lemma 1.1 windows.
# Test: validity on the U-class through U* = (RHO at odd l, 0 at 2)  [mu = 0 of C*2^s + 1 for RHO = 1],
# or with RHO=any: report how many residue classes mod T are valid (sanity).
# Usage: z15_polywin_root.py C E MDEG MCOEF RHO
import sys, math, itertools
from fractions import Fraction as Fr
from sympy import symbols, Poly, QQ, factor_list
C=int(sys.argv[1]); E=int(sys.argv[2]); MDEG=int(sys.argv[3]); MC=int(sys.argv[4]); MODE=sys.argv[5]; ANY=MODE in ('any','two','odd')
RHO=Fr(1) if ANY else Fr(sys.argv[5])
U=symbols('U'); n=Poly(C*U**E+1,U,domain=QQ)
def den(p): return math.lcm(*[Fr(str(x)).denominator for x in p.all_coeffs()])
def F(x): return Fr(str(x))
def ev(p,u): return F(p.eval(u))
def classpoint(T):
    t2=1
    while T%(2*t2)==0: t2*=2
    To=T//t2
    r=(RHO.numerator*pow(RHO.denominator,-1,To))%To if To>1 else 0
    return (r*t2*pow(t2,-1,To))%T if To>1 else 0
hits=0; anyhits=0
mlist=[]
for dg in range(0,MDEG+1):
    for co in itertools.product(range(-MC,MC+1),repeat=dg+1):
        if co[0]<=0: continue
        mlist.append(Poly(list(co),U,domain=QQ))
for m in mlist:
    K=(n+m)*Poly(Fr(1,4),U,domain=QQ)
    fl=[(Poly(f,U,domain=QQ),k) for f,k in factor_list(K.as_expr())[1]]
    if len(fl)==1 and fl[0][1]==1 and m.degree()==0: continue   # irreducible K, constant window: congruence-type only
    for ks in itertools.product(*[range(0,2*k+1) for _,k in fl]):
        d0=Poly(1,U,domain=QQ)
        for (f,_),k in zip(fl,ks): d0=d0*f**k
        if m.degree()>=1:
            r1=K.rem(m); r2=d0.rem(m)
            if r2.is_zero: continue
            q,rr=(-r1).div(r2)
            if not rr.is_zero or q.degree()>0 or q.is_zero: continue
            lams=[F(q.LC())]
        else:
            lams=None
        if lams is None:
            # constant window m: lam must satisfy K + lam*d0 == 0 mod m only as integers on the class: try small lam
            lams=[Fr(s*p,q) for p in range(1,33) for q in (1,2,4,8,16,3) for s in (1,)]
        for lam in lams:
            if lam<=0: continue
            delta=d0*Poly(lam,U,domain=QQ)
            Ap=(K+delta)
            Aq,Ar=Ap.div(m)
            if not Ar.is_zero: continue
            zq,zr=(n*K*Aq).div(delta)
            if not zr.is_zero: continue
            ps=[K,n*Aq,zq]
            if any(p.LC()<=0 for p in ps): continue
            T=8
            for p in ps+[Aq]: T=math.lcm(T,den(p))
            T*=4
            gl=range(T) if ANY else [classpoint(T)]
            if ANY and T>3000: continue
            if MODE in ('two','odd'):
                t2=1
                while T%(2*t2)==0: t2*=2
                gl=[g for g in range(T) if (g%t2==0 if MODE=='two' else (g-1)%(T//t2)==0)]
            good=[]
            for g in gl:
                ok=True
                for t in range(30,33):
                    u=g+T*t; nv=C*u**E+1
                    vals=[ev(p,u) for p in ps]
                    if any(v.denominator!=1 or v<=0 for v in vals) or nv%4!=1: ok=False;break
                    if Fr(4,nv)!=Fr(1,vals[0])+Fr(1,vals[1])+Fr(1,vals[2]): ok=False;break
                if ok: good.append(g)
            if good:
                if ANY: anyhits+=1
                else: hits+=1
                if (hits+anyhits)<=15: print("HIT m=%s delta=%s T=%d classes=%s"%(m.as_expr(),delta.as_expr(),T,good[:6]),flush=True)
print("C=%d E=%d MDEG=%d MC=%d RHO=%s hits=%d anyhits=%d"%(C,E,MDEG,MC,sys.argv[5],hits,anyhits))
