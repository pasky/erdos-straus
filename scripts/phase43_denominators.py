"""Exact replay for PHASE43_DENOMINATORS.md. Standard library only."""
from collections import Counter
from fractions import Fraction
from functools import cache


@cache
def factors(n):
    """Trial division, for the two input primes and their window sizes only."""
    out = Counter()
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] += 1
    return out


def divisors(f):
    ds = [1]
    for p, b in f.items():
        ds = [d * p**j for j in range(b + 1) for d in ds]
    return ds


def square_divs(n, x):
    f = factors(n) + factors(x)
    return divisors(f + f)


def triples(n, x, ds):
    t, h = 4*x-n, n*x
    if t <= 0:
        return []
    hits = []
    for d in ds:
        if d <= h and (h+d) % t == 0:
            dd = h*h//d
            if (h+dd) % t == 0:  # also works with unreduced t/h
                y, z = (h+d)//t, (h+dd)//t
                assert Fraction(1,x) + Fraction(1,y) + Fraction(1,z) == Fraction(4,n)
                hits.append((x,y,z))
    return hits


def phase_check(n, last_prime):
    c = 43
    assert n % 840 == 1 and factors(n) == {n: 1}
    assert [pow(n,(u-1)//2,u) for u in (3,7,11,19,23,31,43)] == [1]*6+[42]
    x = (n+c)//4
    f = factors(x)
    assert f == {13:1, 29:1, 37:1, last_prime:1}
    logs = {pow(3,i,c):i for i in range(42)}
    assert len(logs) == 42
    costs = [sum(b*min(j*logs[p%c]%42,-j*logs[p%c]%42) for p,b in f.items())
             for j in range(1,42,2)]
    D = divisors(f)
    ratios = {d*pow(e,-1,c)%c for d in D for e in D}
    assert set(range(1,c))-ratios == {4,11,14,40,42} and min(costs) == 25
    return costs


def main():
    n, good = 12395549472601, 349219296721
    assert phase_check(n,222158389) == phase_check(good,6258859)
    x = (n+43)//4
    ds = square_divs(n,x)
    assert set(range(1,43))-{d%43 for d in ds} == {-n*x%43} == {30}
    for t in range(3,48,4):
        u = (n+t)//4
        hits = triples(n,u,square_divs(n,u))
        assert len(hits) == (6 if t == 47 else 0)
        if hits:
            print('First window:', t, 'one triple:', min(hits,key=lambda h:h[2]))
    # Rule out putting *any* d | (nx)^2 in any of the three denominator slots.
    base = factors(n) + factors(x)
    for d in ds:
        if 4*d <= n:
            continue
        f, a = factors(n).copy(), d
        for p in base:
            while a % p == 0:
                f[p] += 1
                a //= p
        assert a == 1 and not triples(n,d,divisors(f+f))
    u = (good+43)//4
    hits = triples(good,u,square_divs(good,u))
    a = u//481
    assert good == 1924*a-43 and a%43 == 41 and (good*a+1)%43 == 0
    y = 481*((good*a+1)//43)
    assert (u,y,good*a*y) in hits
    print('Same phase costs, successful complement:', (u,y,good*a*y))


if __name__ == '__main__':
    main()
