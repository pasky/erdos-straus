"""R44a: recompute O11 §4 s-weighted mean of h(M) and the share of Omega# from l<=L^2 (from scratch)."""
import math, sys
from review_o11a_graded import atoms
for T in map(int, sys.argv[1:]):
    L = math.log(T); S = Om = Om_small = 0.0
    for (M, D, fM) in atoms(T):
        s = math.gcd(M, 4 * D + 1) / M
        for l in fM: s *= l / (l - 1)
        hs = {l: sum(1 / i for i in range(1, v + 1)) for l, v in fM.items()}
        S += s; Om += s * sum(hs.values()); Om_small += s * sum(h for l, h in hs.items() if l <= L * L)
    print(f"T={T} S'={S:.2f} Omega={Om:.1f} mean h={Om/S:.3f} share l<=L^2: {Om_small:.0f}/{Om:.0f} loglogT={math.log(L):.3f} L/logL={L/math.log(L):.3f}")
