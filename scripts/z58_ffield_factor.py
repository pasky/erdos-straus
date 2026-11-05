# Factor the non-square zeros listed in data/z58/ffield/star_q{q}_n{n}.zeros (family columns: R_full R_s1 R_s1mod4 R_s3mod4).
# Usage: uv run --with cypari2 python scripts/z58_ffield_factor.py q n [col]   (col 4 = full family; default)
import sys, cypari2
pari = cypari2.Pari()
q, n = int(sys.argv[1]), int(sys.argv[2]); col = int(sys.argv[3]) if len(sys.argv) > 3 else 4
fn = f"data/z58/ffield/star_q{q}_n{n}.zeros"
for line in open(fn):
    w = line.split()
    if int(w[col - 1 + 0]) != 0 if False else int(w[col - 1]) != 0: continue
    coeffs = [int(c) for c in w[1]]  # low..high
    poly = "+".join(f"{c}*x^{i}" for i, c in enumerate(coeffs) if c)
    f = pari(f"Mod(1,{q})*({poly})")
    fa = pari.factor(f)
    degs = [(int(pari.poldegree(fa[0][i])), int(fa[1][i])) for i in range(len(fa[0]))]
    print(w[2], w[1], sorted(degs), pari.lift(f))
