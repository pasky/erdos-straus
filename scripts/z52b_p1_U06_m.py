#!/usr/bin/env python3
"""z52b pass1 U06 (redo run): concrete steps for redo items. Output data/z52b/pass1/U06/redo_m.json"""
import json, math, time, random
from fractions import Fraction
from collections import Counter
import sympy
exec(open("scripts/z52b_p1_U06_i.py").read().split("# ---- Z1462")[0])  # S5, PR, cf_q, cert/menu helpers
exec(open("scripts/z52b_p1_U06_e.py").read().split("# ---------- CF helpers")[0].split("OUT = {}")[1]) if False else None
OUT = {}
def mm(A, B, q):
    return ((A[0]*B[0]+A[1]*B[2])%q,(A[0]*B[1]+A[1]*B[3])%q,(A[2]*B[0]+A[3]*B[2])%q,(A[2]*B[1]+A[3]*B[3])%q)
def menu_items(p, Umax):
    out = []
    for u in range(1, Umax + 1):
        for m in divisors(factor(p + u)):
            if m % (4 * u) == 4 * u - 1: out.append((u, (m + 1) // (4 * u)))
    return out
def sols_unordered(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        a = 4 * x - p; b = p * x
        if a <= 0: continue
        f = {}
        for q, e in factor(p).items(): f[q] = f.get(q, 0) + 2 * e
        for q, e in factor(x).items(): f[q] = f.get(q, 0) + 2 * e
        for d in divisors(f):
            e2 = b * b // d
            if d > e2: continue
            if (d + b) % a or (e2 + b) % a: continue
            y = (b + d) // a; z = (b + e2) // a
            if x <= y <= z: out.append((x, y, z))
    return sorted(set(out))
HARD = {1,121,169,289,361,529}
hp = [q for q in sieve(5000) if q % 4 == 1 and q % 840 in HARD]
hp1e4 = [q for q in sieve(10000) if q % 4 == 1 and q % 840 in HARD]
# Z1998: random ~200-digit prime p ≡ 1 (mod 840) class; certificates (u,C) with uC <= 10^4
random.seed(7)
t0 = time.time()
p = 0
while True:
    base = random.randrange(10**199, 10**200)
    base -= base % 840; base += 1
    if base % 840 in HARD and sympy.isprime(base): p = base; break
cnt = 0; T = 10**4
for u in range(1, T + 1):
    for C in range(1, T // u + 1):
        if (p + u) % (4 * u * C - 1) == 0: cnt += 1
OUT["Z1998"] = {"digits": len(str(p)), "class_mod840": p % 840, "certs_uC_le_1e4": cnt, "seconds": round(time.time()-t0, 1)}
# Z2211: U(p) (unordered ES solutions) vs number of unordered reps of p as ab+bc+ca (0<a<b<c)
def reps_ab(n):
    c = 0
    for a in range(1, int(math.isqrt(n))+2):
        for b in range(a+1, n+2):
            if a*b + a*b*0 > n: break
            for cc in range(b+1, n+2):
                v = a*b + b*cc + cc*a
                if v == n: c += 1
                if v > n: break
    return c
pr = [q for q in sieve(300) if q % 4 == 1]
OUT["Z2211"] = [(q, len(sols_unordered(q)), reps_ab(q)) for q in pr[:8]]
# Z2225: least witness u for ES primes, split by Stern-prime (A060003 odd Stern primes) membership
stern = {1,3,17,137,227,977,1187,1493,5777,5993}
lw = {"stern": [], "other": []}
for q in [x for x in sieve(2000) if x % 4 == 1][:120]:
    mi = sorted(menu_items(q, 200))
    if mi: lw["stern" if q in stern else "other"].append(mi[0][0])
OUT["Z2225"] = {k: (len(v), round(sum(v)/len(v), 2) if v else None) for k, v in lw.items()}
# Z2241: split-hyperbola enumerator for fixed u vs brute force, p <= 200
ok = 0; tot = 0
for p in [x for x in sieve(200) if x % 4 == 1]:
    for u in range(1, 30):
        brute = {(4*u*C-1) for C in range(1, 200) if (p+u) % (4*u*C-1) == 0}
        split = {d for d in divisors(factor(p+u)) if d % (4*u) == 4*u-1 and d >= 4*u-1}
        tot += 1; ok += (brute == split)
OUT["Z2241"] = {"agree": ok, "total": tot}
# Z2256: depth-bounded enumeration: primes with a solution of max denominator <= D*p, D in {1,2,5}
dep = {}
for q in [x for x in sieve(1500) if x % 4 == 1][:100]:
    s = sols_unordered(q)
    dep[q] = min(max(t) for t in s) / q if s else None
OUT["Z2256_min_maxden_over_p"] = {"n": len(dep), "max_over_min": round(max(v for v in dep.values() if v), 3),
    "first_over_2": [q for q, v in dep.items() if v and v > 2][:5]}
# Z2342: exponent of minimal max-denominator vs p
ex = []
for q in [x for x in sieve(1500) if x % 4 == 1][-40:]:
    s = sols_unordered(q)
    m = min(max(t) for t in s)
    ex.append(math.log(m) / math.log(q))
OUT["Z2342_log_minmax_over_logp"] = {"mean": round(sum(ex)/len(ex), 3), "max": round(max(ex), 3)}
# Z2438: sunflowers among the smallest Type II certificate supports (prime sets) for hard primes <= 5000
sets = []
for q in hp:
    mi = [(u, C) for (u, C) in set(menu_items(q, 60))]
    if not mi: continue
    u, C = min(mi, key=lambda t: t[0]*t[1])
    B = (q + u) // (4*u*C - 1)
    supp = frozenset(sympy.primefactors(u*B*C) + sympy.primefactors(q*B*C) + sympy.primefactors(q*u*C))
    sets.append((q, supp))
sf = 0
for i in range(len(sets)):
    for j in range(i+1, len(sets)):
        for k in range(j+1, len(sets)):
            A, B2, C2 = sets[i][1], sets[j][1], sets[k][1]
            core = A & B2 & C2
            if core and (A - core) and (B2 - core) and (C2 - core) and not ((A-core)&(B2-core)) and not ((A-core)&(C2-core)) and not ((B2-core)&(C2-core)):
                sf += 1
OUT["Z2438"] = {"n_sets": len(sets), "sunflowers_3petals": sf}
# Z2536: smoothness yield of 4Cp+1 (hard p <= 5000, C <= 50): fraction with all prime factors <= 1000
sm = 0; tot5 = 0
for q in hp[:150]:
    for C in range(1, 51):
        N = 4*C*q+1; tot5 += 1
        if max(factor(N).keys()) <= 1000: sm += 1
OUT["Z2536_smooth_fraction_1000"] = round(sm / tot5, 4)
# Z2537: time split for certificate check: trial division vs modular multiplication on 10^6 items
t1 = time.time(); c1 = sum(1 for n in range(10**9, 10**9+10**6) if n % 7 == 0); t_div = time.time()-t1
t2 = time.time(); c2 = sum(1 for n in range(10**9, 10**9+10**6) if pow(n, 3, 10**9+7) == 1); t_pow = time.time()-t2
OUT["Z2537_time_div_vs_pow_1e6"] = {"div": round(t_div, 3), "pow": round(t_pow, 3)}
# Z2820: six derived sequences (first terms) + OEIS term query attempts recorded separately
U = [sum(1 for u in range(2, n+3) for t in range(2, n+3) if (n+u) % (t*u-1) == 0 and (n+u)//(t*u-1) >= 2) for n in range(1, 25)]
OUT["Z2820_words_U(n)_n<=24"] = U
OUT["Z2820_R(n)_odd_n<=25"] = [sum(1 for u in range(1, n+2) for C in range(1, n+2) if (n+u) % (4*u*C-1) == 0) for n in range(3, 26, 2)]
OUT["Z2820_Upr_first"] = [len(sols_unordered(q)) for q in pr[:12]]
# Z2857: least-squares fit of U(p) on basis (1, log p, log^2 p, tau(p-1), tau(p+1), tau(4p+1), (2/p), (3/p)) over primes 1 mod 4 <= 2000
import numpy as np
PRU = [x for x in sieve(2000) if x % 4 == 1 and x > 5]
Y = np.array([len(sols_unordered(q)) for q in PRU], dtype=float)
def leg(a, q): return 1 if pow(a % q, (q-1)//2, q) == 1 else -1
X = np.array([[1, math.log(q), math.log(q)**2, len(divisors(factor(q-1))), len(divisors(factor(q+1))),
               len(divisors(factor(4*q+1))), leg(2, q), leg(3, q)] for q in PRU], dtype=float)
coef, res, rk, sv = np.linalg.lstsq(X, Y, rcond=None)
OUT["Z2857_fit_resid_rms"] = round(float(np.sqrt(np.mean((X @ coef - Y)**2))), 3)
OUT["Z2857_Y_std"] = round(float(Y.std()), 3)
# Z3016: P(cert(C,pq) | cert(C,p) and cert(C,q)) vs base, hard p,q <= 2000
hh = [q for q in sieve(2000) if q % 4 == 1 and q % 840 in HARD]
cc = {}
for C in range(1, 7):
    both = nb = base_n = base = 0
    for p_ in hh:
        a = cert(C, p_)
        for q_ in hh[:20]:
            if q_ == p_: continue
            b = cert(C, q_)
            if a and b:
                nb += 1; both += cert(C, p_*q_)
    cc[C] = (nb, both)
OUT["Z3016_cert_pq_given_both"] = cc
# Z3092: R(n) mod m determined by n mod A? (odd n <= 1200, A in {8,12,24,48})
def Rn(n):
    return sum(1 for u in range(1, (n+1)//3+2) for m in divisors(factor(n+u)) if m % (4*u) == 4*u-1)
Rv = {n: Rn(n) for n in range(3, 1201, 2)}
det = {}
for A in (8, 12, 24, 48):
    for m in (2, 4, 8):
        ok = 0; tot6 = 0
        for r in range(A):
            vals = {Rv[n] % m for n in Rv if n % A == r}
            if vals: tot6 += 1; ok += (len(vals) == 1)
        det[f"A{A}_m{m}"] = f"{ok}/{tot6}"
OUT["Z3092_R_mod_m_determined_by_n_mod_A"] = det
# Z3106: cert(C,·) rate per hard class for C <= 24 (periodicity in C?)
rate = {}
for r in sorted(HARD):
    ps = [q for q in hp1e4 if q % 840 == r]
    rate[r] = [round(sum(cert(C, q) for q in ps) / max(1, len(ps)), 2) for C in range(1, 25)]
OUT["Z3106_rates_C1_12"] = {str(k): v[:12] for k, v in rate.items()}
# Z3164: (★) restricted to prime C: hard primes <= 5000 with no prime C <= 200 certificate
pc = [C for C in range(2, 201) if sympy.isprime(C)]
OUT["Z3164_prime_C_failures_hard_le5000"] = [q for q in hp if not any(cert(C, q) for C in pc)]
# Z3176 / Z3187: coverage by (u,B) with u <= U (all C) for hard primes <= 10^4
cov = {}
for U_ in (1, 2, 5, 20, 100):
    cov[U_] = round(sum(1 for q in hp1e4 if menu_items(q, U_)) / len(hp1e4), 4)
OUT["Z3176_coverage_by_umax"] = cov
# Z0641: distinct products of three letters L_a (a mod N) in SL2(Z/N) vs |SL2(Z/N)|
c641 = {}
for N_ in range(2, 13):
    letters = {(a % N_, 1, 1, 0) for a in range(N_)}
    cur = {(1,0,0,1)}
    for k in range(3):
        cur = {mm(M, Lt, N_) for M in cur for Lt in letters}
    sl2 = N_**3 * (1 - Fraction(1, N_**2))
    c641[N_] = (len(cur), int(sl2))
OUT["Z0641_words3_vs_SL2"] = c641
# Z0987: alternative integral branch: for solutions of 4uBC-u-B=q, is u (given B,C) or B (given u,C) integral and different?
alt = 0; tot7 = 0
for q in hp[:60]:
    for (u, C) in set(menu_items(q, 200)):
        B = (q + u) // (4*u*C - 1); tot7 += 1
        u2 = (q + B) / (4*B*C - 1)
        if u2 != u: alt += 1
OUT["Z0987_alt_branch_mismatch"] = [alt, tot7]
json.dump(OUT, open("data/z52b/pass1/U06/redo_m.json","w"), indent=1, default=str)
for k,v in OUT.items(): print(k, str(v)[:160])
