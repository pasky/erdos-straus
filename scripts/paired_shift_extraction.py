"""Exact small certificates for PAIRED_SHIFT_EXTRACTION.md (no dependencies)."""
from math import gcd, isqrt
from signed_two_shifts import eligibility, factors, hits, prime, shifts, slots, divisors_sq


def divisors(n):
    ds = [1]
    for r, e in factors(n):
        ds = [d*r**j for d in ds for j in range(e+1)]
    return ds


def check_triple(p, x, y, z):
    assert min(x, y, z) > 0 and 4*x*y*z == p*(x*y+x*z+y*z)


def exhaustive():
    p = 2521
    assert all(prime(v) for v in [p, 211, 2311, 1321])
    assert not any(hits(p, 11)) and eligibility(p, 211)[1]
    direct, dual = shifts(p, slots(p, trial_y=True))
    root = [[d for d in ds if eligibility(p, d)[1]] for ds in [direct, dual]]
    assert root == [[23, 55, 1583, 13495], []]
    support = {r for n in [p+11, 11*p+1, p+121, 11*p+121] for r, _ in factors(n)}
    assert all(any(r not in support for r, _ in factors(d)) for d in root[0])
    print('2521 root-eligible lists:', root)

    p = 12601
    assert all(prime(v) for v in (p, 1051, 11551, 6361)) and not any(hits(p,11))
    forms = [(1,11), (11,1), (1,121), (11,121)]
    values = [a*p+b for a,b in forms] + [abs(a*d-b*c) for a,b in forms for c,d in forms if a*d != b*c]
    support = {r for n in values for r,_ in factors(n)}
    ds = shifts(p, slots(p, trial_y=True))
    supported = [[d for d in l if all(r in support for r,_ in factors(d))] for l in ds]
    assert supported == [[3,27], [95,735]]
    assert not any(eligibility(p, d)[0] for l in supported for d in l)
    print('12601 supported lists, with determinants:', supported)


def direct():
    q, a, t = 431, 38, 162
    b = q-a
    k = a*b*t
    p = 4*k-q
    assert p == 9676801 and prime(p) and prime(1871) and prime(8870401)
    assert ((p+11)//12, (11*p+1)//12) == (q*1871, 8870401)
    assert eligibility(p, q)[1] and not any(hits(p, 11))
    h = p*k
    assert all(d % q != q-1 for d in divisors(h))
    ratios = {(u//gcd(h,u), h//gcd(h,u)) for u in divisors_sq(factors(h)) if (u+h)%q == 0}
    assert ratios == {(38,393), (393,38)}
    check_triple(p, k, p*a*t, p*b*t)
    print(p, 'all successful direct ratios at 431:', sorted(ratios))


def pell():
    q, s, c, T = 79, 549, 255828, 362210
    n = c*q-11
    assert n == 20210401 and prime(n)
    assert all(prime(v) for v in (q, 21319, 23, 805487))
    assert ((n+11)//12, (11*n+1)//12) == (q*21319, 23*805487)
    assert eligibility(n, q)[1] and not any(hits(n,11))
    A = 49*T-c
    assert isqrt(A*T) == 2517130 and (2*A*q+11)**2 - A*T*(2*s)**2 == 121+4*A
    a,b = (7*q-s)//2, (7*q+s)//2
    N = (n*q+1)//4
    assert T*a*b == N and all(r%q != q-1 for r,_ in factors(N))
    check_triple(n, n*N, 7*T*a, 7*T*b)
    print(n, 'dual split at 79:', (a,b), 'Pell discriminant:', A*T)


if __name__ == '__main__':
    exhaustive()
    direct()
    pell()
