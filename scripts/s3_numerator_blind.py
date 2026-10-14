"""O208 (SYNTHESIS III): the square-denominator / mute relaxation is numerator-blind.

For M = 0 (mod 4) and the primes p where M/p = 1/x+1/y+1/z FAILS (MODEL_SPECIFIC census, data/ms/prime_fail_1e8.txt),
exhibit explicit M^box certificates:
    M/p = 1/x + 1/y + 1/z,  x, y in Z_{>0},  z in Q_{>0} with den(z) an odd square coprime to p,
from the general-M shot identity (g | p + M Q^2, g = -1 mod M):
    m' = (p + M Q^2)/g,  x = (p + m')/M,  y = p (g+1)/M,  z = p x (g+1)/(M Q^2).
Also: least overflow Q1 = Q / gcd(Q, (g+1)/M) and least self-mute cap e over shots with Q <= QMAX (all divisors g),
and the T1 control at odd squares.
Usage: PYTHONPATH=scripts uv run python scripts/s3_numerator_blind.py [QMAX]
"""
import sys
from fractions import Fraction
from math import gcd, isqrt
from sympy import isprime, sqrt_mod, factorint, divisors

QMAX = 60


def fails(M):
    for line in open('data/ms/prime_fail_1e8.txt'):
        if line.startswith(f'm={M} '):
            body = line.split('failures:')[1].split('checked')[0]
            return [int(t) for t in body.split()]
    return []


def shot_solution(M, p, g, Q):
    N = p + M * Q * Q
    assert N % g == 0 and (g + 1) % M == 0
    mp = N // g
    assert (p + mp) % M == 0
    x = (p + mp) // M
    y = p * (g + 1) // M
    z = Fraction(p * x * (g + 1), M * Q * Q)
    assert Fraction(M, p) == Fraction(1, x) + Fraction(1, y) + 1 / z, (M, p, g, Q)
    return x, y, z


def box_ok(z, p):
    d = z.denominator
    r = isqrt(d)
    return r * r == d and d % 2 == 1 and gcd(d, p) == 1


def dirichlet_cert(M, p):
    """least prime g = -1 (mod M), g != p, with -p/M a square mod g; odd Q < 2g prime to p."""
    g = M - 1
    while True:
        if isprime(g) and g != p and p % g:
            a = (-p * pow(M, -1, g)) % g
            s = sqrt_mod(a, g)
            if s is not None:
                for Q in sorted({s, g - s, s + g, 2 * g - s}):
                    if Q > 0 and Q % 2 == 1 and gcd(Q, p) == 1:
                        x, y, z = shot_solution(M, p, g, Q)
                        assert box_ok(z, p)
                        return g, Q, x, y, z
        g += M


def cap(Q, k):
    """least e with: rad(Q1) | k and v_l(Q) <= v_l(k) + e (self-mute cap), Q1 = Q/gcd(Q,k); None if rad fails"""
    e = 0
    for l, c in factorint(Q).items():
        s = 0
        kk = k
        while kk % l == 0:
            kk //= l
            s += 1
        if c > s:
            if s == 0:
                return None
            e = max(e, c - s)
    return e


def best_overflow(M, p):
    best_q1, best_e = None, None
    for Q in range(1, QMAX + 1, 2):
        if gcd(Q, p) > 1:
            continue
        N = p + M * Q * Q
        for g in divisors(N):
            if (g + 1) % M:
                continue
            k = (g + 1) // M
            q1 = Q // gcd(Q, k)
            if best_q1 is None or q1 < best_q1:
                best_q1 = q1
            e = cap(Q, k)
            if e is not None and (best_e is None or e < best_e):
                best_e = e
    return best_q1, best_e


def main():
    global QMAX
    QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    tot = 0
    for M in (8, 12, 16, 20, 24):
        F = [p for p in fails(M) if M % p]
        rows = []
        for p in F:
            g, Q, x, y, z = dirichlet_cert(M, p)
            q1, e = best_overflow(M, p)
            assert q1 is None or q1 > 1, ('shot gives an M-solution at a failing prime?!', M, p)
            rows.append((p, g, Q, q1, e))
            tot += 1
        gmax = max(r[1] for r in rows)
        print(f'M={M}: {len(F)} failing primes, all have explicit M^box certificates; max Dirichlet g = {gmax}')
        print('   min overflow Q1 over shots Q<=%d: ' % QMAX + ' '.join(f'{r[0]}:{r[3]}' for r in rows[:12]),
              '...' if len(rows) > 12 else '')
        print('   min self-mute cap e:  ' + ' '.join(f'{r[0]}:{r[4]}' for r in rows[:12]), '...' if len(rows) > 12 else '')
        hist = {}
        for r in rows:
            hist[r[4]] = hist.get(r[4], 0) + 1
        print('   histogram of min cap e (None = no self-mute shot with Q<=QMAX):', dict(sorted(hist.items(), key=str)))
    ex = dirichlet_cert(8, 131)
    print('example 8/131:', ex)
    # T1 control: odd squares k^2 coprime to M have no shot g | k^2 + M Q^2 with g = -1 (mod M), g prime
    bad = 0
    for M in (4, 8, 12, 16, 20, 24):
        for k in range(3, 120, 2):
            if gcd(k, M) > 1:
                continue
            n = k * k
            for Q in range(1, 40):
                if gcd(Q, k) > 1:
                    continue
                for g in divisors(n + M * Q * Q):
                    if (g + 1) % M == 0 and g > 1:
                        bad += 1
    print('T1 control (odd squares k<120, Q<40, all M): shots with g = -1 (mod M):', bad)
    print('total failing (M,p) certified in M^box:', tot)


if __name__ == '__main__':
    main()
