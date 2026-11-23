"""Exact finite controls only. No computation with nonstandard functions."""
from math import gcd, isqrt


def first(k, n):
    # x <= y <= z forces these two finite intervals. No arbitrary cutoff.
    for x in range(n // k + 1, 3 * n // k + 1):
        a, b = k * x - n, n * x
        for y in range(max(x, b // a + 1), 2 * b // a + 1):
            z, rem = divmod(b * y, a * y - b)
            if not rem:
                assert x <= y <= z and k * x * y * z == n * (x*y + y*z + z*x)
                return x, y, z
    return None


def cbrt(n):
    lo, hi = 0, n + 1
    while hi - lo > 1:
        m = (lo + hi) // 2
        if m**3 <= n:
            lo = m
        else:
            hi = m
    return lo


if __name__ == '__main__':
    for n in [9, 25, 49, 11, 17, 131, 241, 409, 577, 2521, 3361, 5569]:
        v = first(4, n)
        assert v is not None
        a, b = isqrt(n), cbrt(n)
        d = gcd(a, b)
        a1, b1 = a // d, b // d
        s = 0 if b1 == 1 else pow(a1, -1, b1)
        t, rem = divmod(1 - s * a1, b1)
        assert not rem and 0 <= s < b1 and s * a + t * b == d
        print(f'n={n}: 4/n={v}; (sqrt-floor,cube-floor;gcd,s,t)={(a,b,d,s,t)}')
    for n in [11, 17, 131, 241]:
        assert first(8, n) is None
        print(f'8/{n}: no positive sorted triple (exhaustive)')
