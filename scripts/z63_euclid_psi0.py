#!/usr/bin/env python3
"""z63 EUCLID: check that psi0 (restriction of the character S,T -> 1 of PSL2(Z)) is a Hecke eigenclass in E (run from repo root)."""
import sys, os
sys.path.insert(0, 'scripts')
import z63_euclid_hecke as Hk
for p in [73, 409, 1009, 2017]:
    lev = Hk.LevelX(p)
    dep = [lev.depth(x) & 1 for x in range(lev.N)]
    psi0 = 0
    for (x, g), e in lev.eidx.items():
        if (dep[x] + 1 + dep[lev.act[x][g]]) & 1:
            psi0 |= 1 << e
    rows = list(lev.basis.values())
    gens = []
    for (x, g), e in lev.eidx.items():
        y = lev.act[x][g]
        Gm = ((0, -1), (1, 0)) if g == 0 else ((1, 1), (0, 1))
        (a, b), (c, d) = lev.Rx[y]
        gens.append((e, Hk.mm(Hk.mm(lev.Rx[x], Gm), ((d, -b), (-c, a)))))
    ok_rel = all(Hk.dot(psi0, r) == 0 for r in rows)
    ok = True
    for l in [2, 3, 5, 7]:
        lam = (l + 1) % 2
        for e, Y in gens:
            r = Hk.hecke_image(lev, Y, l) ^ ((1 << e) if lam else 0)
            if Hk.dot(psi0, r):
                ok = False
    print(p, 'psi0 cocycle', ok_rel, 'psi0 Hecke-eigen (1+l)', ok, 'psi0 != chi', psi0 != lev.chimask)
