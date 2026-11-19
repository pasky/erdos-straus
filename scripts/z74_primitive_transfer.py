"""Finite checks for Z74_PRIMITIVE_TRANSFER.md. Standard library only."""
from fractions import Fraction as F
from math import gcd, isqrt


def divisors(n):
    for t in range(1, isqrt(n) + 1):
        if n % t == 0:
            yield t
            if t*t != n:
                yield n//t


def prime(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n)+1))


def rows(Q):
    for x in range(Q//4+1, (Q+1)//2):
        a, b = (F(4, Q)-F(1, x)).as_integer_ratio()
        for P in divisors(b):
            for A in divisors(P):
                B = P//A
                if B < A or gcd(A, B) > 1 or (A+B) % a:
                    continue
                m = (A+B)//a
                for p in divisors(m):
                    if p > Q and prime(p):
                        g = (b//P)*m
                        yield p, x, g*A, g*B, (A+B)//p


def repairs(p, x, y):
    c, e = (F(1, x)+F(1, y)).as_integer_ratio()
    for ell in divisors(p*p*c):
        k, rem = divmod(ell+p*c, 4*e)
        v, rem2 = divmod(p*p*c//ell+p, 4)
        if not rem and not rem2 and k % p:
            yield k, v


def check(Q, p, x, y, u, k, v):
    assert prime(p) and Q < p and k % p and min(x, y, u, v) > 0
    assert F(1, x)+F(1, y)+F(1, u) == F(4, Q)
    assert F(1, k*x)+F(1, k*y)+F(1, v) == F(4, p)
    assert (v-k*u)*(p-k*Q) > 0


def brute(Q):
    # Independent enumeration of ordinary donors, no primitive-pair coordinates.
    for x in range(Q//4+1, 3*Q//4+1):
        f = F(4, Q)-F(1, x)
        for y in range(max(x, int(1/f)+1), int(2/f)+1):
            z = 1/(f-F(1, y))
            if z.denominator == 1:
                yield x, y, int(z)


def run():
    for Q in range(2, 46):
        r = 4-Q%4
        ps = [p for p in range(Q+1, Q*Q+2) if prime(p)]
        want = {(p,x,y,z) for x,y,z in brute(Q) for p in ps if y%p == z%p == 0}
        have = {(p,x,y,z) for p,x,y,z,j in rows(Q)}
        assert have == want
        for p,x,y,z in have:
            assert p <= F(Q*(Q+r), 4*r)+1
            for y,u in ((y,z),(z,y)):
                hits = set(repairs(p,x,y))
                for k,v in hits:
                    if k*Q != p:
                        check(Q,p,x,y,u,k,v)
                # Independent fixed-k rational residual check, both signs.
                for k in range(1, 16):
                    f = F(4,p) - (F(1,x)+F(1,y))/k
                    assert (k%p != 0 and f.numerator == 1) == any(K == k for K,v in hits)
    assert [row for row in rows(18) if row[0]==23] == [(23,5,46,2070,2)]
    assert (35,42) in repairs(139,6,139)
    check(23,139,6,139,139*138,35,42)
    p=3636361; x=(7*p+1)//44; Q=4*x-7
    check(Q,p,x,p*x//11,p*x*Q//76,121,121*x//76)
    p=next(n for n in range(178081,100000000,209160) if prime(n))
    x=(9*p+1)//83; Q=4*x-2; k=(p+83)//36
    check(Q,p,x,9*p*x,p*Q//18,k,9*k)
    p=126001; R=(3*p+1)//4; Q=(p-161)//2
    check(Q,p,2*R//11,2*R,Q*R//484,2,p*R)
    check(3,7,2,2,3,2,14)
    check(6,13,2,9,18,2,468)
    assert F(1,2)+2*F(1,12) == F(4,6)
    assert F(14,8) <= F(12,6) < F(13,4) and 12 % (13-4*2) != 0
    print('Primitive rows match independent donors for 2≤Q≤45; both signed repairs checked.')
    print('Endpoint equality, minimum j=2, three hard-class progressions and interval miss verified.')


if __name__ == '__main__':
    run()
