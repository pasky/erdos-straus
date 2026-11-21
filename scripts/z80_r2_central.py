"""Round-2 finite controls; analytic statements are not extrapolations of these."""
from fractions import Fraction as F
from math import gcd, pi, exp, log
from cmath import exp as ce


def parity():
    for j in (0,1):
        for a in range(1,80):
            for b in range(1,81):
                if gcd(a,b)>1 or (a+b)%2==0: continue
                r=(-a-b+4*j*a*b)%(8*a*b)
                assert gcd(r,8*a*b)==1
                for d in range(1,11): assert ((4*a*b*d-a-b)%(8*a*b)==r)==(d%2==j)
        for h in range(1,6):
            q=2**(h+3); a=2**h
            assert {(-a-b+4*j*a*b)%q for b in range(1,q,2)}==set(range(1,q,2))
    print('pair parity classes checked (including fixed valuation 2^1,...,2^5)')
    for p,a,b,d,oo in ((6955940568721,4,59,7368581111,42),(1590284203561,15,26984,982239,52)):
        assert 4*a*b*d-a-b==p and d%2==1
        print('Lane 7 panel: odd witness',p,(a,b,d),'inherited ordered totals odd/even',oo,0)


def areas():
    assert 1-(2-3*F(4,7))**2==F(45,49)
    assert 3*F(1,2)**2==1-(2-3*F(1,2))**2==F(3,4)
    assert 2*F(19,21)**3*(F(1,3)-F(4,19))/(14*19**2)==F(1,3*21**3)
    print('BT central bound',6-12*log(1.5),'relative full first moment upper',6.75-12*log(1.5))
    for theta in [F(1,2),F(4,7),F(2,3)]:
        t=420; hit=0; total=0
        for i in range(t+1):
            for j in range(t-i+1):
                total+=1; hit+=t-max(i,j,t-i-j)<=theta*t
        print('individual theta',theta,'triangle grid fraction',round(hit/total,5))


def inverse_pool():
    # Poisson on Schwartz Gaussians (rather than compact windows): checks both
    # signs and normalisations of (S') at actual traces, not a lower-bound test.
    def e(x):return ce(2j*pi*x)
    for n,x,Q,R,E in ((757,29,15,77,3),(997,37,35,143,4)):
        u0=n/(4*x); factors=[]
        for q,c in ((Q,.7),(R,-.9)):
            p=next(i for i in range(2,q) if q%i==0); r=q//p
            def leg(z,l):
                t=pow(z%l,(l-1)//2,l);return -1 if t==l-1 else t
            def chi(u):
                z=(4*x*u-n)**2-4*u;return leg(z,p)*leg(z,r)
            z=0j
            for h in range(-12*E,12*E+1):
                g=sum(chi(i)*e(h*i/q) for i in range(q))/q**.5
                z+=exp(-pi*(h/E-c)**2)*g*e(-h*u0/q)/E
            z1=0j
            for u in range(int(u0-12*q/E)-1,int(u0+12*q/E)+2):
                t=(u0-u)*E/q
                z1+=chi(u)*exp(-pi*t*t)*e(-c*t)/q**.5
            assert abs(z-z1)<1.e-10
            factors.append((z,z1))
        a,b=factors; diff=abs(a[0]*b[0].conjugate()-a[1]*b[1].conjugate())
        print('pooled vs common-integer transform',Q,R,'residual',f'{diff:.2e}')


def multiplier():
    from math import isqrt
    hits=[0,0]; swaps=set()
    for p in (1009,1223,2003):
        for a in range(1,10,2):
            for k in range(1,10,2):
                for l in (11,13,17,19,23,29,31):
                    b=k*l; f=4*a*b
                    if gcd(a,b)>1:continue
                    for e in range(1,l,2):
                        if (a+b)%e:continue
                        c=(a+b)//e
                        for j in (0,1):
                            numer=(e*p+1,p+e)[j]
                            if numer%f:continue
                            d=numer//f; hits[j]+=1
                            if j: assert 4*a*b*c*d==a+b+p*c and f*(4*a*c*d-1)==4*a*(c*p+a)
                            else: assert 4*a*b*c*d==c+p*(a+b)
    assert min(hits)>0
    print('multiplier injection identities tested on small hits (I,II)',hits)

if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 180 uv run --offline --no-project python -B scripts/z80_r2_central.py')
    parity();areas();inverse_pool();multiplier()
