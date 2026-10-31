# z52b pass1 U00 — batch 1 cheap checks on f4_all_30000.txt (col0 = n, col1 = U(n)).
import numpy as np, json, math, sys
from collections import Counter, defaultdict
from scipy.stats import spearmanr
R = '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
N, U = F[:, 0], F[:, 1]
Ud = dict(zip(N.tolist(), U.tolist()))
out = {}
# Z0682: values of U(n) <= 8 and whether 5 occurs
cnt = Counter(U.tolist())
out['Z0682'] = {'count_U_eq_5': cnt.get(5, 0), 'min_U': int(U.min()), 'small_values': {k: cnt[k] for k in sorted(cnt) if k <= 8},
                'n_with_U_le_8_max_n': max(n for n, u in zip(N.tolist(), U.tolist()) if u <= 8)}
# Z0845: Carmichael numbers (Korselt) <= 30000 vs neighbours (n-2..n+2 with n ≡ 1 mod 4 not needed; use all n)
def is_carm(n):
    if n < 561 or n % 2 == 0: return False
    m = n; ps = []
    d = 2
    while d * d <= m:
        while m % d == 0:
            ps.append(d); m //= d
        d += 1
    if m > 1: ps.append(m)
    if len(set(ps)) != len(ps) or len(ps) < 3: return False
    return all((n - 1) % (p - 1) == 0 for p in ps)
carm = [n for n in range(3, 30001) if is_carm(n)]
ratios = []
for n in carm:
    nb = [Ud[m] for m in range(n - 6, n + 7) if m != n and m in Ud and m % 4 == 1 and m >= 2]
    if nb and Ud.get(n):
        ratios.append(Ud[n] / float(np.median(nb)))
out['Z0845'] = {'n_carmichael_le_3e4': len(carm), 'ratio_median_to_neighbour_median_1mod4': float(np.median(ratios)) if ratios else None,
                'min_ratio': min(ratios) if ratios else None, 'max_ratio': max(ratios) if ratios else None,
                'example': {str(n): Ud[n] for n in carm[:12]}}
# Z0718: mean U(p)/log^2 p by residue class mod 840 among primes p ≡ 1 (4), p ≤ 30000
def primes(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]
P = [int(p) for p in primes(30000) if p % 4 == 1 and p >= 5]
cls = defaultdict(list)
for p in P:
    cls[p % 840].append(Ud[p] / math.log(p) ** 2)
means = sorted(((np.mean(v), k, len(v)) for k, v in cls.items() if len(v) >= 10), reverse=True)
out['Z0718'] = {'n_classes': len(means), 'top5': [(round(m, 3), k, c) for m, k, c in means[:5]],
                'bottom5': [(round(m, 3), k, c) for m, k, c in means[-5:]],
                'square_classes_mod840': {k: round(float(np.mean(cls[k])), 3) for k in [1, 121, 169, 289, 361, 529] if cls[k]}}
# Z0354: D(p) = #{M <= 1000, M >= 2: p mod M is a square residue mod M}; Spearman vs U(p)
Mmax = 1000
sq = []
for M in range(2, Mmax + 1):
    s = np.zeros(M, bool); x = np.arange(M); s[(x * x) % M] = True; sq.append((M, s))
Pa = np.array(P)
D = np.zeros(len(P), int)
for M, s in sq:
    D += s[Pa % M]
Up = np.array([Ud[p] for p in P], float)
rho = spearmanr(D, Up)
rho_norm = spearmanr(D, Up / np.log(Pa) ** 2)
out['Z0354'] = {'n_primes': len(P), 'D_mean': float(D.mean()), 'spearman_D_U': float(rho.correlation),
                'spearman_D_U_over_log2': float(rho_norm.correlation)}
json.dump(out, open('data/z52b/pass1/U00/batch1.json', 'w'), indent=1, default=float)
print(json.dumps(out, indent=1, default=float)[:4000])
