"""zt_poly.py (O227): minimal dense polynomial arithmetic over F_p (coefficient lists, low degree first)."""
P = 3


def norm(a):
    a = [x % P for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return norm([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return norm(r)


def divmod_(a, b):
    a = norm(a)
    b = norm(b)
    assert b
    inv = pow(b[-1], P - 2, P)
    q = [0] * max(0, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b):
        f = r[-1] * inv % P
        s = len(r) - len(b)
        q[s] = f
        for i, y in enumerate(b):
            r[s + i] -= f * y
        r = norm(r)
    return norm(q), r


def mono(k, c=1):
    return norm([0] * k + [c])


def deg(a):
    return len(a) - 1


def tval(a):
    """T-adic valuation (inf for 0)."""
    for i, x in enumerate(a):
        if x % P:
            return i
    return 10 ** 9


def sinv(a, n):
    """power-series inverse of a mod T^n (a(0) != 0)."""
    a0i = pow(a[0], P - 2, P)
    r = [0] * n
    for i in range(n):
        s = sum(a[j] * r[i - j] for j in range(1, min(i, len(a) - 1) + 1))
        r[i] = ((1 if i == 0 else 0) - s) * a0i % P
    return norm(r)


def trunc(a, n):
    return norm(a[:n])
