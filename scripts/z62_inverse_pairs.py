#!/usr/bin/env python3
"""z62 INVERSE: pairwise failure dependence of u-slices within cells (p mod MOD): ratio
sum_cells n_c P(F_u F_v|c) / sum_cells n_c P(F_u|c)P(F_v|c) for u < v <= V. Prints the most repelling/attracting pairs."""
import sys, collections
fn = sys.argv[1]; MOD = int(sys.argv[2]); V = int(sys.argv[3])
cells = collections.defaultdict(list)
for l in open(fn):
    p, s = l.split(); cells[int(p) % MOD].append(s[:V])
res = []
for u in range(V):
    for v in range(u + 1, V):
        O = E = 0.0
        for c, L in cells.items():
            n = len(L)
            if n < 30: continue
            fu = sum(s[u] == '0' for s in L); fv = sum(s[v] == '0' for s in L)
            fuv = sum(s[u] == '0' and s[v] == '0' for s in L)
            O += fuv; E += fu * fv / n
        res.append((O / E, u + 1, v + 1, O, E))
res.sort()
print('most repelling:', ' '.join(f'({a},{b}) {r:.3f} [{o:.0f}/{e:.0f}]' for r, a, b, o, e in res[:12]))
print('most attracting:', ' '.join(f'({a},{b}) {r:.3f} [{o:.0f}/{e:.0f}]' for r, a, b, o, e in res[-12:]))
