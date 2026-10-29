"""Check Lemma 1.1: for p ≡ 1 (24) and odd coprime edge (a,v), a<v, the slot test
(4 | one of t,a,v,ta-1,tv-1) holds iff not (a ≡ v ≡ 1 mod 4). Also check the Legendre colour."""
from sympy import primerange, legendre_symbol as ls
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
H = 2000
tot = bad = 0
for p in primerange(25, N):
    if p % 24 != 1: continue
    for v in range(2, H + 1):
        a = (-p) % v
        if a == 0 or a >= v or (p + a + v) % (a * v): continue
        if a % 2 == 0 or v % 2 == 0: continue
        t = (p + a + v) // (a * v)
        slot = any(x % 4 == 0 for x in (t, a, v, t*a-1, t*v-1))
        rule = not (a % 4 == 1 and v % 4 == 1)
        col = ls(a % p, p) * ls(v % p, p) == -1 if a > 0 else None
        tot += 1
        if slot != rule or col != rule: bad += 1; print("FAIL", p, a, v, t)
print(f"odd edges checked={tot} failures={bad}")
