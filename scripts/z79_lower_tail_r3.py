"""Integer checks for the reciprocal I4 multiplier and disjoint pair chart."""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt


def prime(n):
    return n > 1 and all(n % p for p in range(2, isqrt(n)+1))


def build(z):
    # Toy boxes obey H>2K^2, ell>Z. Not an asymptotic prime-supply test.
    K, H, Z = 5, 60, 130
    one, pair = defaultdict(dict), defaultdict(dict)
    for l in range(137, 770):
        if not prime(l):
            continue
        for k in range(1,K+1,2):
            for a in range(1,K+1,2):
                if gcd(a,k)>1:
                    continue
                for e in range(H+1,Z+1):
                    if (e*z+1)%(4*a*k) or (a+k*l)%e:
                        continue
                    r=-pow(e,-1,l)%l
                    assert r not in one[l]
                    one[l][r]=(a,k,e)
            for a in range(H+2,Z+1,2):
                if (z+a+k*l)%(4*a*k):
                    continue
                r=-a%l
                assert r not in pair[l]
                pair[l][r]=(a,k)
    return one,pair


def checkI(n,a,b,e):
    assert (a+b)%e==0 and (e*n+1)%(4*a*b)==0
    c,d=(a+b)//e,(e*n+1)//(4*a*b)
    x,y,z=n*a*b*d,a*c*d,b*c*d
    assert gcd(y*z,n)==1 and sum(Fraction(1,q) for q in (x,y,z))==Fraction(4,n)
    return (x,y,z,d)


for z in (1,1009,2011):
    one,pair=build(z)
    print('small fibre',z,'distinct leaf targets',sum(map(len,one.values())),sum(map(len,pair.values())))
    for fam in (one,pair):
        for l,tab in fam.items():
            for r,v in tab.items():
                a,k=v[:2]; m=4*a*k
                n=z+m*((r-z)*pow(m,-1,l)%l)
                while n<20000 or not prime(n):
                    n+=m*l
                b=k*l
                if fam is one:
                    checkI(n,a,b,v[2])
                else:
                    d=(n+a+b)//(4*a*b)
                    assert n==4*a*b*d-a-b and (4*a*b)*(4*a*d-1)==4*a*(n+a)

for p in (131,241):
    I=[]
    # Just a bounded I4 search (complete sorted counts are in the Round 1 check).
    for a in range(1,101):
        for b in range(a,101):
            if gcd(a,b)>1:
                continue
            for e in range(1,a+b+1):
                if not ((a+b)%e or (e*p+1)%(4*a*b)):
                    x,y,z,d=checkI(p,a,b,e)
                    assert any(q%2 for q in (x,y,z)) and d%2
                    I.append((a,b,e,d))
    assert I
    print('Type I at',p,'bounded (a,b,e,d):',I)
for n in (9,25,49,81,121,169):
    assert not any((e*n+1)%(4*a*b)==0 for a in range(1,90,2) for b in range(1,90,2)
                   for e in range(1,a+b+1,2) if (a+b)%e==0)
print('square obstructions replayed')
