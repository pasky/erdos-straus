"""Exact finite checks of the valuation and height calculations."""
from fractions import Fraction as F
from math import gcd, prod
from z82_c2es_panel import check, prime


def order(a,s):
    a=abs(a); assert a
    j=0
    while a%s==0: j+=1; a//=s
    return j


def v(f,s): return order(f.numerator,s)-order(f.denominator,s)


def move(t,i):
    a=t[i]; k=a/(1-a)
    return tuple(1-a if j==i else u*k for j,u in enumerate(t))


def check_orbit(n,M,s,xyz,depth):
    check(n,M,xyz)
    t=tuple(F(n,M)/w for w in xyz); vs=sorted(v(u,s) for u in t)
    a,b=-vs[0],vs[2]; assert vs[1]==-a and b>0 and a>=0
    count=0; best=b
    def visit(t,height,last):
        nonlocal count,best
        w=sorted(v(u,s) for u in t); count+=1; best=min(best,max(0,w[-1]))
        if b>a:
            assert w==[-a,-a,b] or (w[0]==0 and w[1]>=b-a and w[1]%(b-a)==w[2]%(b-a)==0 and gcd(w[1],w[2])==b-a)
        if height:
            for i in range(3):
                if i==last:continue
                t1=move(t,i)
                assert sum(t1)==1 and min(t1)>0 and move(t1,i)==t
                # Independent Vieta update on the integral model W.
                W=[u/prod(t) for u in t]; j,k=(i+1)%3,(i+2)%3
                assert sum(W)**2==prod(W)
                W[i]=W[j]*W[k]-2*(W[j]+W[k])-W[i]
                assert tuple(u/sum(W) for u in W)==t1
                visit(t1,height-1,i)
    visit(t,depth,-1)
    assert best==max(0,b-a)
    return (a,b,best,count)


def packet(n,M,s,m):
    assert prime(s) and (s**3+1)%m==0 and (n+m)%(M*s)==0 and gcd(s,n*M*m)==1
    k=(n+m)//M; y=n*k*((s**3+1)//m)
    return (k,y,F(y,s**3))


def ratio(n):
    # Complete two branches, all carriers incl even and both endpoints of the residue interval.
    res=[set(),set()]
    for q in range(1,n+2):
        if gcd(q,n)>1:continue
        # m=-p mod q for the direct test; for reverse, (p*m+1)/(4q) integral.
        for i,r in enumerate((-n%q,-pow(n,-1,q)%q if q>1 else 0)):
            for m in range(r or q,q+2,q):
                if (q+1)%m:continue
                b=(n+m) if i==0 else (n*m+1)
                if b%(4*q):continue
                t=b//(4*q); d=1 if i==0 else n
                x=d*q*t; y=n*q*t*((q+1)//m)//d
                assert n*q*t*((q+1)//m)%d==0
                check(n,4,(x,y,y//q));res[i].add((q,m))
    return [sorted(r) for r in res]


def main():
    for n,s,m,M in ((17,173,22127,4),(409,12281,441707,4),(2521,17,63,4),(3361,22877,362671,4),(8813281,31,19,4),
                    (3189177846574333650961,19,1715,4),(131,20117,321741,8),(241,11,111,8)):
        xyz=packet(n,M,s,m)
        print('cube orbit n M s m (a,b,min,words)',n,M,s,m,check_orbit(n,M,s,xyz,4))
        if n==409:
            print('scaled square cube orbit',n*n,check_orbit(n*n,M,s,tuple(n*u for u in xyz),3))
    for n,x in ((2521,633),(3189177846574333650961,797296593515992469436)):
        m=4*x-n; d=9*x*x; y=n*((x+d)//m); z=F(x*y,d)
        print('9p+4 seed',n,x,check_orbit(n,4,3,(x,y,z),3))
    # Unlinked B2_DUALITY jump: an actual (0,0,b) seed at a nonresidue k.
    p=409; b=(p+1)//2
    for k in range(p+1,100000):
        if k%(p+2)==p+1 and prime(k) and pow(k,(p-1)//2,p)==p-1:break
    else: raise AssertionError('missing unlinked control')
    Z=(k*p*b+1)//(p+2)
    print('unlinked jump',p,k,check_orbit(p,4,k,(b,p*b*Z,F(Z,k)),4))
    # Square control: test swaps on a scaled half packet at a square.
    # Construct a linked half packet on 131 at M=8 and check exact one-pivot clearing at 5.
    n=131;M=8;s,a,b,m=5,1,4,29;k=(n+m)//M;y=n*k*(a*s*s+b)//(m*b);z=F(y*b,a*s*s)
    for factor in (1,131):
        print('half orbit',M,n*factor,s,check_orbit(n*factor,M,s,(k*factor,y*factor,z*factor),3))
    for n in (409,2521,3361,21841):print('all divisible-pair charts',n,ratio(n))
    # Make a negative result in an actual single-S genus-pencil orbit, even ignoring the common third coordinate.
    for n in (2521,21841):
        R=set(q for L in ratio(n) for q,m in L); q=1; seen=[]
        while q<=n+1:
            seen.append(q);assert q not in R;q*=17 if n==2521 else 7
        print('excluded integral pair powers',n,seen)
    # A prime quartic-height packet: Lucas complete factor criterion, trial division on factors up to 1.5e10.
    n=234361;s=68562823404007655447; fac=[2,151,15220091,14916416503]
    assert prime(n) and prod(fac)==s-1 and all(prime(q) for q in fac)
    witnesses=[]
    for q in fac:
        b=next(b for b in range(2,100) if pow(b,s-1,s)==1 and gcd(pow(b,(s-1)//q,s)-1,s)==1)
        witnesses.append(b)
    A=(n*n+11)//4;B=s-A;Z=(n*s+1)//4
    assert s==(n+4*A*A)//11 and A>0 and B>=A and gcd(Z,s)==1
    xyz=(s*A,s*B,F(Z,s)); check(n,4,xyz)
    print('quartic prime packet n s A B Z, Lucas witnesses',n,s,A,B,Z,witnesses)
    # Fixed two-division filter for the sharpness polynomial.
    F4=lambda x:(x*x+11)**2+4*x
    assert all(F4(i)%3 for i in range(3))
    pairs=[(u,121//u) for u in (1,-1,11,-11,121,-121)]
    assert all(not (v-u) or 4%(v-u)!=0 for u,v in pairs)
    # Product +121 forces equal signs. Equal pair gives zero linear coefficient.
    assert all(gcd(3361*2900161742447,q)==1 for q in [2,3,5,7,11]);print('quartic fixed primes and factor tests OK')

if __name__=='__main__':main()
