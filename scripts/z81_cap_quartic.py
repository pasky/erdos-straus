"""Exact packet, residue uniqueness and cubic divisor-budget checks (small boxes only)."""
from math import gcd, prod
from functools import lru_cache
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

def neighbor():
    # R3 reviewer's J=1 case. factorint proposes decompositions; Lucas tests
    # below independently certify every prime used, including the input p.
    from sympy import factorint
    @lru_cache(None)
    def certified_prime(p):
        if p==2: return True
        f={int(l):int(e) for l,e in factorint(p-1).items()}
        assert prod(l**e for l,e in f.items())==p-1 and all(certified_prime(l) for l in f)
        return all(any(pow(a,p-1,p)==1 and gcd(pow(a,(p-1)//l,p)-1,p)==1 for a in range(2,min(p,10000))) for l in f)
    p=3189177846574333650961; x=797296593515992469436; m=4*x-p
    assert certified_prime(p) and (9*p+4)%m==0 and m%12==11
    packet(p,m,9*x*x,3)
    counts=[]
    for j in [-1,0,1]:
        k=x+3*j; mod=4*k-p; N=p*k
        ff={int(l):int(e) for l,e in factorint(k).items()}; ff[p]=1
        assert prod(l**e for l,e in ff.items())==N and all(certified_prime(l) for l in ff)
        ds=divisors({l:2*e for l,e in ff.items()}); assert all((d+N)%mod for d in ds); counts.append(len(ds))
    return p,x,counts

if __name__=='__main__':
    cnt,multi,example=ratio()
    print(f'V collision-safe checks={cnt}, composite roots therein={multi}; separate multisupport example (n,r,a,v,w)={example}')
    print('h=3 exact packets and height integrality:',cubic())
    print('J=1 fixed x+3j misses (p,x,divisors examined):',neighbor())
