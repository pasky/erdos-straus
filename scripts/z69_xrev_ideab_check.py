#!/usr/bin/env python3
"""Bounded review replay. Run from an archive of side-agent/z69-ideab.
Requires numpy/sympy. Builds <=10000 class table; sieve comparison <=1e8.
Independent per-modulus parameter tests also recover actual ES triples.
"""
import importlib.util
import json
import math
from pathlib import Path
import sys
from sympy import divisors, isprime, primerange

sys.set_int_max_str_digits(10000)

def load(name):
    spec = importlib.util.spec_from_file_location(name, f"scripts/z69_ideab_{name}.py")
    mod = importlib.util.module_from_spec(spec)
    saved = sys.argv
    sys.argv = [name, "1e8", "10000", "1", "2", "6"]
    spec.loader.exec_module(mod)
    sys.argv = saved
    return mod

o2 = load("o2")
check = load("o2_check")
cls = o2.build(10000)
mods = sorted(cls)
assert sum(map(len, cls.values())) == 173664

def tab(n):
    return next((m for m in mods if n % m in cls[m]), 10001)

def parameters(n, m):
    """Independent modulus-first tests, no CRT or modular inverses."""
    if m % 4 == 3:
        k = (m + 1) // 4
        for a in divisors(k):
            for d in divisors(k // a):
                if (n + 4*a*a*d) % m == 0:
                    c = k // (a*d)
                    yield 2, a, (n*c+a)//m, c, d
    if m % 4:
        return
    k = m // 4
    for a in divisors(k):
        d = k // a
        for f in divisors(4*a*a*d+1):
            if (n+f) % m == 0:
                c = (n+f)//m
                yield 1, a, (n*a+c)//f, c, d
        b = d
        for e in divisors(a+b):
            c = (a+b)//e
            if (n+e) % m == 0:
                yield 2, a, b, c, (n+e)//m
            if (n*e+1) % m == 0:
                yield 1, a, b, c, (n*e+1)//m
    for f in divisors(k):
        base = m // f
        if f % 4 != 3 or math.gcd(base, f) != 1 or (n+f) % base:
            continue
        for u in divisors(base//4):
            v = base//(4*u)
            if (n*u+v) % f == 0:
                yield 1, u, (n*u+v)//f, v, (n+f)//base
            if (n*n+4*u*u*v) % f == 0:
                a = (n+f)//base
                yield 1, a, (n*a+u)//f, u, v
            if (n+4*u*u*v) % f == 0:
                b = (n+f)//base
                yield 2, u, b, (u+b)//f, v

def independent(n, limit, recover=False):
    for m in range(3, limit+1):
        for typ, a, b, c, d in parameters(n, m):
            assert min(a,b,c,d) > 0
            if recover:
                x,y,z = (a*b*d, a*c*d*n, b*c*d*n) if typ == 2 else (b*c*d, a*c*d, a*b*d*n)
                assert 4*x*y*z == n*(x*y+x*z+y*z)
            return m
    return limit+1

arch = {}
for filename in ("o2_X1e+12_M10000_r1.json", "o2_X1e+12_M10000_r2-6.json"):
    arch.update(json.loads(Path("data/z69/ideab", filename).read_text()))
records = 0
for r, data in sorted(arch.items()):
    for p, expected in data["records"]:
        assert isprime(p) and p % 840 == 1 and p % 11 == int(r)
        assert tab(p) == check.direct_lambda(p, expected) == independent(p, expected, True) == expected
        records += 1
    decades = {row[0]: row[2] for row in data["decades"]}
    print("A", r, [decades[e] for e in (10,11,12)], flush=True)
print("record checks + recovered positive ES triples", records, flush=True)

# Independently sieve the full interval, then compare each progression.
expected = {r: [] for r in (1,2,6)}
for p in primerange(2, 10**8+1):
    if p % 840 == 1 and p % 11 in expected:
        expected[p % 11].append(p)
for r in (1,2,6):
    n0 = next(1+840*t for t in range(11) if (1+840*t) % 11 == r)
    actual = o2.primes_in_class(n0, 9240, 10**8).tolist()
    assert actual == expected[r]
    values = [tab(p) for p in actual]
    decade = next(row for row in arch[str(r)]["decades"] if row[0] == 8)
    assert len(actual) == decade[1] and max(values) == decade[2]
    assert abs(sum(values)/len(values)-decade[3]) < 1e-12
    print("census <=1e8", r, len(actual), max(values), flush=True)

for r in (2,6):
    data = json.loads(Path(f"data/z69/ideab/cert_M10000_r{r}.json").read_text())
    n = int(data["n"])
    assert n % 840 == 1 and n % 11 == r
    assert all(n % p for p in primerange(2,10001))
    assert tab(n) == check.direct_lambda(n,10000) == independent(n,10000) == 10001
    print("certificate", r, "unit; zero hits; mod13", n % 13, flush=True)

assert all(tab(i*i) == 10001 for i in range(1,200,2))
for filename, count, bound in (("r8_zeros_1e10.txt",12,248), ("composite_zeros_le8e6.txt",285,548), ("star_prime_zeros.txt",14,239), ("gstar_zeros.txt",38,239)):
    nums = [int(line.split()[0]) for line in Path("data/z58/screens", filename).read_text().splitlines() if line and not line.startswith("#")]
    assert len(nums) == count
    values = [tab(n) for n in nums]
    assert max(values) == bound
    print("screen", filename, count, "max lambda", max(values), flush=True)

# Z67 coverings and the refuted two-prime point are compatible with z69.
a,d,e = 8,33,11999
r = -4*a*a*d-e
assert r == -20447 and 4*a*d*e == 12670944
assert r % 11 == 2 and r % 169 == 2 and (r-1) % 6816 == 0
assert (6481+55) % 152 == 0 and (6481**2+4*2**2*19) % 55 == 0
assert 6481 % 40 == 1 and 6481 % 209 == 2
print("Z67 pi0 catch and q=2 slice covering verified", flush=True)
print("PASS", flush=True)
