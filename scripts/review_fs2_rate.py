"""review_fs2_rate.py (R218, from scratch): continuum exponent max_p min_route phi(p) - 1/2 (units of log q, per unit s)
of the Lemma 1.6 bounds, on a grid of step 1/G in p = (a, z, y)/s, t = 1 - a - z - y, b = y + t >= a.
Class bound O(1) iff d < rho, or 3 rho > n (Lenstra), or rho > d(n-d)/n (Coppersmith limit; symmetric in d <-> n-d).
EVIDENCE only (finite grid, asymptotic class thresholds). usage: uv run python scripts/review_fs2_rate.py G r,r,..."""
import sys
import numpy as np
G = int(sys.argv[1]); rs = [int(x) for x in sys.argv[2].split(',')]
g = np.arange(0, G + 1) / G
A, Z, Y = np.meshgrid(g, g, g, indexing='ij')
Tt = 1 - A - Z - Y; Bb = Y + Tt
ok = (Tt > 0) & (Bb >= A) & (A > 0)
A, Z, Y, Tt, Bb = A[ok], Z[ok], Y[ok], Tt[ok], Bb[ok]
xl = lambda x: np.where(x > 0, x * np.log(np.maximum(x, 1e-300)), 0.0)
Bn = lambda d, e: xl(d + e) - xl(d) - xl(e)
Gm = lambda x, y, z: xl(x + y + z) - xl(x) - xl(y) - xl(z)
def cls(n, d, rho, L):  # exponent of class-count bound (units log q)
    O1 = (d < rho) | (3 * rho > n) | (rho > d * (n - d) / np.maximum(n, 1e-300))
    return np.where(O1, 0.0, Bn(d, n - d) / L)
for r in rs:
    L = r * np.log(3)
    e = [Z + Y + A, Z + A + Tt, Y + Tt + Z, Y + Tt + A, Tt + Gm(Z, A, Bb) / L,
         Z + Y + cls(1 + 2 * Y + Z, A + Y + Z, Y + Z, L),
         A + Y + cls(1 + Y, A + Y + Z, A + Y, L),
         Z + A + cls(np.ones_like(A), A + Y + Z, A + Z, L),
         Bb + Y + cls(1 + Y, Bb + Y + Z, Bb + Y, L),
         Z + Bb + cls(Z + 2 * Bb, Bb + Y + Z, Z + Bb, L),
         Tt + A + cls(1 - A, Bb, Tt, L), Tt + Bb + cls(1 - Bb, A, Tt, L),
         Tt + Bn(A, 1 - A) / L + cls(1 - A, Bb, Tt, L), Tt + Bn(Bb, 1 - Bb) / L + cls(1 - Bb, A, Tt, L),
         Y + Tt + Bn(A, 1 - A) / L, Y + Tt + Bn(Bb, 1 - Bb) / L, Z + Tt + Bn(A, Bb) / L,
         Z + Tt + cls(A + Bb, A, Tt, L), Tt + Bn(Z, 1 - Z) / L + cls(A + Bb, A, Tt, L)]
    m = np.min(np.array(e), axis=0); i = np.argmax(m)
    print(f"r={r}: max_p min_route - 1/2 = {m[i] - 0.5:+.4f} at (a,z,y,t)=({A[i]:.3f},{Z[i]:.3f},{Y[i]:.3f},{Tt[i]:.3f})")
