#!/usr/bin/env python3
"""z52b pass1 U06 (fix pass): concrete first steps for items Z0152, Z0794, Z0838, Z0854, Z0977, Z0987,
Z1003, Z1005, Z1007, Z1264, Z1461, Z2237, Z2239, Z2571, Z2862, Z2973, Z3085, Z3108, Z3124, Z3146, Z3176,
Z3177, Z3024, Z3132, Z3192, Z1762. Output: data/z52b/pass1/U06/fix_e.json"""
import json, math, cmath, random
from fractions import Fraction
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])  # sieve, factor, divisors, cert, menu_items
OUT = {}
def menu_items(p, Umax):
    out = []
    for u in range(1, Umax + 1):
        N = p + u
        for m in divisors(factor(N)):
            if m % (4 * u) == 4 * u - 1:
                out.append((u, (m + 1) // (4 * u)))
    return out
def sq_free_ok(n): return True

# ---------- U(p): unordered solutions x<=y<=z of 4/p = 1/x+1/y+1/z ----------
def sols_unordered(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        a = 4 * x - p
        if a <= 0: continue
        b = p * x
        if b * b // (b) != b: continue
        f = {}
        for q, e in factor(p).items(): f[q] = f.get(q, 0) + 2 * e
        for q, e in factor(x).items(): f[q] = f.get(q, 0) + 2 * e
        for d in divisors(f):
            dd = d
            e2 = b * b // dd
            if dd > e2: continue
            if (dd + b) % a or (e2 + b) % a: continue
            y = (b + dd) // a; z = (b + e2) // a
            if x <= y <= z: out.append((x, y, z))
    return sorted(set(out))
def U(p): return len(sols_unordered(p))
# brute check for small p
for p in [5, 13, 17, 29, 37, 41]:
    bf = set()
    for x in range(1, 3 * p + 1):
        for y in range(x, 3 * p * x + 1):
            num = 4 * x * y - p * (x + y)
            if num > 0 and (p * x * y) % num == 0 and False: pass
    # direct: z = p x y / (4xy - p(x+y))
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        for y in range(x, 4 * x * p + 2):
            den = 4 * x * y - p * (x + y)
            if den > 0 and (p * x * y) % den == 0:
                z = p * x * y // den
                if z >= y: bf.add((x, y, z))
    assert bf == set(sols_unordered(p)), (p, len(bf), len(sols_unordered(p)))
print("U brute check ok (p<=41)")
PR = [p for p in sieve(3000) if p % 4 == 1]
Up = {p: U(p) for p in PR}
OUT["U_sample"] = {p: Up[p] for p in PR[:12]}

# ---------- CF helpers ----------
def cf_len(fr):
    q = []
    a, b = fr.numerator, fr.denominator
    while b:
        q.append(a // b); a, b = b, a % b
    return len(q), q
def five_slice_count(p):
    return sum(1 for A in range(1, p) if cf_len(Fraction(A, p))[0] <= 3)

def cf_period_sqrt(n):
    a0 = math.isqrt(n); m, d, a = 0, 1, a0; per = 0
    while True:
        m = d * a - m; d = (n - m * m) // d; a = (a0 + m) // d; per += 1
        if a == 2 * a0: break
    return per
def L1(p):  # even real character chi_p = (./p), p = 1 mod 4: L(1) = -(1/sqrt p) sum (a/p) log|2 sin(pi a/p)|
    leg = lambda a: 1 if pow(a, (p - 1) // 2, p) == 1 else -1
    s = sum(leg(a) * math.log(abs(2 * math.sin(math.pi * a / p))) for a in range(1, p))
    return -s / math.sqrt(p)

def pearson(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    return sxy / math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
def resid(y, z):
    n = len(z); mz = sum(z) / n; my = sum(y) / n
    b = sum((a - mz) * (c - my) for a, c in zip(z, y)) / sum((a - mz) ** 2 for a in z)
    return [c - my - b * (a - mz) for a, c in zip(z, y)]

P2 = [p for p in PR if p <= 1500]
lu = [math.log(Up[p]) for p in P2]
lper = [math.log(cf_period_sqrt(p)) for p in P2]
ll = [math.log(abs(L1(p))) for p in P2]
S5 = {p: five_slice_count(p) for p in P2}
OUT["Z0794"] = {"n_primes": len(P2), "corr_logU_logPeriod": pearson(lu, lper), "corr_logU_logL": pearson(lu, ll),
                "corr_logPeriod_logL": pearson(lper, ll),
                "partial_logU_logPeriod_given_logL": pearson(resid(lu, ll), resid(lper, ll))}
print("Z0794", OUT["Z0794"])
# Z0838: five-slice count vs U(p) (Spearman via ranks)
def ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
    for k, i in enumerate(o): r[i] = k
    return r
s5 = [S5[p] for p in P2]; ur = [Up[p] for p in P2]
OUT["Z0838"] = {"n_primes": len(P2), "spearman_S5_U": pearson([float(v) for v in ranks(s5)], [float(v) for v in ranks(ur)])}
print("Z0838", OUT["Z0838"])
# Z1007: parity strings of CF quotients of five-slice A/p vs all A
par_sl = {}; par_all = {}
for p in P2[:150]:
    for A in range(1, p):
        n, q = cf_len(Fraction(A, p))
        key = "".join("e" if t % 2 == 0 else "o" for t in q)
        par_all[key] = par_all.get(key, 0) + 1
        if n <= 3: par_sl[key] = par_sl.get(key, 0) + 1
tot_sl = sum(par_sl.values()); tot_all = sum(par_all.values())
top = sorted(par_sl.items(), key=lambda kv: -kv[1])[:6]
OUT["Z1007"] = {"five_slice_total": tot_sl, "all_total": tot_all,
                "top_parity_strings_fiveslice": [(k, v, round(v / tot_sl, 3), round(par_all[k] / tot_all, 3)) for k, v in top]}
print("Z1007", OUT["Z1007"])

# ---------- Z0152 / Z1461 / Z1264: Engel expansion of 4/p ----------
def engel(fr, cap=60):
    r = fr; terms = []
    for _ in range(cap):
        if r == 0: break
        a = math.ceil(1 / r)
        terms.append(a)
        r = a * r - 1
    return terms
eng = {p: engel(Fraction(4, p)) for p in PR if p <= 10000}
lens = [len(v) for v in eng.values()]
from collections import Counter
OUT["Z0152"] = {"n_primes": len(eng), "length_dist": sorted(Counter(lens).items()), "max_len": max(lens)}
print("Z0152", OUT["Z0152"])
# Z1264: merging two consecutive Engel terms into a single unit fraction term (1/(a1..ak) + 1/(a1..ak a_{k+1}) type)
merge = 0; tried = 0
for p, t in eng.items():
    for i in range(len(t) - 1):
        tried += 1
        # 1/(P) + 1/(P*b) = (b+1)/(P b): a unit fraction iff (b+1) | P*b ... test directly
        P = 1
        for a in t[:i]: P *= a
        ti = Fraction(1, P * t[i]) + Fraction(1, P * t[i] * t[i + 1])
        if ti.numerator == 1: merge += 1
OUT["Z1264"] = {"adjacent_pairs_tried": tried, "merge_to_unit_fraction": merge}
print("Z1264", OUT["Z1264"])

# ---------- Z0854: zero-word families (n = 0 mod 105) ----------
def words(n):
    out = []
    for u in range(2, n + 3):
        t = 2
        while t * u - 1 <= n + u:
            den = t * u - 1
            if (n + u) % den == 0:
                v = (n + u) // den
                if v >= 2: out.append((t, u, v))
            t += 1
    return out
zero = [n for n in range(105, 3001, 105) if not words(n)]
sq = [m for m in range(1, 16) if not words(105 * m * m)]
OUT["Z0854"] = {"n_mult105_le3000": len(range(105, 3001, 105)), "zero_word_n_mult105": zero,
                "105m2_zero_for_m<=15": sq}
print("Z0854", OUT["Z0854"])

# ---------- Z0977: success of x (4/p - 1/x a sum of two unit fractions), transitions ----------
def two_term(p, x):
    a = 4 * x - p; b = p * x
    if a <= 0: return False
    f = {}
    for q, e in factor(p).items(): f[q] = f.get(q, 0) + 2 * e
    for q, e in factor(x).items(): f[q] = f.get(q, 0) + 2 * e
    for d in divisors(f):
        e2 = b * b // d
        if (d + b) % a == 0 and (e2 + b) % a == 0: return True
    return False
tr = 0; tot = 0; sr = 0
for p in [q for q in PR if 200 <= q <= 1500][:40]:
    xs = list(range(p // 4 + 1, 3 * p // 4 + 1))
    s = [two_term(p, x) for x in xs]
    sr += sum(s); tot += len(s)
    tr += sum(1 for i in range(len(s) - 1) if s[i] != s[i + 1])
OUT["Z0977"] = {"success_rate": round(sr / tot, 4), "transition_rate": round(tr / tot, 4), "n_x": tot}
print("Z0977", OUT["Z0977"])

# ---------- Z1003: trace of a product of three elementary matrices ----------
import sympy as sp
t, u, v = sp.symbols("t u v")
S = lambda k: sp.Matrix([[1, k], [0, 1]]); T = lambda k: sp.Matrix([[1, 0], [k, 1]])
tr_expr = sp.expand((S(u) * T(t) * S(v)).trace())
OUT["Z1003"] = {"trace_S(u)T(t)S(v)": str(tr_expr)}
print("Z1003", OUT["Z1003"])

# ---------- Z1005: SL2(Z/16) reached by three-letter continuant products ----------
N = 16
def mm(A, B):
    return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N,
            (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)
letters = [((a % N), 1, 1, 0) for a in range(N)]
cur = {(1, 0, 0, 1)}; reach = {}
for k in range(1, 4):
    cur = {mm(M, L) for M in cur for L in letters}
    reach[k] = len(cur)
sl2 = N ** 3 * (1 - 1 / 4)
OUT["Z1005"] = {"reachable_sizes_len1to3": reach, "SL2(Z/16)_order": int(sl2)}
print("Z1005", OUT["Z1005"])

# ---------- Z2237 / Z2239: denominator sums and unique-orbit primes ----------
p_small = [q for q in sieve(300) if q % 4 == 1][:12]
dsum = {q: Counter(x + y + z for x, y, z in sols_unordered(q)) for q in p_small}
OUT["Z2237"] = {str(q): sorted(dsum[q].items())[:6] for q in p_small[:4]}
uniq = [q for q in PR if Up[q] == 1]
OUT["Z2239"] = {"min_U": min(Up.values()), "argmin_U": [q for q in PR if Up[q]==min(Up.values())][:5], "count_U_eq_min": sum(1 for q in PR if Up[q]==min(Up.values())), "primes_1mod4_le3000": len(PR), "unique_unordered_orbit_primes": uniq[:30],
                "residues_mod840": Counter(q % 840 for q in uniq).most_common(6)}
print("Z2237", OUT["Z2237"]); print("Z2239", OUT["Z2239"])

# ---------- Z2571 / Z2862 / Z2973 / Z3085 / Z3108 / Z3024 / Z3177 / Z3192 / Z3124 / Z3146 / Z3132 / Z1762 ----------
HARD = {1, 121, 169, 289, 361, 529}
hp = [q for q in sieve(100000) if q % 4 == 1 and q % 840 in HARD and q > 5]
CMAX = 200
cert_mat = {p: [cert(C, p) for C in range(1, CMAX + 1)] for p in hp}
least = {p: next((C for C in range(1, CMAX + 1) if cert_mat[p][C - 1]), None) for p in hp}
OUT["Z2862"] = {"n_hard": len(hp), "none_upto_200": sum(1 for p in hp if least[p] is None),
                "max_least_C": max(c for c in least.values() if c), "least_C_by_class_top":
                sorted([(p, least[p]) for p in hp if least[p] and least[p] > 20], key=lambda z: -z[1])[:6]}
print("Z2862", OUT["Z2862"])
# Z3108: fraction of hard primes with no certificate C <= y
OUT["Z3108"] = {str(y): round(sum(1 for p in hp if least[p] is None or least[p] > y) / len(hp), 4)
                for y in [1, 2, 4, 8, 16, 32, 50, 100, 200]}
print("Z3108", OUT["Z3108"])
# Z3085: histogram of certificate C over dyadic ranges (all certificates C<=200, hard primes)
hist = Counter(int(math.log2(C)) for p in hp for C in range(1, CMAX + 1) if cert_mat[p][C - 1])
OUT["Z3085"] = {"dyadic_hist_floor_log2C": sorted(hist.items())}
print("Z3085", OUT["Z3085"])
# Z2973: profile vectors (C <= 12) and product-model comparison
K = 12
prof = Counter(tuple(int(cert_mat[p][C - 1]) for C in range(1, K + 1)) for p in hp)
rate = [sum(cert_mat[p][C - 1] for p in hp) / len(hp) for C in range(1, K + 1)]
def prod_prob(pr):
    q = 1.0
    for i, b in enumerate(pr): q *= rate[i] if b else (1 - rate[i])
    return q
top = prof.most_common(5)
OUT["Z2973"] = {"n_profiles": len(prof), "top5": [(list(k), c, round(c / len(hp), 4), round(prod_prob(k), 4)) for k, c in top]}
print("Z2973", OUT["Z2973"])
# Z3177: correlation matrix of families F_C (C in 1..6,8,10,12)
fam = [1, 2, 3, 4, 5, 6, 8, 10, 12]
M = [[round(pearson([float(cert_mat[p][a - 1]) for p in hp], [float(cert_mat[p][b - 1]) for p in hp]), 3) for b in fam] for a in fam]
OUT["Z3177"] = {"families": fam, "corr": M}
print("Z3177", fam, M[0])
# Z3024: greedy min set of moduli 4C covering hard primes in dyadic windows
def greedy_C(X):
    S = [p for p in hp if X <= p < 2 * X]
    left = set(S); chosen = []
    while left:
        best = max(range(1, CMAX + 1), key=lambda C: sum(1 for p in left if cert_mat[p][C - 1]))
        cov = {p for p in left if cert_mat[p][best - 1]}
        if not cov: break
        chosen.append(best); left -= cov
    return len(S), chosen, len(left)
OUT["Z3024"] = {str(X): greedy_C(X)[:2] + (greedy_C(X)[2],) for X in [1000, 10000]}
print("Z3024", OUT["Z3024"])
# Z3192 / Z1762: certificate (u,C)-density: slope of log count vs log u, log C for hard primes near 10^4
pts = []
for p in [q for q in hp if 5000 <= q <= 20000][:30]:
    for (u, C) in set(menu_items(p, 200)):
        pts.append((math.log(u), math.log(C), math.log(p)))
if pts:
    xu = [a for a, _, _ in pts]; xc = [b for _, b, _ in pts]
    OUT["Z1762"] = {"n_pairs": len(pts), "mean_logu_over_logp": round(sum(xu) / len(pts) / math.log(15000), 3),
                    "mean_logC_over_logp": round(sum(xc) / len(pts) / math.log(15000), 3),
                    "corr_logu_logC": round(pearson(xu, xc), 3)}
print("Z1762", OUT.get("Z1762"))
# Z3146: multiplicative energy of divisor classes mod e (hard primes <=1e4, e<=60)
def energy_div(N, e):
    D = [d % e for d in divisors(factor(N))]
    from collections import Counter as C2
    cnt = C2(D); E = 0
    keys = list(cnt)
    for a in keys:
        for b in keys:
            ab = a * b % e
            for c in keys:
                for d in keys:
                    if ab == c * d % e: E += cnt[a] * cnt[b] * cnt[c] * cnt[d]
    return E / len(D) ** 4
hp2 = [q for q in hp if q <= 10000][:15]
ratios = []
random.seed(2)
for p in hp2[:8]:
    e = 12
    N = (p + e) // 4
    if (p + e) % 4: continue
    rnd = random.randint(N // 2, N)
    ratios.append((p, round(energy_div(N, e), 4), round(energy_div(rnd, e), 4)))
OUT["Z3146"] = ratios
print("Z3146", ratios)
# Z3132: Legendre symbol of certificate divisors d over p (d = 4C p+1 divisor, d = -1 mod 4C)
cnt_leg = Counter()
for p in hp[:40]:
    for C in range(1, 20):
        N = 4 * C * p + 1
        for dv in divisors(factor(N)):
            if dv > 1 and dv % (4 * C) == 4 * C - 1:
                cnt_leg[("(d/p)", 1 if pow(dv % p, (p - 1) // 2, p) == 1 else -1)] += 1
OUT["Z3132"] = {f"{k[0]}{k[1]}": v for k, v in cnt_leg.items()}
print("Z3132", OUT["Z3132"])
# Z3124: per-class mean / min of R(p)/log^2 p (trial form) for hard primes <= 3000
def R_trial(p):
    tot = 0
    for u in range(1, (p + 1) // 3 + 2):
        for m in divisors(factor(p + u)):
            if m % (4 * u) == 4 * u - 1: tot += 1
    return tot
hp3 = [q for q in hp if q <= 3000]
Rv = {q: R_trial(q) for q in hp3}
byc = {}
for q in hp3: byc.setdefault(q % 840, []).append(Rv[q] / math.log(q) ** 2)
OUT["Z3124"] = {str(k): (round(sum(v) / len(v), 3), round(min(v), 3), len(v)) for k, v in sorted(byc.items())}
OUT["Z3124_zeroes"] = [q for q in hp3 if Rv[q] == 0]
print("Z3124", OUT["Z3124"], OUT["Z3124_zeroes"])
# Z2571: distinct-prime count omega(4Cp+1) on hard slices
om = [len(factor(4 * C * p + 1)) for p in hp[:120] for C in (1, 2, 3, 5, 7)]
OUT["Z2571"] = {"mean_omega": round(sum(om) / len(om), 3), "max_omega": max(om), "n": len(om)}
print("Z2571", OUT["Z2571"])
json.dump(OUT, open("data/z52b/pass1/U06/fix_e.json", "w"), indent=1, default=str)
print("written")
