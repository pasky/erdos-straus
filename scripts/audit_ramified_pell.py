"""Exact checks for the ramified-unit and exponent-collision lemmas, not a proof."""
from math import isqrt
from itertools import product


def mul(p, a, b):
    return a[0]*b[0] + p*a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def power(p, u, j):
    if j < 0:
        x, y = u
        norm = x*x-p*y*y
        assert abs(norm) == 1
        return power(p, (norm*x, -norm*y), -j)
    ans = (1, 0)
    while j:
        if j & 1:
            ans = mul(p, ans, u)
        u = mul(p, u, u)
        j >>= 1
    return ans


def val(p, t):
    assert t
    v = 0
    while t % p == 0:
        t //= p
        v += 1
    return v


def main():
    lifts = 0
    for p in (5, 13, 17, 29, 37, 41):
        eta = next((isqrt(p*y*y-1), y) for y in range(1, 1000)
                   if isqrt(p*y*y-1)**2 == p*y*y-1)
        for base in (eta, power(p, eta, p)):  # include initial y divisible by p
            for j in (-p*p, -p, -3, 1, 2, 3, p, p*p):
                actual = power(p, base, j)[1]
                assert val(p, actual) == val(p, base[1])+val(p, j)
                lifts += 1
    p, a = 5, 2
    n = p**(2*a+1)
    u = power(p, (2, 1), p**a)
    # A nonidentity slot attains m=n+1 on a signed exponent collision.
    # Grouping must not assume independent, positive, or sorted indices.
    cases = 0
    for j, k in ((1, 3), (-1, -3), (1, -3), (-1, 3)):
        for e, f in product((-1, 1), repeat=2):
            terms = [(j*3, e**3, n+4, 1), (k, f, -3, 0), (0, 1, 7*(n+1), 7)]
            blocks = {}
            num = [0, 0]; den = [0, 0]
            for h, sign, A, D in terms:
                w = power(p, u, h)
                B = blocks.setdefault(h, [0, 0])
                B[0] += sign*A; B[1] += sign*D
                for i in (0, 1):
                    num[i] += sign*A*w[i]; den[i] += sign*D*w[i]
            target = n+1
            assert (num == [target*v for v in den]) == all(A==target*D for A,D in blocks.values())
            assert (num == [target*v for v in den]) == (k==3*j and e==f)
            cases += 1
    print(f'{lifts} signed lifting tests, {cases} signed exponent-partition tests passed')


if __name__ == '__main__':
    main()
