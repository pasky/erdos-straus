"""Exact local checks for z82/CAP_CONST; no primality or asymptotic oracle."""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd, isqrt, prod, comb
from pathlib import Path


def factor(n):
    ans = {}
    for i in range(2, isqrt(n) + 1):
        if i*i > n:
            break
        while n % i == 0:
            ans[i] = ans.get(i, 0) + 1
            n //= i
    if n > 1:
        ans[n] = 1
    return ans


def packet(n, f, d):
    a = (f+1)//4
    assert f % 4 == 3 and (n+4*d) % f == 0
    v = (n+4*d)//f
    x, y = v*a-d, n*a
    z = F(n*x*a,d)
    assert 4*x == n+v and F(1,x)+F(1,y)+1/z == F(4,n) and x*y*z > 0
    return x,y,z


def check_cap(n, y, z, E):
    r = isqrt(z.denominator)
    return r*r == z.denominator and gcd(r, 2*n) == 1 and all(y % p == 0 and e <= E for p,e in factor(r).items())


def labels(a,E):
    return [prod(w) for w in product(*[[p**i for i in [*range(2*b+1), *(range(2*b+2,2*b+2*E+1,2) if p>2 else ())]] for p,b in factor(a).items()])]


def exhaustive():
    total = composite_roots = invalid = 0
    for a in range(1,150):
        f=4*a-1
        for E in range(1,5):
            for d in labels(a,E):
                # square obstruction checked without Jacobi by direct enumeration
                assert (-4*d)%f not in {i*i%f for i in range(f)}
                for n in ((-4*d)%f+f,(-4*d)%f+2*f):
                    _,y,z=packet(n,f,d)
                    ok=check_cap(n,y,z,E)
                    if gcd(n,d)==1 or E==1:
                        assert ok
                    if not ok:
                        assert E>=2 and gcd(n,d)>1
                        invalid+=1
                    if ok and len(factor(z.denominator))>1:
                        composite_roots+=1
                    total+=1
    print('exact dictionary packets (E=1..4), multi-prime denominators, nonunit counterexamples:',total,composite_roots,invalid)
    f,d=11,3**6
    # use a CRT hit with v_3(n)=1 rather than a deep collision
    n=next(n for n in range(2,1000) if n%3==0 and n%9 and not (n+4*d)%f)
    x,y,z=packet(n,f,d)
    assert not check_cap(n,y,z,2)
    print('illegal composite hit at E=2: n,f,D,x,y,z =',n,f,d,x,y,z)


def ratio():
    num=0
    for a,v,r,w in product((1,3,5,7),(1,3,5,7),(1,3,5,15),(1,2,3,5)):
        if gcd(a,v)*gcd(a,r)*gcd(v,r)*gcd(w,r)!=1: continue
        A=a*v*r*w; f=4*A-1
        d=a*a*r**4*w
        assert d in labels(A,1) and 4*d*v%f==a*r**3%f
        n=(-a*r**3*pow(v,-1,f))%f + f
        if gcd(n,r)>1: n+=f
        if gcd(n,r)>1: continue
        S=(n*v+a*r**3)//f
        assert packet(n,f,d)==(a*r*w*S,n*A,F(n*v*w*S,r*r))
        num+=1
    print('V/C1 identical ordered triples:',num)


def partial():
    for h in (1,3,5,15,35,105):
        primes=[p for p in range(3,50,2) if len(factor(p))==1 and next(iter(factor(p).values()))==1]
        rho={p:sum(pow(x,h,p)==p-1 for x in range(1,p)) for p in primes}
        assert all(v==gcd(h,p-1) for p,v in rho.items())
        # Test mixed CRT factorial moments on a full period and a truncated interval.
        pp=primes[:5]; Q=prod(pp)
        for X in (Q,Q+79):
            m=[0]*4
            for s in range(1,X+1):
                n=sum(pow(s,h,p)==p-1 for p in pp)
                for j in range(len(m)): m[j]+=comb(n,j)
            for j in range(4):
                w=sum(prod(F(rho[p],p) for p in J) for J in combinations(pp,j))
                assert m[j]<=2*X*w and (X!=Q or m[j]==X*w)
    print('6 odd exponents: finite-group root counts and CRT binomial moments verified')


def hc():
    # Compare the two coordinates on the same finite box. This does not
    # model the moving power boxes of HC. A Boolean hit test is independent
    # of the (k,j) enumeration.
    ps=[p for p in range(17,700,8) if factor(p)=={p:1}]
    ss=[s for s in range(5,5000,8) if factor(s)=={s:1}]
    forward=set()
    for s in ss:
        bs=[b for b in factor(s*s-s+1) if b%12==1 and b<=300]
        for d in range(1,40,4):
            if (s+1)%(2*d): continue
            for b in bs:
                if b<=d: continue
                v=(s+1)//(2*d)
                for p in ps:
                    if s<=2*p or (v*b+p)%s: continue
                    j=(b+2*d*p)//s; k=(b+j)//(2*d)
                    assert j*s==b+2*d*p and k%4==0 and j*v==p+k
                    forward.add((p,s,d,b,k,j))
                    m=v*b; K=(p+m)//4
                    assert m%4==3 and (s**3+1)%m==0 and K%s==0
                    A=K*((s**3+1)//m); x,y,z=K,p*A,F(p*A,s**3)
                    assert F(1,x)+F(1,y)+1/z==F(4,p) and check_cap(p,y,z,1)
    inverse=set()
    for p in ps:
        # j <= d+1 for s>2p and b<=300 need not hold in this small test;
        # the exact bound j <= (300+2*d*p)/(2*p+1) gives k < 160.
        for k in range(4,161,4):
            for b in factor(p*p-p*k+k*k):
                if b>300 or b%12!=1: continue
                for j in range(1,p+k+1):
                    if (p+k)%j or j%b==0 or (b+j)%(2*k): continue
                    d=(b+j)//(2*k); s=2*d*((p+k)//j)-1
                    if 1<=d<min(40,b) and d%4==1 and s in ss and s>2*p:
                        inverse.add((p,s,d,b,k,j))
    assert forward==inverse and len(forward)>0
    print('HC two-way bounded search, exact cubic packets:',len(forward),'example (p,s,d,b,k,j)',min(forward))


def screens():
    Z=[105,1465,3865,4545,10305,12145,39361,67425]
    F2=[11,17,131,241,1590284203561,6955940568721]
    star=[int(x) for x in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if x and not x.startswith('#')]
    hard=[2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929]
    family=[(4*a-1,d) for a in range(1,150) for d in labels(a,1)]
    for name,ns in [('squares',[i*i for i in range(1,130,2)]),('8-controls',F2),('Z7',Z),('star',star+[17401609]),('hard',hard)]:
        out=[]
        for n in ns:
            hit=next(((f,d) for f,d in family if not (n+4*d)%f),None)
            if hit:
                _,y,z=packet(n,*hit); assert check_cap(n,y,z,1)
            if name=='squares': assert hit is None
            else: out.append((n,hit))
        print(name,len(ns),'(n,first numerator-4 test (f,D) or None):',out if out else 'all miss')


if __name__=='__main__':
    exhaustive(); ratio(); partial(); hc(); screens()
