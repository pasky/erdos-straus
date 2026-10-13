"""ff2_polyq.py (O166): minimal F_p[T] arithmetic (p prime), polys as lists low->high of ints mod p."""
def trim(a):
    while a and a[-1] == 0: a.pop()
    return a
def parse(s, p):  # high->low digits
    return trim([int(c) % p for c in reversed(s)])
def add(a, b, p):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])
def neg(a, p): return [(-x) % p for x in a]
def sub(a, b, p): return add(a, neg(b, p), p)
def mul(a, b, p):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return trim(r)
def divmod_(a, b, p):
    a = a[:]; inv = pow(b[-1], p - 2, p); q = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p; s = len(a) - len(b); q[s] = c
        for j, y in enumerate(b): a[s + j] = (a[s + j] - c * y) % p
        trim(a)
    return trim(q), a
def mod(a, b, p): return divmod_(a, b, p)[1]
def powmod(a, e, m, p):
    r = [1]; a = mod(a, m, p)
    while e:
        if e & 1: r = mod(mul(r, a, p), m, p)
        a = mod(mul(a, a, p), m, p); e >>= 1
    return r
def legendre(a, l, p):
    """quadratic character of a mod irreducible l (p odd)"""
    e = (p ** (len(l) - 1) - 1) // 2; r = powmod(a, e, l, p)
    if not r: return 0
    return 1 if r == [1] else -1
def deg(a): return len(a) - 1
