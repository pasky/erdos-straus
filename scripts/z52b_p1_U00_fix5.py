# z52b pass1 U00 fix (5): Z2454 (BGT doubling), Z1372 (mutual information U-class vs p mod M), Z1559 (Lucas values),
# Z1475 (closure of winning C under C -> kC), Z2559 (joint witness at consecutive levels), Z1492 (partial sums of witness counts),
# Z0127 (weighted ES, brute force, small n).
import sys, json, math
import numpy as np
from fractions import Fraction as F
from cypari2 import Pari
from sympy import primerange
pari = Pari(); pari.allocatemem(10**9)
out = {}
def divisors_of(N):
    f = pari.factor(N); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def wit_list(p, C):
    N = 4 * C * p + 1; M = 4 * C
    return sorted(a for a in divisors_of(N) if 1 < a < N and a % M == M - 1)
P1 = [q for q in primerange(5, 20000) if q % 4 == 1]
# Z2454 BGT doubling on D_p = witnesses for C ≤ 40 (p in first 30 primes ≡ 1 mod 4 above 100)
Ks = []
for p in [q for q in P1 if q > 100][:12]:
    D = set()
    for C in range(1, 41): D.update(wit_list(p, C))
    D = sorted(D)[:60]
    Q = {F(a, b) for a in D for b in D}
    QQ = {x * y for x in Q for y in Q}
    Ks.append((p, len(D), len(Q), len(QQ), round(len(QQ) / len(Q), 1)))
out['Z2454'] = {'rows(p,|D|,|Q|,|QQ|,K)': Ks, 'median_K': float(np.median([k[4] for k in Ks]))}
print('Z2454', flush=True)
# Z2559 / Z1475 / Z1492: witness indicator W[p][C] for C ≤ 60, primes p ≡ 1 (4) < 20000
W = []
for p in P1:
    W.append([1 if wit_list(p, C) else 0 for C in range(1, 61)])
W = np.array(W, float)
q = W.mean(axis=0)
joint = [(float((W[:, C - 1] * W[:, C]).mean()), float(q[C - 1] * q[C])) for C in range(1, 40)]
out['Z2559'] = {'pairs(C,C+1)_joint_vs_product_mean_ratio': round(float(np.mean([j / (m if m else 1) for j, m in joint])), 3),
                'first5(joint,product)': [(round(a, 4), round(b, 4)) for a, b in joint[:5]]}
