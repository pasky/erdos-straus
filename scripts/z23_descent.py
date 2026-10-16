"""O251 (LATTICE_MEETING §4): a DETERMINISTIC class-group descent and its hit rate.
Start: least admissible window q0 (prime = 3 mod 4, (q0/p) = -1), least root Q of p + 4Q^2 = 0 (mod q0), slice
g0 = (p + 4Q^2)/q0 (ASTRA_BRIDGE Thm 3.1(b)); for each k | h0 = (g0+1)/4 (k <= KM) the Claude point (2k, Y), Y the least
|height| on the line, i.e. the form [g0, 2Y, D] of disc -16 k^2 p.  Descent = Gauss reduction of that form (fixed class).
Along the path record: forms whose first coefficient a is a Claude slice for line k (a = -1 mod 4k), the least such
|Y| (cap descent), and ES hits on line k (a | 4k^2 p + d for some d | k, a = -1 mod 4k; Thm 1.4/Cor 1.5).
Baseline: the same statistics for a uniformly random Claude slice of comparable size is NOT simulated; we compare the
admissible-slice frequency along paths with 1/#{classes mod 4k of squares-times(-1)} heuristics (printed raw).
Usage: z23_descent.py P KM
"""
import sys
from math import gcd
from sympy import primerange, divisors, isprime, legendre_symbol


def reduce_path(a, b, c):
    """Gauss reduction of positive definite [a, b, c]; yield every form visited (a, b, c)."""
    path = [(a, b, c)]
    while True:
        if not (-a < b <= a):  # translate b into (-a, a]
            t = (a - b) // (2 * a)
            b2 = b + 2 * a * t
            c = (b2 * b2 - (b * b - 4 * a * c)) // (4 * a)
            b = b2
            path.append((a, b, c))
        if a > c or (a == c and b < 0):
            a, b, c = c, -b, a
            path.append((a, b, c))
            continue
        return path


P, KM = int(sys.argv[1]), int(sys.argv[2])
st = dict(primes=0, lines=0, forms=0, adm=0, es_hits=0, es_at_start=0, ydrop=0, primes_hit=0)
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    q0 = next(q for q in range(3, 10**6, 4) if isprime(q) and legendre_symbol(p % q, q) == -1)
    Q = next(Q for Q in range(1, q0) if (p + 4 * Q * Q) % q0 == 0)
    g0 = (p + 4 * Q * Q) // q0
    if g0 % 4 != 3 or gcd(g0, p) != 1:
        continue
    st['primes'] += 1
    h0, rho = (g0 + 1) // 4, (2 * Q) % g0
    hit_p = False
    for k in divisors(h0):
        if k > KM:
            break
        Y = (2 * k * rho) % g0
        if Y > g0 // 2:
            Y -= g0
        if Y % 2 == 0 or gcd(abs(Y), 2 * k) != 1:
            continue
        st['lines'] += 1
        D = (4 * k * k * p + Y * Y) // g0
        assert g0 * D == 4 * k * k * p + Y * Y
        ymin_adm = abs(Y)
        for idx, (a, b, c) in enumerate(reduce_path(g0, 2 * Y, D)):
            st['forms'] += 1
            if a % (4 * k) != 4 * k - 1:
                continue
            st['adm'] += 1
            ymin_adm = min(ymin_adm, abs(b) // 2)
            if any((4 * k * k * p + d) % a == 0 for d in divisors(k)):
                st['es_hits'] += 1
                st['es_at_start'] += idx == 0
                hit_p = True
        st['ydrop'] += ymin_adm < abs(Y)
    st['primes_hit'] += hit_p
print(st)
