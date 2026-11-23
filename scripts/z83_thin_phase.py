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
    clash=crt(-3,11,-7*pow(6,-1,11),11)
    assert clash is not None and 1!=6 and (-3*6+7)%11==0
    print(f'two-colour phase: {count} CRT triples, including {off} off-diagonal; colour clash checked')


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
        if gcd(v,w)<=Y:assert x==0
        count+=1;nonzero+=bool(x)
    assert nonzero>0
    print(f'complete-product means: {count} finite squares; {nonzero} nonzero shared-high components')

if __name__=='__main__':
    crt_phase();zero_mode()
