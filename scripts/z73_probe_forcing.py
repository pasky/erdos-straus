"""Exact small screens and counterexamples for the composite-shift steering note.
Run from the root: uv run --with sympy python scripts/z73_probe_forcing.py
"""
from math import gcd
from pathlib import Path

from sympy import divisors, factorint, isprime, jacobi_symbol, n_order, primerange, totient


def verify(n, a, b, c):
    assert min(a, b, c) > 0 and gcd(a, b) == 1 and len(factorint(a*b)) <= 2
    assert (n+c) % (4*a*b) == (a+b) % c == 0
    d, e = (n+c)//(4*a*b), (a+b)//c
    x, y, z = a*b*d, n*a*d*e, n*b*d*e
    assert 4*x*y*z == n*(x*y+x*z+y*z)


def line(n, e):
    N = e*n+1
    return [b for b in divisors(N) if N//b % (4*e) == 4*e-1 and (1+b) % e == 0]


def orbit(n, c):
    k = (n+c)//4
    if jacobi_symbol(n, c) != -1:
        return False
    h = int(n_order(2, c))
    if h != totient(c)//2 or k % (1 << (h//2)):
        return False
    neg = [q for q in factorint(k) if jacobi_symbol(q, c) == -1]
    assert neg
    for q in neg:
        j = next(j for j in range(-(h//2), h//2+1) if (q+pow(2, j, c)) % c == 0)
        verify(n, 1 << max(j, 0), q << max(-j, 0), c)
    return True


def a1(n):
    return [(c, b) for c in range(3, (n+4)//3+1, 4)
            for b in divisors((n+c)//4) if (1+b) % c == 0]


def anchored(n, q):
    """All two-support certificates with q|AB; output unordered splits."""
    out = []
    for k in range(q, (n+1)//3+1, q):
        f = factorint(k)
        if len(f) > 2:
            continue
        z = q**f[q]
        for a, b in {(1, k), (k//z, z)}:
            c = -n % (4*k)
            if c and (a+b) % c == 0:
                verify(n, a, b, c)
                out.append((a, b, c))
    return out


def screens(n):
    if n % 8 == 5:
        verify(n, 1, 2, 3)
        return [True, False, False, False, False]
    assert n % 8 == 1
    q = next((q for q in factorint((n+1)//2) if q % 4 == 3), None)
    if q:
        verify(n, 1, 2*q, 2*q+1)
    result = [bool(q)]
    for e in (2, 4, 5):
        bs = [b for b in line(n, e) if len(factorint(b)) <= 2]
        for b in bs:
            verify(n, 1, b, (1+b)//e)
        result.append(bool(bs))
    q = next((q for q in factorint(n+2) if q % 8 == 5), None)
    if q:
        verify(n, 2, q, q+2)
    return result + [bool(q)]


if __name__ == '__main__':
    tests = {'odd squares': [i*i for i in range(1, 100, 2)]}
    for f in sorted(Path('data/z58/screens').glob('*.txt')):
        tests[f.stem] = [int(x.split()[0]) for x in f.read_text().splitlines()
                         if x and not x.startswith('#')]
    for title, ns in tests.items():
        vals = [screens(n) for n in ns]
        print(title, len(ns), [sum(map(int, col)) for col in zip(*vals)], sum(map(any, vals)))
    for c in [7, 15, 23, 39]:
        assert any([orbit(n, c) for n in range(1, 3000, 8)])
    assert orbit(23317201, 7) and orbit(193, 15) and not orbit(1201, 39)
    assert [p for p in primerange(1, 194) if p % 8 == 1 and not a1(p)] == [193]
    assert line(1201, 4) == [155] and line(313, 4) == []
    for s in (31, 959, 2911):
        assert s % 16 == 15
        p = (5*s*s-1)//4
        u, v = (5*s-1)//2, (5*s+1)//4
        assert isprime(p) and 5*p+1 == 2*u*v
        print(s, p, factorint((p+1)//2), factorint(u), factorint(v), line(p, 4), line(p, 5))
    assert screens(1149601)[1:4] == [False, False, True]
    assert not any(screens(10592401))
    assert not anchored(10592401, 383)
    verify(10592401, 19, 27, 23)
    p = 23317201
    assert isprime(p) and isprime((p+1)//2)
    s = 4319
    assert 4*p+1 == 5*s*s
    for w, q in [(s, 7), ((5*s-1)//2, 59), ((5*s+1)//4, 5399)]:
        assert [r for r in factorint(w) if pow(r, (p-1)//2, p) == p-1] == [q]
        assert not anchored(p, q)
    verify(p, 1, 62, 7)
    for s in range(15, 40000, 16):
        f = factorint(s)
        fail = (all(q % 16 in {1, 5, 7, 9} for q in f) and 5 not in f and
                all(a == 1 for q, a in f.items() if q % 16 == 5))
        actual = min(len(factorint(b)) for b in divisors(5*s*s) if b % 16 == 11)
        assert actual <= 3 and (actual == 3) == fail
