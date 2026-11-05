# Factor the non-square zeros listed in data/z58/ffield/star_q{q}_n{n}.zeros.
# Columns: idx coeffs type R_full R_s1 R_s1mod4 R_s3mod4.  Polynomials are decoded from idx (base-q digits, low..high,
# plus the leading 1), never from the coefficient string; comment lines (#) are skipped.
# Usage: uv run --with cypari2 python scripts/z58_ffield_factor.py q n [col]   (col 4 = R_full, the default)
import sys, cypari2
pari = cypari2.Pari()
q, n = int(sys.argv[1]), int(sys.argv[2]); col = int(sys.argv[3]) if len(sys.argv) > 3 else 4
def decode(idx):
    c = []
    for _ in range(n): c.append(idx % q); idx //= q
    return c + [1]
for line in open(f"data/z58/ffield/star_q{q}_n{n}.zeros"):
    if not line.strip() or line.startswith("#"): continue
    w = line.split()
    if int(w[col - 1]) != 0: continue
    coeffs = decode(int(w[0]))
    f = pari("Mod(1,%d)*(%s)" % (q, "+".join(f"{c}*x^{i}" for i, c in enumerate(coeffs) if c)))
    fa = pari.factor(f)
    degs = [(int(pari.poldegree(fa[0][i])), int(fa[1][i])) for i in range(len(fa[0]))]
    print(w[2], w[0], sorted(degs), pari.lift(f))
