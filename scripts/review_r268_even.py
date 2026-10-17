"""R268 from-scratch: all solutions of k/n = 1/x + 1/y + 1/z (x <= y <= z), integer arithmetic, numpy over y.
Checks the item-(vi) claim 'at 131, 241 every solution of 4/p has an odd denominator' (<=> 8/p unsolvable)."""
import sys
import numpy as np


def sols(n, k):
    out = []
    for x in range(n // k + 1, 3 * n // k + 1):
        num, den = k * x - n, n * x          # remainder num/den
        if num <= 0: continue
        ylo = max(x, den // num + 1); yhi = 2 * den // num
        if ylo > yhi: continue
        y = np.arange(ylo, yhi + 1, dtype=object if den * yhi > 2**62 else np.int64)
        zden = num * y - den
        ok = (zden > 0) & ((den * y) % np.where(zden > 0, zden, 1) == 0)
        for yy in y[ok]:
            yy = int(yy); z = den * yy // (num * yy - den)
            if z >= yy: out.append((x, yy, z))
    return out


if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]]:
        S4 = sols(n, 4); S8 = sols(n, 8)
        ev = [s for s in S4 if all(t % 2 == 0 for t in s)]
        assert sorted(ev) == sorted(tuple(2 * t for t in s) for s in S8)
        print(f"n={n}: #sol(4/n)={len(S4)}, all-even {len(ev)}, #sol(8/n)={len(S8)}; "
              f"solutions of 4/n with ALL denominators odd: {sum(all(t % 2 for t in s) for s in S4)}")
