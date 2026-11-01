"""z52d pass2 TO6 fix: Z2056 / Z2302. Rational parametrisation of 4/n = 1/x+1/y+1/z from the fibre over x:
a=4x-n, b=nx, (ay-b)(az-b)=b^2; with t=u/v: y = nx(u+v)/(v a), z = nx(u+v)/(u a). Verified symbolically (sympy).
Integrality census: for n prime, count (x,u,v) in a box with y,z positive integers; compare with the integer solutions."""
import sympy as sp, sys
from fractions import Fraction
x,n,u,v=sp.symbols('x n u v')
a=4*x-n; b=n*x
y=n*x*(u+v)/(v*a); z=n*x*(u+v)/(u*a)
print('identity check (should be 0):', sp.simplify(1/x+1/y+1/z-4/n))
print('ES cubic check (should be 0):', sp.simplify(4*x*y*z-n*(x*y+y*z+z*x)))
def census(p, X, U):
    sols=set(); total=0; integral=0
    for xx in range(1,X+1):
        a_=4*xx-p
        if a_<=0: continue
        for uu in range(1,U+1):
            for vv in range(1,U+1):
                if sp.gcd(uu,vv)!=1: continue
                total+=1
                num=p*xx*(uu+vv)
                if num % (vv*a_) or num % (uu*a_): continue
                yy=num//(vv*a_); zz=num//(uu*a_)
                integral+=1; sols.add((xx,yy,zz))
    return total, integral, sorted(sols)
res={}
for p in [13,17,29]:
    tot,integ,S=census(p, 400, 60)
    res[p]=dict(box_rational_points=tot, integral=integ, distinct_integer_solutions=len(S), example=S[:4])
    print(p, res[p])

# saturation check with faster loop (math.gcd): does the integer count reach the 24 positive ordered solutions of 4/13?
from math import gcd
def census_fast(p, X, U):
    S=set()
    for xx in range(1,X+1):
        a_=4*xx-p
        if a_<=0: continue
        for uu in range(1,U+1):
            for vv in range(1,U+1):
                if gcd(uu,vv)!=1: continue
                num=p*xx*(uu+vv)
                if num % (vv*a_) or num % (uu*a_): continue
                S.add((xx,num//(vv*a_),num//(uu*a_)))
    return S
for U,X in [(60,400),(200,200)]:
    S=census_fast(13,X,U)
    print('p=13 box U=%d X=%d: distinct integer positive ordered solutions:'%(U,X), len(S), 'max coordinate', max(max(s) for s in S))
