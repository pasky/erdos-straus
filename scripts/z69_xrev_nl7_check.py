"""Independent NL7 review checks. Run with uv run --with sympy python this_file MODE.
Modes: collapse (full 4e5 check, ~40 MB sieve), algebra, screens SOURCE_ROOT.
No imports from the lane's code; no outputs written to the repository.
"""
from array import array
from functools import lru_cache
from math import gcd, isqrt, lcm
from pathlib import Path
import sys


@lru_cache(None)
def factors(n):
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


@lru_cache(None)
def divisors(n):
    ds = [1]
    for p, e in factors(n):
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return ds


def odd_square_mod(n, modulus):
    if n % 8 != 1:
        return False
    for p, e in factors(modulus):
        if p == 2:
            continue
        unit, v = n, 0
        while unit % p == 0:
            unit //= p
            v += 1
        if v < e and (v % 2 or pow(unit, (p - 1) // 2, p) != 1):
            return False
    return True


def collapse():
    bound = 400000
    letters = (1, 2, 3, 4, 5, 6, 7, 8, 12, 15, 24)
    top = max(letters) * (bound - 1) + 1
    largest = array('I', [0]) * (top + 1)
    for p in range(2, top + 1):
        if largest[p] == 0:
            for multiple in range(p, top + 1, p):
                largest[multiple] = p
    # Match original n >= 3 range, but distinguish units from all squares.
    old = {pos: [0, 0, 0, 0] for pos in 'xzy'}
    full = {pos: [0, 0, 0, 0] for pos in 'xzy'}
    first_omitted = {}
    for n in range(3, bound, 2):
        for L in letters:
            for middle in (False, True):
                N = L * n + 1 if middle else n + L
                q = largest[N]
                c = N // q
                if c > 200 or q <= c:
                    continue
                ds = [d * mult for d in divisors(c) for mult in (1, q)]
                if middle:
                    hits = {'y': any((d + 1) % lcm(8, L) == 0 for d in ds)}
                else:
                    hits = {
                        'x': any((d + 1) % lcm(8, L) == 0 for d in ds),
                        'z': any((d + 1) % L == 0 and
                                 ((N // d) * ((d + 1) // L)) % 8 == 0 for d in ds),
                    }
                M = 8 * c * L
                sq = odd_square_mod(n, M)
                unit_sq = sq and gcd(n, M) == 1
                for pos, hit in hits.items():
                    for stat, condition in ((old, unit_sq), (full, sq)):
                        index = 0 if condition else 2
                        stat[pos][index] += 1
                        stat[pos][index + 1] += int(hit)
                    assert not (sq and hit), (n, L, c, q, pos)
                    if sq and not unit_sq:
                        first_omitted.setdefault(pos, (n, L, c, q, M))
    print('Original unit-only counts [square cases, hits, other cases, hits]:', old)
    print('Correct full square-class counts, same n >= 3 range:', full)
    print('First omitted cases (n,L,c,q,modulus):', first_omitted)
    extras = {'x': 0, 'z': 0, 'y': 0}
    for L in letters:
        for pos in 'xzy':
            N = L + 1
            q = largest[N]
            c = N // q
            if q > c and c <= 200:
                extras[pos] += 1
    print('n=1 adds square-class cases with no hits:', extras)


def algebra():
    import sympy as s
    t = s.symbols('t')
    for eps in (-1, 1):
        X = 4 * (t*t - 2*eps*t + 2)
        Y = (4*t*t + 8*eps*t + 9) / 63
        Psg = 16*t**4 + 1
        assert s.expand(X*Y*63 - X - 63 - Psg) == 0
        # Elsholtz–Tao (2.13)–(2.15), with a=1, e=63.
        b, c, d = 4*(t*t + 2*eps*t + 2), Y, X/4
        assert s.expand(4*b*d - Psg - 63) == 0
        assert s.expand(63*c - 1 - b) == 0
        assert s.expand(4*b*c*d - 1 - b - Psg*c) == 0
    print('SG is exactly ET Type-II with a=1, e=63 (both signs)')
    counts = [0, 0]
    for v in range(-200000, 200000):
        if v % 126 not in (18, 108):
            continue
        eps = 1 if v % 126 == 18 else -1
        x = 4*(v*v - 2*eps*v + 2)
        numerator = 4*v*v + 8*eps*v + 9
        assert numerator % 63 == 0
        y = numerator // 63
        n = 16*v**4 + 1
        assert min(x, y, 63) > 0 and x*y % 8 == 0
        assert x*y*63 - x - 63 == n and isqrt(n)**2 != n
        counts[v > 0] += 1
    print('SG exact identities: symbolic both signs; negative/positive counts', counts)
    P = t**4 + 2*t*t - 4*t + 2
    assert s.Poly(P, t).is_irreducible
    assert s.expand((2*t-1)**2 + (t*t-1)**2 - P) == 0
    assert s.expand(t**4 + 2*(t-1)**2 - P) == 0
    assert s.expand((t*t+2)**2 - 2*(t+1)**2 - P) == 0
    assert s.expand((t*t+2*t+4)*(t*t-2*t+2) - P - 6) == 0
    small = {}
    for p in s.primerange(3, 400):
        residues = {v*v % p for v in range(1, p)}
        ok = [v for v in range(p) if (v**4+2*v*v-4*v+2) % p in residues
              and ((v*v+2*v+4)*(v*v-2*v+2)) % p != 0]
        assert ok, p
        if p <= 23:
            small[p] = ok
    print('NL-J norm identities and LC-prime checks <400 pass; small classes:', small)
    print('NL-J discriminant:', s.discriminant(P, t))
    # Check the H | 64 factorisation in the proof, without numerical inference.
    r, u = s.symbols('r u')
    H = r*r*(r*r+2*u*u)**2 - 8*r*r*u**4 - 16*u**6
    assert s.expand(H-(r*r-2*u*u)*(r*r+2*u*u)*(r*r+4*u*u)) == 0
    print('Lemma 8(iii) sextic factorisation verified')


def screens(root):
    import sympy as s
    for name in ('r8_zeros_1e10.txt', 'composite_zeros_le8e6.txt',
                 'star_prime_zeros.txt', 'gstar_zeros.txt'):
        ns = [int(line.split()[0]) for line in
              (Path(root)/'data/z58/screens'/name).read_text().splitlines()
              if line.strip() and not line.startswith('#')]
        zero, family, witnessed = [], [], 0
        for n in ns:
            if (n-1) % 16 == 0:
                v, exact = s.integer_nthroot((n-1)//16, 4)
                if exact and v % 126 in (18, 108):
                    family.append(n)
            # Complete witness bound f <= 2n+1; screen primes stop very early.
            for f in range(7, 2*n+2, 8):
                r = (-n) % f
                if r and (f+1) % r == 0:
                    witnessed += 1
                    break
            else:
                zero.append(n)
        print(name, 'count', len(ns), 'SG members', family,
              'U7 witnessed', witnessed, 'complete zeros', zero)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'collapse':
        collapse()
    elif mode == 'algebra':
        algebra()
    elif mode == 'screens':
        screens(sys.argv[2])
    else:
        raise SystemExit('unknown mode')
