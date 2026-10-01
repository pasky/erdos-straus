#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 8.5: the two frames are nearly independent.
For the W-record primes of notes (65.2) and the three hard p < 1e9 with W(p) > 2047
(found by `pointwise_size_wtail.py census 2047 1000000000`), print
(p, W(p), a_min(p), n_p, factorisation of p-1)."""
import json
from sympy import factorint, primerange
from pointwise_size_amin import amin
from pointwise_size_wtail import build_rows

rows = build_rows(8191)
recs = [73, 193, 1201, 2521, 3361, 33289, 90841, 144169, 167521, 225289, 361321, 915961,
        954409, 1853329, 2031121, 605531161, 610747201]
out = []
for p in recs:
    w = next(M for M, _, t in rows if t[p % M])
    n = next(l for l in primerange(3, 400) if pow(p % l, (l - 1) // 2, l) == l - 1)
    out.append((p, w, amin(p, factorint)[0], n, {str(k): v for k, v in factorint(p - 1).items()}))
print(json.dumps(out))
