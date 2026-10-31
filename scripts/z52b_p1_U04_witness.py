"""Witness-structure pipeline (U04 pass-1; serves Z1019,Z1020,Z1021,Z1050,Z1076,Z1079,Z1080,Z1086,Z1087,Z1343-family).
For primes p≡1 mod 4, p<=PMAX and C<=CMAX, N=4Cp+1, m=4C:
  W(p,C)=1 iff some divisor d|N has d≡-1 (mod m)  (exact witness).
  omega_min(p,C)= min Ω(d) over witnessing d (number of prime factors with multiplicity needed to reach -1).
  reach(p,C)= |{d mod m : d|N}| / φ(m)  (fraction of unit residues hit by divisors, DP over prime factors).
  ap_len(p) = longest arithmetic progression of witnessing C's (C<=CMAX) for each p.
  hit(p)  : greedy hitting set of primes by C-levels (C-levels that witness primes in window).
  rect    : count of 'rectangles' p1<p2, C1<C2 with W=1 on all four cells.
  gf2rank : GF(2) rank of the prime x C witness matrix (matroid rank of witness vectors).
Memory: O(#primes * CMAX) bits. ulimit -v 4000000."""
import sys, json
from math import gcd
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
CMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 30
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def dp_residues(fac, m):
    # map residue -> min Ω of a divisor with that residue (Ω counts prime factors with multiplicity)
    best = {1 % m: 0}
    for q, e in fac.items():
        new = dict(best)
        for r, w in best.items():
            rr, ww = r, w
            for k in range(1, e + 1):
                rr = rr * q % m; ww += 1
                if rr not in new or new[rr] > ww: new[rr] = ww
        best = new
    return best
ps = [p for p in primes_upto(PMAX) if p % 4 == 1 and p > 5]
W = {}; OM = {}; REACH = {}
for p in ps:
    for C in range(1, CMAX + 1):
        m = 4 * C; N = m * p + 1
        dpres = dp_residues(factor(N), m)
        phi = sum(1 for r in range(m) if gcd(r, m) == 1)
        REACH[(p, C)] = sum(1 for r in dpres if gcd(r, m) == 1) / phi
        if (m - 1) in dpres:
            W[(p, C)] = 1; OM[(p, C)] = dpres[m - 1]
        else:
            W[(p, C)] = 0
res = {}
wit_pc = {p: [C for C in range(1, CMAX + 1) if W[(p, C)]] for p in ps}
# longest AP inside witnessing C set
def longest_ap(S):
    S = sorted(S); best = 1 if S else 0; Sset = set(S)
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            d = S[j] - S[i]; L = 2; x = S[j] + d
            while x in Sset: L += 1; x += d
            best = max(best, L)
    return best
ap = {p: longest_ap(wit_pc[p]) for p in ps}
# greedy hitting set of primes by C-levels
uncovered = set(ps); chosen = []
while uncovered:
    cnt = {C: sum(1 for p in uncovered if W[(p, C)]) for C in range(1, CMAX + 1)}
    C, c = max(cnt.items(), key=lambda kv: kv[1])
    if c == 0: break
    chosen.append(C); uncovered = {p for p in uncovered if not W[(p, C)]}
# rectangles: p1<p2 and C1<C2 all witnessed (count, bounded by pairs of primes with equal witness sets is fine)
rect = 0
for i, p1 in enumerate(ps):
    s1 = set(wit_pc[p1])
    for p2 in ps[i + 1:]:
        common = sorted(s1 & set(wit_pc[p2]))
        k = len(common); rect += k * (k - 1) // 2
# GF(2) rank of witness matrix rows = primes, cols = C
rows = []
for p in ps:
    v = 0
    for C in wit_pc[p]: v |= 1 << (C - 1)
    rows.append(v)
basis = []
for v in rows:
    for b in basis: v = min(v, v ^ b)
    if v: basis.append(v)
gf2 = len(basis)
om_hist = {}
for k, v in OM.items():
    om_hist[v] = om_hist.get(v, 0) + 1
res = dict(PMAX=PMAX, CMAX=CMAX, n_primes=len(ps),
           n_pairs=len(W), n_witness=sum(W.values()),
           witness_rate_by_C={C: round(sum(W[(p, C)] for p in ps) / len(ps), 4) for C in range(1, CMAX + 1)},
           omega_min_hist={str(k): v for k, v in sorted(om_hist.items())},
           mean_reach_witnessing=round(sum(REACH[k] for k in W if W[k]) / max(1, sum(W.values())), 4),
           mean_reach_nonwitness=round(sum(REACH[k] for k in W if not W[k]) / max(1, len(W) - sum(W.values())), 4),
           longest_AP_hist={str(k): sum(1 for p in ps if ap[p] == k) for k in sorted(set(ap.values()))},
           greedy_hitting_set_C=chosen, greedy_hitting_size=len(chosen),
           rectangles=rect, gf2_rank_prime_by_C=gf2)
print(json.dumps(res, indent=1))
json.dump(res, open(f'data/z52b/pass1/U04/witness_{PMAX}_{CMAX}.json', 'w'), indent=1)
