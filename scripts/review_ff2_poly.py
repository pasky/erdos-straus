"""R166 from-scratch F_p[T] arithmetic (p prime). Polys = tuples of ints, low degree first, no trailing zeros.
Written independently of scripts/ff2_polyq.py."""
from itertools import product

P_ = [3]


def setp(p):
    P_[0] = p


def tr(a):
    p = P_[0]
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def deg(a):
    return len(a) - 1  # deg 0 = -1


def add(a, b):
    n = max(len(a), len(b))
    return tr([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return tr([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return tr(r)


def scal(c, a):
    return tr([c * x for x in a])


def inv(c):
    return pow(c % P_[0], P_[0] - 2, P_[0])


def dm(a, b):
    """divmod"""
    p = P_[0]
    a = list(a)
    q = [0] * max(0, len(a) - len(b) + 1)
    ib = inv(b[-1])
    while len(a) >= len(b) and a:
        c = a[-1] * ib % p
        s = len(a) - len(b)
        q[s] = c
        for i, y in enumerate(b):
            a[s + i] = (a[s + i] - c * y) % p
        while a and a[-1] == 0:
            a.pop()
    return tr(q), tr(a)


def mod(a, b):
    return dm(a, b)[1]


def divides(d, a):
    return mod(a, d) == ()


def egcd(a, b):
    """returns g, s, t with s a + t b = g (g monic)"""
    r0, r1, s0, s1, t0, t1 = a, b, (1,), (), (), (1,)
    while r1:
        q, r = dm(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    c = inv(r0[-1])
    return scal(c, r0), scal(c, s0), scal(c, t0)


def invmod(a, m):
    g, s, _ = egcd(mod(a, m), m)
    assert g == (1,), "not invertible"
    return mod(s, m)


def Tpow(e):
    return tuple([0] * e + [1])


def monics(d):
    p = P_[0]
    for c in product(range(p), repeat=d):
        yield tuple(c) + (1,)


def monics_upto(d):
    for e in range(d + 1):
        yield from monics(e)


def crt(r1, m1, r2, m2):
    """x = r1 mod m1, x = r2 mod m2 (coprime); least rep mod m1 m2"""
    i = invmod(m1, m2)
    t = mod(mul(sub(r2, r1), i), m2)
    return mod(add(r1, mul(m1, t)), mul(m1, m2))


def monic_divisors(a):
    """all monic divisors of a (slow, brute force over monic polys of deg <= deg a)"""
    return [d for d in monics_upto(deg(a)) if divides(d, a)]
