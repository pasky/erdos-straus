"""Exact packet, residue uniqueness and cubic divisor-budget checks (small boxes only)."""
from math import gcd, prod
from fractions import Fraction
from z81_cap_probe import factors, divisors, prime, packet


def ratio():
    cnt=multi=0
    for ell in range(101,20000,2):
        if not prime(ell): continue
        seen={}
        for k in (1,3,5,7,9):
            f=k*ell
            if (f+1)%4: continue
            Z=(f+1)//4
            for r in divisors(factors(Z)):
                if r<3 or r%2==0 or any(e!=1 for e in factors(r).values()): continue
                for a in divisors(factors(Z//r)):
                    if any(e!=1 for e in factors(a).values()) or a%2==0 or gcd(a,r)>1: continue
                    for v in divisors(factors(Z//(a*r))):
                        w=Z//(a*r*v)
                        if gcd(v,a*r)>1 or v%2==0 or gcd(w,r)>1: continue
                        # Finite box analogue of the large-pivot collision bound.
                        if (a*r**3)**2>=ell or v*v>=ell or 4*a*r*v<=9: continue
                        u=(-a*r**3*pow(v,-1,f))%f
                        assert (u%ell) not in seen; seen[u%ell]=1
                        n=u
                        while gcd(n,r)>1 or n<2: n+=f
                        S=(n*v+a*r**3)//f
                        y=n*a*r*v*w; z=Fraction(n*v*w*S,r*r)
                        assert z.denominator==r*r and y%r==0
                        assert Fraction(1,a*r*w*S)+Fraction(1,y)+1/z==Fraction(4,n)
                        cnt+=1; multi+=not prime(r)
    # Explicit multisupport case outside the tiny collision-safe box above
    a,r,v,w=7,15,11,13; f=4*a*r*v*w-1
    n=(-a*r**3*pow(v,-1,f))%f
    while gcd(n,r)!=1:n+=f
    S=(n*v+a*r**3)//f
    z=Fraction(n*v*w*S,r*r)
    assert z.denominator==225 and Fraction(1,a*r*w*S)+Fraction(1,n*a*r*v*w)+1/z==Fraction(4,n)
    return cnt,multi,(n,r,a,v,w)


def cubic():
    cnt=0
    for s in range(5,500,8):
        if not prime(s):continue
        for m in divisors(factors(s**3+1)):
            if m%4!=3: continue
            assert pow(m,(s-1)//2,s)==s-1
            for p in range(1,500,8):
                if not prime(p) or (p+m)%s or (p+m)%(s*s)==0: continue
                k=(p+m)//4; packet(p,m,k*s**3,s); cnt+=1
                assert (p*p*((s**3+1)//m)+2*p+m)%(s*s)==0
    return cnt

if __name__=='__main__': print('V collision/packet checks, multisupport example:',ratio()); print('h=3 exact packets and height integrality:',cubic())
