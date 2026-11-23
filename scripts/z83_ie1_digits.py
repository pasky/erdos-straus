"""Finite controls for the digit-lift and small-remainder proofs; no ES census."""
from math import isqrt
from pathlib import Path


def f(x):
    return x + 2*x*x


def lift(a, h):
    assert h > 0 and h & (h-1) == 0
    x, d = 0, 1
    while d < h:
        assert (f(x)-a) % d == 0
        if ((f(x)-a)//d) % 2:
            x += d
        d *= 2
    assert 0 <= x < h and (f(x)-a) % h == 0
    return x


def newton(a, r, h):
    assert (f(r)-a) % h == 0
    s = (r - (f(r)-a)*pow(1+4*r, -1, h*h)) % (h*h)
    assert (f(s)-a) % (h*h) == 0
    return s


def check_maps():
    for h in range(1, 513):
        image = {f(x) % h for x in range(h)}
        assert (len(image) == h) == (h & (h-1) == 0)
        if len(image) == h:
            assert len({lift(a, h) for a in image}) == h
        for b in range(3, h+1, 2):
            if h % b == 0:
                k = h//b
                u = -(1+2*k)*pow(4, -1, b) % b
                v = (u+k) % h
                assert u != v and (f(u)-f(v)) % h == 0
    print('F=X+2X²: permutation iff pure dyadic; all odd divisor collision recipes, h=1..512: PASS')


def check_remainders():
    zeros = {int(s) for s in (Path(__file__).resolve().parents[1] / 'data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and not s.startswith('#')}
    hard = {2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929}
    controls = zeros | hard | {17,241,17401609,105,1465,3865,4545,10305,12145,39361,67425,1590284203561,6955940568721,225}
    for p in sorted(controls):
        assert p % 8 == 1
        # Strictly between sqrt(p)/2 and sqrt(p) for these particular inputs.
        h = 1 << (isqrt(p).bit_length()-1)
        assert h*h < p < (2*h)**2
        root = (1+4*lift((p-1)//8, 4*h)) % (2*h)
        r = min(root, 2*h-root)
        t, rem = divmod(p-r*r, h)
        assert rem == 0 and 0 < r <= h and 0 < t < p and t*t < 4*p and t % 4 == 0
        u = t//4
        assert 4 * (2*u)*(3*u)*(6*u) == t*((2*u)*(3*u)+(2*u)*(6*u)+(3*u)*(6*u))
        if p in {17,225,241,409,3153419441929}:
            print(f'p={p} = {r}² + {h}·{t}; t=0 (4), 0<t<2√p')
    print(f'{len(controls)} distinct supplied screen inputs with positive smaller remainders: PASS')


def check_seed():
    # Synthetic seed: checks agreement at H and doubling precision, not primality.
    h, ell, x = 2**16, 840, 91237
    q = 1 + 8*h*ell*x
    for a, b in [(q, 1), ((q-1)//8, 0), (3*q*q-7*q+19, 15)]:
        d, r = h, lift(b, h)
        for _ in range(5):
            r = newton(a, r, d)
            d *= d
            assert r == lift(a, d)
    print('3 masked targets: Newton and bit lifts agree through 512 bits: PASS')


if __name__ == '__main__':
    check_maps()
    check_remainders()
    check_seed()
