"""z52b pass1 U05 Z1587: polynomial ES identities for n = g(t) ∈ {t²+1, 4t²+1, t²+t+1}: search x,y,z ∈ Z[t] of degree ≤2 with
coefficients in {-1,0,1,2} with 4xyz ≡ g(t)(xy+yz+zx) as polynomials (checked at 12 integer points, then exact check by
evaluation at 40 points), positive for t≥2. Also checks repo grep for prior work."""
import itertools, numpy as np
from fractions import Fraction
coefs = [-1, 0, 1, 2]
polys = [(a, b, c) for a in coefs for b in coefs for c in coefs]   # a + b t + c t^2
T = np.arange(2, 14, dtype=object)
def ev(poly, t): a, b, c = poly; return a + b*t + c*t*t
gs = {"t^2+1": lambda t: t*t+1, "4t^2+1": lambda t: 4*t*t+1, "t^2+t+1": lambda t: t*t+t+1}
ptab = {k: [ev(p, t) for t in range(2, 14)] for k, p in zip(range(len(polys)), polys)}
arr = np.array([[int(ev(p, t)) for t in range(2, 14)] for p in polys], dtype=object)
for name, g in gs.items():
    gv = np.array([g(t) for t in range(2, 14)], dtype=object)
    hits = []
    for i, j, k in itertools.product(range(len(polys)), repeat=3):
        if i > j or j > k: continue
        x, y, z = arr[i], arr[j], arr[k]
        if any(v <= 0 for v in x) or any(v <= 0 for v in y) or any(v <= 0 for v in z): continue
        lhs = 4*x*y*z; rhs = gv*(x*y + y*z + z*x)
        if all(l == r for l, r in zip(lhs, rhs)):
            hits.append((polys[i], polys[j], polys[k]))
    print(f"n = {name}: polynomial ES identities with degree ≤2, coeffs in {coefs}: {len(hits)}", hits[:3])
