"""Finite controls for V (both labels), D (pair support) and M (local center)."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt, lcm


def divisors(n):
    lo = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return lo + [n // d for d in lo[::-1] if d != n // d]


def phi(n):
    result = n
    d = 2
    while d*d <= n:
        if n % d == 0:
            result -= result // d
            while n % d == 0:
                n //= d
        d += 1
    return result if n == 1 else result - result // n


def windows():
    stats = Counter()
    for p in range(101, 3000, 4):
        if len(divisors(p)) != 2:
            continue
        for q in range(3, 64, 4):
            x = (p+q)//4
            s = p*x
            ds = divisors(x)
            # All coprime ordered left/right allocations of divisors of x.
            labels = [(a, b) for a in ds for b in ds if gcd(a, b) == 1]
            direct = any((a+b) % q == 0 for a, b in labels)
            extra = any((p*a+b) % q == 0 for a, b in labels)
            # Instead factor the difference of squares at y,z. No ratio search.
            hits = False
            for d in divisors(x*x):
                for h in (d, p*d, p*p*d):
                    if h > s or (h+s) % q:
                        continue
                    k = s*s//h
                    assert (k+s) % q == 0
                    y, z = (h+s)//q, (k+s)//q
                    assert x < y and x < z and 4*x*y*z == p*(x*y+y*z+z*x)
                    hits = True
            assert hits == (direct or extra)
            stats[direct, extra] += 1
    assert all(stats[d, e] for d, e in product((False, True), repeat=2))
    print('two clauses (00,01,10,11):', *(stats[k] for k in product((False, True), repeat=2)))


def last_prime():
    # Do not count a completing residue with more than one split as extra digits.
    tot = duplicate = 0
    for q in (7, 11, 15, 19):
        for seed, older in ((4, 23*29), (10, 23*31), (49, 31*37)):
            if gcd(seed*older, q) != 1:
                continue
            ratios = [(a*pow(b, -1, q)) % q for a in divisors(seed*older)
                      for b in divisors(seed*older) if gcd(a, b) == 1]
            for n in range(1, q):
                if gcd(n, q) != 1:
                    continue
                allowed = Counter()
                for d in ratios:
                    for t in (1, n, pow(n, -1, q)):
                        u = (-t*d) % q
                        allowed.update((u, pow(u, -1, q)))
                for r in (41, 43, 47, 53, 59, 61):
                    m = seed*older*r
                    ds = divisors(m)
                    fresh = any((a % r == 0 or b % r == 0) and gcd(a, b) == 1
                                and ((a+b) % q == 0 or (n*a+b) % q == 0)
                                for a in ds for b in ds)
                    assert fresh == (r % q in allowed)
                    duplicate += int(allowed[r % q] > 1)
                    tot += 1
    print('fresh top tests / multiple labels same digit:', tot, duplicate)


def interval_pairs():
    X = 40000
    cells = [(a, 4*a*d-1) for a in range(18, 23) for d in range(24, 30)]
    table = defaultdict(list)
    for i, (a, q) in enumerate(cells):
        for n in range(X+1+((-a-X-1) % q), 2*X+1, q):
            table[n].append(i)
    supported = {p for row in table.values() for p in combinations(row, 2)}
    nhit = comparisons = 0
    masses = [F(0), F(0)]
    for i,j in combinations(range(len(cells)), 2):
        a, q = cells[i]
        b, h = cells[j]
        g = gcd(q, h)
        if (a-b) % g:
            assert (i,j) not in supported
            continue
        per = lcm(q,h)
        t = (-a + q*(((a-b)//g * pow(q//g, -1, h//g)) % (h//g))) % per
        assert gcd(t, per) == 1
        count = (2*X-t)//per - (X-t)//per
        assert bool(count) == ((i,j) in supported)
        nhit += count
        comparisons += 1
        masses[bool(count)] += F(1, phi(per))
    assert nhit == sum(len(row)*(len(row)-1)//2 for row in table.values())
    print('toy pair cylinder census (compatible, supported, interval incidences):', comparisons, len(supported), nhit)
    print('toy Haar miss-support fraction (rounded):', round(float(masses[False]/sum(masses)), 6))
    for t in (2, 3, 5, 11):
        a = t**8; d = (a+1)*t+1
        q = 4*a*d-1; h = 4*(a+1)*(d-t)-1
        assert h == q+4 and gcd(q, h) == 1
        assert 4*((2*t**25+a+1)//h)-1 < q
        start = (-a + q*((-pow(q, -1, h)) % h)) % (q*h)
        assert (start+a+1) % h == (start+a) % q == 0
        assert (2*t**25-start)//(q*h) == (t**25-start)//(q*h)
    print('explicit empty coprime pairs: 4 exact dyads')


def repaired_center():
    cells = [(3,17,1),(9,17,4),(15,17,7),(9,19,2),(15,19,8),(5,19,3)]
    def repair(n):
        a = n % 9 if n % 3 else 1
        b = n % 5 if n % 5 else 1
        return a + 9*((4*(b-a)) % 5)
    def zparts(n):
        return [(r,u) for k,r,u in cells if (repair(n)+u) % k == 0]
    period = lcm(45,17,19)
    moment = [F(0)]*45
    for n in range(period):
        row = zparts(n)
        mu = sum((F(1,r) for r,u in row), F(0))
        moment[n % 45] += (sum((n+u) % r == 0 for r,u in row)-mu)**4
    means = set()
    for a in range(45):
        row = zparts(a)
        ps = [F(sum(t==r for t,u in row),r) for r in (17,19)]
        mu = sum(ps); means.add(mu)
        expected = sum((i+j-mu)**4 * (ps[0] if i else 1-ps[0]) * (ps[1] if j else 1-ps[1])
                       for i,j in product(range(2), repeat=2))
        assert moment[a] == expected*(period//45)
    print('repaired center fourth moments:', len(moment), 'fibres;', len(means), 'different centers')


if __name__ == '__main__':
    windows()
    last_prime()
    interval_pairs()
    repaired_center()
