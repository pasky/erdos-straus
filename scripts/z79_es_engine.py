"""Exact small arithmetic checks; not a primality or density oracle."""
from math import gcd, isqrt, lcm
from pathlib import Path


def jac(a, n):
    s = 1
    while a % n:
        a %= n
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        if a % 4 == n % 4 == 3:
            s = -s
        a, n = n, a
    return s if n == 1 else 0


def triple(n, d):
    x, y, z = d
    assert min(d) > 0 and 4*x*y*z == n*(x*y+x*z+y*z)


def star(n, t, u, v):
    assert n == t*u*v-u-v and t % 8 == 4 and min(t,u,v) >= 2
    assert n % 4 == 1 and jac(t*u-1, n) == -1
    C = t//4
    triple(n, (u*v*C, n*v*C, n*u*C))


def nested(x):
    y = x*x+2
    A = y*y-y+1
    u, t = y-x, y+x
    assert t*u == A+1 and t % 8 == 4
    return y, A, u, t


def first_nested(x, M):
    y, A, u, t = nested(x)
    k = M*(((u+1)*pow(M,-1,A)) % A or A)
    assert gcd(1+k*y**3, M*y**3*A) == 1
    return k, M*A


def binary(x, y):
    A = x*x-x*y+y*y
    n = 24*(x**3+y**3)-23
    u, t, v = 23, (A+1)//23, 24*(x+y)
    assert t*u == A+1 and n == t*u*v-u-v and n % 840 == 1
    assert jac(A, n) == -1 and (n+u+v) % lcm(8,u*v) == 0
    w = v//4
    triple(n, (w*A,t*n*w,t*n*w*A))


def main():
    roots = [(a, b) for a in range(23) for b in range(23)
             if (a**3+b**3-1) % 23 == (a*a-a*b+b*b+1) % 23 == 0]
    print('binary local pairs mod 23:', roots)
    a,b = roots[0]
    xs = [x for x in range(1,805*10+1,35) if x % 23 == a]
    ys = [y for y in range(35,805*10+1,35) if y % 23 == b]
    for x in xs:
        for y in ys:
            binary(x,y)
    print('binary triples:',len(xs)*len(ys))
    for B in (7,15,30,60):
        M = lcm(840,*range(1,B+1))
        # x=0 at odd primes except 3, x=1 at 3 and mod 8
        m=M
        while m%2==0: m//=2
        while m%3==0: m//=3
        x=M + m*pow(m,-1,24)
        y,A,u,t=nested(x)
        k0,period=first_nested(x,M)
        for j in range(20):
            k=k0+j*period
            n=1+k*y**3
            star(n,t,u,(n+u)//A)
            assert n%M==1
    print('nested triples: 80')
    # Finite falsifiers. Test the nested kernel even without the trap modulus
    # and all size-eligible prime square locks, relaxing the ell size window.
    zeros=[int(l) for l in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if l and not l.startswith('#')]
    Z7=[105,1465,3865,4545,10305,12145,39361,67425]
    F=sorted(set(zeros+Z7+[17401609,131,241,1590284203561]+[m*m for m in range(3,502,2)]))
    prime=bytearray(b'\1')*(isqrt(max(F))+5); prime[:2]=b'\0\0'
    for d in range(2,isqrt(len(prime)-1)+1):
        if prime[d]: prime[d*d::d]=b'\0'*len(prime[d*d::d])
    for n in F:
        locks=[]; cubes=[]; bins=[]; classes=[]
        # The parent Type II classes, without the cube condition. A>n+u
        # once x^4>n, since A-u = x^4+2*x*x+x+1.
        for x in range(1,isqrt(isqrt(n))+1,8):
            y,A,u,t=nested(x)
            if n%4==1 and (n+u)%A==0 and (n+u)//A>=2:
                star(n,t,u,(n+u)//A); classes.append(x)
        for x in range(1,isqrt(isqrt(n))+2,8):
            y,A,u,t=nested(x)
            if y**3 > n-1: break
            k,r=divmod(n-1,y**3)
            if r==0 and (k-u-1)%A==0:
                star(n,t,u,(n+u)//A); cubes.append(x)
        for q in range(3,isqrt(n)+3,8):
            if not prime[q]: continue
            u=(-n)%(q*q)
            if 2<=u<=q and (q+1)%u==0 and ((q+1)//u)%8==4 and n%4==1:
                star(n,(q+1)//u,u,(n+u)//q); locks.append((q,u))
        if n%840==1:
            for x in range(1,isqrt(n)+1,35):
                if 24*x**3>=n+23: break
                for y in range(35,x+1+(n+23)//(24*x*x),35):
                    s=24*(x**3+y**3)-23
                    if s>n: break
                    if s==n and x%23==a and y%23==b: binary(x,y);bins.append((x,y))
        if n in zeros+Z7+[17401609,131,241,1590284203561]:
            print(n,'cube',cubes,'lock',locks,'binary',bins,'parent class',classes)
        if n in zeros+[17401609] or isqrt(n)**2==n: assert not (locks or cubes or classes)
        if n in Z7 or isqrt(n)**2==n: assert not bins
    print('square controls:',len(range(3,502,2)))

if __name__=='__main__': main()
