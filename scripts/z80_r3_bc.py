"""Exact small-cell/optimization checks for the first beyond-half central chart."""
from fractions import Fraction as F
from math import gcd, lcm, pi
from cmath import exp
from collections import Counter, defaultdict


def patch():
    k,l=F(7,20),F(1,4)
    r1=1+2*k+l; h1=F(1,2)+k-1
    r2=1+2*F(3,8)+F(1,8); h2=F(1,2)+F(3,8)+F(1,8)-1
    assert (r1,h1,r2,h2)==(F(39,20),F(-3,20),F(15,8),0)
    intercept=1-r1/2; slope=r1+2*h1; smax=intercept/(1+slope)
    assert (smax,intercept)==(F(1,106),F(1,40))
    for x,s in ((0,0),(intercept,0),(smax,smax)):
        y=F(1,2)+s
        assert x+r1*y+h1*(2*y-1)<=1 and x+r2*y<1
        assert y>2*x and x+s<=F(1,2) and r1+h1>0
        print('x,s',x,s,'BC-1,BC-2',x+r1*y+h1*(2*y-1),x+r2*y)
    assert 2*smax*intercept==F(1,2120)
    print('normalized boost',2*smax*intercept,'full coefficient in M0 units',F(3,4)+2*smax*intercept)


def congruences():
    atoms=[(a,4*a*d-1) for a in range(1,10) for d in range(1,6)]
    nchecks=0; noncop=0
    for a,q in atoms:
        for b,r in atoms:
            g=gcd(q,r); m,n=q//g,r//g; L=g*m*n
            if a==b or (a-b)%g:continue
            for t in (1,2,3,5,6,10):
                if gcd(t,L)!=1:continue
                u=(a-b)//g
                phase=-F(a,t*L)+F(u*pow(t*m,-1,n),n)+F(a*pow(q*n,-1,t),t)
                # Not a recomputation of the CRT formula: check directly at both periods.
                y=(phase%1)*L; assert y.denominator==1
                assert (t*y+a)%q==0 and (t*y+b)%r==0
                nchecks+=1; noncop+=int(g>1)
    print('CRT cases',nchecks,'with gcd>1',noncop)


def marked():
    counts=Counter(); tags=defaultdict(Counter)
    for a in range(4,13):
        for b in range(4,13):
            for d in range(4,13):
                t,u=a*b*d,a+b; counts[4*t-u]+=1; tags[t][u]+=1
    cross=0; coupled=0; off=0
    for t,row in list(tags.items()):
        for u,z in row.items():
            for h in range(-5,6):
                c=z*tags.get(t+h,{}).get(u+4*h,0); coupled+=c
                if h:off+=c
                cross+=z*sum(tags.get(t+h,{}).values())
    assert coupled==sum(x*x for x in counts.values()) and 0<off<coupled<cross
    print('toy 6-variable sum',coupled,'nonzero-shift portion',off,'unmarked',cross)


def rational_band():
    # Aliases and short primitive-frequency mass of the actual polynomial. Small primes
    # here: numerical control, not an asymptotic bound with a specified constant.
    ps=[5,7,11,13]; m=5*7*11*13; x=17; n=4*5**19
    assert all((x*(4*x*n+1))%p for p in ps)
    tables={}
    for p in ps:
        row=[]
        for u in range(p):
            a=pow(((4*x*u-n)**2-4*u)%p,(p-1)//2,p); row.append(-1 if a==p-1 else a)
        tables[p]=[sum(s*exp(-2j*pi*(b*u%p)/p) for u,s in enumerate(row))/p for b in range(p)]
    alias={}
    for i,j,k,l in ((5,7,11,13),(5,11,7,13),(5,13,7,11)):
        assert i*j*k*l==m
    masses=[]
    for offset in (0,600,1800):
        mass=0.
        for b in range(1+offset,1+offset+m//5):
            if gcd(b,m)>1:continue
            coeff=1
            for p in ps: coeff*=tables[p][b*pow(m//p,-1,p)%p]
            mass+=m*abs(coeff)**2
        masses.append(round(mass/(m//5),4))
    print('primitive interval masses / length for toy m',m,masses)

if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 120 uv run --offline --no-project python -B scripts/z80_r3_bc.py')
    patch();congruences();marked();rational_band()
