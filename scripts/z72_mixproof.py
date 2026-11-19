"""Integer certificates for data/z72/mixproof.md. No class-group oracle."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt, prod

from sympy import divisors, isprime, legendre_symbol, primerange, sqrt_mod
from sympy.ntheory.modular import crt


def words(p, d):
    """All signed ideal words; one root per prime power, no conjugate pair."""
    Q = {False: [], True: []}
    for q in primerange(3, 200):
        if legendre_symbol(-d*p, q) != 1:
            continue
        cell = Q[legendre_symbol(-d, q) == -1]
        if len(cell) < 3:
            cell.append(q)
        if all(len(v) == 3 for v in Q.values()):
            break
    assert all(len(v) == 3 for v in Q.values())
    W = []
    for k in (1, 2, 3):
        for S in combinations(sorted(Q[True]+Q[False]), k):
            for es in product((1, 2), repeat=k):
                ms = [q**e for q, e in zip(S, es)]
                if sum(e for q, e in zip(S, es) if q in Q[True]) % 2 == 0:
                    continue
                for rr in product(*(sqrt_mod(-d*p, m, all_roots=True) for m in ms)):
                    r, N = map(int, crt(ms, rr))
                    W.append((N, r))
    assert len(W) == len(set(W))
    return sorted(Q[True]+Q[False]), W


def reduced(N, r, p):
    a, b, c = N, 2*r, (r*r+p)//N
    assert b*b-4*a*c == -4*p
    while True:
        j = (a-b)//(2*a)
        b, c = b+2*j*a, c+j*(b+j*a)
        if a <= c:
            return a, abs(b) if a == c else b, c
        a, b, c = c, -b, a


def check_d1():
    p = 409
    Q, W = words(p, 1)
    assert {5, 7} <= set(Q) and any(n == 35 for n, r in W)
    hit = lambda m: [a for a in divisors((p+35)//4) if (4*a*a+p) % m == 0]
    assert (hit(5), hit(7), hit(35)) == ([3, 37], [1, 111], [])

    p = 9601
    assert isprime(p)
    Q, W = words(p, 1)
    f = {reduced(N, r, p) for N, r in W}
    ranked = sorted(f, key=lambda t: (Fraction(abs(t[1]), t[0]), t))
    gg = set()
    for a in range(1, 1+isqrt((p+(p+4)//3)//4)):
        for A in divisors(p+4*a*a):
            if (A+1) % (4*a) == 0:
                gg.update(reduced(A, r, p) for r in (2*a, -2*a))
    assert gg and gg.isdisjoint(ranked[:4])
    assert Fraction(abs(ranked[3][1]), ranked[3][0]) < Fraction(abs(ranked[4][1]), ranked[4][0])
    print('9601: four ranked forms', ranked[:4], 'good', sorted(gg))

    p = 15322362791157241  # < 2^64: SymPy's deterministic range
    assert isprime(p) and p % 840 == 1
    Q, W = words(p, 1)
    ranked = sorted({reduced(n, r, p) for n, r in W}, key=lambda t: (Fraction(abs(t[1]), t[0]), t))
    N, a = 17**2 * 19 * 23**2, 311
    e, c = (p+4*a*a)//N, (N+1)//(4*a)
    b = (p+e)//(4*a)
    assert 4*a*b == p+e and c*e == a+b and N == 4*a*c-1
    assert (N, 2*a) in W and reduced(N, 2*a, p) in ranked[:4]
    print('top-four mixed hit', p, Q, (a, b, c, e), ranked[0][:2])


def check_d2():
    p0 = 9601
    Q, W = words(p0, 2)
    assert Q == [3, 11, 13, 17, 23, 29]
    norms = {n for n, r in W}
    assert (len(W), len(norms), max(norms)) == (710, 103, 5783557)
    assert all((p0+8*a*a) % n != 0 for n in norms if n % 8 == 7
               for a in divisors((n+1)//8))
    M = 840*prod(q*q for q in primerange(3, 30))
    x, L = map(int, crt((M, 31), (p0, -8)))
    assert gcd(x, L) == 1 and x % 840 == 361
    print('d=2 exclusion:', len(W), 'words,', len(norms), 'norms, max', max(norms))
    print('nonempty on progression:', x, 'mod', L)


if __name__ == '__main__':
    check_d1()
    check_d2()
