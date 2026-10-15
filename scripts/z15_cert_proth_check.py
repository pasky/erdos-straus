# O240 independent checker: ES for all n_s = c0*2^s + 1 from ET/divisor classes (JSON, polynomials in n) plus the
# Sophie-Germain window-11 rules (polynomials in X = 2^((s-4)/4), n = 16*c0*X^4 + 1, c0 = 3 only):
#   window m = 11 = 4*3*1^4 - 1, K = (n+11)/4 = 3(4X^4+1) = 3 f+ f-, f± = 2X^2 ± 2X + 1, d = 3^a f+^b f-^c,
#   x = K, y = n(K+d)/11, z = nK(K+d)/(11 d).   Rule for s == r (mod 40) uses X == 2^((r-4)/4) (mod 11).
import sys, json
from fractions import Fraction as F
from math import comb, isqrt
import sympy as sp
C=json.load(open(sys.argv[1])); SMAX=int(sys.argv[2]) if len(sys.argv)>2 else 1500
c0=C['c0']; assert c0==3 and C['k']==1 and C['b']==2
n=sp.Symbol('n'); X=sp.Symbol('X')
def intvalued(P,var,r,M):
    d=sp.degree(P,var) if P.has(var) else 0
    vals=[P.subs(var,r+M*t) for t in range(d+1)]
    return all(sp.Rational(sum((-1)**(i-j)*comb(i,j)*vals[j] for j in range(i+1))).q==1 for i in range(d+1))
ET=[]
for cl in C['classes']:
    P3=[sum(sp.Rational(c)*n**i for i,c in enumerate(p)) for p in cl['xyz']]
    assert sp.expand(4*P3[0]*P3[1]*P3[2]-n*(P3[0]*P3[1]+P3[1]*P3[2]+P3[0]*P3[2]))==0
    M,r=cl['M'],cl['r']
    for P in P3:
        assert intvalued(P,n,r,M)
        co=sp.Poly(P,n).all_coeffs(); assert co[0]>0 and (len(co)==1 or 1+max(abs(c/co[0]) for c in co[1:])<2**10)
    Mp=M
    while Mp%2==0: Mp//=2
    assert (2**360-1)%Mp==0 and M//Mp<=2**10       # n_s mod M periodic mod 360 for s >= 10
    if cl['fam']!='D': assert not any((a*a-r)%M==0 for a in range(1,4*M,2)), 'odd square in class'
    ET.append((M,r,[[F(c) for c in pp] for pp in cl['xyz']]))
# Sophie-Germain rules
N=16*c0*X**4+1; fp=2*X**2+2*X+1; fm=2*X**2-2*X+1; K=3*fp*fm
assert sp.expand(K-(N+11)/4)==0
SGRULE={}
for r in C['SG']:
    assert r%4==0
    X0=pow(2,((r-4)//4)%10,11)
    sol=None
    for a in range(3):
        for b in range(3):
            for c in range(3):
                d=3**a*fp**b*fm**c
                xs=[K,sp.cancel(N*(K+d)/11),sp.cancel(N*K*(K+d)/(11*d))]
                if not all(sp.fraction(sp.together(v))[1].free_symbols==set() for v in xs): continue
                if not all(intvalued(sp.expand(v),X,X0,11) for v in xs): continue
                assert sp.simplify(1/xs[0]+1/xs[1]+1/xs[2]-4/N)==0
                for v in xs:
                    co=sp.Poly(sp.expand(v),X).all_coeffs(); assert co[0]>0
                sol=(a,b,c,xs); break
            if sol: break
        if sol: break
    assert sol, ('no SG rule for residue',r)
    SGRULE[r]=sol
print('SG rules (a,b,c) per s mod 40:',{r:v[:3] for r,v in SGRULE.items()})
def etclass(s):
    N0=c0*2**s+1
    for M,r,f in ET:
        if N0%M==r: return f
    return None
for s in range(400,760):
    assert (s%40 in SGRULE) or etclass(s), ('uncovered',s%360)
used={'SG':0,'brute':0}
for s in range(0,SMAX+1):
    N0=c0*2**s+1; sol=None
    if s%40 in SGRULE and s>=4:
        xs=SGRULE[s%40][3]; Xv=2**((s-4)//4); assert 48*Xv**4+1==N0
        vals=[sp.Rational(v.subs(X,Xv)) for v in xs]
        if all(v.q==1 and v>0 for v in vals): sol=[int(v) for v in vals]; used['SG']+=1
    if sol is None:
        f=etclass(s)
        if f:
            vals=[sum(co*N0**i for i,co in enumerate(pp)) for pp in f]
            if all(v.denominator==1 and v>0 for v in vals): sol=[int(v) for v in vals]; used['ET']=used.get('ET',0)+1
    if sol is None:
        from ec_cert import es_brute
        sol=es_brute(N0); assert sol, ('no solution',s); sol=list(sol); used['brute']+=1
    a,b,cc=sol; assert 4*a*b*cc==N0*(a*b+b*cc+a*cc) and min(sol)>0, s
print('CHECK OK: ES for all 3*2^s+1; exact for s <=',SMAX,used)
