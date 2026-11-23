"""Finite checks only; no analytic error bound is tested."""
from math import gcd, isqrt
from fractions import Fraction as F


def fac(n):
    d, out = 2, {}
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = 1
    return out


def chi(n):
    return (0, 1, -1)[n % 3]


def mu(n):
    fs = fac(n)
    return 0 if max(fs.values(), default=0) > 1 else (-1)**len(fs)


def rr(n):
    return sum(chi(k) + (chi(n//k) if k*k < n else 0)
               for k in range(1, isqrt(n)+1) if n % k == 0)


def norm_checks(limit=3500):
    all_rep, prim_rep = [0]*(limit+1), [0]*(limit+1)
    b = isqrt(4*limit//3)
    for i in range(-b, b+1):
        for j in range(-b, b+1):
            n = i*i+i*j+j*j
            if 1 <= n <= limit:
                all_rep[n] += 1
                prim_rep[n] += gcd(i, j) == 1
    for n in range(1, limit+1):
        prim = sum(mu(t)*rr(n//(t*t)) for t in range(1, isqrt(n)+1) if n % (t*t) == 0)
        assert (6*rr(n), 6*prim) == (all_rep[n], prim_rep[n])
        if n % 3:
            assert prim == 2**len(fac(n))*all(chi(p) == 1 for p in fac(n))
    print(f'norm & square-Moebius: every n through {limit} (including ramification)')


def local_checks():
    # Finite planes sample lattice pairs, not integers weighted by Euler factors.
    for l in (11, 13, 17, 19, 23, 31, 37, 43, 47):
        tot = hit = all_tot = all_hit = 0
        for i in range(l):
            for j in range(l):
                u = (i*i+i*j+j*j) % l
                if (4*u-3) % l:
                    all_tot += 1
                    all_hit += (u+1) % l == 0
                    if i or j:
                        tot += 1
                        hit += (u+1) % l == 0
        assert F(hit, tot) == F(1, l-1+chi(l))
        fall = 1 + F(chi(l)*l, (l-1)*(l-chi(l)))
        assert F(all_hit, all_tot) == 1 / ((l-1)*fall)
        fp = fall - F(1, (l-1)*(l-chi(l)))
        assert (l-1)*fp == l-1+chi(l)
    print('primitive and all local laws: 9 complete F_l^2 enumerations')


def crt_checks():
    from itertools import product
    from math import lcm
    count = yes = 0
    for a,c,m,r,d,e in product((7,13),(7,19),(11,13,17),(11,17,19),(1,11,13,17),(1,11,17,19)):
        if gcd(a,d*m)*gcd(c,e*r) != 1:
            continue
        H = lcm(d,e,m,r)
        ok = (gcd(d,m) == gcd(e,r) == 1 and (a-c) % gcd(d,e) == (a-c) % gcd(m,r) == 0
              and (4*c+3*a) % gcd(d,r) == (4*a+3*c) % gcd(e,m) == 0)
        v1 = (-pow(a,-1,d)) % d
        actual = sum((c*v+1) % e == (4*a*v-3) % m == (4*c*v-3) % r == 0
                     for v in range(v1,H,d))
        assert actual == ok
        count += 1
        yes += actual
    print(f'joint-modulus full-period CRT: {count} tuples, {yes} compatible')


if __name__ == '__main__':
    norm_checks()
    local_checks()
    crt_checks()
