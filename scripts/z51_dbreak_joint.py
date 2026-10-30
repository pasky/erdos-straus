# z51 dbreak round 4: joint behaviour of the band residual R (file of "n R H Q") and a disjoint top layer X (file of
# "n C X W" from z51_dbreak_candidates.c run on the same n). Usage: python3 z51_dbreak_joint.py Rfile Xfile mu
import sys, math
R = [tuple(map(float, l.split())) for l in open(sys.argv[1])]
T = [tuple(map(float, l.split())) for l in open(sys.argv[2])]
mu = float(sys.argv[3])
assert len(R) == len(T) and all(int(a[0]) == int(b[0]) for a, b in zip(R, T))
r = [a[1] for a in R]; x = [b[2] for b in T]; n = len(r)
mr = sum(r) / n; mx = sum(x) / n
cov = sum((a - mr) * (b - mx) for a, b in zip(r, x)) / n
vr = sum((a - mr) ** 2 for a in r) / n; vx = sum((b - mx) ** 2 for b in x) / n
print(f"n={n} corr(R_band, X_layer)={cov / math.sqrt(vr * vx):+.4f} (s.e. ~ {1/math.sqrt(n):.4f})")
p0 = sum(1 for b in x if b == 0) / n
sel = [b for a, b in zip(r, x) if a <= -mu / 2]
print(f"P(X=0)={p0:.5f}; given R<=-mu/2 (count {len(sel)}): P(X=0)={sum(1 for b in sel if b == 0) / len(sel):.5f}, mean X {sum(sel) / len(sel):.3f} vs {mx:.3f}")
sel = [a for a, b in zip(r, x) if b == 0]
pr = sum(1 for a in r if a <= -mu / 2) / n
print(f"given X=0 (count {len(sel)}): mean R {sum(sel) / len(sel):.3f} vs {mr:.3f}; P(R<=-mu/2) {sum(1 for a in sel if a <= -mu / 2) / len(sel):.4f} vs {pr:.4f}")
pj = sum(1 for a, b in zip(r, x) if b == 0 and a <= -mu / 2) / n
print(f"P(both) {pj:.5f} vs product {p0 * pr:.5f}  ratio {pj / (p0 * pr) if p0 * pr > 0 else float('nan'):.3f}")
