#!/usr/bin/env python3
"""z62 INVERSE test 2 (pre-registered escape hatch): observed vs product-of-marginals frequency of
'all u-slices u <= U fail', marginals estimated within cells (p mod 840) x chi_p(11) x chi_p(13).
Input: output of scripts/z62_inverse_joint.c. Usage: z62_inverse_joint_oe.py file [extra primes for cells ...]"""
import sys, collections, math
fn = sys.argv[1]
extra = [int(x) for x in sys.argv[2:]] or [11, 13]
rows = []
for l in open(fn):
    p, s = l.split(); p = int(p)
    cell = (p % 840,) + tuple(pow(p, (q - 1) // 2, q) == 1 for q in extra)
    rows.append((p, cell, s))
for U in (4, 8, 16, 32, 64):
    cnt = collections.Counter(); fails = collections.defaultdict(lambda: [0] * U)
    for p, cell, s in rows:
        cnt[cell] += 1
        for u in range(U):
            if s[u] == '0': fails[cell][u] += 1
    O = sum(1 for p, c, s in rows if '1' not in s[:U])
    E = 0.0
    for p, cell, s in rows:
        pr = 1.0
        for u in range(U): pr *= fails[cell][u] / cnt[cell]
        E += pr
    # Poisson-ish CI for O
    print(f'U={U:3d} primes={len(rows)} cells={len(cnt)} O={O} E={E:.2f} O/E={O/E if E else float("nan"):.2f}')
