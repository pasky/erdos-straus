"""Level-wise filter from the 6 exceptional classes mod 720720 (task O100).
usage: m13c_level.py Mmax stages(comma primes) [complete] [out.txt]
Stage p: refine every survivor x mod L at p (children x+L t, units only); drop children covered by a class
with modulus M | L*p (brute-force tables M <= Mmax, mordell_dfs engine).  With 'complete', the final
survivors are re-tested with m13c_witness.witness_all (all M | L, no size cap)."""
import sys, time
import numpy as np
import mordell_dfs as D
from m13c_witness import witness_all
EXC = [112561, 352801, 380881, 418321, 473761, 483841]
Mmax = int(sys.argv[1]); stages = [int(s) for s in sys.argv[2].split(',')]
complete = len(sys.argv) > 3 and sys.argv[3] == 'complete'
out = sys.argv[4] if len(sys.argv) > 4 else None
D.BOUND[0] = Mmax
L = 720720; X = list(EXC); t0 = time.time()
for p in stages:
    q = p
    if L % p == 0:
        e = 0
        while L % p ** (e + 1) == 0: e += 1
        q = p ** (e + 1)
    mods, L2 = D.new_moduli(L, q, p, Mmax)
    newX = []
    t = np.arange(p, dtype=np.int64)
    for x in X:
        T = t[(x % p + (L % p) * t) % p != 0]
        cov = D.covered_by(x, L, T, mods)
        newX += [x + L * int(tt) for tt, c in zip(T, cov.tolist()) if not c]
    X, L = newX, L2
    print(f"stage {p}: L={L} survivors {len(X)} t={time.time()-t0:.0f}s", flush=True)
if complete:
    X = [x for x in X if not witness_all(x, L)]
    print(f"complete witness (all M | L): survivors {len(X)} t={time.time()-t0:.0f}s", flush=True)
from collections import Counter
print("by root:", Counter(x % 720720 for x in X))
if out:
    open(out, 'w').write(f"{L}\n" + "\n".join(map(str, X)) + "\n")
