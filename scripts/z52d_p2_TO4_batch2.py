# z52d pass2 TO4 batch 2: Z1101, Z1283, Z1293, Z1397, Z1555, Z1605, Z1624, Z1629, Z1195, Z1041
import math, sys, statistics
from fractions import Fraction
from collections import Counter, defaultdict
from sympy import primerange, factorint, divisors
sys.path.insert(0,'scripts')
exec(open('scripts/z52d_p2_TO4_residual.py').read().split('# ---- Z0996')[0])  # reuse reduce, two_term
rows=[]
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); rows.append((t[0],t[2:2+t[1]]))
# ---- Z1101: 4M = d1+d2+d3 with d_i | pM (equiv. ES with denominators dividing pM); M ≤ 60
res=[]
for p in [p for p in primerange(5,400) if p%4==1]:
    ok=None
    for M in range(1,61):
        L=p*M; D=divisors(L)
        found=False
        target=4*M
        Ds=set(D)
        for i,d1 in enumerate(D):
            if d1>target: break
            for d2 in D:
                if d2<d1: continue
                d3=target-d1-d2
                if d3<d2: break
                if d3 in Ds: found=True; break
            if found: break
        if found: ok=M; break
    res.append((p,ok))
print("Z1101 p (p<400), least M≤60 with 4M=d1+d2+d3, d_i|pM:", [r for r in res][:12], "none:",[p for p,m in res if m is None])
# ---- Z1283 S-unit box: S={2,3,5,p}; x,y,z = 2^a 3^b 5^c p^d (≤ bound), 4/p = Σ1/x (count solutions), p small
def sunit_solutions(p, A=12):
    cand=set()
    for a in range(A+1):
        for b in range(A+1):
            for c in range(A+1):
                for d in range(2):
                    v=2**a*3**b*5**c*p**d
                    if v<=10**9: cand.add(v)
    cand=sorted(cand)
    sols=0
    for i,x in enumerate(cand):
        if 4*x<=p: continue
        for y in cand:
            if y<x: continue
            r=Fraction(4,p)-Fraction(1,x)-Fraction(1,y)
            if r<=0: continue
            if r.numerator==1 and r.denominator in set(cand) and r.denominator>=y: sols+=1
    return sols
print("Z1283 S-unit (S={2,3,5,p}, exps≤12, p-exp≤1, values≤1e9) solutions:", {p:sunit_solutions(p) for p in [13,37,73,97,193]})
# ---- Z1293 lines through rational point P=(3p/4,3p/4,3p/4) on 4xyz=p(xy+yz+zx): second intersection; integrality test
def second_points(p, P, D):
    # line X(t)=P+tD; F(t)=t*G(t) (P on surface); return rational points from roots of G (the two other intersections)
    import sympy as sp
    x0,y0,z0=P; d1,d2,d3=D
    t=sp.symbols('t')
    F=sp.expand(4*(x0+t*d1)*(y0+t*d2)*(z0+t*d3)-p*((x0+t*d1)*(y0+t*d2)+(y0+t*d2)*(z0+t*d3)+(z0+t*d3)*(x0+t*d1)))
    G=sp.cancel(F/t)
    out=[]
    for r in sp.solve(sp.Eq(G,0),t):
        if r.is_rational:
            out.append(tuple(sp.Rational(x0)+r*sp.Rational(d) for d in D))
    return out
def integral_positive(Q):
    if Q is None: return False
    xs=[sp.Rational(q) for q in Q]
    from math import lcm
    return all(q>0 for q in xs)
import sympy as sp
Zint=0; tot=0; examples=[]
for p in [409, 577, 2521]:
    P=(sp.Rational(3*p,4),)*3
    for d1 in range(-4,5):
        for d2 in range(-4,5):
            for d3 in range(-4,5):
                if (d1,d2,d3)==(0,0,0): continue
                for Q in second_points(p,P,(d1,d2,d3)):
                    tot+=1
                    if all(q.is_integer and q>0 for q in Q):
                        Zint+=1; examples.append((p,(d1,d2,d3),Q))
