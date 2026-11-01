"""Z2865 driver: Weyl-symmetrised δ-blocks Ẑ_δ of all ES Seifert spaces M(-3;(x-1)/x,(y-1)/y,(z-1)/z), 5<=n<=NMAX, z<=ZMAX.
Tests which features depend on n only (vs. on the solution)."""
import sys, json
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z52d_p2_ZF1_Z2865_zhat import es_solutions, es_delta_block, fmt
from fractions import Fraction as Fr
NMAX, ZMAX, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
rows = []
for n in range(5, NMAX + 1):
    for (x, y, z) in es_solutions(n):
        if z > ZMAX:
            continue
        ordc, sc, S, ser = es_delta_block(n, x, y, z, nterms=6)
        ex = list(ser)
        e0 = ex[0]
        rows.append({"n": n, "sol": [x, y, z], "sigma2": x*y+y*z+z*x, "ord_ec": ordc, "selfconj": sc,
                     "Delta": str(e0), "Delta_mod1": str(e0 - (e0.numerator // e0.denominator)),
                     "rel_exps": [str(e - e0) for e in ex], "coefs": [str(c) for c in ser.values()]})
json.dump(rows, open(OUT, "w"), indent=0)
byn = defaultdict(list)
for r in rows:
    byn[r["n"]].append(r)
print("n  #sols  distinct Δmod1   first-two-terms always 1-q?  min/max 3rd rel exponent  selfconj-count")
for n, rs in byn.items():
    d = sorted(set(r["Delta_mod1"] for r in rs), key=Fr)
    two = all(r["coefs"][:2] == ["1", "-1"] and r["rel_exps"][:2] == ["0", "1"] for r in rs)
    third = [Fr(r["rel_exps"][2]) for r in rs if len(r["rel_exps"]) > 2]
    print(n, len(rs), d, two, (min(third), max(third)) if third else None, sum(r["selfconj"] for r in rs))
