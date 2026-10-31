#!/usr/bin/env python3
"""z52b pass1 U06: Z2438 fix — sunflowers (3 petals) among certificate prime-supports with prime 2 removed (hard primes <= 5000)."""
import json, sympy
exec(open("scripts/z52b_p1_U06_m.py").read().split("# Z1998")[0])
sets = []
for q in hp:
    mi = set(menu_items(q, 60))
    if not mi: continue
    u, C = min(mi, key=lambda t: t[0]*t[1])
    B = (q + u) // (4*u*C - 1)
    supp = frozenset(p_ for p_ in sympy.primefactors(u*B*C) + sympy.primefactors(q*B*C) + sympy.primefactors(q*u*C) if p_ > 13)
    sets.append((q, supp))
sf = 0; ex = []
n = len(sets)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            A, Bs, Cs = sets[i][1], sets[j][1], sets[k][1]
            core = A & Bs & Cs
            pa, pb, pc = A - core, Bs - core, Cs - core
            if core and pa and pb and pc and not (pa & pb) and not (pa & pc) and not (pb & pc):
                sf += 1
                if len(ex) < 3: ex.append((sets[i][0], sets[j][0], sets[k][0], sorted(core)))
out = {"n_sets": n, "sunflowers_3petals_primes_gt13": sf, "examples": ex}
json.dump(out, open("data/z52b/pass1/U06/final_p_sunflower.json","w"))
print(out)