# Z1475: P(C-witness | kC-witness) for k in 2,3,5 vs P(C-witness)
clo = {}
for k in [2, 3, 5]:
    rows = [(W[i, C - 1], W[i, k * C - 1]) for i in range(len(P1)) for C in range(1, 61 // k + 1)]
    a = np.array(rows)
    clo[k] = {'P(W_kC | W_C)': round(float(a[a[:, 0] == 1][:, 1].mean()), 4), 'P(W_kC)': round(float(a[:, 1].mean()), 4)}
out['Z1475'] = clo
# Z1492: partial sums of witness counts c_C(p) = #{a|4Cp+1: a≡-1 (4C)} for p ≈ 1e6; ratio S(X)/X and S(X)/Σ(τ−2)/φ(4C) at X=100,300,1000
def c_count(p, C):
    N = 4 * C * p + 1; M = 4 * C
    return sum(1 for a in divisors_of(N) if 1 < a < N and a % M == M - 1), (len(divisors_of(N)) - 2) / int(pari.eulerphi(M))
rows = []
for p in [q for q in primerange(10 ** 6, 10 ** 6 + 3000) if q % 4 == 1][:3]:
    S = 0.0; E = 0.0; pts = {}
    for C in range(1, 1001):
        c, e = c_count(p, C); S += c; E += e
        if C in (100, 300, 1000): pts[C] = (S, round(E, 1), round(S / E, 3))
    rows.append({'p': p, 'pts(S,E,S/E)': pts})
out['Z1492'] = rows
# Z1372: mutual information between [U(p) >= median] and p mod M, U from f4 data, primes ≡ 1 (4), p ≤ 3e4
import math as m
F4 = np.loadtxt('/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
Ud = dict(zip(F4[:, 0].tolist(), F4[:, 1].tolist()))
pp = [q for q in primerange(5, 30001) if q % 4 == 1]
u = np.array([Ud[p] / m.log(p) ** 3 for p in pp]); med = np.median(u)
hi = (u >= med).astype(int)
def MI(keys):
    from collections import Counter
    n = len(keys); cj = Counter(zip(keys, hi.tolist())); ck = Counter(keys); ch = Counter(hi.tolist())
    return sum((c / n) * m.log((c / n) / ((ck[k] / n) * (ch[h] / n))) for (k, h), c in cj.items()) / m.log(2)
out['Z1372'] = {'MI_bits_hi_vs_p_mod': {M: round(MI([p % M for p in pp]), 5) for M in [4, 8, 24, 120, 840]},
                'MI_bits_baseline_permuted(840)': round(float(np.mean([MI([p % 840 for p in np.random.permutation(pp).tolist()]) for _ in range(1)])), 5),
                'n_primes': len(pp)}
# Z1559: is 4Cp+1 ∈ {U_n(P,Q), V_n(P,Q)} (Lucas) for |P|,|Q| ≤ 3, n ≤ 30? compare hit rate with base rate of the value set
vals = set()
for P_ in range(-3, 4):
    for Q_ in range(-3, 4):
        if Q_ == 0: continue
        a0, a1 = 0, 1; b0, b1 = 2, P_
        for n in range(1, 31):
            if abs(a1) > 10 ** 9 or abs(b1) > 10 ** 9: break
            vals.add(abs(a1)); vals.add(abs(b1))
            a0, a1 = a1, P_ * a1 - Q_ * a0
            b0, b1 = b1, P_ * b1 - Q_ * b0
Vs = sorted(v for v in vals if v > 1)
hits = 0; tot = 0
for p in [q for q in primerange(5, 2000) if q % 4 == 1]:
    for C in range(1, 101):
        tot += 1
        if (4 * C * p + 1) in vals: hits += 1
base = len([v for v in Vs if v <= 8 * 10 ** 5]) / (8 * 10 ** 5)
out['Z1559'] = {'value_set_size(<=1e9)': len(Vs), 'pairs_tested': tot, 'hits': hits, 'hit_rate': round(hits / tot, 5), 'value_density_base_rate_<=8e5': round(base, 5)}
# Z0127: weighted ES a/x+b/y+c/z = 4/n, a,b,c ∈ 1..4, n ≤ 40: exists? brute force with bounds x ≤ 3·max(a)·n, y,z via divisor-free loops
def weighted_exists(a, b, c, n):
    target = F(4, n)
    Xmax = 3 * max(a, b, c) * n
    for x in range(1, Xmax + 1):
        r1 = target - F(a, x)
        if r1 <= 0: continue
        Ymax = 3 * max(b, c) * n
        for y in range(1, Ymax + 1):
            r2 = r1 - F(b, y)
            if r2 <= 0: continue
            # c/z = r2 → z = c / r2
            z = F(c) / r2
            if z.denominator == 1 and z >= 1: return (x, y, int(z))
    return None
rows = {}
for n in range(2, 41):
    found = 0; tot = 0
    for a, b, c in [(1, 1, 1), (1, 2, 3), (2, 2, 3), (3, 3, 4), (4, 4, 4), (1, 3, 4), (2, 3, 4)]:
        tot += 1
        if weighted_exists(a, b, c, n): found += 1
    rows[n] = f'{found}/{tot}'
out['Z0127'] = {'n_2_40_weights_sample': rows}
json.dump(out, open('data/z52b/pass1/U00/fix5.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str)[:6000])
