"""Extra exact tests for Round 2. A slice count is exhaustive only where stated."""
from fractions import Fraction as F
from math import gcd,prod
from pathlib import Path
from z82_c2es_min import divs,factors,solve
from z82_c2es_panel import prime,check
from z82_c2es_moves import move,v
from z82_c2es_normal import all_integral


def audit_case(p,D,A,B,Z):
    check(p,4,(D*A,D*B,F(Z,D)));T=4*Z-p*D
    assert gcd(D,2*p*Z)==1 and (A+B)%D==0
    C=(A+B)//D;k=4*T*A-p*p
    assert k>0 and C*k*D==p*T*C+4*T*A*A
    if Z%p:
        assert gcd(D*T,p*Z)==1
        return 'outside'
    W=Z//p;t=T//p;h=gcd(p,t);u=t//h
    assert gcd(D*t//h,p*W//h)==1
    check(p,4,(t*A,t*B,F(Z,t)))
    assert F(Z,t).denominator==u
    if t%p:
        if B%p:A,B=B,A
        assert B%p==0 and A%p!=0
        b=B//p;J=4*D*t*b-D-t;assert J%p==0
        r=J//p;assert b*(D+t)==r*A
        return 'split'
    return 't%p=0'


def lanes():
    for p in (5,17,41,73,109,409,577,2521,3361,5569,9601,21841,8813281):
        b=(p+1)//2;W=(b,p*b,F(p,2));check(p,4,W)
        t=tuple(F(p,4)/x for x in W)
        stack=[(t,-1,4)];vs=tuple(v(a,2) for a in t)
        while stack:
            u,last,r=stack.pop();assert tuple(v(a,2) for a in u)==vs
            if r: stack.extend((move(u,i),i,r-1) for i in range(3) if i!=last)
        # This negative certificate requires all divisors, unlike the capped witness search.
        fb=factors(b)
        assert prime(p) and p not in fb and all(prime(q) for q in fb)
        assert prod(q**k for q,k in fb.items())==b
        g=p*b; ds=divs(((p,2),(b,2)))
        assert len(set(ds))==3*prod(2*k+1 for k in fb.values()) and all(g*g%e==0 for e in ds)
        rows=[]
        for x,j in ((b,p+2),(p*b,2*p+1)):
            hits=set()
            for D in divs(((b,1),)):
                if D==1:continue
                for e in ds:
                    if gcd(e,D)>1 or (e+g*D)%j:continue
                    Z=(e+g*D)//j;B=(g//D+g*g//e)//j
                    check(p,4,(x,D*B,F(Z,D)));assert gcd(D,Z)==1
                    hits.add(D)
            rows.append(sorted(hits))
        print('W: p, 2-valuations of shares, #divisors of g², all D>1 at b and pb',p,vs,len(ds),rows)
    for p in (17,41,409,577,2521,3361):
        tallies=[0,0]
        for xyz in all_integral(p):
            J=[i for i in xyz if i%p==0];u=min(J)//p;f=4*u-1;D=f//gcd(f,p)
            assert D>1 and D%4==3 and gcd(D,p)==1 and (len(J)==1)==(f%p==0)
            ab=list(xyz);ab.remove(p*u);new=(ab[0]*f,ab[1]*f,F(p*u,f));check(p,4,new)
            assert new[2].denominator==D; tallies[len(J)-1]+=1
        print('ES -> nontrivial locally clearable, Type I/II',p,tallies)


def chart():
    counts={};checked=0;mix=False
    for f in range(3,1600,4):
        A=(f+1)//4
        for J in divs(((A,5),)):
            if J>100000:continue
            n=(-4*J)%f
            if n<=1 or gcd(n,f*J)>1:continue
            x=(n*A+J)//f;assert f*x==n*A+J
            z=F(n*x*A,J);d=z.denominator
            check(n,4,(x,n*A,z));checked+=1
            for l in (2,3,5,7,11,13):
                a=v(F(A),l);j=v(F(J),l);assert v(F(d),l)==max(j-2*a,0)
                assert (v(F(d),l)<=a)==(j<=3*a)
            if d==9 and A%3==0 and A%9!=0: mix=True
    assert mix
    for L in Path('data/z82/cap_to_es/min.txt').read_text().splitlines():
        if not L[:1].isdigit() or L.startswith('1 mod 8 prime census:'):continue
        p,M,D,label,X,Y,z=L.split();p,M,D,X,Y=map(int,(p,M,D,X,Y));z=F(z)
        if M==4 and (p>=10**8 or prime(p)):
            kind=audit_case(p,D,X//D,Y//D,z.numerator);counts[kind]=counts.get(kind,0)+1
    print('unit-chart tests, trapped exponent-4 example exists',checked,mix)
    print('prime 4/p panel chart counts (prime status of large rows from cited ledgers)',counts)
    for p in (17,41,409,577,2521,3361,21841,113035442521,3189177846574333650961):
        s=5 if p%3==1 else 7
        x=(p+s)//3;check(p,4,(x,p,F(p*x,s)));assert gcd(s,x*p)==1
    p=2521
    # An actual two-way swap; constructed backward from an integral p-bearing coordinate.
    for t in all_integral(p):
        for c in t:
            if c%p or (4*(c//p)-1)<=p:continue
            ab=list(t);ab.remove(c);D=4*(c//p)-1
            if gcd(D,p)==1: audit_case(p,D,*ab,c);break
    print('unlinked small carriers and reverse pivots OK')
    p=10311841
    assert all(prime(q) for q in [p,(p+11)//12,(3*p+1)//4]) and solve(p,4,3,1) is None
    nxt=next(i for i in range(2,51) if solve(p,4,3,i))
    print('Dickson offset control',p,'least successful prefix size',nxt,solve(p,4,3,nxt))

def rectangles():
    for J in (496,496+840*7*11*13,496+2*840*7*11*13):
        p=2288*J-7;t=13;a=11;g=4*J;b0=(676*J+11)//7
        b=p*b0;D=44*b0-13;A=g*a;B=g*b;Z=p*((D+t)//4)
        assert gcd(a,b)==gcd(D,t*p)==1 and (a+b)%4==0 and (D+t)%4==0
        rows=((A*D,B*D,F(Z,D)),(A*t,B*t,F(Z,t)),(A*t,A*D,F(p*(a+b),4*a)))
        for xyz in rows:
            check(p,4,xyz);assert xyz[0]%xyz[2].denominator==xyz[1]%xyz[2].denominator==0
        assert [w[-1].denominator for w in rows]==[D,13,11] and D>p and 2*g*11**2-11<=p
        assert [v(F(w),13) for w in rows[0]]==[0,0,0] and sorted(v(F(w),13) for w in rows[-1])==[0,1,1]
        if J==496:
            assert prime(37) and prime(56963) and 37*56963==D
        print('rectangle p D -> 13 -> 11',p,D,'prime verified' if prime(p) else 'composite')

if __name__=='__main__':lanes();chart();rectangles()
