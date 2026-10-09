"""Validate m13c_witness.witness_all against brute-force residue tables (mordell_lib) for all units x mod L.
usage: m13c_witness_validate.py L"""
import sys
from math import gcd
from mordell_lib import iter_classes, cls_modulus_residues
from m13c_witness import witness_all, divs
L = int(sys.argv[1])
brute = {}   # x mod L -> set of classes
for M in divs(L):
    if M < 3:
        continue
    for fam, P in iter_classes(M):
        _, R = cls_modulus_residues(fam, P)
        for r in R:
            for t in range(L // M):
                brute.setdefault(r + M * t, set()).add((fam, tuple(P)))
bad = 0; n = 0; ncov = 0
for x in range(1, L):
    if gcd(x, L) != 1:
        continue
    n += 1
    w = set((f, tuple(P)) for f, P in witness_all(x, L, first=False))
    b = brute.get(x, set())
    ncov += bool(b)
    if w != b:
        bad += 1
        if bad < 5:
            print("MISMATCH", x, sorted(w - b)[:3], sorted(b - w)[:3])
print(f"L={L}: {n} units, {ncov} covered, mismatches {bad}")
