"""z52b pass-1 batch U08, correlation / structure checks.

  Z1042 / Z1396  pairwise correlations of the per-parameter success events
                 S_C(p) := exists d | 4Cp+1, d > 1, d ≡ -1 (mod 4C)   ((★)-type level-C certificate), C <= 40,
                 over primes p ≡ 1 (mod 4), 100 < p <= 1e5. Grouped by gcd(C, D) and compared with independence.
  Z1130          overlap of two solutions of 4/p (shared denominators), primes p ≡ 1 (4), p <= 3000 (uses enum module).
  Z0862 / Z1272  all-squarefree solution existence; existence of a primitive solution (gcd(x,y,z)=1), primes p <= 3000.
  Z0304          4/n = sum of three reciprocals of nonzero squares over F_q (q prime <= 200): which residues fail.
  Z0143          4/n = 1/x + 1/y + 1/z^2 for 2 <= n <= 300, searched over z <= 60 (two-term reduction via divisors).

Run: uv run --with numpy --with sympy python scripts/z52b_p1_U08_corr.py
"""
import json, math, os, importlib.util
import numpy as np
from sympy import primerange, factorint, divisors, isprime
from itertools import combinations

OUT = "data/z52b/pass1/U08"
os.makedirs(OUT, exist_ok=True)
res = {}

# ---------- Z1042 / Z1396 ----------
Cmax = 40
ps = [p for p in primerange(101, 100001) if p % 4 == 1]
S = np.zeros((len(ps), Cmax + 1), dtype=np.int8)
for i, p in enumerate(ps):
    for C in range(1, Cmax + 1):
        N = 4 * C * p + 1
        m = 4 * C
        ok = False
        for d in divisors(N):
            if d > 1 and d % m == m - 1:
                ok = True
                break
        S[i, C] = ok
# marginal success rate per C and pairwise phi-correlations
rates = {C: float(S[:, C].mean()) for C in range(1, Cmax + 1)}
pairs = []
for C, D in combinations(range(1, Cmax + 1), 2):
    a, b = S[:, C].astype(float), S[:, D].astype(float)
    if a.std() == 0 or b.std() == 0:
        continue
    r = float(np.corrcoef(a, b)[0, 1])
    pairs.append((C, D, math.gcd(C, D), r))
by_gcd = {}
for C, D, g, r in pairs:
    by_gcd.setdefault(g, []).append(r)
gcd_summary = {int(g): dict(n=len(v), mean_corr=round(float(np.mean(v)), 4), max_abs=round(float(np.max(np.abs(v))), 4))
               for g, v in sorted(by_gcd.items())}
top = sorted(pairs, key=lambda t: -abs(t[3]))[:8]
# joint-success check for independence: P(C and D both fail) vs product of failure rates
fail_both_obs, fail_both_ind = [], []
for C, D, g, r in pairs[:]:
    fb = float(np.mean((S[:, C] == 0) & (S[:, D] == 0)))
    fi = float(np.mean(S[:, C] == 0) * np.mean(S[:, D] == 0))
    fail_both_obs.append(fb / fi if fi > 0 else float('nan'))
res["Z1042_Z1396"] = dict(n_primes=len(ps), Cmax=Cmax, rate_C1=round(rates[1], 4), rate_C2=round(rates[2], 4),
                          rates_first10={C: round(rates[C], 4) for C in range(1, 11)},
                          corr_by_gcd=gcd_summary,
                          top_abs_pairs=[dict(C=C, D=D, gcd=g, corr=round(r, 4)) for C, D, g, r in top],
                          ratio_P_bothfail_over_indep_median=round(float(np.nanmedian(fail_both_obs)), 4),
                          ratio_P_bothfail_over_indep_max=round(float(np.nanmax(fail_both_obs)), 4))

# ---------- Z1130: solution overlap ----------
spec = importlib.util.spec_from_file_location("enum", "scripts/z52b_p1_U08_enum.py")
en = importlib.util.module_from_spec(spec); spec.loader.exec_module(en)
ov_hist = {}
npairs = 0
sq_fail = []
prim_all = []
prim_primes = []
for p in primerange(5, 3001):
    if p % 4 != 1:
        continue
    sols = en.reps(4, p)
    if not sols:
        continue
    # squarefree / primitive
    def sqf(n):
        return all(e == 1 for e in factorint(n).values())
    sf = [s for s in sols if all(sqf(d) for d in s)]
    if not sf:
        sq_fail.append(p)
    prim_all.append(any(math.gcd(math.gcd(x, y), z) == 1 for x, y, z in sols))
    prim_primes.append(p)
    sets = [set(s) for s in sols]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            k = len(sets[i] & sets[j])
            ov_hist[k] = ov_hist.get(k, 0) + 1
            npairs += 1
res["Z1130"] = dict(pairs=npairs, shared_denominator_hist={int(k): v for k, v in sorted(ov_hist.items())},
                    frac_pairs_share_ge1=round(sum(v for k, v in ov_hist.items() if k >= 1) / npairs, 4))
res["Z0862"] = dict(primes_no_all_squarefree_solution_le3000=sq_fail,
                    primes_without_primitive_solution_le3000=[p for p, ok in zip(prim_primes, prim_all) if not ok],
                    n_primes=len(prim_all))

# ---------- Z0304: squares over F_q ----------
fail_q = {}
for q in primerange(3, 201):
    if q == 2:
        continue
    sq = {(x * x) % q for x in range(1, q)}
    s3 = set()
    for a in sq:
        for b in sq:
            for c in sq:
                s3.add((a + b + c) % q)
    # 4/n for n in F_q^* ranges over all nonzero residues (4 is a nonzero square mod odd q... check value)
    bad = [r for r in range(1, q) if r not in s3]
    if bad:
        fail_q[q] = bad[:8]
res["Z0304"] = dict(primes_q_le_200_with_failures=fail_q, n_primes_with_failure=len(fail_q))

# ---------- Z0143: 4/n = 1/x + 1/y + 1/z^2 ----------
def two_term(a, b):
    """solutions of a/b = 1/x + 1/y with x<=y (positive integers), via (ax-b)(ay-b)=b^2."""
    out = []
    fac = factorint(b)
    fac2 = {q: 2 * e for q, e in fac.items()}
    for u in divisors(b * b):
        if (u + b) % a:
            continue
        v = (b * b) // u
        if (v + b) % a:
            continue
        x = (u + b) // a
        y = (v + b) // a
        if x <= y:
            out.append((x, y))
    return out

unsolved = []
first_z = {}
for n in range(2, 301):
    found = None
    for z in range(1, 61):
        a = 4 * z * z - n
        if a <= 0:
            continue
        b = n * z * z
        if two_term(a, b):
            found = z
            break
    if found is None:
        unsolved.append(n)
    else:
        first_z[n] = found
res["Z0143"] = dict(n_range="2..300", z_max=60, unsolved_n=unsolved[:40], n_unsolved=len(unsolved),
                    max_first_z=max(first_z.values()) if first_z else None,
                    z_hist={int(z): sum(1 for v in first_z.values() if v == z) for z in sorted(set(first_z.values()))[:12]})

json.dump(res, open(os.path.join(OUT, "corr.json"), "w"), indent=1)
print(json.dumps(res, indent=1)[:6000])
