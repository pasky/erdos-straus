"""Exact small controls for mixed pinning, factorial bookkeeping and q^2 overlap."""
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd, lcm, prod
from functools import cache


@cache
def phi(n):
    x, v, p = n, n, 2
    while p*p <= x:
        if x % p == 0:
            v -= v//p
            while x % p == 0:
                x //= p
        p += 1
    return v-v//x if x>1 else v


def prob(atoms, Q=1):
    classes = [(Q,1)] + [(4*a*c*d-1, -a*pow(c,-1,4*a*c*d-1)) for a,c,d in atoms]
    if any((r-t)%gcd(f,g) for (f,r),(g,t) in combinations(classes,2)):
        return Fraction()
    return Fraction(phi(Q), phi(lcm(*(f for f,r in classes))))


def check():
    atoms = [(a,c,d) for a,c,d in product(range(1,5),range(1,4),range(1,10))
             if gcd(a,c)==1 and 4*a*c*d-1 in (3,7,11,15,23,35)]
    Q=24
    M=lcm(Q,*(4*a*c*d-1 for a,c,d in atoms))
    units=[n for n in range(1,M,Q) if gcd(n,M)==1]
    direct=[sum((n*c+a)%(4*a*c*d-1)==0 for a,c,d in atoms) for n in units]
    for j in range(1,5):
        sums=[Fraction(),Fraction()]
        for row in combinations(atoms,j):
            collision=len({(a,c) for a,c,d in row})<j
            sums[collision]+=prob(row,Q)
        assert sum(sums)==Fraction(sum(comb(n,j) for n in direct),len(units))
        print('unordered factorial',j,'no collision / collision:',*sums)
    pins=[(2,1,2),(15,1,5)]
    atom=(2,1,5)
    assert prob(pins)==prob(pins+[atom])>0
    print('mixed period deterministic hit:',[4*a*c*d-1 for a,c,d in pins],'force',4*atom[0]*atom[2]-1)
    for B in (11,17,31):
        Q=8*prod(p for p in range(3,B+1) if all(p%d for d in range(2,p)))
        a=3*Q-1
        pair=[(a,1,2),(a,1,11)]
        # f1,f2 grow rapidly: evaluate ratio by the gcd identity, no phi of their lcm needed.
        f,g=[4*a*d-1 for _,_,d in pair]; h=gcd(f,g)
        assert h==9 and (a+1)%Q==0
        normalized=Fraction(phi(h),phi(gcd(h,Q)))
        assert normalized==3
        print('positive covariance at gap 9:',B,Q,normalized)
    # Product correcting the missing large primes, at four possible small bases.
    for m in (1,24,24*35,24*35*11):
        for a,c,d in atoms:
            f=4*a*c*d-1; g=gcd(m,f)
            z=sum(Fraction(1,phi(e)) for e in range(1,f+1) if f%e==0 and gcd(m,e)==1
                  and all(e%(q*q)!=0 for q in range(2,e+1)))
            assert z*g/f==Fraction(phi(g),phi(f))
    print('unweighted residual Euler expansions verified')


if __name__=='__main__':
    check()
