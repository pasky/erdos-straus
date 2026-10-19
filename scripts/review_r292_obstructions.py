#!/usr/bin/env python3
"""Independent R292 obstruction arithmetic; no author-code imports.
Fraction arithmetic and divisor triples; no large arrays.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from sympy import factorint, factor_list, symbols, Poly
Y=symbols('Y')

def divisors(n):
    low=[a for a in range(1,isqrt(n)+1) if n%a==0]
    return sorted(set(low+[n//a for a in low]))

def two_power(e): return F(2**e) if e>=0 else F(1,2**(-e))

def check(c,k):
    total=c+k; J=next(j for j in range(1,10) if 4**j==total); E=2*J+2
    assert k%8==1 and c%2==1 and max(factorint(c).values())<4
    # Universal Capelli hypotheses: a valuation ±1 rules out every odd power,
    # and v2(k/(4c))=-2 rules out a rational fourth power.
    vals=dict(factorint(F(k,c).numerator))
    for p,v in factorint(F(k,c).denominator).items(): vals[p]=-v
    assert any(abs(v)==1 for v in vals.values())
    def bound(m):
        r=F(total+m,m)
        return max(2**E*total+2**(2*E+2)*r*r, 2**(E+2)*r*r+total)
    # Derive one coarse constant bound at the smallest positive candidate,
    # then enumerate w by that constant, unlike the author's stopping loop.
    w0=1
    while 4*c*w0**4-k<=0: w0+=2
    B0=bound(4*c*w0**4-k)
    ws=[]; hits=[]
    for w in range(w0,1000,2):
        m=4*c*w**4-k
        if m>B0: break
        if m>bound(m): continue
        ws.append(w); M=total+m
        for a1 in divisors(M):
            for a2 in divisors(M//a1):
                for t1,t2,t3 in [(i,j,2-i-j) for i in range(3) for j in range(3-i)]:
                    for owner in range(3):
                        e1=-t1+2*J*(owner==0); e2=-t2+2*J*(owner==1)
                        v=(two_power(e1)*a1+two_power(e2)*a2)/m
                        if v.denominator & (v.denominator-1)==0:
                            hits.append((m,a1,a2,e1,e2))
        # Newton valuations tested on every irreducible factor for modest D;
        # NOT a replacement for the general proof/Capelli theorem.
        for D in range(1,17):
            assert len(factor_list(c*Y**D+k)[1])==1
            for poly,power in factor_list(c*Y**D+k+m)[1]:
                Q=Poly(poly,Y); ratio=F(Q.eval(1),Q.eval(0))
                def v2(n):
                    out=0
                    while n%2==0: out+=1; n//=2
                    return out
                assert v2(ratio.numerator)-v2(ratio.denominator)==F(-2*Q.degree(),D)
    else: raise AssertionError('coarse bound unexpectedly too large')
    print((c,k),'candidate odd w',ws,'relation windows',sorted({h[0] for h in hits}))
    return {h[0] for h in hits}

for c,k in [(15,1),(31,33),(7,57),(63,1),(47,17),(55,9)]: assert check(c,k)==set()
for c,k,m in [(3,1,11),(7,9,19),(23,41,51),(39,25,131)]: assert check(c,k)=={m}

# Different bounds for boxed equation: from a>=1, d<=21 and
# (m1-16)(m2-1)<=20. If m2>=2, m1<=36. If m2=1,
# d=1 gives m1=4+20/(a-1)<=24; d>=2 gives m1<=20.
# Retain a<=81 from the paper's separately re-derived P<=4 cases.
sol=[]
for d,m1,a in product(range(1,22),range(1,37),range(1,82)):
    num=m1+4*a; den=a*m1*d-16
    if den>0 and num%den==0:
        m2=num//den
        assert a*(m1*m2*d-4)==m1+16*m2
        sol.append((a,d,m1,m2))
odd=[r for r in sol if r[0]%2 and r[1]%2]
assert len(sol)==39 and len(odd)==31
special={(a,d,(4*a*a*d+1)//15) for a,d,_,_ in odd if (4*a*a*d+1)%15==0}
assert special=={(1,11,3)}
print('boxed equation:',len(sol),'solutions;',len(odd),'odd;',special)

# Attack incidental Open Problem 4 claim: are the displayed Proth3 rules
# sufficient for all 48X^4+1 with X=2^t 3^u?
for t,u in product(range(20),repeat=2):
    X=2**t*3**u; n=48*X**4+1
    sg=X%11 not in (0,1,10)
    elementary=n%7 in (0,6) or n%15 in (7,13) or n%5==0 or n%61==0
    if not (sg or elementary):
        print('Open Problem 4 counterexample to claimed rule coverage:',(t,u),'X=',X,'n=',n,
              'residues mod 7,15,61=',[n%q for q in (7,15,61)])
        break
else: raise AssertionError('no counterexample found')
print('PASS obstruction enumeration; incidental overclaim exposed')
