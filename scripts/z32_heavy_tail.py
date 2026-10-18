"""O262: where would the first counterexample sit if the zero law were heavier-tailed than measured?
P0 = exp(-0.535 mu^beta) with mu = c L^3 for every prime (c = 0.037: hardest m = 4 cell, Type II only;
c = 0.074: crude Type I + II, f_I ~ f_II).  Prints expected failures in [1e8,1e18) and [1e18,1e60)."""
import math
for c in (0.037, 0.074):
    for beta in (0.91, 0.6, 0.55, 0.5, 0.45, 0.4):
        lo = hi = 0.0
        for k in range(80, 600):
            xa, xb = 10**(k/10), 10**((k+1)/10); L = math.log(math.sqrt(xa*xb))
            v = (xb - xa)/L*math.exp(-0.535*(c*L**3)**beta)
            if k < 180: lo += v
            else: hi += v
        print(f'c={c} beta={beta}: E#[1e8,1e18)={lo:.3g}  E#[1e18,1e60)={hi:.3g}')
