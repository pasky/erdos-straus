#!/usr/bin/env python3
"""R292 independent checker. Reads printed TeX tables, never author code/data.
Exact modular class membership, symbolic identities, and complete periods.
Run: PYTHONPATH=scripts uv run --with sympy python scripts/review_r292_certificates.py
"""
import re
from pathlib import Path
from math import gcd, lcm
from fractions import Fraction as F
from sympy import symbols, cancel, Poly, Rational, n_order

text = Path('paper/es-exponential-families.tex').read_text()
Y = symbols('Y')

def exact(n, xyz):
    assert all(v > 0 and F(v).denominator == 1 for v in xyz), (n, xyz)
    x,y,z = xyz
    assert 4*x*y*z == n*(x*y+y*z+z*x)

def prime_solution(q):
    # Different search: enumerate x,y; derive z directly, bounded by ordering.
    for x in range(q//4+1, 3*q//4+2):
        r = F(4,q)-F(1,x)
        for y in range(max(x, r.denominator//r.numerator+1), 2*r.denominator//r.numerator+1):
            t = r-F(1,y)
            if t > 0 and t.numerator == 1:
                ans=(x,y,t.denominator); exact(q,ans); return ans
    raise AssertionError(q)

def et(kind, p, n):
    """Return actual defining modulus, membership predicate, coordinates.
    Side conditions checked independently; integer parameters are also checked.
    """
    if kind == 'D':
        q, = p
        return q, lambda v:v%q == 0, tuple(Rational(t,q)*n for t in prime_solution(q)), []
    if kind == 'II2':
        a,d,f=p; assert (f+1)%(4*a*d)==0
        c=(f+1)//(4*a*d); b=(n*c+a)/f
        M=f; pred=lambda v:(v+4*a*a*d)%f==0
    elif kind == 'I1':
        a,d,f=p; assert (4*a*a*d+1)%f==0
        e=(4*a*a*d+1)//f; b=(n*e+1)/(4*a*d); c=(n+f)/(4*a*d)
        M=4*a*d; pred=lambda v:(v+f)%M==0
    elif kind == 'I2':
        a,c,f=p; assert gcd(4*a*c,f)==1
        d=(n+f)/(4*a*c); b=(n*a+c)/f
        M=4*a*c*f; pred=lambda v:(v+f)%(4*a*c)==0 and (v*a+c)%f==0
    elif kind == 'I3':
        c,d,f=p; assert gcd(4*c*d,f)==1
        a=(n+f)/(4*c*d); b=(n*n+n*f+4*c*c*d)/(4*c*d*f)
        M=4*c*d*f; pred=lambda v:(v+f)%(4*c*d)==0 and (v*v+4*c*c*d)%f==0
    elif kind in ('I4','II1'):
        a,b,e=p; assert (a+b)%e==0 and gcd(e,4*a*b)==1
        c=(a+b)//e; M=4*a*b
        d=(n*e+1)/M if kind=='I4' else (n+e)/M
        pred=(lambda v:(v*e+1)%M==0) if kind=='I4' else (lambda v:(v+e)%M==0)
    elif kind=='II3':
        a,d,e=p; assert gcd(4*a*d,e)==1
        c=(n+4*a*a*d+e)/(4*a*d*e); b=(n+e)/(4*a*d)
        M=4*a*d*e; pred=lambda v:(v+4*a*a*d+e)%M==0
    else: raise AssertionError(kind)
    abc=[a,b,c,d]
    xyz=(a*b*d*n,a*c*d,b*c*d) if kind.startswith('I') and not kind.startswith('II') else (a*b*d,a*c*d*n,b*c*d*n)
    return M,pred,xyz,abc

def table(label):
    for t in re.findall(r'\\begin\{table\}.*?\\end\{table\}',text,re.S):
        if '\\label{tab:'+label+'}' in t: return t
    raise AssertionError(label)

def residues(cell):
    hit=re.search(r's\\equiv\s*([\d,]+)\\pmod\{(\d+)\}',cell)
    assert hit,cell
    return int(hit[2]),set(map(int,hit[1].split(',')))

def rows(label,c0,base,k):
    out=[]
    for line in table(label).splitlines():
        hit=re.search(r'(II[123]|I[1234]|D)\$\(([^)]+)\)',line)
        if not hit: continue
        if label=='nine':
            km=re.match(r'\$(\d+)\$',line)
            if km: k=int(km[1])
        kind=hit[1]; p=tuple(map(int,hit[2].split(',')))
        P,R=residues(line)
        th=re.search(r's\\ge(\d+)',line); threshold=int(th[1]) if th else 0
        n=c0*Y+k
        M,pred,xyz,params=et(kind,p,n)
        assert cancel(4*xyz[0]*xyz[1]*xyz[2]-n*(xyz[0]*xyz[1]+xyz[1]*xyz[2]+xyz[2]*xyz[0]))==0
        # All ET coordinate/parameter polynomials here have nonnegative coefficients.
        for v in (*xyz,*params):
            coeffs=Poly(v,Y).all_coeffs(); assert all(a>=0 for a in coeffs) and any(a>0 for a in coeffs)
        odd=M; a=0
        while odd%2==0: odd//=2; a+=1
        start=max(threshold,(a+({2:1,4:2}[base])-1)//{2:1,4:2}[base])
        order=int(n_order(base,odd)) if odd>1 else 1
        Q=lcm(P,order)
        for s in range(start,start+Q):
            assert pred((c0*pow(base,s,M)+k)%M)==(s%P in R),(label,kind,p,s)
        for s in range(threshold,start):
            if s%P in R: assert pred((c0*pow(base,s,M)+k)%M),(label,p,s)
        for r in R:
            s=r+P*max(0,(threshold-r+P-1)//P)
            val=base**s
            exact(c0*val+k,[cancel(v).subs(Y,val) for v in xyz])
            assert all(F(cancel(v).subs(Y,val)).denominator==1 for v in params)
        out.append((k,P,R,threshold,kind,p))
    print(label,': verified',len(out),'printed ET/divisor rows')
    return out

def cover(name,rs,extra=(),missing=()):
    terms=[(P,R,th) for _,P,R,th,*_ in rs]+list(extra)
    L=lcm(*(P for P,R,th in terms)); holes=[s for s in range(L) if not any(s%P in R for P,R,th in terms)]
    assert holes==list(missing),(name,L,holes)
    # Small exceptions are not hidden by asymptotic periodicity.
    exceptions=[s for s in range(max(th for P,R,th in terms)) if not any(s>=th and s%P in R for P,R,th in terms)]
    print(name,': period',L,'holes',holes,'small exceptions',exceptions)
    return exceptions

r15=rows('15',15,2,1); assert cover('15',r15,missing=[0])==[]
r63=rows('63',63,2,1)
assert cover('63 ET only',r63,missing=[0,840,1680])==[0]
assert cover('63 complete',r63,[(24,{0},24)])==[0]
n=63*Y**3+1; a,d=5,17
b=(63*Y**3+3*Y**2-9*Y+28)/340; c=(21*Y+64)/340
assert cancel(4*a*b*c*d-n*c-a-b)==0
# b numerator positive: 63Y^3+3Y^2−9Y+28 > 0 for Y>=1.
assert Poly((63*(Y+1)**3+3*(Y+1)**2-9*(Y+1)+28),Y).all_coeffs()==[63,192,186,85]
for t in range(1,10):
    V=2**(8*t); exact(63*V**3+1,[v.subs(Y,V) for v in (a*b*d,a*c*d*n,b*c*d*n)])
exact(64,(32,64,64))

r105=rows('105',1,4,105)
assert cover('105 ET only',r105,missing=[34,124])==[]
assert cover('105 complete',r105,[(45,{34},4)])==[]
u=Y; n=256*u**3+105; A=2*(32*u+33)*(u*u-u+1)/151
xyz=(64*(u**3+1),n*A,32*n*(u+1)*A)
assert cancel(4*xyz[0]*xyz[1]*xyz[2]-n*(xyz[0]*xyz[1]+xyz[1]*xyz[2]+xyz[2]*xyz[0]))==0
assert int(n_order(4,151))==15 and pow(4,10,151)==32
# A>0 for u>=1 from displayed factorisation, u^2-u+1=(u-1)^2+u.
exact(4**34+105,[v.subs(Y,4**10) for v in xyz])
rnine=rows('nine',1,4,None)
for k in sorted({row[0] for row in rnine}): assert cover(str(k),[r for r in rnine if r[0]==k])==[]

# Independently transcribed factor products from Table c7w, NOT z14 codes.
fp=2*Y**2+2*Y+1; fm=2*Y**2-2*Y+1; C=Y**2-Y+1
# m,j,root denominator h (0=SG),shift, d1,d2, exponent period/residues.
wdata=[
(19,1,1,1,1,Y+1,9,{6}),
(19,1,0,2,fm,7,36,{18,26}),
(19,1,0,2,fp,7,36,{0,8}),
(19,1,0,2,1,fm,36,{8,32}),
(103,1,1,1,Y+4,7,51,{44}),
(103,1,1,1,1,'n',51,{8}),
(103,1,1,1,1,Y+4,51,{41}),
(103,2,1,2,1,'14*n',51,{17}),
(103,2,1,2,4,'7*n',51,{47}),
(103,2,1,2,4,7*(Y+1),51,{38}),
(103,2,1,2,2,Y+1,51,{32}),
(103,2,3,2,1,'14*n*C',153,{128}),
(103,2,3,2,4*C,'7*n',153,{137}),
(103,2,3,2,2*C,7*(Y+1),153,{32,74}),
(103,2,3,2,4,7*C,153,{29}),
(103,2,3,2,2*(Y+1),7*C,153,{65,98}),
(103,2,3,2,'n*(Y+1)',28,153,{56}),
(103,2,3,2,2,'n*C',153,{11}),
(103,2,3,2,C,'n',153,{20}),
(103,2,9,2,1,'14*n*(Y+1)',459,{146,155}),
(103,2,9,2,1,'7*n*C',459,{128,308}),
(663,2,1,2,2,7*(Y+6),12,{10})]
extras=[]
for m,j,h,shift,d1,d2,P,R in wdata:
    sigma,omega,D=(2,1,4) if h==0 else (h,2,h)
    n=7*4**shift*Y**D+9; x=(n+m)/4; N=n*x
    # Strings are local, fixed expressions, not external input.
    d1=eval(d1,{},dict(n=n,Y=Y,C=C)) if isinstance(d1,str) else d1
    d2=eval(d2,{},dict(n=n,Y=Y,C=C)) if isinstance(d2,str) else d2
    for d in (d1,d2):
        Q=Poly(cancel(N/d),Y)
        assert all(F(c).denominator==1 for c in Q.all_coeffs())
        # Positivity for Y>=1 by shifted nonnegative coefficients.
        assert all(c>=0 for c in Poly(Q.as_expr().subs(Y,Y+1),Y).all_coeffs())
        assert all(c>=0 for c in Poly((Y*0+d).subs(Y,Y+1),Y).all_coeffs())
    xyz=(x,cancel(N*(d1+d2)/(m*d2)),cancel(N*(d1+d2)/(m*d1)))
    assert cancel(4*xyz[0]*xyz[1]*xyz[2]-n*(xyz[0]*xyz[1]+xyz[1]*xyz[2]+xyz[2]*xyz[0]))==0
    order=int(n_order(2**omega,m)); period=sigma*order
    for s in range(shift,shift+lcm(P,period)):
        valid=False
        if (s-shift)%sigma==0:
            V=pow(2,omega*((s-shift)//sigma),m)
            valid=int((Y*0+d1+d2).subs(Y,V))%m==0
        assert valid==(s%P in R),(m,j,h,s,R)
    for r in R:
        s=r+P*max(0,(shift-r+P-1)//P); V=2**(omega*((s-shift)//sigma))
        exact(7*4**s+9,[v.subs(Y,V) for v in xyz])
    extras.append((P,R,shift))
rc7=rows('c7et',7,4,9)
assert cover('c7',rc7,extras)==[0,1]
# s=1: I3(1,5,3) works even though the table's sufficient threshold says >=2.
_,_,xyz,_=et('I3',(1,5,3),Y)
exact(37,[v.subs(Y,37) for v in xyz]); exact(16,(8,12,24))
print('c7: all 22 window rows symbolically and periodically verified')

# Proth proof: four SG budgets and six literal displayed identities.
n=48*Y**4+1; K=3*fp*fm
for beta,gamma in [(2,1),(0,2),(2,0),(1,2)]:
    d=fp**beta*fm**gamma
    xyz=(K,n*(K+d)/11,cancel(n*K*(K+d)/(11*d)))
    assert cancel(4*xyz[0]*xyz[1]*xyz[2]-n*(xyz[0]*xyz[1]+xyz[1]*xyz[2]+xyz[2]*xyz[0]))==0
    assert Poly(cancel(K*K/d),Y).domain.is_ZZ
for X in range(11):
    assert ((int((K+fp**2*fm).subs(Y,X))%11==0 or int((K+fm**2).subs(Y,X))%11==0 or int((K+fp**2).subs(Y,X))%11==0 or int((K+fp*fm**2).subs(Y,X))%11==0)==(X not in (0,1,10)))
assert int(n_order(2,11))==10
for s in range(1,121):
    n=3*2**s+1
    if s%3==1: xyz=(F(2*n,7),F(15*n,7),30*n)
    elif s%3==2: xyz=(F(2*(n+1),7),2*n,F(2*n*(n+1),7))
    elif s%4==1: xyz=(F(4*n+2,15),4*n,F(4*n*(2*n+1),15))
    elif s%4==2: xyz=(F(4*n+8,15),4*n,F(2*n*(n+2),15))
    elif s%4==3: xyz=(F(2*n,5),F(4*n,5),4*n)
    elif s%60==24: xyz=(F(16*n,61),F(326*n,61),2608*n)
    else:
        X=2**((s-4)//4); f=2*X*X+2*X+1; g=2*X*X-2*X+1; x=3*f*g
        d=next(d for d in [f*f*g,g*g,f*f,f*g*g] if (x+d)%11==0)
        xyz=(x,F(n*(x+d),11),F(n*x*(x+d),11*d))
    exact(n,xyz)
exact(4,(2,3,6))
print('Proth3: all symbolic SG identities, all congruence roots, complete period 120 checked')
print('PASS independent printed-certificate checks')
