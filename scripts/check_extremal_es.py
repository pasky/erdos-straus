"""Exact certificates for EXTREMAL_ES.md. Run with uv run --no-sync python."""
from collections import defaultdict, deque
from fractions import Fraction as Q
from math import ceil, floor


def gap(n, u):
    x, y, z = u
    return abs(Q(4, n) - Q(1, x) - Q(1, y) - Q(1, z))


def band(n, e, strict=False):
    """Sorted triples at error <= e (or < e); reject every infinite-fibre case."""
    out = set()
    r = Q(4, n)
    assert 0 <= e < r
    for x in range(1, floor(3 / (r - e)) + 1):
        a = r - Q(1, x)
        if a <= -e:
            continue
        assert a > e  # else this enumeration cannot certify the band
        for y in range(x, floor(2 / (a - e)) + 1):
            b = a - Q(1, y)
            if b <= -e:
                continue
            assert b > e
            for z in range(max(y, ceil(1 / (b + e))), floor(1 / (b - e)) + 1):
                u = x, y, z
                if not strict or gap(n, u) < e:
                    out.add(u)
    return out


def reaches(vertices, start, ends):
    by_den = defaultdict(list)
    for u in vertices:
        for v in set(u):
            by_den[v].append(u)
    seen = {start}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u in ends:
            return True
        for v in u:
            for w in by_den.pop(v, ()):
                if w not in seen:
                    seen.add(w)
                    queue.append(w)
    return False


def first_trap():
    for n in range(2, 74):
        # Exact one/two terms: appending a denominator tending to infinity
        # (split one term first if needed) precludes a closest nonexact triple.
        if n % 2 == 0 or any(n % d == 0 for d in range(3, n + 1, 4)):
            continue
        x = (n + 3) // 4
        y = n*x // (4*x-n) + 1
        z = n*x*y // ((4*x-n)*y-n*x) + 1
        near = x, y, z
        vertices = band(n, gap(n, near))
        exact = {u for u in vertices if gap(n, u) == 0}
        best = min(gap(n, u) for u in vertices - exact)
        opt = {u for u in vertices if gap(n, u) == best}
        assert opt == {near}
        repair = any(set(near) & set(u) for u in exact)
        print(n, near, 'repair' if repair else 'TRAP')
        assert repair == (n < 73)
    return near, exact


def square_divisors(b):
    v, p, ds = b, 2, [1]
    while p*p <= v:
        k = 0
        while v % p == 0:
            k += 1
            v //= p
        if k:
            ds = [d * p**i for d in ds for i in range(2*k + 1)]
        p += 1
    return ds if v == 1 else [d * v**i for d in ds for i in range(3)]


def gates(n):
    x = (n+3)//4
    y = (n*x+2)//3
    return (any(d % 3 == 2 for d in square_divisors(n*x)),
            any(d % (4*y-n) == 2 for d in square_divisors(n*y)))


def integer_band(n, h):
    assert 0 <= h < n
    out = set()
    for x in range(n//4 + 1, (3*n+h)//4 + 1):
        a, b = 4*x-n, n*x
        for y in range(max(x, b//a + 1), (2*b+h)//a + 1):
            s, t = a*y-b, b*y
            for z in range(max(y, (t-h+s-1)//s), (t+h)//s + 1):
                out.add((x, y, z))
    return out


if __name__ == '__main__':
    start, exact = first_trap()
    route = [start, (19,514,4599), (20,351,514), (20,210,30660)]
    assert route[-1] in exact
    assert all(set(u) & set(v) for u, v in zip(route, route[1:]))
    h = max(gap(73, u) for u in route)
    assert h == Q(1, 44913834)
    vertices = band(73, h, strict=True)
    assert start in vertices and exact <= vertices and not reaches(vertices, start, exact)
    print('p=73 strict band size:', len(vertices), 'barrier / optimum:', h/gap(73, start))
    for n, expected in [(25,(True,False)), (73,(False,False)), (409,(False,False)),
                        (577,(True,False)), (2521,(False,False))]:
        assert gates(n) == expected
    p = 10156800001  # listed R8 zero; test the X gate for 4/p only
    assert p % 24 == 1 and len(square_divisors(p)) == 3
    assert all(d % 3 == 1 for d in square_divisors((p+3)//4))
    for n in range(2, 18):
        exact = integer_band(n, 0)
        vertices = integer_band(n, 1)
        trapped = {u for u in vertices - exact if not reaches(vertices, u, exact)}
        assert trapped == ({(7,11,654), (7,11,655)} if n == 17 else set())
    exact = integer_band(17, 0)
    assert not reaches(integer_band(17, 2), (7,11,655), exact)
    assert (9,11,30) in integer_band(17, 3) and (5,30,510) in exact
    print('All certificates passed.')
