# z58 DISPROOF §6.2: is the zero law universal in the local mean?  Compare observed vs predicted zeros (law
# exp(-a mu^beta) with the R8 fit a = 0.398, beta = 1.014 and the smoothed cell means of z58_disproof_zerolaw.py)
# split by (i) class of one mod 840 / other Mordell classes / non-Mordell, (ii) n_p > 23 cells (bits = 31 and square
# mod 840) vs rest, (iii) decade; for R8 and for R.
# Run: uv run --with numpy --with scipy python scripts/z58_disproof_lawclass.py data/z58/disproof/cells_2e8.txt
import sys, math
import numpy as np
sys.argv += ['1e4']
exec(open('scripts/z58_disproof_zerolaw.py').read().split('mu8 = (s8')[0])   # reuse loading + smoothing
a, b = 0.398, 1.014
M = {1, 121, 169, 289, 361, 529}
cls = np.where(a840 == 1, 0, np.where(np.isin(a840, list(M)), 1, 2))
deep = (bits == 31) & np.isin(a840, list(M))
dec = np.floor(hb / 2 * math.log10(2)).astype(int)
for name, S, Z, MU in [("R8", s8, z8, MU8), ("R", sR, zR, MUR)]:
    pred = n * np.exp(-a * MU ** b)
    print(f"# {name}: observed / predicted zeros by group (p >= 1e4)")
    for gname, g in [("class 1 mod 840", cls == 0), ("other Mordell", cls == 1), ("non-Mordell", cls == 2),
                     ("n_p > 23 (Mordell & bits 31)", deep), ("not deep", ~deep)]:
        m = keep & g
        print(f"  {gname:30s} obs {Z[m].sum():6.0f}  pred {np.nansum(pred[m]):9.2f}  primes {n[m].sum():.0f}")
    for d in range(4, 9):
        m = keep & (dec == d)
        print(f"  decade 1e{d}: obs {Z[m].sum():.0f} pred {np.nansum(pred[m]):.2f};  class1: obs {Z[m & (cls==0)].sum():.0f} pred {np.nansum(pred[m & (cls==0)]):.2f}")
