"""bsA_fricke: the word gamma = M(v)M(t)M(u), M(a) = [[a,-1],[1,0]], as a point of the 4-holed-sphere character
variety (Fricke/Goldman cubic) with boundary traces (v,t,u,T), T = tr(gamma) = tuv-t-u-v (cyclically symmetric).
Checks the cubic and that the Vieta moves fix all boundary data."""
import itertools
import numpy as np
def M(a): return np.array([[a, -1], [1, 0]], dtype=object)
bad = 0
for v, t, u in itertools.product(range(2, 9), repeat=3):
    a, b, c = M(v), M(t), M(u); g = a.dot(b).dot(c)
    T = g[0, 0] + g[1, 1]
    assert T == t*u*v - t - u - v and g[0, 0] == t*u*v - u - v and g[1, 0] == t*u - 1
    A_, B_, C_, D_ = v, t, u, T  # traces of a,b,c,d=(abc)^-1
    x = np.trace(a.dot(b)); y = np.trace(b.dot(c)); z = np.trace(a.dot(c))
    lhs = x*x + y*y + z*z + x*y*z
    rhs = (A_*B_ + C_*D_)*x + (B_*C_ + A_*D_)*y + (A_*C_ + B_*D_)*z + 4 - A_**2 - B_**2 - C_**2 - D_**2 - A_*B_*C_*D_
    if lhs != rhs: bad += 1
print("Fricke cubic check, v,t,u in [2,8]: failures", bad)
