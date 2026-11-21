"""Integer checks for the reciprocal I4 multiplier and disjoint pair chart."""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt


def prime(n):
    return n > 1 and all(n % p for p in range(2, isqrt(n)+1))


def build(z):
    # Toy boxes obey H>2K^2, ell>Z. Not an asymptotic prime-supply test.
    K, H, Z = 5, 60, 130
    one = defaultdict(dict)
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
    return one


def checkI(n,a,b,e):
    assert (a+b)%e==0 and (e*n+1)%(4*a*b)==0
    c,d=(a+b)//e,(e*n+1)//(4*a*b)
    x,y,z=n*a*b*d,a*c*d,b*c*d
    assert gcd(y*z,n)==1 and sum(Fraction(1,q) for q in (x,y,z))==Fraction(4,n)
    return (x,y,z,d)


for z in (1,1009,2011):
    one=build(z)
    print('small fibre',z,'distinct Type I leaf targets',sum(map(len,one.values())))
    for l,tab in one.items():
        for r,(a,k,e) in tab.items():
            m=4*a*k
            n=z+m*((r-z)*pow(m,-1,l)%l)
            while n<20000 or not prime(n):
                n+=m*l
            checkI(n,a,k*l,e)

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

# Original equal-sum point recovered from the reduced product ratio and (i,j).
seen=set()
for total in range(5,100):
    for a in range(1,total):
        b=total-a
        if gcd(a,b)!=1: continue
        for c in range(1,total):
            d=total-c
            if gcd(c,d)!=1 or c in (a,b): continue
            ratio=Fraction(c*d,a*b); P,Q1=ratio.numerator,ratio.denominator
            G=gcd(a,c); i,j=a//G,c//G
            num,den=Q1*j*(i-j),P*i-Q1*j
            assert den and gcd(num,den)<=P*Q1*abs(P-Q1)
            assert Fraction(num,den)==Fraction(b,G) and Fraction(num,den).denominator==G
            key=(i,j,P,Q1)
            assert key not in seen
            seen.add(key)
print('unique off-diagonal conic configurations',len(seen))
for h in (2,3,5):
    for power in (1,2,3):
        hpow=h**power
        for z in range(1,hpow):
            if z%h==0: continue
            acc=0
            for a in range(hpow):
                for b in range(hpow):
                    if (h==2 and (a+b)%2==0) or a%h==b%h==0: continue
                    g=gcd(hpow,4*a*b)
                    acc+=g*((a+b+z)%g==0)
            assert Fraction(acc,hpow**2)==(1 if h==2 else 1+Fraction(1,h*h))
    print('pinned local moment prime',h,'powers 1,2,3, every unit digit passed')
