"""Finite arithmetic controls for SPECIFIC_CLASS; no probabilistic validation."""
from fractions import Fraction as Q
from itertools import product
from math import prod, isqrt, gcd
from collections import Counter


def divisors(n):
    return sorted(d for i in range(1, isqrt(n)+1) if n % i == 0
                  for d in ({i, n//i}))


def factor(n):
    i = 2
    while i*i <= n:
        v = 0
        while n % i == 0:
            v += 1
            n //= i
        if v:
            yield i, v
        i += 1
    if n > 1:
        yield n, 1


def box(m, q):
    out = {1}
    for p, v in factor(m):
        if p != q:
            out = {x*pow(p,e,q) % q for x in out for e in range(-v,v+1)}
    return out


def energies():
    rows = 0
    for M in (2, 4, 6, 9, 10):
        for k in (1,2,3):
            collision = missing = 0
            for g in product(range(M), repeat=k):
                counts = Counter(sum(e1*g1 for e1,g1 in zip(e,g)) % M
                                 for e in product((-1,0,1),repeat=k))
                collision += sum(c*c for c in counts.values())
                missing += M-len(counts)
            expectation = Q(collision, M**k * 9**k)
            exact = Q(1,M) + Q(M-1,M*3**k) + Q((gcd(2,M)-1)*(5**k-3**k),M*9**k)
            assert expectation == exact
            assert Q(missing, M**(k+1)) <= M*expectation-1
            rows += 1
    return rows


def physical():
    hits = holes = tests = squares = coprime_triples = 0
    for t in range(1, 513):
        n = 4*t+1
        for q in (3, 7, 11, 19, 31, 43):
            m = t+(q+1)//4
            D = [d for d in divisors(m) if d%q]
            ratios = {x*pow(y,-1,q)%q for x in D for y in D}
            assert ratios == box(m,q)
            tests += 1
            if isqrt(n)**2 == n:
                squares += 1
                assert q-1 not in ratios
            if q-1 not in ratios:
                holes += 1
                continue
            hits += 1
            for a,b in product(D,repeat=2):
                if (a+b)%q or gcd(a,b)>1:
                    continue
                c,d = (a+b)//q, m//(a*b)
                assert a*b*d==m and 4*a*b*c*d==a+b+n*c
                f,g=4*a*c*d-1,4*b*c*d-1
                assert q*min(f,g)>=n and q*min(f,g)<=2*n+q
                assert Q(1,m)+Q(1,n*a*c*d)+Q(1,n*b*c*d)==Q(4,n)
                coprime_triples += 1
    return tests,hits,holes,squares,coprime_triples


def torus():
    X=16
    qs=(3,7,11)
    h=[(q+1)//4 for q in qs]
    fs=[[int(len(box(X+t,q))<q-1) for t in range(X)] for q in qs]
    z=3
    gs=[[1+(z-1)*f for f in row] for row in fs]
    def correlation(offset):
        return Q(sum(prod(g[(t+a)%X] for a,g in zip(offset,gs)) for t in range(X)), X)
    base=prod(Q(sum(g),X) for g in gs)
    assert sum(correlation(a) for a in product(range(X),repeat=len(qs)))==X**len(qs)*base
    assert correlation(h)==correlation([i+5 for i in h])
    return correlation(h)/base


if __name__=='__main__':
    print('exact collision and support-energy checks:',energies())
    print('window tests, hits, misses, square tests, ordered reduced witnesses:',*physical())
    print('K at physical offset in exact all-offset torus check:',torus())
