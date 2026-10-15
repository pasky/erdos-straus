# Independent checker: ES for all n_s = 4^s + 105, s >= 0, from 13 ET/divisor classes (data/s6_cert105_et.json,
# polynomials in n) plus ONE exponential class:  s = 34 (mod 45),  u := 4^((s-4)/3) = 32 (mod 151),  n = 256u^3 + 105,
#   x = 64(u^3+1),  A = (64u^3 + 2u^2 - 2u + 66)/151,  y = n*A,  z = 32 n (u+1) A.
import sys, json
from fractions import Fraction as F
from math import comb
import sympy as sp
C=json.load(open(sys.argv[1])); SMAX=max(100,int(sys.argv[2]) if len(sys.argv)>2 else 1000)   # always covers s<64
n=sp.Symbol('n'); u=sp.Symbol('u')
ET=[]
for cl in C['classes']:
    X=[sum(sp.Rational(c)*n**i for i,c in enumerate(p)) for p in cl['xyz']]
    assert sp.expand(4*X[0]*X[1]*X[2]-n*(X[0]*X[1]+X[1]*X[2]+X[0]*X[2]))==0
    M,r=cl['M'],cl['r']
    for P in X:   # integer-valued on n = r + M t: forward differences at t=0..deg integral
        d=sp.degree(P,n) if P.has(n) else 0
        vals=[P.subs(n,r+M*t) for t in range(d+1)]
        for i in range(d+1):
            assert sp.Rational(sum((-1)**(i-j)*comb(i,j)*vals[j] for j in range(i+1))).q==1
        # positivity for n >= 4^4: check leading coeff and Cauchy bound
        co=sp.Poly(P,n).all_coeffs()
        assert co[0]>0 and (len(co)==1 or 1+max(abs(c/co[0]) for c in co[1:])<4**4)
    Mp=M
    while Mp%2==0: Mp//=2
    assert (4**360-1)%Mp==0 and (M//Mp)<=2**128   # 2-part divides 4^64: n_s mod M periodic for s>=64
    ET.append((M,r,[[F(c) for c in pp] for pp in cl['xyz']],X))
# exponential class
x=64*(u**3+1); A=(64*u**3+2*u**2-2*u+66)/151; N=256*u**3+105
assert sp.simplify(4/N-1/x-1/(N*A)-1/(32*N*(u+1)*A))==0
for t in range(4):   # A integer-valued on u = 32 + 151 t (cubic: differences at t=0..3)
    pass
vals=[A.subs(u,32+151*t) for t in range(4)]
assert all(sp.Rational(sum((-1)**(i-j)*comb(i,j)*vals[j] for j in range(i+1))).q==1 for i in range(4))
assert pow(4,10,151)==32 and pow(4,15,151)==1    # s=34 (45) => (s-4)/3 = 10 (15) => u = 4^10 = 32 (151)
# T1 controls: n mod 151 on the exponential class is a non-residue (no square there); ET non-divisor classes: no odd squares
from math import isqrt
# exp class is not a congruence class in n (n = 59 mod 151 is a QR); T1 holds globally (Lemma-1.1 T1 / ET Prop 1.6):
assert not any(isqrt(256*(32+151*t)**3+105)**2==256*(32+151*t)**3+105 for t in range(200000))
for cl in C['classes']:
    if cl['fam']!='D': assert not any((a*a-cl['r'])%cl['M']==0 for a in range(1,4*cl['M'],2)), ('square in class',cl['M'],cl['r'])
print('static checks ok',flush=True)
# coverage of every s mod 360 at representatives s in [64, 424)
def etclass(s):
    N0=4**s+105
    for M,r,f,X in ET:
        if N0%M==r: return (M,r,f)
    return None
for s in range(64,64+360):
    assert etclass(s) or s%45==34, ('uncovered',s%360)
# exact verification for all 0 <= s <= SMAX (any s: ET class if it applies and values positive integers, else exp class)
used={'exp':0}
for s in range(0,SMAX+1):
    N0=4**s+105; sol=None
    c=etclass(s)
    if c:
        xs=[sum(co*N0**i for i,co in enumerate(pp)) for pp in c[2]]
        if all(v.denominator==1 and v>0 for v in xs): sol=[int(v) for v in xs]; used[c[0]]=used.get(c[0],0)+1
    if sol is None and s%45==34 and s>=4:
        U=4**((s-4)//3); assert (64*U**3+2*U**2-2*U+66)%151==0
        Aa=(64*U**3+2*U**2-2*U+66)//151; sol=[64*(U**3+1),N0*Aa,32*N0*(U+1)*Aa]; used['exp']+=1
    if sol is None:   # small s: brute force
        from ec_cert import es_brute
        sol=es_brute(N0); assert sol, ('no solution',s); sol=list(sol); used['brute']=used.get('brute',0)+1
    a,b,cc=sol; assert 4*a*b*cc==N0*(a*b+b*cc+a*cc) and min(sol)>0, s
print('timing ok',flush=True) if False else None
print('CERTIFIED-CHECK OK: ES for 4^s+105, all s; exact for s <=',SMAX,'usage',used)
