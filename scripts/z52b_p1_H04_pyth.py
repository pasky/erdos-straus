#!/usr/bin/env python3
"""Z1583: do primitive Pythagorean pairs (u,v), u^2+v^2 = w^2, hit every class (u0,v0) mod Q that can carry a
Mordell-hard prime p = u^2+v^2 (p mod 840 in the six square classes)?  If yes, any identity polynomial in (u,v),
valid on a congruence class of (u,v) (and a cone), produces a Type I/II solution at the odd square w^2 -> T1 kills it."""
import math, sys
Q = int(sys.argv[1]) if len(sys.argv) > 1 else 840
hard = {1, 121, 169, 289, 361, 529}
need = {(a, b) for a in range(Q) for b in range(Q) if (a*a + b*b) % 840 in hard and math.gcd(a, b) % 2 == 1}
hit = set(); R = 1200
for r in range(2, R):
    for s in range(1 + r % 2, r, 2):
        if math.gcd(r, s) != 1: continue
        u, v = r*r - s*s, 2*r*s
        for a, b in ((u, v), (v, u)):
            hit.add((a % Q, b % Q))
miss = need - hit
print(f"Q={Q}: classes able to carry hard primes: {len(need)}; hit by primitive Pythagorean pairs: {len(need & hit)}; missed: {len(miss)}")
print("sample missed:", sorted(miss)[:10])
# allow non-primitive points k*(u,v), k a unit mod Q (k*w still odd, n = (k w)^2 still an odd square -> T1 still applies)
units = [k for k in range(1, Q) if math.gcd(k, Q) == 1]
hit2 = {((k*a) % Q, (k*b) % Q) for (a, b) in hit for k in units}
print(f"with unit scalings k: hit {len(need & hit2)} / {len(need)}; missed {len(need - hit2)}")
