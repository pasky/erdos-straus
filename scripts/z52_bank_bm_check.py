"""Check the local invariants of A = (-q,-d) on S_{n,k}, q = 4y-n, d = qz-ny (z52 bank §1(a)).
For random rational points P of S_{n,k} (y,z random integers, x = (k + n y z)/d), and every prime l at which P is
l-integral and l divides some numerator/denominator involved (plus l = 2), compute (-q,-d)_l.
Predictions (PROVED in Z52_BANKED.md): k = 4: inv_l = 0 at odd l on S(Z_l); at l = 2 inv = 0 if n = 1 (8).
k = 1: same with n = 5 (8) at l = 2.  Also checks the global product formula prod_v (-q,-d)_v = 1 on every point.
Also the k = 0 comparison: on U_n (k = 0), compare (-q,-d) with Bright-Loughran's (-x/z, -y/z) place by place."""
import random, sys
from fractions import Fraction as Fr
from sympy import factorint, legendre_symbol

def vp(r, p):
    r = Fr(r); a, b = r.numerator, r.denominator; v = 0
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v, a * b  # unit part up to squares (a*b has same square class as a/b)

def hilbert(a, b, p):
    """(a,b)_p for nonzero rationals a,b; p prime or 0 (= real place)."""
    a, b = Fr(a), Fr(b)
    if p == 0: return -1 if (a < 0 and b < 0) else 1
    al, u = vp(a, p); be, v = vp(b, p)
    if p != 2:
        s = (-1) ** ((al * be * ((p - 1) // 2)) % 2)
        if be % 2: s *= legendre_symbol(u % p, p)
        if al % 2: s *= legendre_symbol(v % p, p)
        return s
    eps = lambda w: ((w - 1) // 2) % 2
    om = lambda w: ((w * w - 1) // 8) % 2
    e = eps(u % 8) * eps(v % 8) + al * om(v % 8) + be * om(u % 8)
    return (-1) ** (e % 2)

def primes_of(*rs):
    S = {2}
    for r in rs:
        r = Fr(r)
        for t in (abs(r.numerator), r.denominator):
            if t > 1: S |= set(factorint(t).keys())
    return S

def integral_at(p, *rs):
    return all(Fr(r).denominator % p != 0 for r in rs)

def run(n, k, trials, rng, stats):
    for _ in range(trials):
        y = rng.randint(-60, 60); z = rng.randint(-60, 60)
        q = 4 * y - n; d = q * z - n * y
        if d == 0 or q == 0: continue
        x = Fr(k + n * y * z, d)
        if x == 0: continue
        assert 4 * x * y * z - n * (x * y + y * z + z * x) == k
        dd = Fr(d); qq = Fr(q)
        prod = hilbert(-qq, -dd, 0)
        for p in primes_of(x, y, z, q, d, n):
            h = hilbert(-qq, -dd, p); prod *= h
            if integral_at(p, x, y, z):
                key = (k, 'odd' if p != 2 else 'two:n%8=' + str(n % 8))
                stats.setdefault(key, [0, 0])
                stats[key][0 if h == 1 else 1] += 1
        assert prod == 1, (n, k, x, y, z)
        stats['prodformula_ok'] = stats.get('prodformula_ok', 0) + 1

def bl_compare(n, rng, stats, trials):
    """k = 0: rational points of U_n; compare A=(-q,-d) with BL=(-x/z,-y/z) at all places."""
    for _ in range(trials):
        y = rng.randint(-60, 60); z = rng.randint(-60, 60)
        q = 4 * y - n; d = q * z - n * y
        if d == 0 or q == 0 or y == 0 or z == 0: continue
        x = Fr(n * y * z, d)
        assert 4 * x * y * z - n * (x * y + y * z + z * x) == 0
        places = [0] + sorted(primes_of(x, y, z, q, d, n))
        diff = [p for p in places if hilbert(-Fr(q), -Fr(d), p) != hilbert(-x / z, -Fr(y) / z, p)]
        stats.setdefault('BLdiff', {})
        key = tuple(diff)
        stats['BLdiff'][key] = stats['BLdiff'].get(key, 0) + 1

if __name__ == '__main__':
    rng = random.Random(52)
    stats = {}
    for n in [9, 17, 25, 33, 41, 73, 89, 97, 105, 113, 5, 13, 21, 29, 37, 45, 53, 61, 77, 85]:
        for k in (4, 1):
            run(n, k, 400, rng, stats)
    for key in sorted(k for k in stats if isinstance(k, tuple)):
        print(key, 'symbol +1:', stats[key][0], ' symbol -1:', stats[key][1])
    print('product formula verified on', stats['prodformula_ok'], 'points')
    st2 = {}
    for n in [5, 13, 17, 9, 25, 105, 41]:
        bl_compare(n, rng, st2, 300)
    print('k=0: places where (-q,-d) != BL class (-x/z,-y/z):', st2['BLdiff'])
