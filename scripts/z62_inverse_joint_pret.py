#!/usr/bin/env python3
"""z62 INVERSE test 2b (post-hoc, after test 2): is the joint-failure excess at U = 32, 64 explained by
1-pretentiousness of chi_p on small primes?  D2(p; y) = sum_{l <= y, l odd prime} (1 - chi_p(l))/l.
O/E with marginals estimated within cells (p mod 840) x (D2(p;Y) quantile bin).  Usage: file Y nbins"""
import sys, collections
from sympy import primerange
fn = sys.argv[1]; Y = int(sys.argv[2]); nb = int(sys.argv[3])
P = [l for l in primerange(3, Y + 1)]
rows = []
for l in open(fn):
    p, s = l.split(); p = int(p)
    d2 = sum((1 - (1 if pow(p, (q - 1) // 2, q) == 1 else -1)) / q for q in P)
    rows.append((p, d2, s))
ds = sorted(r[1] for r in rows); cuts = [ds[int(len(ds) * k / nb)] for k in range(1, nb)]
def b(d): return sum(d > c for c in cuts)
for U in (16, 32, 64):
    cnt = collections.Counter(); fails = collections.defaultdict(lambda: [0] * U)
    cells = []
    for p, d2, s in rows:
        cell = (p % 840, b(d2)); cells.append(cell); cnt[cell] += 1
        for u in range(U):
            if s[u] == '0': fails[cell][u] += 1
    O = 0; E = 0.0; Ob = collections.Counter(); Eb = collections.Counter()
    for (p, d2, s), cell in zip(rows, cells):
        pr = 1.0
        for u in range(U): pr *= fails[cell][u] / cnt[cell]
        E += pr; Eb[cell[1]] += pr
        if '1' not in s[:U]: O += 1; Ob[cell[1]] += 1
    print(f'Y={Y} bins={nb} U={U}: O={O} E={E:.2f} O/E={O/E:.2f}; by D2-bin (low D2 = pretentious) ' +
          ' '.join(f'{k}:{Ob[k]}/{Eb[k]:.1f}' for k in range(nb)))
