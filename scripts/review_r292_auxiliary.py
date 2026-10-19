#!/usr/bin/env python3
"""R292 independent audit of auxiliary JSON leaves and incidental identities.
Imports only this review's independent checker, not the author's code.
"""
import json
from math import prod,lcm,gcd
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from sympy import symbols, Poly, cancel, cyclotomic_poly, divisors, factorint, n_order
from review_r292_certificates import et,exact,Y

for c,k in [(3,1),(6,1),(7,9)]:
    leaves=json.loads(Path(f'data/c1/cert_c{c}_k{k}_leaves.json').read_text())
    L=lcm(*(r['L'] for r in leaves)); assert all(any(s%r['L']==r['u'] for r in leaves) for s in range(L))
    mismatches=[]
    for leaf in leaves:
        tok=leaf['tok']; u,ell=leaf['u'],leaf['L']
        if tok[0]!='W':
            kind={'P':'II2','I':'I3','D':'D'}[tok[0]]
            p=tuple(map(int,tok[1:]))
            if kind!='D': p=(*p[:2],prod(p[2:]))
            M,pred,xyz,params=et(kind,p,c*Y+k)
            odd=M
            while odd%2==0: odd//=2
            period=int(n_order(4,odd)) if odd>1 else 1
            start=u+ell*((10-u+ell-1)//ell)
            for s in range(start,start+lcm(ell,period),ell):
                if not pred((c*pow(4,s,M)+k)%M): mismatches.append((u,ell,tok,s)); break
            # Denominators still verified, independently of membership.
            exact(c*4**start+k,[cancel(v).subs(Y,4**start) for v in xyz])
        else:
            m,j,code,w,h=map(int,tok[1:]); E=2*j-2
            assert c%2==1, 'no even-c window in these files'
            n= c*Y+k
            if code==0:
                shift,sigma,omega,D=j,h,2,h
                pieces=[cancel(w**int(Poly(cyclotomic_poly(2*d,Y),Y).degree())*cyclotomic_poly(2*d,Y/w)) for d in divisors(h)]
            elif code==2:
                shift,sigma,omega,D=j+1,2,1,4
                pieces=[2*Y**2+2*w*Y+w*w,2*Y**2-2*w*Y+w*w]
            else: raise AssertionError(code)
            n=c*4**shift*Y**D+k; N=n*(n+m)/4
            pieces=[p for p,v in factorint(c).items() for _ in range(v)]+[n]+pieces
            assert cancel(2**E*prod(pieces)-N)==0
            eps=leaf['rel']['eps']; i=leaf['rel']['i']
            d1=2**max(0,i)*prod(p for p,e in zip(pieces,eps) if e==1)
            d2=2**max(0,-i)*prod(p for p,e in zip(pieces,eps) if e==-1)
            for d in (d1,d2): assert Poly(cancel(N/d),Y).domain.is_ZZ
            period=sigma*int(n_order(2**omega,m))
            start=u+ell*max(0,(shift-u+ell-1)//ell)
            for s in range(start,start+lcm(ell,period),ell):
                assert (s-shift)%sigma==0
                V=pow(2,omega*((s-shift)//sigma),m)
                assert int((Y*0+d1+d2).subs(Y,V))%m==0
    print('Auxiliary leaves',c,k,'count',len(leaves),'period',L,'class-membership mismatches',mismatches)
    assert mismatches==[]

# All seven ET shapes: bounded side-condition sample, symbolic identities,
# odd-square exclusion with the precise fixed-parameter coprimality caveat.
counts={}
for kind in ['I1','I2','I3','I4','II1','II2','II3']:
    count=0
    for p in product(range(1,7),repeat=3):
        try: M,pred,xyz,params=et(kind,p,Y)
        except AssertionError: continue
        x,y,z=xyz
        assert cancel(4*x*y*z-Y*(x*y+y*z+z*x))==0
        constants=list(p)
        if kind=='I1': constants.append((4*p[0]*p[0]*p[1]+1)//p[2])
        elif kind in ('I4','II1'): constants.append((p[0]+p[1])//p[2])
        elif kind=='II2': constants.append((p[2]+1)//(4*p[0]*p[1]))
        P=prod(constants)
        for t in range(1,24,2):
            if gcd(t,P)==1: assert not pred(t*t),(kind,p,t)
        count+=1
    counts[kind]=count
print('All seven ET shapes, odd-square tests:',counts)

# Proth elementary six identities, now symbolic as well as period-checked.
n=Y
triples=[(2*n/7,15*n/7,30*n),(2*(n+1)/7,2*n,2*n*(n+1)/7),
((4*n+2)/15,4*n,4*n*(2*n+1)/15),((4*n+8)/15,4*n,2*n*(n+2)/15),
(2*n/5,4*n/5,4*n),(16*n/61,326*n/61,2608*n)]
for x,y,z in triples: assert cancel(4*x*y*z-n*(x*y+y*z+z*x))==0
# Third mechanism in Remark 4.2(ii).
n=3*Y**3+1; a=80; c=1; d=(21*Y+64)/320; b=(Y**2-3*Y+9)/7
assert cancel(4*a*b*c*d-n*c-a-b)==0
for s in [36,48,72,84]:
    V=2**(s//3); assert all(F(q.subs(Y,V)).denominator==1 for q in [b,d])
    exact(3*2**s+1,[q.subs(Y,V) for q in (a*b*d,a*c*d*n,b*c*d*n)])
# Remark 4.10(i): independent primality by trial division + order/nonresidue.
q=18837001
assert all(q%p for p in range(2,int(q**0.5)+1))
assert int(n_order(4,q))==45 and pow((pow(4,34,q)+105)%q,(q-1)//2,q)==q-1
# Remark 2.9: screen the 360 exponent classes, streaming primes below 3e6.
from sympy import primerange
uncovered=set(range(360)); witnesses={}
for q in primerange(3,3_000_000):
    if pow(4,360,q)!=1: continue
    for s in list(uncovered):
        n=(pow(4,s,q)+105)%q
        if n==0 or pow(n,(q-1)//2,q)==q-1:
            uncovered.remove(s); witnesses[s]=q
    if not uncovered: break
assert not uncovered,uncovered
print('4^s+105 unit-square screen: all 360 residues excluded, largest prime used',max(witnesses.values()))
# Mordell-hard claims are assertions about primitive square residues.
hard={1,121,169,289,361,529}
for s in range(3,123):
    assert (((3*pow(2,s,840)+1)%840 in hard)==(s%12==0))
    assert (((63*pow(2,s,840)+1)%840 in hard)==(s%4==0))
    if s%2==0: assert (7*pow(4,s,840)+9)%840==121
    assert (pow(4,s,840)+105)%840 in hard
    if s%3==0: assert (15*pow(2,s,840)+1)%840==121
print('PASS auxiliary leaves, seven ET shapes, incidental identities and screens')
