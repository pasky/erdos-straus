"""Independent controls, concrete one-place repairs, and full 8/p rescues. Stdlib."""
from fractions import Fraction
from math import gcd,isqrt,lcm
from pathlib import Path
from z75_obstruct_check import check


def prime(n):return n>1 and all(n%j for j in range(2,isqrt(n)+1))

def fullsmall(n,k):
    # x<=y<=z. If residual is a/b, then b/a<y<=2b/a.
    ans=[]
    for x in range(n//k+1,3*n//k+1):
        a,b=k*x-n,n*x
        for y in range(max(x,b//a+1),2*b//a+1):
            z,r=divmod(b*y,a*y-b)
            if not r:ans.append((x,y,z))
    return ans


def repair(n,k,m):
    for q in range(k-1,1000000,k):
        if (m*n*(n+1))%q==0 or not prime(q) or gcd(m,q-1)!=2 or pow(-n,(q-1)//2,q)!=1:continue
        # B'=(n+1)*q^(m-1), known by construction; verify u' modulo q^2 without giant integers
        C=(q+1)//k
        b=(n+1)*pow(q,m-1,q*q)%(q*q)
        u=(n+b)*pow(k*b*C-1,-1,q*q)%(q*q)
        assert pow(u,q*(q-1)//gcd(m,q*(q-1)),q*q)==1
        return q
    raise ValueError(n)


def full8(p):
    # acd=g small or moderate; enumerate all ordered factorizations, for a witness only
    for g in range(2,500000):
        f=8*g-1
        # a == -pc (mod f) and a,c|g
        for c in range(2,min(g,120)+1):
            if g%c:continue
            a=(-p*c)%f
            if not a or (g//c)%a:continue
            b=(a+p*c)//f;d=g//(a*c)
            xyz=(a*b*d,a*c*d*p,b*c*d*p)
            assert sum(Fraction(1,j) for j in xyz)==Fraction(8,p)
            return a,b,c,d
    raise ValueError(p)

if __name__=='__main__':
    prev=Path('data/z60/ms105/zeros105_1e10.txt').read_text().splitlines()
    zeros=[int(t.split()[0]) for t in prev if prime(int(t.split()[0]))]
    for p in zeros:assert not check(p,4)
    print('14 prior R zeros checked',zeros)
    # Exhaust n=4545 by e=4abd-n; e<=a+b<=2abd implies e<=n.
    n=4545;tested=hit=0
    for e in range(3,n+1,4):
        N=(n+e)//4
        for a in range(1,isqrt(N)+1):
            if N%a:continue
            for b in range(a,N//a+1):
                if (N//a)%b==0:
                    tested+=1;hit+=((a+b)%e==0)
    assert hit==0
    print('4545 unordered integral (e,a,b,d) tested',tested,'hit',hit)
    for n in (131,241):
        assert not fullsmall(n,8)
        print('full 8/n zero',n)
    m=lcm(*range(1,129))
    for n,k in ((4545,4),(131,8),(241,8),(179530327201,8),(452438542081,8)):
        print('repair denominator q; m=lcm(1,...,128)',n,k,repair(n,k,m))
    for p in (25277866681,25606400401,27112836481,28154878561,37165786681,39919266721,179530327201,452438542081):
        print('full 8/p Type II rescue (a,b,c,d)',p,full8(p))
