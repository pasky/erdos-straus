"""O182 TWISTED_T1 §3: Eisenstein arithmetic + twisted Egyptian-fraction solver over Z[w], w = zeta_3.

Elements are pairs (a, b) = a + b w, w^2 = -1 - w.  Provides: mul, divexact, divmod (Euclidean), norm, gcd,
factorisation into primes (normalised representatives), divisors, tame cubic Hilbert symbol at a prime.
"""
from functools import lru_cache
import itertools
import math

ONE, ZERO, W = (1, 0), (0, 0), (0, 1)
UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]  # 1, w, w^2, -1, -w, -w^2
LAM = (1, -1)  # 1 - w


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])


def mul(x, y):
    a, b = x; c, d = y
    # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2 = (ac - bd) + (ad + bc - bd) w
    return (a * c - b * d, a * d + b * c - b * d)


def conj(x):  # w -> w^2 = -1 - w
    a, b = x
    return (a - b, -b)


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def divmod_(x, y):
    n = norm(y)
    num = mul(x, conj(y))
    q = ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))
    r = sub(x, mul(q, y))
    return q, r


def divexact(x, y):
    n = norm(y)
    num = mul(x, conj(y))
    if num[0] % n or num[1] % n:
        return None
    return (num[0] // n, num[1] // n)


def divides(y, x): return divexact(x, y) is not None


def gcd(x, y):
    while y != ZERO:
        _, r = divmod_(x, y)
        x, y = y, r
    return x


def power(x, k):
    r = ONE
    for _ in range(k):
        r = mul(r, x)
    return r


def factor_int(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def normalise(p):
    """canonical associate: the one with smallest (a, b) lexicographically among positive-ish choices."""
    return min((mul(u, p) for u in UNITS), key=lambda t: (t[0] < 0, -t[0], abs(t[1]), t[1]))


@lru_cache(None)
def split_prime(p):
    """for p = 1 mod 3: the two primes above p (normalised)."""
    for a in range(0, int(math.isqrt(4 * p)) + 2):
        for b in range(-a - 2, a + 3):
            if norm((a, b)) == p:
                pi = normalise((a, b))
                return (pi, normalise(conj(pi)))
    raise ValueError(p)


def primes_above(p):
    if p == 3:
        return [normalise(LAM)]
    if p % 3 == 2:
        return [(p, 0)]
    return list(split_prime(p))


def valuation(x, pi):
    v = 0
    while True:
        q = divexact(x, pi)
        if q is None:
            return v, x
        x = q
        v += 1


def factor(x):
    """returns (unit, {prime: exponent}) with x = unit * prod primes^e."""
    assert x != ZERO
    res = {}
    for p in factor_int(norm(x)):
        for pi in primes_above(p):
            v, x = valuation(x, pi)
            if v:
                res[pi] = v
    assert x in UNITS, x
    return x, res


def divisors(fac):
    items = list(fac.items())
    for exps in itertools.product(*[range(e + 1) for _, e in items]):
        d = ONE
        for (pi, _), e in zip(items, exps):
            d = mul(d, power(pi, e))
        yield d


# ---------- residue fields and the tame cubic symbol ----------
@lru_cache(None)
def residue_data(pi):
    """returns (q, red) where red maps an element (pi-adic unit, integral) to a canonical residue rep."""
    n = norm(pi)
    if pi[1] == 0 and n == pi[0] ** 2:  # inert rational prime p, residue field F_{p^2}
        p = pi[0]
        return n, ('inert', p, None)
    p = n
    # find r with w = r mod pi
    for r in range(p):
        if divides(pi, sub(W, (r, 0))):
            return n, ('split', p, r)
    raise ValueError(pi)


def reduce_(x, pi):
    q, (kind, p, r) = residue_data(pi)
    if kind == 'inert':
        return (x[0] % p, x[1] % p)
    return (x[0] + x[1] * r) % p


def rmul(a, b, pi):
    q, (kind, p, r) = residue_data(pi)
    if kind == 'inert':
        m = mul(a, b)
        return (m[0] % p, m[1] % p)
    return a * b % p


def rpow(a, k, pi):
    q, (kind, p, r) = residue_data(pi)
    res = (1, 0) if kind == 'inert' else 1
    while k:
        if k & 1:
            res = rmul(res, a, pi)
        a = rmul(a, a, pi)
        k >>= 1
    return res


def cubic_class(x, pi):
    """x an integral pi-adic unit; returns j in Z/3 with x^{(q-1)/3} = w^j mod pi."""
    q, (kind, p, r) = residue_data(pi)
    s = rpow(reduce_(x, pi), (q - 1) // 3, pi)
    for j in range(3):
        wj = power(W, j)
        if reduce_(wj, pi) == s:
            return j
    raise ValueError((x, pi, s))


def frac_val(num, den, pi):
    vn, num1 = valuation(num, pi)
    vd, den1 = valuation(den, pi)
    return vn - vd, num1, den1


def tame_symbol(a, b, pi):
    """a = (num, den), b = (num, den) in O x O; returns Z/3 class of the tame symbol {a,b}_pi (signs dropped)."""
    va, an, ad = frac_val(a[0], a[1], pi)
    vb, bn, bd = frac_val(b[0], b[1], pi)
    # a'^{vb} b'^{-va}, with a' = an/ad, b' = bn/bd units
    j = (vb * (cubic_class(an, pi) - cubic_class(ad, pi)) - va * (cubic_class(bn, pi) - cubic_class(bd, pi))) % 3
    return j


def quad_class(x, pi):
    """x integral pi-unit, pi odd: 0 if square mod pi, 1 otherwise."""
    q, (kind, p, r) = residue_data_any(pi)
    s = rpow_any(reduce_any(x, pi), (q - 1) // 2, pi)
    return 0 if s == one_any(pi) else 1


@lru_cache(None)
def residue_data_any(pi):
    if norm(pi) == 3:  # lambda: residue field F_3, w = 1
        return 3, ('split', 3, 1)
    return residue_data(pi)


def reduce_any(x, pi):
    q, (kind, p, r) = residue_data_any(pi)
    if kind == 'inert':
        return (x[0] % p, x[1] % p)
    return (x[0] + x[1] * r) % p


def one_any(pi):
    q, (kind, p, r) = residue_data_any(pi)
    return (1, 0) if kind == 'inert' else 1


def rpow_any(a, k, pi):
    q, (kind, p, r) = residue_data_any(pi)
    res = one_any(pi)
    while k:
        if k & 1:
            res = (lambda m: (m[0] % p, m[1] % p))(mul(res, a)) if kind == 'inert' else res * a % p
        a = (lambda m: (m[0] % p, m[1] % p))(mul(a, a)) if kind == 'inert' else a * a % p
        k >>= 1
    return res


def tame_symbol2(a, b, pi):
    """quadratic tame symbol at odd pi (incl. lambda), as 0/1, including the sign (-1)^{v(a)v(b)}."""
    va, an, ad = frac_val(a[0], a[1], pi)
    vb, bn, bd = frac_val(b[0], b[1], pi)
    j = vb * (quad_class(an, pi) + quad_class(ad, pi)) + va * (quad_class(bn, pi) + quad_class(bd, pi))
    j += va * vb * quad_class((-1, 0), pi)
    return j % 2
