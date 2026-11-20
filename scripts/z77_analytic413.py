"""Rational exponent and CRT checks for notes/z77/ANALYTIC_413.md."""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from collections import defaultdict

k,l=F(1418,5119),F(2917,5119)
for a in [1,F(1,2),0]:
    m=a+(1+a)*k
    t1=2*m/(1-l+6*m); t2=(1+l+k)/(4+2*l+3*k); t=max(t1,t2)
    print(f'prefactor P^{a}: first={t1}, second={t2}, global={t}')
    for alpha,b,g in [(t,1-2*t,t),(t,t,1-2*t),((1-t)/2,(1-t)/2,t)]:
        assert alpha+b+g==1 and b>=alpha>=t and g>=t
        r=b-t; j=2*(a*r+g-t); d=1+2*r+j-b-2*g
        last=a*r+((1+l)*g+k*d)/2
        assert r>=0 and j>=0 and 2*r+j<g and 2*r+g>=b and 3*g-1<l*g
        assert d>0 and b-2*r<=t and b-g<=t and last<=t
        print('  alpha,beta,gamma',alpha,b,g,'H margin',g-2*r-j,'d',d,'last',last)
for t in [F(3,10), F(4,13), F(7955,24966)]:
    r=1-3*t; print('theta',t,'rho',r,'allowed corr exponent',t-2*r,'excess vs sqrt',t/2-(t-2*r))
    assert t/2-(t-2*r)==2-F(13,2)*t

# CRT test of the complete-sum factorisations, as coefficient identities
# BEFORE evaluation at a root of unity. A coefficient is indexed by its
# additive phase in Q^-1 Z/Z. Test n divisible by none, one, or both primes.
def chi(x,p):
    u=pow(x%p,(p-1)//2,p); return u if u<=1 else -1
for q,r in combinations((3,5,7),2):
    Q=q*r
    for n,c,h in product([1,q,r,Q],range(Q),range(Q)):
        def v(x,p): return chi((4*c*x-n)**2-4*x,p)
        lhs=defaultdict(int); rhs=defaultdict(int)
        for x in range(Q): lhs[h*x%Q]+=v(x,q)*v(x,r)
        for x,y in product(range(q),range(r)):
            j=r*(h*pow(r,-1,q)%q)*x+q*(h*pow(q,-1,r)%r)*y
            rhs[j%Q]+=v(x,q)*v(y,r)
        assert lhs==rhs
        if h%q==0:
            K=sum(v(x,q) for x in range(q)); assert K==(0 if c%q==0 else q-1 if (4*c*n+1)%q==0 else -1)
            assert all(lhs[j]==K*sum(v(y,r) for y in range(r) if (h*y)%Q==j) for j in range(0,Q,q))
print('CRT coefficient and exceptional-mode checks passed')
for D in (3,15,105):
    count=lambda u,v: sum((n+u+v)%(u*v)==0 for n in range(0,D*u*v,D))
    for u,v in product(range(1,19),repeat=2):
        g=gcd(D,u*v); assert count(u,v)==(g if (u+v)%g==0 else 0)
    for p in (3,5,7):
        # Local conditional weight relative to 1/(uv), in p-by-p boxes.
        z=sum((p if i==j==0 else 0) if i*j%p==0 else 1 for i,j in product(range(p),repeat=2))
        assert F(z,p*p)==1-F(1,p)+F(1,p*p)
print('nonunit endpoint-pair local factors checked')
