# review_r235_brute.py -- independent ES solver for n = 4^s + k, s <= SMAX (R235). Uses (a y - d)(a z - d) = d^2.
import sys
from sympy import factorint
from itertools import product


def divisors_sq(fac):
    ps = list(fac.items())
    for es in product(*[range(2 * e + 1) for _, e in ps]):
        v = 1
        for (p, _), e in zip(ps, es):
            v *= p ** e
        yield v


def es(n):
    fn = factorint(n)
    for x in range(n // 4 + 1, n + 1):
        a, d = 4 * x - n, n * x
        fac = dict(fn)
        for p, e in factorint(x).items():
            fac[p] = fac.get(p, 0) + e
        for dl in divisors_sq(fac):
            if dl <= d and (dl + d) % a == 0:
                y = (dl + d) // a
                z = (d * d // dl + d) // a
                assert 4 * x * y * z == n * (x * y + y * z + z * x)
                return x, y, z
    return None


if __name__ == '__main__':
    SMAX = int(sys.argv[1])
    for k in [9, 57, 81, 129, 153, 177, 201, 225, 249, 33, 105, 273, 297]:
        for s in range(SMAX + 1):
            n = 4 ** s + k
            sol = es(n)
            assert sol, (k, s)
        print(k, 'ES ok for s <=', SMAX, 'last', (n, sol))
