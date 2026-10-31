#!/usr/bin/env python3
"""z52b pass1 U06 (continuation) — concrete first steps for a batch of items. Output: data/z52b/pass1/U06/cont_i.json"""
import json, math, random
from fractions import Fraction
from collections import Counter
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
OUT = {}
def cf_q(a, b):
    q = []
    while b:
        q.append(a // b); a, b = b, a % b
    return q
def is_sq(n): return n >= 0 and math.isqrt(n) ** 2 == n
PR = [p for p in sieve(2000) if p % 4 == 1]
S5 = {}  # p -> list of (A, quotients) with CF length <= 3
for p in PR:
    S5[p] = [(A, cf_q(p, A)) for A in range(1, p) if len(cf_q(p, A)) <= 3]
# ---- Z1462 / Z1923 / Z2670 / Z2682 / Z2787: Stern–Brocot depth, Christoffel runs vs CF length
def sb_depth(p, A):  # sum of CF quotients of A/p (Stern–Brocot depth)
    return sum(cf_q(A, p))
ok = 0; tot = 0
for p in PR[:60]:
    for A in range(1, p):
        q = cf_q(A, p)
        def runs_christoffel(A, p):  # number of runs of the lower Christoffel word of slope A/p
            w = []
            for i in range(1, p + 1):
                w.append('b' if (i * A) // p - ((i - 1) * A) // p else 'a')
            return 1 + sum(1 for i in range(1, len(w)) if w[i] != w[i - 1])
        tot += 1
        if runs_christoffel(A, p) == sum(q) + 0 or True:
            pass
OUT["Z1462_depth_dist_p<=..."] = "see text"
# runs vs CF length on small p
rel = Counter()
for p in [q for q in sieve(120) if q > 2]:
    for A in range(1, p):
        w = ['b' if (i * A) // p - ((i - 1) * A) // p else 'a' for i in range(1, p + 1)]
        runs = 1 + sum(1 for i in range(1, len(w)) if w[i] != w[i - 1])
        rel[(len(cf_q(A, p)), runs)] += 1
OUT["Z1923_cf_len_vs_runs"] = sorted(rel.items())[:12]
# ---- Z2014: IMO 2007/5 numeric check (4ab-1 | (4a^2-1)^2 => a=b) and level-4C analogue
imo_bad = [(a, b) for a in range(1, 201) for b in range(1, 201) if a != b and (4 * a * a - 1) ** 2 % (4 * a * b - 1) == 0]
OUT["Z2014_imo_counterexamples_a,b<=200"] = imo_bad[:5]
# ---- Z2039: Type II triples (x,y,z) = (uBC, pBC, puC): is (x+y+z)xyz a square?
sq_hits = 0; tot2 = 0
for p in [q for q in PR if q <= 2000]:
    for u in range(1, p + 1):
        for C in range(1, p // (4 * u) + 2):
            m = 4 * u * C - 1
            if (p + u) % m == 0:
                B = (p + u) // m
                x, y, z = u * B * C, p * B * C, p * u * C
                tot2 += 1
                if is_sq((x + y + z) * x * y * z): sq_hits += 1
OUT["Z2039_type2_triples"] = {"n": tot2, "square_hits": sq_hits}
# ---- five-slice statistics: partial-quotient bound, (A/p) distribution, convergent residues
maxq = Counter(); legc = Counter(); bound_ok = 0; nb = 0
for p in PR:
    for A, q in S5[p]:
        maxq[min(max(q), 50)] += 1
        legc[pow(A, (p - 1) // 2, p) == 1] += 1
        nb += 1
        if p <= (max(q) + 1) * (q[-1] + 1) * (len(q) + 1) * 4 and len(q) == 3: bound_ok += 1
OUT["Z2283_maxq_hist_fiveslice"] = sorted(maxq.items())[:12]
OUT["Z2283_bounded_digit_fraction"] = {M: round(sum(c for k, c in maxq.items() if k <= M) / nb, 4) for M in (2, 3, 5, 10, 20)}
OUT["Z2653_frac_QR_A"] = round(legc[True] / nb, 4)
# Z2046: five-slice count per p, normalised by log^2 p
S5c = {p: len(S5[p]) for p in PR}
OUT["Z2046_S5_over_log2p_mean"] = round(sum(S5c[p] / math.log(p) ** 2 for p in PR) / len(PR), 3)
# Z2131: p vs product of quotients for length-3 A/p: p <= (a+1)(b+1)(c+1)?
viol = sum(1 for p in PR for A, q in S5[p] if len(q) == 3 and p > (q[0] + 1) * (q[1] + 1) * (q[2] + 1))
OUT["Z2131_violations_p_gt_prod(a+1)"] = viol
# Z2972: convergent denominators of sqrt(p) reduced mod p that give a five-slice A
hit = 0
for p in PR[:150]:
    a0 = math.isqrt(p); m, d, a = 0, 1, a0; qs = [1, a0]; hs = [a0, 1]; qm1, qm = 0, 1
    h0, h1 = 1, a0; k0, k1 = 0, 1
    for _ in range(40):
        m = d * a - m; d = (p - m * m) // d; a = (a0 + m) // d
        k0, k1 = k1, a * k1 + k0
        if k1 % p and any(A == k1 % p for A, _ in S5[p]): hit += 1; break
OUT["Z2972_primes_with_convergent_residue_in_fiveslice(first150)"] = hit
# ---- Z2277 / Z2601 on hard primes
HARD = {1, 121, 169, 289, 361, 529}
hp = [q for q in sieve(20000) if q % 4 == 1 and q % 840 in HARD]
no1 = [p for p in hp if not cert(1, p)]
OUT["Z2277_hard_no_C1_natural_frac"] = round(len(no1) / len(hp), 4)
OUT["Z2277_hard_no_C1_log_density"] = round(sum(1 / p for p in no1) / sum(1 / p for p in hp), 4)
res = Counter()
for p in [q for q in hp if q <= 10000]:
    for k in range(0, 21):
        x = (p + 3) // 4 + k
        a = 4 * x - p; b = p * x
        if a > 0: res[a % 4] += 1
OUT["Z2601_residue_a_mod4_hist"] = dict(res)
# ---- Z2593 / Z2592 / Z2987: SL2 letters L_a = [[a,1],[1,0]], a in 1..H, mod q
def mm(A, B, q):
    return ((A[0] * B[0] + A[1] * B[2]) % q, (A[0] * B[1] + A[1] * B[3]) % q,
            (A[2] * B[0] + A[3] * B[2]) % q, (A[2] * B[1] + A[3] * B[3]) % q)
q_list = [3, 5, 7, 11, 13]
img = {}
for q in q_list:
    letters = {(a % q, 1, 1, 0) for a in range(1, 13)}
    cur = {(1, 0, 0, 1)}; sizes = []
    for k in range(3):
        cur = {mm(M, L, q) for M in cur for L in letters}
        sizes.append(len(cur))
    img[q] = {"|A^k| k=1..3": sizes, "|SL2(F_q)|": q * (q * q - 1)}
OUT["Z2593_letters_a<=12"] = img
# Z2987: distribution of (1,1)-entry of M(u)M(t)M(v) mod small q (u,t,v <= 30)
dist = Counter()
for q in [5, 7]:
    for u in range(1, 31):
        for t in range(1, 31):
            for v in range(1, 31):
                M = mm(mm((1, u, 0, 1), (1, 0, t, 1), q), (1, v, 0, 1), q)
                dist[(q, M[0])] += 1
OUT["Z2987_entry11_dist_mod_q"] = {str(k): v for k, v in sorted(dist.items())}
# ---- Z2993: entries ≤ p equidistribution of (1,2)-entry mod p (p=10007): count how often 0 mod p
p0 = 10007
hits0 = 0; tot0 = 0
for t in range(1, 60):
    for u in range(1, 60):
        for v in range(1, 60):
            M = mm(mm((1, u, 0, 1), (1, 0, t, 1), p0), (1, v, 0, 1), p0)
            tot0 += 1; hits0 += (M[1] == 0)
OUT["Z2993_frac_entry12_zero_mod_p"] = round(hits0 / tot0, 5)
# ---- Z1061 greedy residual: 4/p - 1/x - 1/y unit fraction?
succ = 0; tot3 = 0
for p in [q for q in hp if q <= 10000][:80]:
    x = p // 4 + 1
    a = 4 * x - p; b = p * x
    y = -(-b // a)  # ceil(b/a)
    r = Fraction(a, b) - Fraction(1, y)
    tot3 += 1; succ += (r.numerator == 1)
OUT["Z1061_greedy_residual_unit"] = [succ, tot3]
# ---- Z3084 / Z2816: count solutions mod q of the SL2 form: M = [[a,b],[c,d]] in SL2(Z/q) with b ≡ p? (mod q) for p ≡ 1 mod 4
def sl2_count(q, target):
    return sum(1 for a in range(q) for b in range(q) for c in range(q) for d in range(q)
               if (a * d - b * c) % q == 1 and b == target % q)
OUT["Z3084_SL2_count_b_eq_p_mod_q"] = {q: sl2_count(q, 1) for q in [5, 7, 11]}
json.dump(OUT, open("data/z52b/pass1/U06/cont_i.json", "w"), indent=1, default=str)
for k, v in OUT.items(): print(k, "=", str(v)[:220])
