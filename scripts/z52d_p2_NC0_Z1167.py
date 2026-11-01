"""Z1167: McCormick relaxation of the bounded ES search (G4, NC0).
Bilinear auxiliary: w = xy (McCormick envelope on a box [x1,x2] x [y1,y2]).
Necessary condition for a certificate (x,y,z) of 4/p: D := 4xy - p(x+y) >= 1 (so that z = pxy/D > 0);
equivalently 4w - p(x+y) >= 1 with w = xy.
McCormick (exact for the bilinear term at box corners):
  w <= U1 = x2*y + y1*x - x2*y1 ,  w <= U2 = x1*y + y2*x - x1*y2   (upper envelope; lower ones not needed for pruning)
Box test (exact LP over the box): max over box of g(x,y) = 4*min(U1,U2) - p(x+y).  Concave piecewise linear;
maximum attained at a box vertex or where U1 = U2 meets the box boundary (checked exactly with Fractions).
Prune box if max g < 1.  Branch on the longer side until the box has <= 1 integer column/row.
Soundness check: no true solution (x,y) with D | pxy is ever pruned.  Measure: surviving integer points,
false positives (leaves that contain no true solution), and pruning fraction per depth."""
import sys, math
from fractions import Fraction as Fr


def gmax(x1, x2, y1, y2, p):
    U1 = lambda x, y: x2 * y + y1 * x - x2 * y1
    U2 = lambda x, y: x1 * y + y2 * x - x1 * y2
    g = lambda x, y: 4 * min(U1(x, y), U2(x, y)) - p * (x + y)
    cands = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    # line U1 = U2 : (x2 - x1)*y + (y1 - y2)*... solve U1-U2 = 0 (linear in x,y)
    # U1 - U2 = (x2-x1)*y + (y1-y2)*x + (y2*x1 - x2*y1) ... compute coefficients numerically
    a = (x2 - x1) * 1  # coefficient of y
    b = (y1 - y2)      # coefficient of x
    c = -(x2 * y1 - x1 * y2)
    # check: U1 - U2 == a*y + b*x + c  (verified below by assertion)
    for xx, yy in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
        assert U1(xx, yy) - U2(xx, yy) == a * yy + b * xx + c
    # intersections with box edges
    for xv in (x1, x2):
        if a != 0:
            yv = Fr(-(b * xv + c), a)
            if y1 <= yv <= y2:
                cands.append((Fr(xv), yv))
    for yv in (y1, y2):
        if b != 0:
            xv = Fr(-(a * yv + c), b)
            if x1 <= xv <= x2:
                cands.append((xv, Fr(yv)))
    return max(g(Fr(x), Fr(y)) for x, y in cands)


def solutions_in(x1, x2, y1, y2, p):
    out = set()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            D = 4 * x * y - p * (x + y)
            if D >= 1 and (p * x * y) % D == 0:
                out.add((x, y))
    return out


def bnb(p, X1, X2, Y1, Y2, true_sols):
    stats = {"leaves": 0, "fp_leaves": 0, "pruned_pts": 0, "surv_pts": 0, "missed": 0}
    depth_hist = {}
    stack = [(X1, X2, Y1, Y2, 0)]
    total_pts = (X2 - X1 + 1) * (Y2 - Y1 + 1)
    while stack:
        x1, x2, y1, y2, d = stack.pop()
        if gmax(x1, x2, y1, y2, p) < 1:
            pts = (x2 - x1 + 1) * (y2 - y1 + 1)
            stats["pruned_pts"] += pts
            # soundness: no true solution in the pruned box
            if any(x1 <= x <= x2 and y1 <= y <= y2 for x, y in true_sols):
                stats["missed"] += 1
            depth_hist[d] = depth_hist.get(d, 0) + 1
            continue
        if x2 - x1 <= 0 and y2 - y1 <= 0:
            stats["leaves"] += 1
            stats["surv_pts"] += 1
            if not any(x1 <= x <= x2 and y1 <= y <= y2 for x, y in true_sols):
                stats["fp_leaves"] += 1
            continue
        if x2 - x1 >= y2 - y1:
            m = (x1 + x2) // 2
            stack.append((x1, m, y1, y2, d + 1)); stack.append((m + 1, x2, y1, y2, d + 1))
        else:
            m = (y1 + y2) // 2
            stack.append((x1, x2, y1, m, d + 1)); stack.append((x1, x2, m + 1, y2, d + 1))
    return stats, total_pts, depth_hist


PS = [int(a) for a in sys.argv[1:]] or [13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
print(f"{'p':>4s} {'box pts':>8s} {'pruned%':>8s} {'leaves':>6s} {'leafFP':>6s} {'#sol(box)':>9s} {'missed':>6s}")
for p in PS:
    X1 = math.ceil(p / 4) + 1
    X2 = (3 * p) // 4
    # y range: y >= x, and y <= 2/(4/p - 1/x) which is largest at x = X1
    Y1 = X1
    Y2 = math.floor(2 / (Fr(4, p) - Fr(1, X1)))
    sols = solutions_in(X1, X2, Y1, Y2, p)
    # exact solutions include x<=y only (box is x in [X1,X2], y in [Y1,Y2]); also check x>y ones: same set by symmetry
    st, tot, hist = bnb(p, X1, X2, Y1, Y2, sols)
    pr = 100 * st["pruned_pts"] / tot
    print(f"{p:4d} {tot:8d} {pr:8.2f} {st['leaves']:6d} {st['fp_leaves']:6d} {len(sols):9d} {st['missed']:6d}")
