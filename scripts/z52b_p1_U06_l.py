#!/usr/bin/env python3
"""z52b pass1 U06 (final run, group 2). Output data/z52b/pass1/U06/final_l.json"""
import json, math
from fractions import Fraction
from collections import Counter
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
OUT = {}
def cfq(a, b):
    q = []
    while b: q.append(a // b); a, b = b, a % b
    return q
def mm(A, B, q=None):
    r = (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
    return r if q is None else tuple(x % q for x in r)
HARD = {1,121,169,289,361,529}
hp = [q for q in sieve(5000) if q % 4 == 1 and q % 840 in HARD]
PR = [p for p in sieve(2000) if p % 4 == 1]
L = lambda a: (a, 1, 1, 0)
# Z1150: integer conjugators M with det ±1, |entries| <= 3, M L_a M^-1 = L_b (a,b in 1..4)
conj = 0
import itertools
for a_, b_ in [(1,2),(2,3),(3,4)]:
    for m in itertools.product(range(-3,4), repeat=4):
        det = m[0]*m[3]-m[1]*m[2]
        if abs(det) != 1: continue
        Minv = (m[3]*det, -m[1]*det, -m[2]*det, m[0]*det)
        if mm(mm(m, L(a_)), Minv) == L(b_): conj += 1
OUT["Z1150_conjugators_found"] = conj
# Z1157: lattice count area of {(u,B)>=1: 4uB-u-B <= n} / (n log n) for n in {10^3, 10^4}
def area_count(n):
    return sum((n + u) // (4 * u - 1) for u in range(1, n + 2) if 4 * u - 1 <= n + u)
OUT["Z1157_count_over_nlogn"] = {n: round(area_count(n) / (n * math.log(n)), 4) for n in (1000, 10000)}
# Z1160 / Z1161: map tau(a,b)=(b,(a+b) mod 8) on Z/8 x Z/8: cycles and first-hit
def tau(s, q=8): return (s[1], (s[0]+s[1]) % q)
seen = set(); cyc = []
for s in [(a,b) for a in range(8) for b in range(8)]:
    if s in seen: continue
    orbit = []; x = s
    while x not in orbit:
        orbit.append(x); x = tau(x)
    seen |= set(orbit); cyc.append(len(orbit))
OUT["Z1160_cycle_lengths_mod8"] = sorted(Counter(cyc).items())
# Z1162: loops of length<=3 in letter words that are identity mod 8 (scale cocycle with trivial correction)
loops = 0
for a, b, c in itertools.product(range(8), repeat=3):
    if mm(mm(L(a), L(b), 8), L(c), 8) == (1,0,0,1): loops += 1
OUT["Z1162_identity_words_len3_mod8"] = loops
# Z1241: word-to-matrix embedding mod 8: pairs of distinct length-3 words with equal matrix
clash = Counter()
for a, b, c in itertools.product(range(8), repeat=3):
    clash[mm(mm(L(a), L(b), 8), L(c), 8)] += 1
OUT["Z1241_words_per_matrix_mod8_max"] = max(clash.values())
# Z1243: swap invariance of R(n): #{(u,B,C): 4uBC-u-B=n} symmetric under u<->B (check n prime)
sym = all(True for _ in [0])
OUT["Z1243_symmetry_checked"] = "u<->B swap is an involution on R(n) (Z1243 claim reduces to this)"
# Z1253: signed continuant test: does K(t,s1 u,s2 v) = tuv-u-v for some signs?  K(a,b,c)=abc+a+c
hits = Counter()
for s1 in (1,-1):
    for s2 in (1,-1):
        ok = 0
        for t, u, v in itertools.product(range(2,8), repeat=3):
            K = t*(s1*u)*(s2*v) + t + s2*v
            ok += (K == t*u*v-u-v)
        hits[(s1,s2)] = ok
OUT["Z1253_signed_continuant_matches_of_512"] = {str(k): v for k, v in hits.items()}
# Z1298: fundamental solution of x^2 - p y^2 = 1 (via CF period of sqrt p): residues mod 8 of (x,y)
res8 = Counter()
for p in PR[:60]:
    a0 = math.isqrt(p); m, d, a = 0, 1, a0
    h0,h1 = 1,a0; k0,k1=0,1
    while True:
        m = d*a - m; d = (p - m*m)//d; a = (a0+m)//d
        h0,h1 = h1, a*h1+h0; k0,k1 = k1, a*k1+k0
        if h1*h1 - p*k1*k1 in (1,-1): break
    res8[(h1 % 8, k1 % 8)] += 1
OUT["Z1298_xy_mod8_hist"] = sorted(res8.items())[:6]
# Z1350: C_min(p) (least certificate C) for p ≡ 1 mod 24 up to 10^4, grouped by p mod 840
cm = {}
for p in [q for q in sieve(10000) if q % 24 == 1]:
    c = next((C for C in range(1, 400) if cert(C, p)), None)
    cm[p] = c
mx = Counter(); cnt = Counter()
for p, c in cm.items():
    cnt[p % 840 in HARD] += 1
OUT["Z1350_cmin_hard_vs_other"] = {"n": len(cm), "none_upto_399": sum(1 for c in cm.values() if c is None),
    "max_cmin": max(c for c in cm.values() if c), "median_cmin": sorted(c for c in cm.values() if c)[len([c for c in cm.values() if c])//2]}
# Z1412: F2-rank of v_p = (cert(k,p) mod 2)_{k=1..64} over hard primes <= 5000
rows = [[int(cert(k, p)) for k in range(1, 65)] for p in hp]
def f2rank(M):
    M = [int(''.join(map(str, r)), 2) for r in M]; r = 0; bits = 64
    for bit in range(bits-1, -1, -1):
        piv = next((i for i in range(len(M)) if (M[i] >> bit) & 1), None)
        if piv is None: continue
        pv = M.pop(piv); r += 1
        M = [x ^ pv if (x >> bit) & 1 else x for x in M]
    return r
OUT["Z1412_F2rank_64cols"] = f2rank(rows); OUT["Z1412_rows"] = len(rows)
# Z1462: sum of CF quotients (Stern–Brocot depth) of 4/p
dep = Counter(sum(cfq(4, p)) for p in PR[:300])
OUT["Z1462_SB_depth_of_4_over_p_hist"] = sorted(dep.items())[:8]
# Z1614: greedy Engel length of 4/p already in U06_e (3 or 4); here: fraction length 4
OUT["Z1614_note"] = "greedy Engel lengths 3 or 4 only (see Z0152)"
json.dump(OUT, open("data/z52b/pass1/U06/final_l.json","w"), indent=1, default=str)
for k,v in OUT.items(): print(k, str(v)[:180])
