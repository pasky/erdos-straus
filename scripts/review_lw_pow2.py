"""R180 from-scratch check of LORENZINI_W Thm 9.1 (even half).
(1) For every odd m mod 36 find which of the six families applies, using pow(2,m,d) directly.
(2) For every odd m in [1, MMAX] build the explicit (x,y,z), check exact identity and x,y,z>=2.
(3) Brute-force: all even n < NB that are not values, compare with {0,2,6,14,510}.
(4) Symbolic check of the six identities with sympy.
"""
import sys
from math import isqrt

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
NB = int(sys.argv[2]) if len(sys.argv) > 2 else 200000

# families: kind, a, b ; (x,z)-kind: x=a, z=b, d=a*b, y=(n+a+b)/d ; (x,y)-kind: x=a,y=b, d=ab-1, z=(n+a)/d
FAM = [("xz", 3, 3), ("xz", 6, 12), ("xy", 7, 2), ("xz", 3, 9), ("xy", 10, 11), ("xz", 8, 74)]


def sol(n, kind, a, b):
    if kind == "xz":
        d = a * b
        if (n + a + b) % d == 0:
            return (a, (n + a + b) // d, b)
    else:
        d = a * b - 1
        if (n + a) % d == 0:
            return (a, b, (n + a) // d)
    return None


def f(x, y, z):
    return x * y * z - x - z

# (1) periodicity: divisibility of 2^m-2+c by d depends on m mod lcm(ord) once m >= v2-threshold.
# check classes directly on a representative m0 in [37, 72] and on m0+36k for k up to 50 (exact ints)
bad = []
cover = {}
for r in range(1, 36, 2):
    fams = []
    for (kind, a, b) in FAM:
        ok = all(sol(2 ** (m) - 2, kind, a, b) is not None for m in range(36 + r, 36 + r + 36 * 60, 36))
        if ok:
            fams.append((kind, a, b))
    cover[r] = fams
    if not fams:
        bad.append(r)
print("cover of odd m mod 36:", cover)
print("uncovered classes:", bad)

# (2) explicit for all odd m <= MMAX
fails = []
for m in range(1, MMAX + 1, 2):
    n = 2 ** m - 2
    found = None
    for (kind, a, b) in FAM:
        s = sol(n, kind, a, b)
        if s and min(s) >= 2 and f(*s) == n:
            found = s
            break
    if not found:
        fails.append(m)
print("odd m <= %d with no valid family solution:" % MMAX, fails)

# (3) brute force even n < NB: n = x*y*z - x - z ; enumerate x<=z (symmetric), y>=2
val = bytearray(NB)
x = 2
while x * 2 * x - 2 * x < NB:  # minimal value with z>=x, y=2
    z = x
    while x * 2 * z - x - z < NB:
        y = 2
        while True:
            v = x * y * z - x - z
            if v >= NB:
                break
            val[v] = 1
            y += 1
        z += 1
    x += 1
miss_even = [n for n in range(0, NB, 2) if not val[n]]
miss_all = [n for n in range(0, NB) if not val[n]]
print("even non-values < %d:" % NB, miss_even)
print("first non-values overall (<200):", [n for n in miss_all if n < 200], "count", len(miss_all))

# (4) symbolic
import sympy as sp
k, M = sp.symbols("k M", integer=True)
# n = 2^m - 2 with P = 2^m; identities: f(x,y,z) == P - 2 with y or z as given rational expr
P = sp.symbols("P")
for (kind, a, b) in FAM:
    n = P - 2
    if kind == "xz":
        e = f(a, (n + a + b) / sp.Integer(a * b), b)
    else:
        e = f(a, b, (n + a) / sp.Integer(a * b - 1))
    print(kind, a, b, "identity residual:", sp.simplify(e - n))
