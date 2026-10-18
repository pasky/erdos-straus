"""R282: collider check for SPARKS9 Prop 1.3 'shared factor = |W(p)|'. Input: review_r282_union.c output (p W A B U F).
Also verifies F (ES-five count) = #{words with Legendre((tu-1)/p) = -1} for small p by brute force."""
import sys, numpy as np
D = np.loadtxt(sys.argv[1], dtype=np.int64); lo, hi = float(sys.argv[2]), float(sys.argv[3])
# brute-force sigma check
for row in D[D[:, 0] < 3000]:
    p, Wc, F = int(row[0]), int(row[1]), int(row[5]); cnt = tot = 0
    for t in range(1, p + 3):
        for u in range(1, p + 3):
            m = t*u - 1
            if m < 1: continue
            if m - u > p: break
            if (p + u) % m == 0:
                tot += 1; cnt += pow(m % p, (p-1)//2, p) == p - 1
    assert tot == Wc and cnt == F, (p, tot, Wc, cnt, F)
D = D[(D[:, 0] > lo) & (D[:, 0] <= hi)]
p, W, A, B, U, F = D.T; L2 = np.log(p.astype(float))**2
X = np.column_stack([np.ones(len(p)), np.log(p)] + [(p % 840 == r).astype(float) for r in np.unique(p % 840)[1:]])
def res(y, Z): return y - Z @ np.linalg.lstsq(Z, y, rcond=None)[0]
def pc(Z): return np.corrcoef(res(A/L2, Z), res(B/L2, Z))[0, 1]
for name, extra in [("none", []), ("log W", [np.log(W)]), ("log(W-U)", [np.log(W-U)]), ("log W+ (sigma=+1 words)", [np.log(W-F)]),
                    ("log(F-U) (sigma=-1, not in union)", [np.log(np.maximum(F-U, 1))]), ("log F (=W-)", [np.log(F)])]:
    print(f"({lo:.0e},{hi:.0e}] partial corr(A,B | p mod 840, log p, {name}) = {pc(np.column_stack([X]+extra)):.3f}")
