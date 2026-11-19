"""Exact replay for SIGNED_TWO_SHIFTS.md; standard library, no campaign solver."""
from collections import Counter
from functools import lru_cache
from math import gcd


@lru_cache(maxsize=8192)
def factors(n):
    assert n > 0
    result = []
    q = 2
    while q*q <= n:
        if n % q == 0:
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            result.append((q, e))
        q = 3 if q == 2 else q+2
    return tuple(result) + (((n, 1),) if n > 1 else ())


def prime(n):
    return n > 1 and factors(n) == ((n, 1),)


def divisors_sq(f):
    result = [1]
    for q, e in f:
        result = [q**j * t for j in range(2*e+1) for t in result]
    return result


def eligibility(p, d):
    assert d > 0 and d % 4 == 3
    if gcd(p, d) > 1:
        return False, False
    # First component uses reciprocity; second lifts unit roots at odd primes.
    sign = pow(d, (p-1)//2, p) == p-1
    root = all(pow(-p, (q-1)//2, q) == 1 for q, _ in factors(d))
    assert not root or sign
    return sign, root


def slots(p, trial_y=False):
    out = []
    for x in range(p//4+1, 3*p//4+1):
        h, c = p*x, 4*x-p
        if trial_y:
            ys = range(max(x, h//c+1), 2*h//c+1)
        else:
            ys = [(h+t)//c for t in divisors_sq(factors(x)+((p, 1),))
                  if max(1, c*x-h) <= t <= h and (h+t) % c == 0]
        for y in ys:
            z, rem = divmod(h*y, c*y-h)
            if rem == 0:
                assert x <= y <= z and 4*x*y*z == p*(x*y+x*z+y*z)
                out.append((x, y, z))
    return sorted(out)


def shifts(p, triples):
    s = {v for row in triples for v in row}
    return (sorted(4*v-p for v in s if v % p),
            sorted((4*(v//p)-1)//p for v in s if v % p == 0 and (4*(v//p)-1) % p == 0))


def ratios(h, f, d):
    inv = pow(h, -1, d)
    return {t*inv % d for t in divisors_sq(f)}


def windows(p, d):
    k, n = (p+d)//4, (p*d+1)//4
    assert k % p and gcd(d, p) == 1 and gcd(k, p) == 1
    return ratios(p*k, factors(k)+((p, 1),), d), ratios(n, factors(n), d)


def hits(p, d):
    return tuple(d-1 in window for window in windows(p, d))


def case11(p):
    q, r = (p+11)//12, (11*p+1)//12
    assert 11*q-10 == r and eligibility(p, 11)[1]
    a = sorted(v % 11 for v, e in factors(q) for _ in range(e) if v % 11 != 1)
    b = sorted(v % 11 for v, e in factors(r) for _ in range(e) if v % 11 != 1)
    return (not (p % 11 in (2, 6) and a == [p % 11]),
            not (all(v in {3, 4, 5, 9} for v in b) or b == [2, 6]))


def audit():
    p = 193
    t = slots(p)
    assert t == slots(p, trial_y=True) and len(t) == 6
    print('193 sorted triples:', t)
    d1, d2 = shifts(p, t)
    assert d1 == [7, 15, 39, 967, 2511, 5327, 5607] and d2 == [3, 7, 143]
    for ds in (d1, d2):
        print('shifts (d, Jacobi eligible, root eligible):', [(d, *eligibility(p, d)) for d in ds])
        for d in ds:
            assert (not eligibility(p, d)[1] and
                    eligibility(p, d)[0] == (d in [15, 39, 5327, 5607]))
            assert hits(p, d) == (d in d1, d in d2)
    literal = sorted({4*(v//p)-1 for row in t for v in row if v % p == 0})
    assert [d for d in literal if eligibility(p, d)[1]] == [103]
    print('d=11 fixed denominators:')
    for s, h in [(51, 9843), (51, 51), (102483, 531), (579, 579)]:
        ts = divisors_sq(factors(h))
        residues = sorted({v % 11 for v in ts})
        assert -h % 11 not in residues
        print(s, h, len(ts), residues, -h % 11)
    assert [n for n in range(25, 193, 24) if prime(n)] == [73, 97]
    for n, d in [(73, 7), (97, 7), (193, 11), (2521, 11)]:
        assert d == next(j for j in range(3, n, 4) if prime(j) and eligibility(n, j)[1])
        assert hits(n, d)[0] == (n in (73, 97))
    assert 2521 == next(n for n in range(841, 3000, 840) if prime(n))
    for n, d, expected in [(193, 19, (False, False)), (2521, 19, (False, False)),
                            (2521, 23, (True, False)), (2521, 55, (True, False)),
                            (12601, 55, (False, False)), (3361, 11, (False, True))]:
        assert eligibility(n, d)[1] and hits(n, d) == expected
    for n, d, counts, outcome in [(12395549472601, 43, (41, 41), (False, False)),
                                  (349219296721, 43, (42, 3), (True, False)),
                                  (3117161329, 715, (12, 27), (False, False)),
                                  (1201, 39, (24, 9), (True, False))]:
        assert prime(n)
        win = windows(n, d)
        assert tuple(map(len, win)) == counts and hits(n, d) == outcome
        if n == 12395549472601:
            assert all(w == set(range(1, 42)) for w in win)
            assert next(c for c in range(3, 60, 4) if eligibility(n, c)[1] and any(hits(n, c))) == 59
        print('comparison:', n, d, eligibility(n, d), counts, outcome)


def survey():
    primes_d = [d for d in range(3, 201, 4) if prime(d)]
    tab = Counter()
    first = Counter()
    for p in range(841, 10_000_001, 840):
        if not prime(p):
            continue
        for d in primes_d:
            if not eligibility(p, d)[1]:
                continue
            result = hits(p, d)
            if d == 11:
                assert result == case11(p)
                tab[result] += 1
            if any(result):
                first[d] += 1
                if d == 199:
                    assert p == 6348721
                    print('longest by shift:', p, [(c, hits(p, c)) for c in primes_d
                                                    if c <= d and eligibility(p, c)[1]])
                break
        else:
            raise AssertionError(('no hit through 199', p))
    assert sum(first.values()) == 3426 and first[199] == 1
    print('least successful prime shifts:', sorted(first.items()))
    print('d=11 counts:', sorted(tab.items()))


if __name__ == '__main__':
    audit()
    survey()
