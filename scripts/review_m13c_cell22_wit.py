#!/usr/bin/env python3
"""R100: verify, with the reviewer's own literal membership test, author-engine witnesses (13B/O100 inv_*.pkl,
fields boxes[(fam, MT, r)] = P) for the (2,2)-cell subcells that review_m13c_cell22_cover.py (B=120) left
uncovered but the author claims covered.  Also: T-levels of the N = 11^4 13^4 boxes.
usage: review_m13c_cell22_wit.py RUNDIR"""
import glob, pickle, sys
sys.path.insert(0, "scripts")
from review_m13c_cell22_cover import modulus, member, tpart, F, cells
claimed_unc = {(a, b) for a in (2, 57, 79) for b in (15, 28, 54, 132, 145)}
targets = [u for u in cells if (u % 121, u % 169) not in claimed_unc and
           (u % 121 in (2, 57, 68, 79) and u % 169 in (15, 28, 54, 93, 132, 145))]
found = {}
for fn in sorted(glob.glob(sys.argv[1] + "/inv_*.pkl")):
    D = pickle.load(open(fn, "rb"))
    if D["N"] == 418161601:
        lv = {MT for (fam, MT, r) in D["boxes"]}
        print("N=11^4 13^4:", len(D["boxes"]), "boxes; T-levels dividing 11^2 13^2:", sorted(m for m in lv if F % m == 0))
    for (fam, MT, r), P in D["boxes"].items():
        if F % MT: continue
        M = modulus(fam, tuple(P)); Mp = M // tpart(M)
        for u in targets:
            if u in found: continue
            n = (1 + Mp * ((u - 1) * pow(Mp, -1, tpart(M)))) % M if tpart(M) > 1 else 1
            if member(fam, tuple(P), n): found[u] = (fam, tuple(P), M, D["N"])
for u in targets:
    print((u % 121, u % 169), found.get(u, "NOT FOUND"))
