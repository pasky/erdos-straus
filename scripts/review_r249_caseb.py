"""R249 from-scratch Case B tuple enumerator over F_q[T] (q odd prime), k = 2.

Case B tuple (DEPTH_ASPECT (B)): monic m', g', w = T w1, C = T C1 with
  m' w1 C1 = T^{s-2} + v1,  w1 + C1 = T g' v1,  T not| m' g' w1 C1, v1 != 0.
Route used (re-derived): E = T m' g' w1 - 1 and E*C1 = g' T^{s-1} + w1.
Enumerate a <= b (a = deg w = 1 + deg w1) only, add the swap (w1 <-> C1).
Degree pruning uses only v1 != 0: deg(w1 + C1) = 1 + y + deg v1 <= max(a,b) - 1.
Also a brute-force mode over (m', w1, C1) (no pruning beyond a+b+z = s) for validation.

Polys: tuples of ints mod q, low -> high, no trailing zeros.
"""
import itertools, sys

Q = 3


def trim(p):
    p = list(p)
    while p and p[-1] % Q == 0:
        p.pop()
    return tuple(x % Q for x in p)


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return tuple((-x) % Q for x in a)


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
    return trim(r)


def divmod_(a, b):
    a = list(a)
    db = len(b) - 1
    inv = pow(b[-1], Q - 2, Q)
    if len(a) <= db:
        return (), trim(a)
    qq = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] % Q
        if c:
            f = c * inv % Q
            qq[i - db] = f
            for j in range(db + 1):
                a[i - db + j] -= f * b[j]
    return trim(qq), trim(a[:db])


def Tpow(n):
    return tuple([0] * n + [1])


def monic_unitT(d):
    """monic polys of degree d with nonzero constant term"""
    if d == 0:
        yield (1,)
        return
    for c0 in range(1, Q):
        for mid in itertools.product(range(Q), repeat=d - 1):
            yield (c0,) + mid + (1,)


def monic_all(d):
    for mid in itertools.product(range(Q), repeat=d):
        yield tuple(mid) + (1,)


def check_tuple(s, m, g, w1, C1):
    """return v1 if (m,g,w1,C1) is a Case B tuple of parameter s else None"""
    if m[0] == 0 or g[0] == 0 or w1[0] == 0 or C1[0] == 0:
        return None
    if m[-1] != 1 or g[-1] != 1 or w1[-1] != 1 or C1[-1] != 1:
        return None
    v1 = sub(mul(mul(m, w1), C1), Tpow(s - 2))
    if not v1:
        return None
    if add(w1, C1) != mul(mul((0, 1), g), v1):
        return None
    return v1


def tuples_T0(s):
    """all Case B tuples of parameter s (both orientations)"""
    out = []
    for z in range(0, s):
        for a in range(1, s):
            b = s - a - z
            if b < a:
                continue
            for y in range(0, b - 1):  # y <= b - 2
                for m in monic_unitT(z):
                    for g in monic_unitT(y):
                        L = mul(m, g)
                        for w1 in monic_unitT(a - 1):
                            E = sub(mul((0, 1), mul(L, w1)), (1,))
                            num = add(mul(g, Tpow(s - 1)), w1)
                            C1, r = divmod_(num, E)
                            if r or not C1:
                                continue
                            if len(C1) - 1 != b - 1:
                                continue
                            v1 = check_tuple(s, m, g, w1, C1)
                            if v1 is None:
                                continue
                            out.append((m, g, w1, C1))
                            if a < b or w1 != C1:
                                out.append((m, g, C1, w1))
    return sorted(set(out))


def tuples_brute(s):
    """brute force over (m', w1, C1) with a + b + z = s; g' derived."""
    out = []
    for z in range(0, s):
        for a in range(1, s):
            b = s - a - z
            if b < 1:
                continue
            for m in monic_unitT(z):
                for w1 in monic_unitT(a - 1):
                    for C1 in monic_unitT(b - 1):
                        v1 = sub(mul(mul(m, w1), C1), Tpow(s - 2))
                        if not v1:
                            continue
                        den = mul((0, 1), v1)
                        g, r = divmod_(add(w1, C1), den)
                        if r or not g or g[-1] != 1 or g[0] == 0:
                            continue
                        out.append((m, g, w1, C1))
    return sorted(set(out))


def E_of(m, g, w1):
    return sub(mul((0, 1), mul(mul(m, g), w1)), (1,))


if __name__ == "__main__":
    S = int(sys.argv[1])
    for s in range(3, S + 1):
        A = tuples_T0(s)
        if s <= int(sys.argv[2]) if len(sys.argv) > 2 else False:
            B = tuples_brute(s)
            print(s, len(A), len(B), A == B)
        else:
            print(s, len(A))
