"""O69 (POINTWISE_TYPEI2.md §2.2): exact Haar measure of the union of certificate boxes in
Sigma = {x_2 = 1 (mod 8)} x {x_7 non-square unit} (normalised to measure 1), for box lists produced by
typei2_s27 (columns ... M2 r2 M7 r7 in fields 10-13).  Also reports the uncovered cells (largest first).
Usage: typei2_union.py boxfile [maxLambda]
"""
import sys
from collections import defaultdict


def load(fn, maxL=None):
    boxes = set()
    for line in open(fn):
        t = line.split()
        al, ga, a, b = map(int, t[:4])
        L = 2 ** (2 + al + 2 * ga) * 7 ** (a + 2 * b)
        if maxL and L > maxL:
            continue
        M2, r2, M7, r7 = map(int, t[9:13])
        if r2 % min(M2, 8) != 1 % min(M2, 8):
            continue
        if r7 % 7 not in (3, 5, 6):
            continue
        boxes.add((M2, r2, M7, r7))
    return list(boxes)


def union_measure(boxes, maxdepth=60):
    """cells: (A, r2, B, r7) meaning x_2 = r2 mod 2^A, x_7 = r7 mod 7^B. Start A=3 r2=1, B=1, r7 in {3,5,6}."""
    covered = 0.0
    uncovered = []
    stack = [(3, 1, 1, r7, 1.0 / 3, boxes) for r7 in (3, 5, 6)]
    while stack:
        A, r2, B, r7, mu, bx = stack.pop()
        rel = []
        hit = False
        for (M2, s2, M7, s7) in bx:
            m2 = min(M2, 2 ** A)
            m7 = min(M7, 7 ** B)
            if s2 % m2 != r2 % m2 or s7 % m7 != r7 % m7:
                continue
            if M2 <= 2 ** A and M7 <= 7 ** B:
                hit = True
                break
            rel.append((M2, s2, M7, s7))
        if hit:
            covered += mu
            continue
        if not rel:
            uncovered.append((mu, A, r2, B, r7))
            continue
        if A + B > maxdepth:
            uncovered.append((mu, A, r2, B, r7, 'unresolved'))
            continue
        # split the coordinate needed by the coarsest relevant box
        need2 = min((M2 for (M2, s2, M7, s7) in rel if M2 > 2 ** A), default=None)
        need7 = min((M7 for (M2, s2, M7, s7) in rel if M7 > 7 ** B), default=None)
        if need2 is not None and (need7 is None or need2 <= need7):
            for d in (0, 1):
                stack.append((A + 1, r2 + d * 2 ** A, B, r7, mu / 2, rel))
        else:
            for d in range(7):
                stack.append((A, r2, B + 1, r7 + d * 7 ** B, mu / 7, rel))
    return covered, uncovered


if __name__ == '__main__':
    fn = sys.argv[1]
    maxL = int(sys.argv[2]) if len(sys.argv) > 2 else None
    bx = load(fn, maxL)
    cov, unc = union_measure(bx)
    print(f"boxes in Sigma: {len(bx)}; covered measure {cov:.6f}; uncovered {1 - cov:.6f} in {len(unc)} cells")
    unc.sort(reverse=True)
    for u in unc[:15]:
        print("  uncovered cell mu=%.3g x2=%d mod 2^%d, x7=%d mod 7^%d" % (u[0], u[2], u[1], u[4], u[3]), *u[5:])
