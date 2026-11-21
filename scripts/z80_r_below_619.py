"""Small pointwise controls and exact arithmetic for R_BELOW_619.md (stdlib)."""
from fractions import Fraction as F
from math import gcd, lcm, isqrt, pi, exp as real_exp
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
                    if n>=2:
                        ans[n]+=1+(a!=b)
                        if M>=37:
                            N,r=divmod(n,M); v=(a+b+r)//M
                            assert (a+b+r)%M==0 and N+v==a*b*d
                            # §2.1 exact discrepancy, multiplied by M(a+b).
                            assert a*d*M*(a+b)==n+M*a*a*d+(a+b)
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


def traces():
    for p in (7,11,17,23,31):
        psi=[exp(2j*pi*j/p) for j in range(p)]
        largest=0.
        for n in (0,2,3):
            tab={}
            for v in (1,2,p-1):
                vals=[]
                for c in range(p):
                    def leg(x):
                        a=pow(x%p,(p-1)//2,p); return -1 if a==p-1 else a
                    raw=sum(leg((4*c*k-n)**2-4*k)*psi[v*k%p] for k in range(p))
                    if c and (4*n*c+1)%p:
                        a=(n*pow(4*c,-1,p)+pow(8*c*c,-1,p))%p
                        b=v*v*(4*n*c+1)*pow(256*c**4,-1,p)%p
                        kl=sum(psi[(j+b*pow(j,-1,p))%p] for j in range(1,p))
                        assert abs(raw-psi[(v*a)%p]*kl)<1e-10
                    vals.append(raw/(p**.5))
                tab[v]=vals
            for v,f in tab.items():
                for w,g in tab.items():
                    for delta in (0,1,3):
                        for b in range(p):
                            z=sum(f[(c+delta)%p]*g[c].conjugate()*psi[b*c%p] for c in range(p))
                            main=p*int(delta==0 and v==w and b==0)
                            largest=max(largest,abs(z-main)/p**.5)
        print('trace normalization checked at p=',p,'sample max mixed error/sqrt(p)',round(largest,5))


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


def disjoint_packet():
    # Signed test kernel. The c-amplitude is one smoothness-control polynomial
    # bump rather than the exact detector window: this is not a bound on (1).
    primes=(7,11,13,17); P=7; W=P**6; n=4*P**19+41
    qi=primes[0]*primes[1]; qj=primes[2]*primes[3]; m0=qi*qj
    for hi,hj in ((2,-3),(3,2),(4,-1)):
        D=hi*qj-hj*qi; assert gcd(D,m0)==1
        # Local trace at the ONE primitive numerator D mod m0. CRT signs match
        # hi and -hj exactly, since D/m0=hi/qi-hj/qj.
        tables=[]
        for p in primes:
            v=D*pow(m0//p,-1,p)%p
            psi=[exp(2j*pi*j/p) for j in range(p)]
            tab=[]
            for c in range(p):
                summands=[pow(((4*c*k-n)**2-4*k)%p,(p-1)//2,p) for k in range(p)]
                tab.append(sum((t if t!=p-1 else -1)*psi[v*k%p] for k,t in enumerate(summands))/p**.5)
            tables.append(tab)
        l1=1.
        for p,tab in zip(primes,tables):
            coeff=[sum(tab[t]*exp(-2j*pi*(b*t%p)/p) for t in range(p))/p for b in range(p)]
            assert abs(sum(abs(x)**2 for x in coeff)-sum(abs(x)**2 for x in tab)/p)<1.e-11
            l1*=sum(map(abs,coeff))
        print('disjoint CRT Fourier l1/sqrt(m0)',round(l1/m0**.5,5),'D',D)
        periodic=[tables[0][x%7]*tables[1][x%11]*tables[2][x%13]*tables[3][x%17] for x in range(m0)]
        z=0j
        for x in range(W+1,2*W):
            den=4*m0*x; phase=(-n*D)%den
            weight=(4*(x-W)*(2*W-x)/W**2)**6
            z+=weight*periodic[x%m0]*exp(2j*pi*(phase/den))
        print('toy signed disjoint kernel',hi,hj,'D',D,'|K|/sqrt(W)',round(abs(z)/W**.5,5),'|K|/(W/P^2)',round(abs(z)/(W/P**2),5))


def binding_energy():
    # Direct enlarged energy with a fixed C-infinity bump on [W,2W]. No
    # approximation by stationary phase, and no detector trace remaining.
    for P in (5,7):
        W=P**6; H=P**2
        weight=[]
        for x in range(W+1,2*W):
            y=(2*x-3*W)/W
            weight.append(real_exp(-y*y/(1-y*y)))
        diag=sum(b*b for b in weight); ratios=[]
        for Q in range(P**2,2*P**2+1,P):
            for ell in (1,P-1):
                C=P**19*ell
                E=0.
                for r in range(Q):
                    seq=[]
                    for a in range(r,len(weight),Q):
                        den=(W+1+a)*Q
                        seq.append(weight[a]*exp(2j*pi*((-C)%den)/den))
                    rolling=0j
                    for t in range(len(seq)+H-1):
                        if t<len(seq): rolling+=seq[t]
                        if t>=H: rolling-=seq[t-H]
                        E+=abs(rolling)**2
                ratios.append(E/(H*diag))
        print('binding energy / primal diagonal P=',P,'sample size',len(ratios),'min mean max',*(round(t,5) for t in (min(ratios),sum(ratios)/len(ratios),max(ratios))))


def central_triangle():
    # Exact decomposition, including all boundary cases, not the log-cube truncations.
    B=500000; sieve=bytearray([1])*(B+1); sieve[:2]=bytes(2)
    for q in range(2,isqrt(B)+1):
        if sieve[q]: sieve[q*q::q]=bytes((B-q*q)//q+1)
    total=[0]*(B+1); covered=[0]*(B+1)
    for a in range(1,(1+isqrt(1+4*B))//4+1):
        d=1
        while (4*a*d-1)*a<=B+a:
            f=4*a*d-1
            for b in range(a,(B+a)//f+1):
                n=f*b-a
                if n<3 or not sieve[n]: continue
                total[n]+=1+(a!=b)
                # Comparison to sqrt(n) without floating point, for both orientations.
                hits=int(f*f<=n)+int((4*b*d-1)**2<=n)+int((4*a*b)**2<=n)
                assert hits<=1
                if hits: covered[n]+=1+(a!=b)
            d+=1
    # Independent fixed-input replay: solve (4ad-1)b=p+a by divisors of p+a,
    # instead of sweeping p upward on a progression. Sample, not independent
    # full coverage of the three dyads.
    ps=[p for p in range(5000,B) if sieve[p]][::971]
    for p in ps:
        tot=cov=0
        for a in range(1,(1+isqrt(1+4*p))//4+1):
            s=p+a
            for r in range(1,isqrt(s)+1):
                if s%r: continue
                for b in ((r,) if r*r==s else (r,s//r)):
                    if b<a or (s//b+1)%(4*a): continue
                    d=(s//b+1)//(4*a)
                    tot+=1+(a!=b)
                    if min(4*a*b,4*a*d-1,4*b*d-1)**2<=p: cov+=1+(a!=b)
        assert (tot,cov)==(total[p],covered[p])
    print('independent divisor replay of word and chart counts at',len(ps),'sample primes')
    for X in (10000,50000,250000):
        num=sum(covered[X+1:2*X+1]); den=sum(total[X+1:2*X+1])
        print('chart partition prime dyad',X,2*X,'covered',num,'total',den,'fraction',round(num/den,4))


def bm_window():
    # Existing tabulation, not a new census. Do not interpret the finite rate
    # as uniform in epsilon or X. Resolve from the script rather than cwd.
    from pathlib import Path
    import gzip,csv
    from statistics import median
    source=Path(__file__).resolve().parents[1]/'data/z52c/bmL/window.tsv.gz'
    with gzip.open(source,'rt') as fh:
        ratios=[int(row['R'])/(float(row['M0'])-float(row['T'])) for row in csv.DictReader(fh,delimiter='\t')]
    print('archived BM window (rounded reals) size',len(ratios),'below 3/4',sum(r<.75 for r in ratios),'median',round(median(ratios),5))


def exponents():
    t=F(6,19); r=1-3*t; h=2*r; j=1+r-2*t
    for u in (F(2,7), F(142,465), F(213,607)):
        d=1-2*u; cube=d/3; ep=F(55,181)*d; density=d/2-u/4; approx=d/2-u/6
        if u==F(2,7): assert cube==density>ep
        if u==F(142,465): assert ep==density<cube
        if u==F(213,607): assert ep==approx and ep>density
    assert (3*h+j)/2-t==F(1,19)
    # A separate test: sqrt cancellation for one residue train, theta-vertex.
    assert 4*r-t/2==r and 4*(1-3*F(8,25))-F(8,25)/2==0
    t=F(8,25); assert (1+7*(1-3*t)-4*t)==0
    assert 3*F(12,4)*F(1,2)**2/2==F(9,8)
    assert 2*F(6,7)/4*F(1,2)**3/6==F(1,112)
    assert (F(3,7)*F(-7,6)+F(1,2))==0
    for v in (2,4,6):
        assert F(25,26*v)**3/F(25,52*v)**3==8
        assert 3*F(12,4)*F(1,v)**2/2==F(9,2*v**2)
        assert 2*F(6,7)/4*F(1,v)**3/6==F(1,14*v**3)
    for k,l,goal in ((F(1,6),F(2,3),F(4,13)),(F(13,84),F(55,84),F(55,181))):
        t=l/(1+2*l-k); assert t==goal and 4*t>1
        B=1-2*t; H=(B*(1-l+2*k)-k)/(1+k)
        assert B-H==t and k*(H+1-2*B)+l*B==t
        print('reciprocal discrepancy pair',k,l,'power',t,'cutoff power at large B',H)
    print('exact arithmetic: absolute lift deficit 1/19, level-one constants 9/8, 1/112')


if __name__=='__main__':
    print('# ulimit -v 6000000; timeout 180 uv run --offline --no-project python -B scripts/z80_r_below_619.py')
    exponents(); selberg(); partial_pin(); small_words(); controls(); plancherel(); traces(); central_triangle(); disjoint_packet(); binding_energy(); bm_window()
