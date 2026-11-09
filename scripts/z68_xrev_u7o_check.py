"""Independent word reconstruction, screen checks and engine comparisons.
uv run --with sympy scripts/z68_xrev_u7o_check.py /tmp/xrev_U7O
Prepare that directory with git archive side-agent/z68-u7o, and compile its
scripts/z68_u7o_cascade.c to <directory>/cascade. Bounded-memory, serial.
"""
import math
from pathlib import Path
import random
import re
import subprocess
import sys

from sympy import divisors, isprime, nextprime

root = Path(sys.argv[1])

def valid(n, word):
    x, y, z = word
    return min(word) > 0 and x*y*z-x-z == n and x*y % 8 == 0


def at_letter(n, c):
    # Reconstruct both orientations of a fixed endpoint, not residue tests.
    for d in divisors(n+c):
        if (d+1) % c == 0:
            for w in ((c, (d+1)//c, (n+c)//d),
                      ((n+c)//d, (d+1)//c, c)):
                if valid(n, w):
                    return w
    for d in divisors(c*n+1):
        e = (c*n+1)//d
        if (d+1) % c == 0 and (e+1) % c == 0:
            w = ((d+1)//c, c, (e+1)//c)
            if valid(n, w):
                return w
    return None


def depth(n):
    for c in range(1, 129):
        w = at_letter(n, c)
        if w:
            assert min(w) == c
            return c, w
    raise AssertionError((n, 'depth exceeds sample cap'))


def engine_depth(n):
    run = subprocess.run([str(root/'cascade'), str(n), str(n), '0'],
                         check=True, capture_output=True, text=True, timeout=60)
    m = re.search(r'primes=1 max m=(\d+)', run.stdout)
    assert m, (n, run.stdout)
    return int(m[1])


def numbers(path):
    return [int(s.split()[0]) for s in path.read_text().splitlines()
            if s.strip() and not s.startswith('#')]


def direct(n):
    # If f>n, r=f-n divides f+1, hence r divides n+1 and f<=2n+1.
    # Check the defining least residue, independently of word searches.
    for f in range(7, 2*n+2, 8):
        r = (-n) % f
        if r and (f+1) % r == 0:
            return f, r
    return None

least_records = re.findall(r'REC p=(\d+) f=(\d+) r=(\d+)',
                          (root/'data/z68/u7o/least_1e8.txt').read_text())
for p, f, r in least_records:
    assert direct(int(p)) == (int(f), int(r))
print('LEAST-F RECORDS PASS', len(least_records))

records = {}
for path in sorted((root/'data/z68/u7o').glob('cascade_*.txt')):
    for p, m in re.findall(r'(?:REC|DEEP) p=(\d+) m=(\d+)', path.read_text()):
        p, m = int(p), int(m)
        assert p not in records or records[p] == m
        records[p] = m
for p, expected in sorted(records.items()):
    m, w = depth(p)
    assert m == expected == engine_depth(p), (p, expected, m, w)
    print('RECORD/DEEP', p, m, tuple(map(int, w)))

for C in (3, 4):
    M = math.lcm(840, *(8*k*(k+1) for k in range(1, C+1)))
    for p in numbers(root/f'data/z68/u7o/dickson_C{C}.txt'):
        assert p % M == 1 and isprime(p)
        for k in range(1, C+1):
            assert isprime((p+k)//(k+1)) and isprime((k*p+1)//(k+1))
        m, w = depth(p)
        assert m > C and m == engine_depth(p)
        print('DICKSON', C, p, m, tuple(map(int, w)))

rng = random.Random(68007)
sample = set(numbers(root/'data/z68/u7o/deep_m10_1e8.txt'))
while len(sample) < 188:
    p = int(nextprime(rng.randrange(17, 4000000000)))
    if p % 8 == 1:
        sample.add(p)
for p in sorted(sample):
    m, w = depth(p)
    assert m == engine_depth(p), (p, m, w)
print('SAMPLE deep60+random128 PASS', len(sample))

# Reconstruct the seven claimed Gaussian failures without importing its engine.
gaussian_failures = []
for row in (root/'data/z68/u7o/gausstest_deep1e8.txt').read_text().splitlines():
    if not row.endswith('[]'):
        continue
    p, a, b = map(int, row.split()[:3])
    assert a*a+b*b == p and isprime(p)
    candidates = {int(d) for v in (a, b, a+b, abs(a-b)) if v
                  for d in divisors(v) if 2 <= d <= math.isqrt(2*p)}
    assert not any(at_letter(p, d) for d in candidates), p
    gaussian_failures.append(p)
assert len(gaussian_failures) == 7
print('GAUSSIAN FAILURES VERIFIED', gaussian_failures)

p = 1000829135329
m, w = depth(p)
assert m == 4 == engine_depth(p)
print('COMPOSITE-RESIDUAL REGRESSION', p, m, tuple(map(int, w)))

screens = root/'data/z58/screens'
for filename, expected_count in [('star_prime_zeros.txt', 14),
                                 ('gstar_zeros.txt', 38),
                                 ('r8_zeros_1e10.txt', 12)]:
    ns = numbers(screens/filename)
    assert len(ns) == expected_count
    for n in ns:
        assert isprime(n)
        assert direct(n), (filename, n)
    print('SCREEN', filename, 'all U7', len(ns))
composites = numbers(screens/'composite_zeros_le8e6.txt')
assert len(composites) == 285
assert all(not isprime(n) and math.isqrt(n)**2 != n for n in composites)
zeros = [n for n in composites if not direct(n)]
assert zeros == [105, 1465, 3865, 4545, 10305, 12145, 39361, 67425], zeros
print('COMPOSITE SCREEN 285: hits=277 zeros=', zeros)
for m in range(1, 1000, 2):
    assert not direct(m*m), m
print('ODD-SQUARE SCREEN: 500 zeros PASS')

# A word's first letter need not be the least-residue target (y=1 case).
assert valid(41, (8, 1, 7))
assert (-41) % 7 == 1
print('WORD NORMALIZATION: (8,1,7) has f=7 and residue=1, not x=8')
