"""Finite CRT / dispersion algebra; no assertion about power saving."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm


def crt(a, q, b, r):
    g = gcd(q, r)
    if (b-a) % g:
        return None
    return (a + q * (((b-a)//g * pow(q//g, -1, r//g)) % (r//g))) % lcm(q,r)


def crt_phase():
    count = off = 0
    for q,r,s in [(11,13,17),(13,17,19),(17,11,23)]:
        for n in range(2,40):
            for n2 in range(n,65):
                if (n2-n)%q or gcd(n,q*r*s)>1 or gcd(n2,q*r*s)>1: continue
                c = crt(-3*pow(n,-1,r),r,-3*pow(n2,-1,s),s)
                mixed = crt(c,r*s,-7*pow(n,-1,q),q)
                mono = crt(c,r*s,-3*pow(n,-1,q),q)
                assert (F(mixed-mono,q*r*s) + F(4*pow(n*r*s,-1,q),q)).denominator==1
                count+=1;off+=n!=n2
    # Cross-colour shared factors: compatibility is not n1 == n2.
    clashes = compatible = 0
    for v,w in ((11*13,11*17),(13*11,13*19),(11,11)):
        for n1,n2 in product(range(1,12), repeat=2):
            if gcd(n1,v)*gcd(n2,w)!=1:continue
            actual=sum((m*n1+3)%v==0 and (m*n2+7)%w==0 for m in range(lcm(v,w)))
            assert actual==int((-3*n2+7*n1)%gcd(v,w)==0)
            clashes+=1;compatible+=actual
    print(f'two-colour phase: {count} CRT triples, including {off} off-diagonal')
    print(f'cross-colour shared factor: {clashes} pairs, {compatible} compatible (full periods)')


def phi(q): return sum(gcd(k,q)==1 for k in range(1,q+1))

def divs(q): return [j for j in range(1,q+1) if q%j==0]

def mu(q):
    if q==1:return 1
    return -sum(mu(d) for d in divs(q) if d<q)

def kernel(n,a,v,Y):
    if gcd(n,v)>1:return F(0)
    low=sum(mu(k//s)*phi(s) for k in divs(v) if k<=Y for s in divs(k) if (n-a)%s==0)
    return int((n-a)%v==0)-F(low,phi(v))

def zero_mode():
    # Orthogonal projections: mixed means over a complete common period vanish
    # whenever the shared factor cannot carry an excised-high character.
    count=nonzero=0
    for v,w,n1,n2 in product((15,21,33),(15,21,35),(1,2,3),(1,2)):
        a,b=2,4;Y=4;k=lcm(v,w)
        x=sum(kernel(m*n1,a,v,Y)*kernel(m*n2,b,w,Y) for m in range(k))/k
        # Shared primitive characters: on units the argument is (n1*b)/(n2*a).
        # Sum the primitive projectors by Moebius, with no m-period summation.
        num=n1*b;den=n2*a
        shared=sum(sum(mu(k//s)*phi(s) for s in divs(k) if (num-den)%s==0)
                   for k in divs(gcd(v,w)) if k>Y)
        expected=F(phi(lcm(v,w))*shared,lcm(v,w)*phi(v)*phi(w)) if gcd(n1,v)*gcd(n2,w)==1 else F(0)
        assert x==expected
        count+=1;nonzero+=bool(x)
    assert nonzero>0
    print(f'complete-product means vs shared-primitive formula: {count} finite squares; {nonzero} nonzero shared-high components')

if __name__=='__main__':
    crt_phase();zero_mode()
