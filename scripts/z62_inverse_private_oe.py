#!/usr/bin/env python3
"""z62 INVERSE test 3 aggregator: reads z62_inverse_private.c output (file or stdin) twice-pass-free:
stores compact per-prime codes, then O/E of 'all u <= U fail' under the independence model with leave-one-out
per-slice marginals P(F_u | coarse signature (u, m1, w, k)) and optionally also per cell p mod MOD.
Usage: z62_inverse_private_oe.py file [MOD]"""
import sys, collections
fn = sys.argv[1]; MOD = int(sys.argv[2]) if len(sys.argv) > 2 else 1
rows = []
for l in open(fn):
    f = l.split(); p = int(f[0]); rows.append((p % MOD, f[1:]))
U = len(rows[0][1])
cnt = collections.Counter(); fl = collections.Counter()
for cell, codes in rows:
    for u, c in enumerate(codes):
        key = (cell, u, c[1:]); cnt[key] += 1; fl[key] += (c[0] == '0')
print(f'primes={len(rows)} MOD={MOD} signatures={len(cnt)}')
for UU in (8, 16, 32, 48, 64):
    if UU > U: break
    O = 0; E = 0.0; allfail = []
    for cell, codes in rows:
        pr = 1.0
        for u in range(UU):
            c = codes[u]; key = (cell, u, c[1:]); own = (c[0] == '0')
            n = cnt[key] - 1
            pr *= ((fl[key] - own) / n) if n > 0 else 1.0
        E += pr
        if all(c[0] == '0' for c in codes[:UU]): O += 1
    print(f'U={UU}: O={O} E={E:.2f} O/E={O/E if E else float("nan"):.2f}')
