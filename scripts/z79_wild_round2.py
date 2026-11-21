"""Round-2 finite local checks (no inference about density or prime gaps)."""
from math import gcd, isqrt
from itertools import product


def prime(x): return x>=2 and all(x%i for i in range(2,isqrt(x)+1))


def jac(a,b):
    z=1
    while b>1:
        a%=b
        if not a: return 0
        while not a%2:
            a//=2
            if b%8 in (3,5): z=-z
        if a%4==b%4==3: z=-z
        a,b=b,a
    return z


def main():
    ls=[l for l in range(17,300) if prime(l)]
    for s in (1,2,3,5,6,13,35):
        ok=[0,0]
        for l,k,u,v in product(ls,[1,3,5,7,9,11],range(1,19),range(1,7)):
            f=k*l
            if s%l==0 or gcd(u,v)>1 or (f+1)%(4*u*v): continue
            if not any((s*j*j*v+u)%k==0 for j in range(k)): continue
            chi=jac(s,f)
            r=sum((s*j*j*v+u)%l==0 for j in range(l))
            assert r==1-chi
            if r:
                ok[(f%8)//4]+=1
                if s==2: assert f%8==3
        print('s, split atoms (f=3,7 mod 8):',s,*ok)
    for h in [3,4,6,10,15,24]:
        m=4
        for p in range(3,h+1,2):
            if prime(p) and h%p==0: m*=p
        ls1=[l for l in range(3,4000,2) if prime(l) and l%m==m-1]
        assert ls1
        for l in ls1:
            deg=gcd(l-1,h)
            assert deg==gcd(h,2)
            if l<500:
                assert {pow(j,h,l) for j in range(l)}=={pow(j,deg,l) for j in range(l)}
        print('degree, modulus, tested primes:',h,m,len(ls1))
    count=0
    for p in range(841,20000,840):
        if not prime(p): continue
        for u in range(2,100):
            for t in range(2,100):
                a=t*u-1
                if (p+u)%a or (p+u)//a<2: continue
                b=a
                while not b%2: b//=2
                assert jac(a,p)==jac(-u,b)
                count+=1
    print('HJ symbol/target comparisons',count)

if __name__=='__main__': main()
