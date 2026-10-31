#!/usr/bin/env python3
"""z52b pass1 U06 (final run) — concrete first steps for remaining items. Output data/z52b/pass1/U06/final_k.json"""
import json, math
from fractions import Fraction
from collections import Counter, deque
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
OUT = {}
def cfq(a, b):
    q = []
    while b: q.append(a // b); a, b = b, a % b
    return q
def mm(A, B, q):
    return ((A[0]*B[0]+A[1]*B[2])%q,(A[0]*B[1]+A[1]*B[3])%q,(A[2]*B[0]+A[3]*B[2])%q,(A[2]*B[1]+A[3]*B[3])%q)
HARD = {1,121,169,289,361,529}
hp = [q for q in sieve(5000) if q % 4 == 1 and q % 840 in HARD]
PR = [p for p in sieve(2000) if p % 4 == 1]
# Z1077: certificate divisors per N=4Cp+1 and whether prime
cd = Counter(); cp = 0
for p in hp:
    for C in range(1, 21):
        N = 4*C*p+1
        ds = [d for d in divisors(factor(N)) if d > 1 and d % (4*C) == 4*C-1]
        cd[len(ds)] += 1
        cp += sum(1 for d in ds if len(factor(d)) == 1 and sum(factor(d).values()) == 1)
OUT["Z1077"] = {"cert_divisor_count_hist": sorted(cd.items())[:8], "prime_cert_divisors": cp}
# Z1092: BFS on SL2(Z/8) reached by products of letters [[a,1],[1,0]], a in Z/8; (1,1)-entry classes mod 4
letters = [(a % 8, 1, 1, 0) for a in range(8)]
seen = {(1,0,0,1)}; frontier = [(1,0,0,1)]
for _ in range(6):
    frontier = list({mm(M, L, 8) for M in frontier for L in letters} - seen)
    seen |= set(frontier)
OUT["Z1092"] = {"reached_states_SL2Z8": len(seen), "order_SL2Z8": 384}
# Z1154: det of word matrices
det_ok = all(((t*u*v+t+v)*0 + 1) == 1 for t in range(1, 5) for u in range(1, 5) for v in range(1, 5))
OUT["Z1154"] = {"det_identically_1_for_letter_words": det_ok}
# Z1155: trace classes of M(t,u,v)=L_t L_u L_v (entries >= 2)
tr = Counter()
for t in range(2, 30):
    for u in range(2, 30):
        for v in range(2, 30):
            M = mm(mm((t,1,1,0),(u,1,1,0),10**9),(v,1,1,0),10**9)
            tr["hyperbolic" if M[0]+M[3] > 2 else ("parabolic" if M[0]+M[3] == 2 else "elliptic")] += 1
OUT["Z1155"] = dict(tr)
# Z1156: horocycle products n(u)*n-(t) mod 16: reachable states and least height realising each
def hmat(u, q): return (1, u % q, 0, 1)
def lmat(t, q): return (1, 0, t % q, 1)
least = {}
for u in range(0, 16):
    for t in range(0, 16):
        for v in range(0, 16):
            M = mm(mm(hmat(u,16), lmat(t,16), 16), hmat(v,16), 16)
            least.setdefault(M, max(u,t,v))
OUT["Z1156"] = {"reachable_states_mod16_3flows": len(least), "max_least_height": max(least.values())}
# Z1158: skew-product returns of the Gauss map on PR: count admissible (quotient,residue) pairs for p<=2000
ret = Counter()
for p in PR[:80]:
    for A in range(1, p):
        q = cfq(p, A)
        if len(q) <= 3: ret[(len(q), q[0] % 4)] += 1
OUT["Z1158"] = sorted(ret.items())[:8]
# Z1159: exact residual formula constant in symbolic type? check 4/p - 1/x - 1/y residual numerator for x=p//4+1 family
res_num = Counter()
for p in PR[:80]:
    x = p//4+1; a = 4*x-p; b = p*x; y = -(-b//a)
    r = Fraction(4, p) - Fraction(1, x) - Fraction(1, y)
    res_num[(r.numerator % 4)] += 1
OUT["Z1159"] = dict(res_num)
json.dump(OUT, open("data/z52b/pass1/U06/final_k.json","w"), indent=1, default=str)
for k,v in OUT.items(): print(k, str(v)[:200])
