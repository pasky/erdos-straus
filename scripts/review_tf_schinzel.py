"""R194 from-scratch checks for TES_FINITE §5 (Schinzel m/n = 1/x + 1/y + 1/z, x, y, z in N).

Solver 1 (divisor): x <= y <= z  =>  n/m < x <= 3n/m;  A = m x - n > 0, B = n x;
  (A y - B)(A z - B) = B^2, d := A y - B in (0, B] (y <= z), d ≡ -B (mod A), y >= x.
Solver 2 (brute, small n only): for each x, y runs over (B/A, 2B/A], z = B y / (A y - B) tested.
Hilbert symbols over Q: own formulas (Serre, Cours d'arithmétique III.1.2).
"""
import sys, math
from fractions import Fraction as Fr


def factor_int(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def solve_div(m, n, first_only=False):
    sols = []
    fn = factor_int(n)
    for x in range(n // m + 1, 3 * n // m + 1):
        A = m * x - n
        if A <= 0:
            continue
        B = n * x
        f = dict(fn)
        for p, e in factor_int(x).items():
            f[p] = f.get(p, 0) + e
        f2 = {p: 2 * e for p, e in f.items()}
        for d in divisors_from(f2):
            if d > B or (d + B) % A:
                continue
            y = (d + B) // A
            if y < x:
                continue
            e2 = B * B // d
            if (e2 + B) % A:
                continue
            z = (e2 + B) // A
            assert Fr(m, n) == Fr(1, x) + Fr(1, y) + Fr(1, z)
            sols.append((x, y, z))
            if first_only:
                return sols
    return sorted(set(sols))


def solve_brute(m, n):
    sols = []
    for x in range(n // m + 1, 3 * n // m + 1):
        A, B = m * x - n, n * x
        if A <= 0:
            continue
        y = max(x, B // A + 1)
        while A * y <= 2 * B:
            den = A * y - B
            if den > 0 and (B * y) % den == 0:
                z = B * y // den
                if z >= y:
                    sols.append((x, y, z))
            y += 1
    return sorted(set(sols))


# ---------- Hilbert symbols over Q ----------
def vp(a, p):
    if a == 0:
        raise ValueError
    v = 0
    while a % p == 0:
        a //= p; v += 1
    return v


def hilbert_int(a, b, p):
    """(a, b)_p for non-zero integers a, b; p prime or 0 (= infinity). Returns ±1."""
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, be = vp(a, p), vp(b, p)
    u, v = a // p ** al, b // p ** be
    if p != 2:
        leg = lambda t: 1 if pow(t % p, (p - 1) // 2, p) == 1 else -1
        s = (-1) ** (al * be * ((p - 1) // 2))
        return s * leg(u) ** be * leg(v) ** al
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    e = (eps(u) * eps(v) + al * om(v) + be * om(u)) % 2
    return -1 if e else 1


def hilbert(a, b, p):
    """a, b non-zero Fractions."""
    a, b = Fr(a), Fr(b)
    # (a, b) = (num_a * den_a, num_b * den_b) since den^2 is a square
    return hilbert_int(a.numerator * a.denominator, b.numerator * b.denominator, p)


def alpha(u, p):
    u1, u2, u3 = map(Fr, u)
    return hilbert(-u1 / u3, -u2 / u3, p)


def primes_of(*vals):
    s = set()
    for v in vals:
        v = Fr(v)
        for t in (abs(v.numerator), v.denominator):
            if t > 1:
                s |= set(factor_int(t))
    return s


def is_prime(n):
    return n > 1 and factor_int(n) == {n: 1}
