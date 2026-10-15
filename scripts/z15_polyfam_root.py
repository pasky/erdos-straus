# O240 (MENU_STERILITY §4): search Type I/II polynomial families in U for n = phi(U) = C*U^E + 1 that are valid on a
# U-class whose closure contains the profinite point U* (U* = RHO at every odd prime, U* = 0 at 2).
# For n_s = 3*2^s + 1 and s = E*t, U = 2^t: s -> 0 in Z^ gives U* = (1 at odd l, 0 at 2): the sterile point mu = 0 of
# EXPONENT_COVERING Cor 1.5.  A hit = one exponential class covering a neighbourhood of mu = 0.
# Usage: z15_polyfam_root.py C E R
import sys, itertools, math
from fractions import Fraction as Fr
from sympy import symbols, Poly, QQ, factor_list
C=int(sys.argv[1]); E=int(sys.argv[2]); R=int(sys.argv[3]); RHO=1
U=symbols('U')
phi=Poly(C*U**E+1,U,domain=QQ)
mon=[Poly(1,U,domain=QQ)]+[Poly(U+r,U,domain=QQ) for r in range(-R,R+1)]
mon+=[Poly(U**2+b*U+g,U,domain=QQ) for b in range(-R,R+1) for g in range(-R,R+1)]
lams=[Fr(1),Fr(2),Fr(4),Fr(8),Fr(1,2),Fr(1,4),Fr(3),Fr(3,2),Fr(1,3)]
def subsets(fl):
    # all divisors (as monic polys) of prod f_i^m_i
    out=[Poly(1,U,domain=QQ)]
    for f,mlt in fl:
        new=[]
        for o in out:
            for k in range(mlt+1): new.append(o*Poly(f,U,domain=QQ)**k)
        out=new
    return out
def den(p): return math.lcm(*[Fr(str(x)).denominator for x in p.all_coeffs()])
def check(polys,kind):
    T=1
    for p in polys: T=math.lcm(T,den(p))
    T*=8
    t2=1
    while T%(2*t2)==0: t2*=2
    To=T//t2
    # g == RHO mod To, g == 0 mod t2
    g=(RHO*t2*pow(t2,-1,To))%T if To>1 else 0
    for t in range(50,56):
        u=g+T*t
        n=C*u**E+1
        vals=[Fr(str(p.eval(u))) for p in polys]
        if any(v.denominator!=1 or v<=0 for v in vals) or n%4!=1: return None
    a,b,c,d,e,f=[int(Fr(str(p.eval(g+T*60)))) for p in polys]; u=g+T*60; n=C*u**E+1
    if kind=='II': x,y,z=a*b*d,a*c*d*n,b*c*d*n
    else: x,y,z=a*b*d*n,a*c*d,b*c*d
    assert Fr(4,n)==Fr(1,x)+Fr(1,y)+Fr(1,z), (kind,polys)
    return T
hits=0; seen=set()
for ma,md in itertools.product(mon,mon):
    for la,ld in itertools.product(lams,lams):
        a=ma*Poly(la,U,domain=QQ); d=md*Poly(ld,U,domain=QQ); ad4=a*d*4
        # ---- Type II: e f = n + 4a^2 d, f = 4acd - 1
        P=phi+a*a*d*4
        if P.degree()<0: continue
        lc=P.LC(); fl=factor_list(P.as_expr())[1]
        for E0 in subsets(fl):
            Q0=P.quo(E0)               # f = Q0/lam_e
            if ad4.degree()>=1:
                rr=Q0.rem(ad4)
                if rr.degree()>0: continue
                r0=rr.LC() if not rr.is_zero else 0
                if r0==0: continue
                lame=[-Fr(str(r0))]
            else: lame=lams+[Fr(k) for k in range(5,64,2)]
            for le in lame:
                if le<=0: continue
                e=E0*Poly(le,U,domain=QQ); f=Q0*Poly(1/le,U,domain=QQ)
                cq,cr=(f+1).div(ad4)
                if not cr.is_zero: continue
                c=cq; b=c*e-a
                if b.is_zero or c.is_zero: continue
                if e.degree()==0 and False: pass
                ps=[a,b,c,d,e,f]
                if any(p.LC()<=0 for p in ps): continue
                key=('II',)+tuple(str(p.as_expr()) for p in ps)
                if key in seen: continue
                T=check(ps,'II')
                if T:
                    seen.add(key); hits+=1
                    print("HIT TypeII T=%d const_e=%s"%(T,e.degree()==0),[str(p.as_expr()) for p in ps],flush=True)
        # ---- Type I: e f = 4a^2 d + 1, f = 4acd - n, b = (n a + c)/f
        P=a*a*d*4+1
        fl=factor_list(P.as_expr())[1]
        for F0 in subsets(fl):
            if ad4.degree()>=1:
                # need phi + lam F0 == 0 mod ad4
                r1=phi.rem(ad4); r2=F0.rem(ad4)
                if r2.is_zero: continue
                # lam = -r1/r2 must be a constant
                q,rr=(-r1).div(r2)
                if not rr.is_zero or q.degree()>0: continue
                lamf=[Fr(str(q.LC()))] if not q.is_zero else []
            else: lamf=lams+[Fr(k) for k in range(5,64,2)]
            for lf in lamf:
                if lf<=0: continue
                f=F0*Poly(lf,U,domain=QQ); e=P.quo(f)
                cq,cr=(phi+f).div(ad4)
                if not cr.is_zero: continue
                c=cq; bq,br=(phi*a+c).div(f)
                if not br.is_zero: continue
                b=bq; ps=[a,b,c,d,e,f]
                if any(p.is_zero or p.LC()<=0 for p in ps): continue
                key=('I',)+tuple(str(p.as_expr()) for p in ps)
                if key in seen: continue
                T=check(ps,'I')
                if T:
                    seen.add(key); hits+=1
                    print("HIT TypeI T=%d"%T,[str(p.as_expr()) for p in ps],flush=True)
print("C=%d E=%d R=%d hits=%d"%(C,E,R,hits))
