"""R93 from-scratch exact union of boxes in C_5 (u ≡ 5 mod 17) for POINTWISE_MORDELL17B §3.
Inputs (directory D):
  b{K}.txt   P-data "a b c d" (N-points of Σ^II_{17^K}, a<=b, 17∤cd), from review_m17b_brute.c / _k11.c;
  S{k}.txt   R83 engine (review_m17_enum.c S k): "S a m d" (Q-data), boxes -4a^2d, -4m^2d, and the
             I2 (Q^{-1}) boxes -m/a, -a/m; √Q roots checked to be absent (non-residue);
  U{k}.txt   R83 engine (U k): "U e a b i", boxes -e and -1/e.
Box of level L = residue class mod 17^L.  Measure relative to the cell: 17^(1-L).
Usage: review_m17b_union.py D Kmax_P kmax_QU [Kmax_P_list...]
"""
import sys, os
from fractions import Fraction

def boxes(D, KP, kQU):
    bx = {}  # (L, r) -> set of types
    def add(L, r, t):
        r %= 17 ** L
        bx.setdefault((L, r), set()).add(t)
    for K in KP:
        L = (K + 1) // 2; F = 17 ** L
        for line in open(os.path.join(D, f"b{K}.txt")):
            a, b, c, d = map(int, line.split())
            assert 4 * a * b * c * d == a + b + 17 ** K * c and a <= b and c % 17 and d % 17
            add(L, -(4 * a * c * d - 1), "P"); add(L, -(4 * b * c * d - 1), "P")
    for k in range(1, kQU + 1):
        F = 17 ** k
        p = os.path.join(D, f"S{k}.txt")
        if os.path.exists(p):
            for line in open(p):
                _, a, m, d = line.split(); a, m, d = int(a), int(m), int(d)
                for x in (a, m):
                    t = -4 * x * x * d % F
                    assert pow(t % 17, 8, 17) == 16, "sqrt(Q) box would exist"
                    add(k, t, "Q")
                add(k, -m * pow(a, -1, F), "Qinv"); add(k, -a * pow(m, -1, F), "Qinv")
        p = os.path.join(D, f"U{k}.txt")
        if os.path.exists(p):
            for line in open(p):
                e = int(line.split()[1])
                add(k, -e, "U"); add(k, -pow(e, -1, F), "Uinv")
    return bx

def union(bx, cell=5):
    inc = sorted((L, r) for (L, r) in bx if r % 17 == cell)
    kept = set(); rows = {}
    for L, r in inc:
        if any((j, r % 17 ** j) in kept for j in range(1, L)) or (L, r) in kept:
            continue
        kept.add((L, r)); rows.setdefault(L, []).append(bx[(L, r)])
    cov = sum((Fraction(17) ** (1 - L) for L, _ in kept), Fraction(0))
    return cov, rows, inc

if __name__ == "__main__":
    D = sys.argv[1]; KP = [int(x) for x in sys.argv[2].split(",")]; kQU = int(sys.argv[3])
    bx = boxes(D, KP, kQU)
    for cell in (5, 7):
        cov, rows, inc = union(bx, cell)
        print(f"cell {cell}: covered {cov} uncovered {1 - cov} = {float(1 - cov):.9f}")
        for L in sorted(rows):
            ts = {}
            for s in rows[L]:
                for t in s: ts[t] = ts.get(t, 0) + 1
            nin = sum(1 for (l, r) in inc if l == L)
            print(f"  level {L}: in-cell {nin}, new {len(rows[L])}, new-by-type {ts}, "
                  f"added {float(len(rows[L]) * Fraction(17) ** (1 - L)):.3e}")
