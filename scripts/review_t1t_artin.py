"""R183: Thm 3.1 numerics, from scratch.  For primes p, count degree-one primes q of Z[phi] (N q = l < X) with
(i) l = 1 (mod 4), (ii) (p/l) = -1, (iii) phi a primitive root mod q, and for each such q verify the conclusion of
the proof: there is k with q | a_k = p + 4 phi^{2k+1} (found by explicit search over k mod (l-1)/2).
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_t1t_artin.py X p1 p2 ...
"""
import sys
from sympy import primerange, factorint
from sympy.ntheory import sqrt_mod

def is_prim(r, l, fac):
    return all(pow(r, (l - 1) // q, l) != 1 for q in fac)

def leg(a, l):
    a %= l
    return 0 if a == 0 else (1 if pow(a, (l - 1) // 2, l) == 1 else -1)

X = int(sys.argv[1]); ps = [int(a) for a in sys.argv[2:]]
deg1 = [l for l in primerange(7, X) if l % 5 in (1, 4)]
for p in ps:
    tot = good = verified = 0; first = None
    for l in deg1:
        if l == p: continue
        s = sqrt_mod(5, l); i2 = pow(2, -1, l)
        fac = list(factorint(l - 1))
        for r in {(1 + s) * i2 % l, (1 - s) * i2 % l}:
            tot += 1
            if l % 4 == 1 and leg(p, l) == -1 and is_prim(r, l, fac):
                good += 1
                if verified < 300:   # explicit k search for the first 300
                    t = r; r2 = r * r % l; ok = False
                    for k in range((l - 1) // 2):
                        if (p + 4 * t) % l == 0: ok = True; break
                        t = t * r2 % l
                    assert ok, (p, l, r)
                    verified += 1
                    if first is None: first = (l, r, k)
    print(f"p={p}: degree-1 primes q with N q < {X}: {tot}; satisfying (i)-(iii): {good} "
          f"(ratio {good / tot:.4f}); k found explicitly for first {verified}; first (l, phi mod q, k) = {first}")
