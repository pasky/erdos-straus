"""z52b pass-1 batch U08, last redo checks:
 Z2538  exact (Fraction) verification of every enumerated solution of 4/p, primes p ≡ 1 (4), 5 < p <= 3000
 Z1125  rhythm: 4/p = sum of unit fractions with denominators dividing 60 (a 60-slot cycle), p ≡ 1 (4), 5 < p <= 3000
 Z2989  sum-product window check: e prime ≡ 3 (4), N_e = (p+e)/4 integer; fraction of prime factors q of N_e that are QR mod e
        vs 1/2 (random baseline), over p ≤ 20000
 Z2680  Legendre Ising on F_p: bichromatic edges (x, x+1) of the Legendre-symbol configuration, and largest monochromatic arc, p ≡ 1 (4) ≤ 2000
Output: data/z52b/pass1/U08/final.json"""
import json, os, math
from fractions import Fraction
import numpy as np
from sympy import primerange, factorint, legendre_symbol
import importlib.util
spec = importlib.util.spec_from_file_location("enum", "scripts/z52b_p1_U08_enum.py")
en = importlib.util.module_from_spec(spec); spec.loader.exec_module(en)
OUT = "data/z52b/pass1/U08"; res = {}
# Z2538
bad = 0; tot = 0
for p in primerange(7, 3001):
    if p % 4 != 1: continue
    for x, y, z in en.reps(4, p):
        tot += 1
        if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p): bad += 1
res["Z2538"] = dict(solutions_checked=tot, failures=bad)
# Z1125: denominators dividing 60
divs60 = [d for d in range(1, 61) if 60 % d == 0]
hits = []
for p in primerange(7, 201):
    if p % 4 != 1: continue
    ok = any(Fraction(4, p) == Fraction(1, a) + Fraction(1, b) + Fraction(1, c) for a in divs60 for b in divs60 for c in divs60 if a <= b <= c)
    if ok: hits.append(p)
res["Z1125"] = dict(primes_checked=len([p for p in primerange(7, 201) if p % 4 == 1]), solvable_with_denominators_dividing60=hits)
# Z2989
rng = np.random.default_rng(3)
fr_QR, fr_all, n = [], [], 0
for e in primerange(5, 200):
    if e % 4 != 3: continue
    for p in primerange(5, 20001):
        if (p + e) % 4: continue
        N = (p + e) // 4
        if N < 2: continue
        fac = factorint(N)
        for q in fac:
            if q == e or e % q == 0: continue
            if legendre_symbol(q % e, e) == 1: fr_QR.append(1)
            else: fr_QR.append(0)
        n += 1
arr = np.array(fr_QR, float)
res["Z2989"] = dict(e_range="3 mod 4 primes 5..199", N_windows=n, prime_factor_count=len(arr),
                    frac_QR=round(float(arr.mean()), 4), binom_sd_at_half=round(float(0.5 / math.sqrt(len(arr))), 5))
# Z2680
rs = []
for p in primerange(5, 2001):
    if p % 4 != 1: continue
    col = [1 if legendre_symbol(x, p) == 1 else -1 for x in range(1, p)]
    bich = sum(1 for i in range(len(col) - 1) if col[i] != col[i + 1])
    # longest monochromatic arc
    best = cur = 1
    for i in range(1, len(col)):
        cur = cur + 1 if col[i] == col[i - 1] else 1
        best = max(best, cur)
    rs.append((bich / (len(col) - 1), best / p))
res["Z2680"] = dict(n=len(rs), mean_bichromatic_edge_frac=round(float(np.mean([a for a, b in rs])), 4),
                    mean_longest_arc_over_p=round(float(np.mean([b for a, b in rs])), 4),
                    max_longest_arc_over_p=round(float(np.max([b for a, b in rs])), 4))
os.makedirs(OUT, exist_ok=True)
json.dump(res, open(f"{OUT}/final.json", "w"), indent=1)
print(json.dumps(res, indent=1))

# Z2989 variant: prime factors q > 100 only (small q dominate the unweighted count via fixed (q/e) signs); windows for
# the same p overlap across e, so the sample is not independent: treat the sigma as optimistic.
fr_big = []
for e in primerange(5, 200):
    if e % 4 != 3: continue
    for p in primerange(5, 20001):
        if (p + e) % 4: continue
        N = (p + e) // 4
        if N < 2: continue
        for q in factorint(N):
            if q == e or e % q == 0 or q <= 100: continue
            fr_big.append(1 if legendre_symbol(q % e, e) == 1 else 0)
arr_b = np.array(fr_big, float)
res["Z2989_q_gt_100"] = dict(prime_factor_count=len(arr_b), frac_QR=round(float(arr_b.mean()), 4),
                             z_iid=round(float((arr_b.mean() - 0.5) / (0.5 / math.sqrt(len(arr_b)))), 2))
json.dump(res, open(f"{OUT}/final.json", "w"), indent=1)
print(res["Z2989_q_gt_100"])
