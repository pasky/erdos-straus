"""O259: check the pair genus law (B1_LINE.md Lemma 1.3) on all b = 1 pairs, p = 1 (4) prime < P.
Pair (s, t): s t | p + s + t, 4 | s (the 4-divisible coordinate), t = 3 (4).  Claims:
  (st/p) = -1 always;  (s't/p) = -(2/p)^k  where s = 2^k s', k >= 2;  'free' pairs (s't/p) = +1 occur iff p = 5 (8), k odd.
Also the (★) law: for all pairs with 4 | N = (p+x+y)/(xy) (one coordinate even, x = 2^k x'): (xy/p) = -1, (x'y/p) = -(2/p)^k.
usage: PYTHONPATH=scripts uv run python scripts/z29_genus.py 20000
"""
import sys
from sympy import primerange, legendre_symbol as L, divisors

def pairs(p):
    out = []
    s = 1
    while (s - 1) ** 2 <= p + 1:
        for t in divisors(p + s):
            if t > s and ((p + s) // t + 1) % s == 0:
                out.append((s, t))
        s += 1
    return out

P = int(sys.argv[1])
bad = free = tot = c1 = c1bad = 0
freecls = set()
for p in primerange(5, P):
    if p % 4 != 1:
        continue
    for (s, t) in pairs(p):
        N = (p + s + t) // (s * t)
        if s % 4 == 0 or t % 4 == 0:
            S, T = (s, t) if s % 4 == 0 else (t, s)
            k = (S & -S).bit_length() - 1
            sp = S >> k
            tot += 1
            if L(S * T % p, p) != -1: bad += 1
            pred = -(L(2, p) ** k)
            if L(sp * T % p, p) != pred: bad += 1
            if pred == 1:
                free += 1; freecls.add((p % 8, k % 2))
        if N % 4 == 0:   # c = 1 line (★); may overlap the b = 1 line
            c1 += 1
            if L(s * t % p, p) != -1: c1bad += 1
            X = s if s % 2 == 0 else t          # x, y cannot both be odd (then N would be odd)
            k = (X & -X).bit_length() - 1
            odd = (s * t) >> k
            if L(odd % p, p) != -(L(2, p) ** k): c1bad += 1
print(f"p<{P}: b=1 pairs {tot}, violations {bad}, free pairs {free} in (p mod 8, k mod 2) classes {sorted(freecls)}; "
      f"c=1 pairs {c1}, violations {c1bad}")
