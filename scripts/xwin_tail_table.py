#!/usr/bin/env python3
"""POINTWISE_XWIN.md §1 table: T(x,Z)*(log x)^{1+J/2}/x from a_min censuses
(pointwise_size_amin.py census N; hard primes p=1 (24), p<N)."""
import json, math, sys
files = sys.argv[1:]
rows = []
for f in files:
    d = json.load(open(f))
    h = {int(k): v for k, v in d['hist'].items()}
    x = d['N']
    out = []
    for Z in [3, 7, 11, 15, 19, 23]:
        T = sum(v for q, v in h.items() if q > Z)
        J = (Z + 1) // 4
        out.append(f"{T} ({T*math.log(x)**(1+J/2)/x:.3f})")
    print(f"| {x:.0e} | " + " | ".join(out) + " |")
