"""R282 from-scratch statistics for SPARKS9 Prop 1.3 on output of review_r282_union.c (p W A B U, p = 1 mod 4).
(1) corr(A,B) after standardising within (2000-prime window) x (p mod 24); (2) B/E[B|cell] when A = 0 and in bottom 1% of A/E[A];
(3) partial corr of A/L^2, B/L^2 given one-hot(p mod 840), log p, log 47-smooth parts of p-1, p+1; then + log W."""
import sys, numpy as np
lo, hi = float(sys.argv[2]), float(sys.argv[3])
D = np.loadtxt(sys.argv[1], dtype=np.int64)
D = D[(D[:, 0] > lo) & (D[:, 0] <= hi)]
p, W, A, B, U = D.T; pf = p.astype(float); L2 = np.log(pf)**2
def cellstd(x, cells):
    z = np.empty(len(x))
    for c in np.unique(cells):
        m = cells == c; s = x[m].std()
        z[m] = (x[m] - x[m].mean())/(s if s > 0 else 1)
    return z
def cellmean(x, cells):
    out = np.empty(len(x))
    for c in np.unique(cells):
        m = cells == c; out[m] = x[m].mean()
    return out
cells = (np.arange(len(p)) // 2000) * 24 + p % 24
za, zb = cellstd(A.astype(float), cells), cellstd(B.astype(float), cells)
print(f"range ({lo:.0e},{hi:.0e}]: {len(p)} primes; corr(A,B) cell-standardised = {np.corrcoef(za, zb)[0,1]:.3f}")
EB, EA = cellmean(B.astype(float), cells), cellmean(A.astype(float), cells)
if (A == 0).any(): print(f"  A=0 ({(A==0).sum()} primes): mean B/E[B|cell] = {(B/EB)[A==0].mean():.2f}")
q = np.quantile(A/EA, 0.01); m = A/EA <= q
print(f"  bottom 1% of A/E[A]: B/E[B|cell] = {(B/EB)[m].mean():.2f}")
def smooth(x, P=47):
    s = np.ones(len(x))
    for q in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
        y = x.copy()
        while True:
            mm = y % q == 0
            if not mm.any(): break
            s[mm] *= q; y[mm] //= q
    return s
X = [np.ones(len(p)), np.log(pf), np.log(smooth(p-1)), np.log(smooth(p+1))]
oh = p % 840; X += [(oh == r).astype(float) for r in np.unique(oh)[1:]]
X = np.column_stack(X)
def pc(X):
    ra = A/L2 - X @ np.linalg.lstsq(X, A/L2, rcond=None)[0]
    rb = B/L2 - X @ np.linalg.lstsq(X, B/L2, rcond=None)[0]
    return np.corrcoef(ra, rb)[0, 1]
print(f"  partial corr given controls: {pc(X):.3f};  + log W: {pc(np.column_stack([X, np.log(W)])):.3f}")
print(f"  W/L^2 mean {np.mean(W/L2):.3f}, 1% quantile {np.quantile(W/L2,0.01):.3f}, min W (p>1e5) {W[p>1e5].min() if (p>1e5).any() else '-'}; U/W mean {np.mean(U/W):.3f}")
# (4) collider check: control by the size of the COMPLEMENT R = W - U (words with no coordinate = 0 mod 4) instead of W
R = (W - U).astype(float)
print(f"  partial corr given controls + log(W-U): {pc(np.column_stack([X, np.log(R)])):.3f};  + log W and log(W-U): {pc(np.column_stack([X, np.log(W), np.log(R)])):.3f}")
# multinomial null: given W, split A,B as independent thinnings? report corr of A,B within narrow W bins
