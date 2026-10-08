"""O93: exact union of boxes in the cell C_v (v=5 default) from
  P-data files  DIR/p{K}.txt   (lines "a b c d", from m17b_penum.py), K odd; boxes -f, -(4bcd-1) mod 17^((K+1)/2)
  Q/U box files DIR/{Q,U}{k}.txt (lines "Q r" / "U r", from m17_enum), plus inverses (Q^-1, U^-1).
Prints covered fraction of the cell (exact rational and float) and new-box counts per level.
Usage: m17b_union.py DIR KPmax kQUmax [v]
"""
import sys, os
from fractions import Fraction

D, KP, KQ = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
v = int(sys.argv[4]) if len(sys.argv) > 4 else 5
boxes = {}  # level -> set of residues (in cell)
src = {}

def add(L, r, t):
    F = 17 ** L
    r %= F
    if r % 17 != v: return
    boxes.setdefault(L, set()).add(r)
    src.setdefault((L, r), set()).add(t)

for K in range(1, KP + 1, 2):
    L = (K + 1) // 2
    n = 17 ** K
    for line in open(os.path.join(D, f"p{K}.txt")):
        a, b, c, d = map(int, line.split())
        assert 4 * a * b * c * d == a + b + n * c and a <= b and c % 17 and d % 17
        add(L, -(4 * a * c * d - 1), "P"); add(L, -(4 * b * c * d - 1), "P")
for T in "QU":
    for k in range(1, KQ + 1, 2):
        for line in open(os.path.join(D, f"{T}{k}.txt")):
            t, r = line.split(); r = int(r); F = 17 ** k
            add(k, r, T)
            if r % 17: add(k, pow(r, -1, F), T + "inv")

covered = Fraction(0)
kept = set()
for L in sorted(boxes):
    new = 0; bytype = {}
    for r in sorted(boxes[L]):
        if any((j, r % 17 ** j) in kept for j in range(1, L)): continue
        kept.add((L, r)); new += 1
        covered += Fraction(1, 17 ** (L - 1))
        for t in src[(L, r)]: bytype[t] = bytype.get(t, 0) + 1
    print(f"level {L}: boxes {len(boxes[L])} new {new} {dict(sorted(bytype.items()))} covered {float(covered):.9f}")
print(f"covered = {covered} = {float(covered):.12f}; uncovered = {1 - covered} = {float(1 - covered):.12f}")
