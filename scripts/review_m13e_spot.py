"""R107: spot-check O107's raw m13e_es chunk output in the 128-bit regime against an own plain-Python
enumeration.  For each random x-window [x0, x0+W) at level N: all y>=x with 4/N-1/x-1/y = 1/z, z>=y, found by
the identity (r*y - s)(r*z - s) = s^2 (r/s = 4/N - 1/x reduced), D = r*y - s running over ALL divisors of s^2
with D <= s (sympy factorint), checked with exact Fractions.  Compared with the lines of the author's chunk file.
usage: review_m13e_spot.py RUNDIR N n_windows W seed"""
import sys, glob, random
from fractions import Fraction as Fr
from sympy import factorint

rd, N, nw, W, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
random.seed(seed)
chunks = []
for fn in glob.glob(f'{rd}/es_{N}_*.txt'):
    last = open(fn).read().rstrip().split('\n')[-1]
    f = dict(t.split('=') for t in last[1:].split()); chunks.append((int(f['xlo']), int(f['xhi']), fn))
chunks.sort()
assert chunks[0][0] == N // 4 + 1 and chunks[-1][1] == 3 * N // 4
assert all(chunks[i][1] + 1 == chunks[i + 1][0] for i in range(len(chunks) - 1))
fN = factorint(N)
def mine(x):
    num, den = 4 * x - N, N * x
    from math import gcd
    g = gcd(num, den); r, s = num // g, den // g
    fs = dict(fN)
    for p, e in factorint(x).items(): fs[p] = fs.get(p, 0) + e
    for p, e in factorint(g).items(): fs[p] -= e
    ds = [1]
    for p, e in fs.items():
        ds = [d * p**k for d in ds for k in range(2 * e + 1) if d * p**k <= s]
    out = set()
    for D in ds:
        if (D + s) % r == 0:
            y = (D + s) // r
            if y < x: continue
            rest = Fr(4, N) - Fr(1, x) - Fr(1, y)
            assert rest.numerator == 1 and rest.denominator >= y
            out.add((x, y))
    return out
tot = 0; big = 0
for _ in range(nw):
    x0 = random.randint(N // 4 + 1, 3 * N // 4 - W)
    if random.random() < 0.3: x0 = N // 4 + 1 + random.randint(0, 50 * W)   # near N/4: many solutions
    xs = range(x0, x0 + W)
    M = set()
    for x in xs: M |= mine(x)
    A = set()
    for lo, hi, fn in chunks:
        if hi < x0 or lo >= x0 + W: continue
        for line in open(fn):
            if line[0] == '#': continue
            x, y = map(int, line.split())
            if x0 <= x < x0 + W: A.add((x, y))
    big += sum(1 for x in xs if N * x // 1 > 2**64)
    tot += len(M)
    print(f'N={N} window [{x0},{x0+W}): mine {len(M)} author {len(A)} equal={M == A}', flush=True)
    assert M == A, (sorted(M ^ A)[:5])
print(f'all windows equal; {tot} solutions; x with N*x > 2^64: {big}')
