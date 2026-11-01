# z53 HCSHIFTS (N2): line-independence test from the sampler masks.
# For each scale, empirical P(HC > X) = P(no line x in C ∩ [4,X] fires) vs the product of the marginal miss
# probabilities prod_x P(line x misses), and the same with the marginals conditioned on the small-prime class pattern.
import sys, math
C128 = [x for x in range(4, 129) if x % 4 == 0 or x % 8 == 7]
def load(fn):
    rows = []
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split()
        if len(f) < 13: continue
        rows.append((int(f[0]), int(f[1]), int(f[11], 16) | int(f[12], 16)))
    return rows
Xs = [7, 8, 12, 15, 16, 20, 23, 24, 28, 31, 32, 40, 48, 64]
for fn in sys.argv[1:]:
    rows = load(fn); n = len(rows)
    fire = [0] * len(C128)
    for _, _, m in rows:
        for i in range(len(C128)):
            if m >> i & 1: fire[i] += 1
    print(f"== {fn}: n={n}, p≈{rows[0][0]:.3g}")
    print(" X   emp P(HC>X)   prod-marginals   ratio   (#HC>X)")
    for X in Xs:
        k = sum(1 for x in C128 if x <= X)
        mask = (1 << k) - 1
        emp = sum(1 for _, _, m in rows if m & mask == 0)
        prod = 1.0
        for i in range(k): prod *= 1 - fire[i] / n
        print(f"{X:3d}  {emp/n:.3e}   {prod:.3e}   {emp/n/prod if prod>0 else float('nan'):7.2f}   {emp}")
    print(" marginal miss probabilities m_x (x: m):", " ".join(f"{x}:{1-fire[i]/n:.3f}" for i, x in enumerate(C128) if x <= 64 or x % 32 == 0))
