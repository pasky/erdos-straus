"""Local replay for exact-valuation multiplier atoms (toy cutoffs)."""
from math import comb, gcd, isqrt
from fractions import Fraction


def v2(x):
    assert x > 0
    return (x & -x).bit_length()-1


def check(a, b):
    nclass = nword = 0
    for ell in range(101, 4000):
        if any(ell % h == 0 for h in range(2, isqrt(ell)+1)):
            continue
        seen = set()
        for k in range(1, 12, 2):
            f = k*ell
            for w in range(13, min(90, (ell-1)//2**a)+1, 2):
                x = 2**a*w
                mod = 2**(a+b+1)*w
                test = (f - (2**(a+b)*w-1)) % mod == 0
                assert test == ((f+1)%x==0 and v2((f+1)//x)==b)
                if not test:
                    continue
                assert gcd(k,w)==1 and x<ell and x not in seen
                seen.add(x)
                nclass+=1
                y=(f+1)//x
                for z in (1,2,5,100):
                    n=f*z-x
                    assert n>0 and (-n)%f==x and (f+1)%x==0 and f%8==7
                    assert x*y*z-x-z==n==4*x*(y//4)*z-x-z
                    if (a,b)==(1,2):
                        assert ((f+1)//8)%x!=0 and x%8!=0 and (y//4)%2
                    if (a,b)==(0,3):
                        assert (y//4)%2==0
                    assert isqrt(n)**2!=n
                    nword+=1
    assert nword>0
    print('v2(x),v2(y),classes,words:',a,b,nclass,nword)


if __name__=='__main__':
    for a,b in ((1,2),(0,3),(2,2),(3,5)):
        check(a,b)
    for z in range(101):
        for d in range(0,42,2):
            q=sum(Fraction((-1)**j*comb(z,j),2**j) for j in range(d+1))
            assert 0<=q-Fraction(1,2**z)<=Fraction(comb(z,d+1),2**(d+1))
    print('exact lower-tail majorant: Z=0..100, even d=0..40; passed')
