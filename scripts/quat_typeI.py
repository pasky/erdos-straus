"""O130 step 1 checks on all Type I solutions, p < P.
(a) K-identity: (1+2a w)(1+2b w) = e(2c w - p), w = sqrt(-d)   [Lemma 1.1]
(b) for each split d1*d2 = a*b*d (d1 in {d, ad, bd, abd, a, b, 1, ...}) the quaternion algebra
    Q<u,v>, u^2=-d1, v^2=-d2, uv+vu=1  ~  (-d1, -d1(4 d1 d2 - 1)) = (-d1, -d1 p e):
    record its finite ramification set.
Run: PYTHONPATH=scripts uv run python scripts/quat_typeI.py [P]"""
import sys
from collections import Counter
from sympy import isprime, factorint
from geo_common import es_solutions, hilbert
import math
from math import gcd


def abcd(N, X, Y, Z):
    d = gcd(gcd(X, Y), Z); x_, y_, z_ = X//d, Y//d, Z//d
    abc = math.isqrt(x_*y_*z_); assert abc*abc == x_*y_*z_
    return abc//z_, abc//y_, abc//x_, d

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000


def ram(A, B):
    ps = set(factorint(abs(A)).keys()) | set(factorint(abs(B)).keys()) | {2}
    return frozenset(q for q in ps if hilbert(A, B, q) == -1)


stats = Counter()
nsol = 0
for p in range(5, P):
    if not isprime(p):
        continue
    seen = set()
    for sol in es_solutions(p):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            x, y, z = [sol[k] for k in perm]
            if not (x % p == 0 and y % p and z % p):
                continue
            a, b, c, d = abcd(p, x//p, y, z)
            if (a, b, c, d) in seen or (b, a, c, d) in seen:
                continue
            seen.add((a, b, c, d))
            nsol += 1
            e = (a+b)//c; f = 4*a*c*d - p
            assert e*f == 4*a*a*d+1 and 4*a*b*d - 1 == p*e
            # (a) (1+2a w)(1+2b w) = 1 - 4abd + 2(a+b) w  =  e(-p + 2c w)
            assert 1 - 4*a*b*d == -e*p and 2*(a+b) == e*2*c
            # (b) splits
            for name, d1 in [("d|ab", d), ("ad|b", a*d), ("bd|a", b*d), ("1|abd", 1)]:
                d2 = a*b*d//d1
                R = ram(-d1, -d1*(4*d1*d2-1))
                stats[(name, R == frozenset({p}))] += 1
print(f"Type I unordered-in-(a,b) solutions, p<{P}: {nsol}")
for k in sorted(stats):
    print(k, stats[k])
