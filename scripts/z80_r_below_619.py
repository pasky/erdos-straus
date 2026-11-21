"""Small pointwise controls and exact arithmetic for R_BELOW_619.md (stdlib)."""
from fractions import Fraction as F
from math import gcd, lcm, isqrt, pi
from cmath import exp


def controls():
    from z79_analytic_push import has_word, has_u7
    zeros = (409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281)
    z7 = (105,1465,3865,4545,10305,12145,39361,67425)
    for ns,m in ((range(3,80,2),4),((131,241),8),(zeros+(17401609,),4),(z7,4)):
        sq = isinstance(ns,range)
        for n in ns:
            assert not has_word(n*n if sq else n, m)
        print('zero controls M=',m,'odd squares' if sq else '',len(ns))
    assert not any(map(has_u7,z7))
    print('U7 misses',z7)


def all_counts(B,M):
    ans=[0]*(B+1)
    for a in range(1, (1+isqrt(1+M*B))//M+1):
        d=1
        while (M*a*d-1)*a<=B+a:
            k=M*a*d-1
            if k>0:
                for b in range(a,(B+a)//k+1):
                    n=k*b-a
                    if n>=2: ans[n]+=1+(a!=b)
            d+=1
    return ans


def small_words():
    B=50000
    ans4=all_counts(B,4)
    for m in (1,4,8,37,193,1000):
        c=all_counts(B,m)
        if m==8: assert all(x<=y for x,y in zip(c,ans4))
        # Only a finite observed ratio, not a choice of analytic implied constant.
        i=max(range(2,B+1),key=lambda n:c[n]/(1+n**.5/m**(7/6)))
        print('M',m,'max (n,R)',c.index(max(c)),max(c),'largest observed R/(1+n^.5/M^(7/6))',round(c[i]/(1+i**.5/m**(7/6)),5),'at',i)
        if m>=4: assert c[m-2]>=1


def selberg():
    primes=(5,7,11,13)
    D=sorted({1,5,7,11,13,35})
    mu=lambda d:(-1)**sum(d%p==0 for p in primes)
    phi=lambda d:sum(gcd(i,d)==1 for i in range(1,d+1))
    G=1/sum(F(1,phi(d)) for d in D)
    lam={d:G*d*sum(F(mu(k)*mu(k//d),phi(k)) for k in D if k%d==0) for d in D}
    assert lam[1]==1 and max(map(abs,lam.values()))<=1
    assert sum(x*y/lcm(i,j) for i,x in lam.items() for j,y in lam.items())==G
    # Restricted unit class, simultaneous small-prime factor and large-prime deletion.
    mod=lcm(2,3,*D); l=15; r=7
    terms=[(i,x) for i,x in lam.items()]
    mass=sum((gcd(n,6)==1)*sum(x for i,x in terms if n%i==0)**2 for n in range(r,mod,l))/ (mod//l)
    expect=F(1,2)*sum(x*y/lcm(i,j) for i,x in terms for j,y in terms if gcd(i*j,l)==1)
    assert mass==expect
    print('finite Selberg example',G,'conditional product',mass)


def partial_pin():
    # Compare the partial-k reversal and full-cylinder mass by exact finite Haar.
    # Here f=3*5 samples its mixed gcd from two different earlier periods.
    atoms=[(3,1),(5,3),(15,13),(4,1),(7,6)]
    period=lcm(*(l for l,r in atoms)); units=[n for n in range(period) if gcd(n,period)==1]
    from itertools import permutations
    seen=set()
    for a,b,j in permutations(atoms,3):
        q,r=j; u=lcm(a[0],b[0]); h=gcd(q,u)
        for k in range(1,h+1):
            if h%k: continue
            good=lambda n:n%a[0]==a[1] and n%b[0]==b[1]
            pins=[n for n in units if good(n)]
            partial=[n for n in units if n%k==r%k]
            forward=F(len(pins),len(units))*int(bool(pins) and pins[0]%k==r%k)
            reverse=F(len(partial),len(units))*F(sum(map(good,partial)),len(partial))
            assert forward==reverse
            if h not in (gcd(q,a[0]),gcd(q,b[0])): seen.add((q,h,k))
    assert (15,15,3) in seen
    print('exact identity on toy CRT fibre (not a row estimate); mixed cases',sorted(seen))


def plancherel():
    def e(z):return exp(2j*pi*z)
    for Q,H,W,C in ((9,4,24,6773),(15,9,80,118867),(6,2,13,3881)):
        # Compactly supported integer signal, no transform interpolation at boundaries.
        z={x:(1-((x-1.5*W)/(.5*W))**2)**3*e(-C/(Q*x)) for x in range(W+1,2*W)}
        lhs=sum(abs(sum(z.get(x+i*Q,0) for i in range(1,H+1)))**2 for x in range(W-H*Q,2*W))/H
        # Poisson alias sum represented by the exact finite DTFT of the samples.
        # Uniform quadrature in u on the union of Q arcs, exact for the resulting
        # trigonometric polynomial in xi when Q*K exceeds its degree.
        K=128
        rhs=0.
        for a in range(Q):
            for j in range(K):
                u=(j+.5)/K-.5; xi=(a+u)/Q
                rhs+=abs(sum(b*e(x*xi) for x,b in z.items()))**2*abs(sum(e(i*u) for i in range(1,H+1)))**2/(Q*K*H)
        assert abs(rhs-lhs)<1.e-8
        print('Plancherel Q,H,W',Q,H,W,'energy',round(lhs,6),'absolute residual',f'{abs(rhs-lhs):.2e}')


def exponents():
    t=F(6,19); r=1-3*t; h=2*r; j=1+r-2*t
    assert (3*h+j)/2-t==F(1,19)
    t=F(8,25); assert (1+7*(1-3*t)-4*t)==0
    assert 3*F(12,4)*F(1,2)**2/2==F(9,8)
    assert 2*F(6,7)/4*F(1,2)**3/6==F(1,112)
    assert (F(3,7)*F(-7,6)+F(1,2))==0
    for v in (2,4,6):
        assert F(25,26*v)**3/F(25,52*v)**3==8
        assert 3*F(12,4)*F(1,v)**2/2==F(9,2*v**2)
        assert 2*F(6,7)/4*F(1,v)**3/6==F(1,14*v**3)
    print('exact arithmetic: absolute lift deficit 1/19, level-one constants 9/8, 1/112; no new exponent pair used')


if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 180 uv run --offline --no-project python -B scripts/z80_r_below_619.py')
    exponents(); selberg(); partial_pin(); small_words(); controls(); plancherel()
