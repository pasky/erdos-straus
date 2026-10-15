# z8_numerators.py — sign fields for numerators nu: test of SIGN_FIELDS §2.
# Words of n: (t,u,v) >= 1 with tuv - u - v = n; A = tu-1, A* = tv-1.  nu-word: nu divides one of t,u,v,A,A*
# (gives nu/n = 1/x+1/y+1/z, e.g. nu | u = nu w: nu/n = 1/(w A*) + 1/(t n w) + 1/(t n w A*)).
# Checks: (1) every nu-word gives an explicit nu/n decomposition (exact); (2) "coprime u-side" classification:
# if gcd(nu, u) = gcd(nu, A) = 1 and nu does not divide n+u, then nu-word <=> A = -1 (mod nu) or A = -(n+u)/n (mod nu);
# (3) T1: count nu-words at odd squares; classify each by (slot, coprime?, sqrt(-u) in Q(zeta_{nu u})?).
# Usage: PYTHONPATH=scripts uv run python scripts/z8_numerators.py NMAX_PRIME MSQ nu1 nu2 ...
import sys
from fractions import Fraction as Fr
from math import gcd
from sympy import isprime, factorint

NP, MSQ = int(sys.argv[1]), int(sys.argv[2])
nus = [int(x) for x in sys.argv[3:]]


def words(n):
    for t in range(1, n + 3):  # (R236 repair: t = n + 2 gives the word (n + 2, 1, 1))
        N = t * n + 1
        # divisors A of N with A = -1 mod t, A >= t-1 (u >= 1 ... u = (A+1)/t)
        for A in range(t - 1 if t > 1 else 1, int(N ** .5) + 1, t if t > 1 else 1):
            if A > 0 and N % A == 0:
                for a in {A, N // A}:
                    if (a + 1) % t == 0:
                        b = N // a
                        if (b + 1) % t == 0:
                            u, v = (a + 1) // t, (b + 1) // t
                            if u >= 1 and v >= 1 and u <= v:
                                yield (t, u, v)


def disc_divides(u, M):  # sqrt(-u) in Q(zeta_M) <=> disc(Q(sqrt(-u))) | M
    f = factorint(u); d = 1
    for q, e in f.items():
        if e % 2: d *= q
    D = -d
    if D % 4 != 1: D *= 4  # D = -d if -d = 1 mod 4 else -4d
    return M % abs(D) == 0


def sol(nu, n, t, u, v):
    A, As = t * u - 1, t * v - 1
    for X, (p, q, Y) in [(u, (t, v, As)), (v, (t, u, A)), (A, (t, u, As)), (As, (t, v, A))]:
        if X % nu == 0:
            w = X // nu
            if X in (u, v):  # nu/n = 1/(w Y) + 1/(t n w) + 1/(t n w Y)
                return (w * Y, t * n * w, t * n * w * Y)
            # X = A (or A*): nu/n = 1/(w v') + 1/(w v' Y') + 1/(n w Y'), Y' the other of A, A*, v' its partner
            other_v = v if X == A else u
            Yp = As if X == A else A
            return (w * other_v, w * other_v * Yp, n * w * Yp)
    if t % nu == 0:
        return 'T'
    return None


stats = {}
for kind, ns in [('prime', [p for p in range(5, NP) if isprime(p)]), ('square', [m * m for m in range(3, MSQ, 2)])]:
    for n in ns:
        for (t, u, v) in words(n):
            A, As = t * u - 1, t * v - 1
            for nu in nus:
                hit = [nm for nm, X in zip('tuvAB', (t, u, v, A, As)) if X % nu == 0]
                s = sol(nu, n, t, u, v) if hit else None
                if s not in (None, 'T'):
                    x, y, z = s
                    assert Fr(nu, n) == Fr(1, x) + Fr(1, y) + Fr(1, z), (nu, n, t, u, v)
                if gcd(nu, u) == 1 and gcd(nu, A) == 1 and (n + u) % nu and gcd(n, nu) == 1:
                    pred = (A + 1) % nu == 0 or (A * n + n + u) % nu == 0
                    assert pred == bool(hit), ('coprime classification', nu, n, t, u, v, hit)
                if kind == 'square' and hit:
                    cop = gcd(nu, u) == 1 and gcd(nu, A) == 1 and (n + u) % nu != 0
                    key = (nu, ''.join(hit), cop, disc_divides(u, nu * u), 'Aodd' if A % 2 else 'Aeven',
                           'psi(-1)' if (A + 1) % (nu * u) == 0 else 'other')
                    stats[key] = stats.get(key, 0) + 1
                if kind == 'prime' and hit:
                    stats[(nu, 'prime-words')] = stats.get((nu, 'prime-words'), 0) + 1
for key in sorted(stats, key=str):
    print(key, stats[key])
