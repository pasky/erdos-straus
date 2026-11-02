"""z54 UPPER2 §3: fixed-level ("congruence") certificates for p = 1 (mod 8).

A test (kind, x, d) with x in C_p (x = 0 mod 4 or x = 7 mod 8, p = 1 mod 8), d = -1 (mod x), d | M fires on the
residue class of p mod M given by   U: p = -x (mod d)    T: x p = -1 (mod d).
For M = 8 * m (m odd), list the classes p mod M (p = 1 mod 8, gcd(p,m)=1) not covered by any test with x <= X,
and compare with Q(M) = {p : p is a square mod every prime q | m}  (Lemma J says Q(M) is never covered).
Also output, for each covered class, the least x that covers it (=> HC(p) <= that x for every prime p in the class).
usage: z54_upper2_cover.py m X
"""
import sys
from math import gcd
from sympy import divisors, factorint

m = int(sys.argv[1])
X = int(sys.argv[2])
M = 8 * m
qs = list(factorint(m).keys())
classes = [r for r in range(1, M, 8) if gcd(r, m) == 1]
best = {r: None for r in classes}
divs = divisors(M)
for x in range(4, X + 1):
    if not (x % 4 == 0 or x % 8 == 7):
        continue
    for d in divs:
        if d % x != x - 1:
            continue
        for r in classes:
            if best[r] is not None and best[r] <= x:
                continue
            if (r + x) % d == 0 or (x * r + 1) % d == 0:
                best[r] = x
unc = [r for r in classes if best[r] is None]
Q = [r for r in classes if all(pow(r, (q - 1) // 2, q) == 1 for q in qs if q > 2)] if all(
    e == 1 for e in factorint(m).values()) else None
hist = {}
for r in classes:
    hist[best[r]] = hist.get(best[r], 0) + 1
print(f"M={M} X={X}: classes {len(classes)}, uncovered {len(unc)}")
if Q is not None:
    print(f"  |Q(M)| = {len(Q)}; uncovered == Q: {set(unc) == set(Q)}; Q subset of uncovered: {set(Q) <= set(unc)}")
print("  least covering x histogram:", sorted(hist.items(), key=lambda kv: (kv[0] is None, kv[0] or 0)))
if len(unc) <= 40:
    print("  uncovered:", unc)
