"""Exact replay for SIGNED_ROOT_TRANSFER.md, standard library only."""
from math import gcd, prod

from signed_factor_transfer import certified
from signed_two_shifts import eligibility, factors, hits, prime, windows


def check_triple(n, row):
    x,y,z = row
    assert min(row)>0 and 4*x*y*z == n*(x*y+x*z+y*z)


def root_transfer(a,b):
    x = a*b
    q,p = 4*x-3, 48*x-47
    assert gcd(a,b)==1 and a%3==2 and (a+b)%47==0 and gcd(a,47)==1
    assert (a*a+p)%47==0
    _, donor = certified(q,3,1,a,b)
    _, target = certified(p,47,a,b,12)
    assert {12*s for s in donor} & set(target) == {12*x}
    check_triple(q,donor)
    check_triple(p,target)
    return donor,target


def inspect(p, expected):
    q = (p+11)//12
    l = (q+1)//2
    x = (q+3)//4
    assert p%840==1 and p==12*q-11==24*l-23==48*x-47
    assert all(prime(n) for n in (p,q,l)) and q%11 in (2,6) and l%23 in (5,14)
    assert all(eligibility(p,d)[1] for d in (11,23,47))
    assert hits(p,11)==hits(p,23)==(False,False) and hits(p,47)==expected
    y = 47*x-46
    assert 12*y==(47*p+1)//4 and gcd(x,y)==gcd(x,46)
    earlier=q*l*(11*q-10)*(23*l-22)
    assert gcd(earlier, x*y)==gcd(x,y)==1
    print('p,Q,L,x,Y:',p,q,l,x,y)
    print('x,Y,R11,M23:',[factors(v) for v in (x,y,11*q-10,23*l-22)])
    if expected==(True,True):
        a,b=323,617
        assert x==a*b and x==q//4+1 and y%563==0
        print('minimal transfer:', *root_transfer(a,b))
        n=12*y
        dual=(p*n,(n+n//563)//47,(n+n*563)//47)
        check_triple(p,dual)
        print('dual 47:', dual)
    else:
        assert prime(x) and x%47==13 and x%3==q%3==1
        qr={i*i%47 for i in range(1,47)}
        box={pow(2,i,47)*pow(3,j,47)%47 for i in range(-2,3) for j in (-1,0,1)}
        assert {(-pow(x,i,47))%47 for i in (-1,1)} <= qr-box
        assert all(v%47 in qr for v,e in factors(y))
        assert 2 not in windows(q,3)[0]


def progression():
    t=840*11*23*47*563*599*323
    mods=(48*323*t,4*323*t,2*323*t,44*323*(t//599),46*323*t)
    constants=(9565921,797161,398581,14639,9167341)
    assert all(prime(c) and gcd(c,prod(mods))==1 for c in constants)
    # Distinct roots of the five affine forms in the common x-coordinate.
    forms=((48,-47),(4,-3),(2,-1),(44,-43),(46,-45))
    assert all(a*d!=b*c for i,(a,b) in enumerate(forms) for c,d in forms[:i])
    for j in (0,1,2):
        b=617+t*j
        x=323*b
        p,q,l,r,m=(c+s*j for c,s in zip(constants,mods))
        assert (p,q,l,599*r,m)==tuple(a*x+b0 for a,b0 in forms)
        assert (47*x-46)%563==0 and p%840==1 and q%11==2 and l%23==14
        root_transfer(323,b)


if __name__=='__main__':
    inspect(9565921,(True,True))
    inspect(6206649121,(False,False))
    progression()
