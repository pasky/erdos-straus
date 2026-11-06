"""z60 RAYCLASS: correlate per-prime counts with L(1, chi_{-4p}) = pi*h(-4p)/(2 sqrt p)  (w = 2).
usage: uv run --with cypari2 --with numpy --with scipy python scripts/z60_rayclass_lcorr.py COUNTS_FILE [ZEROS_FILE]
COUNTS_FILE lines: p R Sq_u Sq_C S1  (from z60_rayclass_fam.c range mode)."""
import sys, math
import cypari2, numpy as np
from scipy.stats import spearmanr
pari = cypari2.Pari()
def Lval(p):
    h = int(pari.qfbclassno(-4 * p))
    return math.pi * h / (2 * math.sqrt(p)), h
rows = [list(map(int, l.split())) for l in open(sys.argv[1]) if l.strip()]
P = np.array([r[0] for r in rows]); R = np.array([r[1] for r in rows]); Su = np.array([r[2] for r in rows])
SC = np.array([r[3] for r in rows]); S1 = np.array([r[4] for r in rows])
L = np.array([Lval(int(p))[0] for p in P])
print(f"n = {len(P)} primes p = 1 (4) in [{P.min()}, {P.max()}]")
print(f"mean L(1,chi_-4p) = {L.mean():.4f}")
for name, X in [("R", R), ("Sq_u", Su), ("Sq_C", SC), ("S1", S1), ("R - Sq_u - Sq_C", R - Su - SC)]:
    rho, pv = spearmanr(X, L)
    # ratio of means in top vs bottom L-quartile
    q1, q3 = np.quantile(L, [0.25, 0.75])
    lo, hi = X[L <= q1].mean(), X[L >= q3].mean()
    print(f"{name:16s} mean {X.mean():8.3f}  spearman(X, L) = {rho:+.3f} (p={pv:.1e})  mean|L<=Q1 = {lo:7.3f}  mean|L>=Q3 = {hi:7.3f}  ratio {hi/lo:.3f}")
# R/S1 with log-ratio regression slope: log X ~ a + b log L
for name, X in [("R", R), ("S1", S1), ("Sq_C", SC), ("Sq_u", Su)]:
    m = X > 0
    b = np.polyfit(np.log(L[m]), np.log(X[m]), 1)[0]
    print(f"elasticity d log {name} / d log L = {b:+.3f}  (on X>0, {m.sum()} primes)")
if len(sys.argv) > 2:
    Z = [int(x) for x in open(sys.argv[2]) if x.strip() and not x.startswith('#')]
    LZ = np.array([Lval(z)[0] for z in Z])
    print(f"zeros file {sys.argv[2]}: {len(Z)} primes; L at zeros: mean {LZ.mean():.4f} median {np.median(LZ):.4f}; "
          f"fraction with L < 0.5: {np.mean(LZ < 0.5):.3f} (control fraction {np.mean(L < 0.5):.3f}); max {LZ.max():.3f}")