print("Z1293 lines through (3p/4)^3 (|d_i|≤4): rational second points",tot,"; with positive integer coordinates:",Zint, examples[:3])
# ---- Z1397: for x fixed, min over solutions of max(y,z)/p; scan primes p≡1 mod 24 ≤ 3000
mins=[]
for p in primerange(1000,3000):
    if p%24!=1: continue
    best=None
    for x in range(p//4+1,(3*p)//4+1):
        a,b=reduce(4*x-p,p*x)
        if a<=0: continue
        for (y,z) in two_term(a,b):
            m=max(y,z)/p
            if best is None or m<best: best=m
    mins.append((p,best))
print("Z1397 min over ES solutions of max(y,z)/p (p≡1 mod 24, 1000≤p<3000): median %.3f max %.3f"%(statistics.median([b for p,b in mins if b]), max(b for p,b in mins if b)), "p with min > sqrt(p)/p:", sum(1 for p,b in mins if b and b*p>math.sqrt(p)), "of", len(mins))
# ---- Z1555: fraction of primes (≡1 mod 4, p≤1e7 sample from file) with NO winner C ≤ K, vs K
ps=[(p,w) for p,w in rows if p>=1000]
for K in (10,25,50,100,200,400):
    z=sum(1 for p,w in ps if not any(c<=K for c in w))
    print("Z1555 K=%d zero-fraction %.5f (count %d of %d)"%(K, z/len(ps), z, len(ps)))
# ---- Z1041 (Janson-style): empirical P(N(p)=0) vs Poisson(mean) for p≡1 mod 24 in [1e4,1e6]
sample=[(p,w) for p,w in rows if 10**4<=p<=10**6 and p%24==1]
mu=statistics.mean(len(w) for p,w in sample)
z=sum(1 for p,w in sample if not w)
print("Z1041 P(N=0) empirical %.2e (count %d/%d) vs Poisson(mu=%.2f) %.2e"%(z/len(sample), z, len(sample), mu, math.exp(-mu)))
# ---- Z1605: minimal c with Type II (c,d) solution for C-form exceptions ≤1e6 (and 193,2521 controls)
exec(open('scripts/z52d_p2_TO4_forms.py').read().split('if __name__')[0])
def min_c(p, cmax=12, dmax=60):
    for c in range(1,cmax+1):
        for d in range(1,dmax+1):
            if typeII(p,c,d): return (c,d)
    return None
for p in [193,409,577,2521,5569,9601]:
    print("Z1605 p=%d minimal (c,d) Type II:"%p, min_c(p))
# ---- Z1624: Type I (c=1) ⟺ ∃k: kp+1 has a divisor f ≡ -p (mod 4k)  (f = 4dk - p). Verify vs direct typeI(c=1,d≤D)
agree=0; tot=0; dis=[]
for p in primerange(5,600):
    if p%4!=1: continue
    direct=any(typeI(p,1,d) for d in range(1,80))
    alt=False
    for k in range(1,400):
        m=4*k; N=k*p+1
        for f in divisors(N):
            if f>0 and f%m==(-p)%m: alt=True; break
        if alt: break
    tot+=1
    if direct==alt: agree+=1
    else: dis.append((p,direct,alt))
print("Z1624 agreement direct(d<80) vs shifted-k form (k<400):",agree,"of",tot,"disagreements",dis[:6])
# ---- Z1629: p=409 symbol vs congruence: divisors a of 4C*409+1 with a≡3 (mod 4) and (a/409)=-1 vs a≡-1 mod 4C
from sympy import jacobi_symbol
p=409; n4=0; nQNR=0; nwin=0
for C in range(1,301):
    N=4*C*p+1; f=factorint(N); divs=[1]
    for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
    m=4*C
    if any(a>1 and a%4==3 and jacobi_symbol(a%p,p)==-1 for a in divs): n4+=1
    if any(a>1 and a%m==m-1 for a in divs): nwin+=1
print("Z1629 p=409, C≤300: #C with a divisor ≡3 mod 4 that is QNR mod 409:",n4," #C with winner (a≡-1 mod 4C):",nwin)
