"""zi_lib.py (O244): minimal F_p[T] arithmetic, p prime. Polys = tuples/lists low->high, ints mod p, trimmed."""
import itertools


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])


def neg(a, p):
    return [(-x) % p for x in a]


def sub(a, b, p):
    return add(a, neg(b, p), p)


def scal(c, a, p):
    return trim([(c * x) % p for x in a])


def mul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return trim(r)


def divmod_(a, b, p):
    a = list(a)
    b = trim(b)
    assert b, "division by zero"
    inv = pow(b[-1], p - 2, p)
    q = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p
        s = len(a) - len(b)
        q[s] = c
        for j, y in enumerate(b):
            a[s + j] = (a[s + j] - c * y) % p
        a = trim(a)
    return trim(q), a


def mod(a, b, p):
    return divmod_(a, b, p)[1]


def exact(a, b, p):
    q, r = divmod_(a, b, p)
    return q if not r else None


def gcd(a, b, p):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, mod(a, b, p)
    if a:
        a = scal(pow(a[-1], p - 2, p), a, p)
    return a


def deg(a):
    return len(a) - 1


def lc(a):
    return a[-1]


def T(n):
    return [0] * n + [1]


def val_T(a):
    v = 0
    while v < len(a) and a[v] == 0:
        v += 1
    return v


def tfree(a):
    return list(a[val_T(a):])


def monics(d, p):
    for co in itertools.product(range(p), repeat=d):
        yield list(co) + [1]


def polys(d, p):
    """all polys of exact degree d (any lc)"""
    for c in range(1, p):
        for co in itertools.product(range(p), repeat=d):
            yield list(co) + [c]


def is_irred(f, p):
    """Rabin-free simple test: no monic factor of degree <= deg/2 (small degrees only)."""
    n = deg(f)
    if n <= 0:
        return False
    for d in range(1, n // 2 + 1):
        for g in monics(d, p):
            if not mod(f, g, p):
                return False
    return True


def inv_mod_Tn(u, n, p):
    """inverse of power series u (u[0] != 0) mod T^n"""
    u = list(u) + [0] * n
    r = [0] * n
    i0 = pow(u[0], p - 2, p)
    r[0] = i0
    for m in range(1, n):
        s = sum(u[j] * r[m - j] for j in range(1, m + 1)) % p
        r[m] = (-s * i0) % p
    return r


def trunc(a, n):
    a = list(a) + [0] * n
    return a[:n]


def show(a):
    return "".join(map(str, reversed(a))) if a else "0"
