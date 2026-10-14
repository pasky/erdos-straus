"""O211: check of the 2-group slice criterion (y3_frob_infinity): for cd | 6 (m = 4cd | 24, (Z/m)^* elementary
2-group), M = p + 4c^2 d has a divisor h = -1 (mod m)  <=>  no odd quadratic character chi mod m (chi(-1) = -1)
has chi(q) = 1 for every prime q | M (F_2-span criterion / genus theory).  Checked for primes 5 <= p < P and odd squares.
Usage: PYTHONPATH=scripts uv run python scripts/y3_span.py P"""
import sys
from sympy import primerange, divisors, factorint
P = int(sys.argv[1]); bad = n = fires = 0
slices = [(c, 6//c//e*0 + e) for c in (1, 2, 3, 6) for e in (1, 2, 3, 6) if 6 % (c*e) == 0]
import itertools, math
def chars(m):
    G = [a for a in range(1, m) if math.gcd(a, m) == 1]; out = []
    for vals in itertools.product((1, -1), repeat=len(G)):
        ch = dict(zip(G, vals))
        if all(ch[a*b % m] == ch[a]*ch[b] for a in G for b in G): out.append(ch)
    return out
CH = {m: chars(m) for m in (4, 8, 12, 24)}
def check(N):
    global bad, n, fires
    for c, d in slices:
        m = 4*c*d; M = N + 4*c*c*d
        if math.gcd(M, m) != 1: continue
        direct = any(h % m == m - 1 for h in divisors(M))
        qs = [q % m for q in factorint(M)]
        killer = any(ch[m - 1] == -1 and all(ch[q] == 1 for q in qs) for ch in CH[m])
        if direct == killer: bad += 1
        n += 1; fires += direct
for p in primerange(5, P): check(p)
sqf = 0; nprime = n
for r in range(3, int(P**.5) + 1, 2):
    nb = n; f0 = fires; check(r*r); sqf += fires - f0
print(f"P={P}: slice checks={n} (primes: {nprime}), criterion mismatches={bad}, firing slices={fires}; odd-square firing slices={sqf}")
