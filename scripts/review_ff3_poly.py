"""review_ff3_poly.py (R173): minimal from-scratch F_p[T] arithmetic (p odd prime).
Polynomials are lists of ints in [0, p), low -> high, normalized (no trailing zeros; zero = [])."""

P = 3


def setp(p):
    global P
    P = p


def norm(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    p = P
    if len(a) < len(b):
        a, b = b, a
    r = list(a)
    for i, x in enumerate(b):
        r[i] = (r[i] + x) % p
    return norm(r)


def neg(a):
    p = P
    return [(-x) % p for x in a]


def sub(a, b):
    return add(a, neg(b))


def scal(a, c):
    p = P
    c %= p
    if c == 0:
        return []
    return [(x * c) % p for x in a]


def mul(a, b):
    if not a or not b:
        return []
    p = P
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return norm([x % p for x in r])


def inv(c):
    return pow(c % P, P - 2, P)


def divmod_(a, b):
    """a = q b + r, deg r < deg b."""
    p = P
    if not b:
        raise ZeroDivisionError
    r = list(a)
    db = len(b) - 1
    il = inv(b[-1])
    q = [0] * max(len(a) - db, 0)
    while len(r) - 1 >= db and r:
        f = (r[-1] * il) % p
        s = len(r) - 1 - db
        q[s] = f
        for i, y in enumerate(b):
            r[s + i] = (r[s + i] - f * y) % p
        norm(r)
    return norm(q), r


def mod(a, b):
    p = P
    r = list(a)
    db = len(b) - 1
    il = inv(b[-1])
    while r and len(r) - 1 >= db:
        f = (r[-1] * il) % p
        s = len(r) - 1 - db
        for i, y in enumerate(b):
            r[s + i] = (r[s + i] - f * y) % p
        norm(r)
    return r


def trunc(a, n):
    return norm(list(a[:n]))


def series_inv(a, n):
    """1/a mod T^n, a(0) != 0."""
    p = P
    a0i = inv(a[0])
    r = [0] * n
    for i in range(n):
        s = 1 if i == 0 else 0
        for j in range(1, min(i, len(a) - 1) + 1):
            s -= a[j] * r[i - j]
        r[i] = (s * a0i) % p
    return norm(r)


def monic(a):
    return bool(a) and a[-1] == 1


def deg(a):
    return len(a) - 1


def Tpow(n):
    return [0] * n + [1]


def all_monic(d):
    """all monic polys of degree d."""
    p = P
    for idx in range(p ** d):
        c = []
        x = idx
        for _ in range(d):
            c.append(x % p)
            x //= p
        yield c + [1]


_irr_cache = {}


def irreducibles(dmax):
    """monic irreducibles of degree 1..dmax, by trial division by smaller irreducibles."""
    key = (P, dmax)
    if key in _irr_cache:
        return _irr_cache[key]
    irr = []
    for d in range(1, dmax + 1):
        for f in all_monic(d):
            ok = True
            for g in irr:
                if 2 * (len(g) - 1) > d:
                    break
                if not mod(f, g):
                    ok = False
                    break
            if ok:
                irr.append(f)
    _irr_cache[key] = irr
    return irr


def factor(a):
    """monic a -> list of (irreducible, exponent), by trial division."""
    assert monic(a)
    res = []
    r = list(a)
    dmax = max(1, (len(r) - 1) // 2)
    for f in irreducibles(dmax):
        if len(r) - 1 < 2 * (len(f) - 1):
            break
        e = 0
        while True:
            qq, rr = divmod_(r, f)
            if rr:
                break
            r = qq
            e += 1
        if e:
            res.append((f, e))
    if len(r) > 1:
        res.append((r, 1))
    return res


def divisors(a):
    """all monic divisors of monic a."""
    divs = [[1]]
    for f, e in factor(a):
        new = []
        for d in divs:
            x = d
            for _ in range(e + 1):
                new.append(x)
                x = mul(x, f)
        divs = new
    return divs
