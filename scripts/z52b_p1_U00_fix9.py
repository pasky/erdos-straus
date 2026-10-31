# z52b pass1 U00 fix (9): Z2375 (least prime witness), Z1502 (C_min purity on p mod 840), Z1938 (witness mass by C-range),
# Z2796 (cross-level dependence of witness indicators, from W60.npy), Z2642 (R² of I3 minima by n mod 840 in windows),
# Z3189 (Berlekamp–Massey-type recurrence test on Cmin(3·2^s+1)), Z0351 (e-slice correlation conditioned on p mod 24).
import json, numpy as np
from cypari2 import Pari
from sympy import primerange, isprime
pari = Pari(); pari.allocatemem(10**9)
def divisors_of(N):
    f = pari.factor(N); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
out = {}
P1 = [q for q in primerange(5, 20000) if q % 4 == 1]
W = np.load('/tmp/u00/W60.npy').astype(float)
# Z2375: for each p, the least prime q | 4Cp+1 with q ≡ -1 (mod 4C), C ≤ 60 (least over C); distribution of q/p
least = []
for p in P1:
    best = None
    for C in range(1, 61):
        N = 4 * C * p + 1; M = 4 * C
        for a in divisors_of(N):
            if 1 < a < N and a % M == M - 1 and isprime(a):
                if best is None or a < best[0]: best = (a, C)
    least.append(best)
have = [b for b in least if b]
out['Z2375'] = {'primes': len(P1), 'with_prime_witness': len(have), 'median_least_prime_q': int(np.median([b[0] for b in have])),
                'frac_q_lt_p/10': round(float(np.mean([b[0] < p / 10 for b, p in zip(have, [pp for pp, b in zip(P1, least) if b])])), 3),
                'examples(p,q,C)': [(p, b[0], b[1]) for p, b in list(zip(P1, least))[:8] if b]}
# Z1502: first winning level C_min(p) (min C with W), purity within classes p mod 840 (fraction equal to the class mode)
cmin = np.array([next((C for C in range(1, 61) if W[i, C - 1]), 99) for i in range(len(P1))])
from collections import Counter, defaultdict
cls = defaultdict(list)
for i, p in enumerate(P1): cls[p % 840].append(cmin[i])
purity = [Counter(v).most_common(1)[0][1] / len(v) for k, v in cls.items() if len(v) >= 5]
out['Z1502'] = {'classes_mod840_with_ge5': len(purity), 'mean_purity_of_Cmin_in_class': round(float(np.mean(purity)), 3),
                'baseline_purity_all_primes': round(Counter(cmin.tolist()).most_common(1)[0][1] / len(cmin), 3)}
# Z1938: witness mass by C-range for p=409, 1000033 (C ≤ 1000)
mass = {}
for p in [409, 1000033]:
    m = [0, 0, 0]
    for C in range(1, 1001):
        N = 4 * C * p + 1; M = 4 * C
        c = sum(1 for a in divisors_of(N) if 1 < a < N and a % M == M - 1)
        m[0 if C <= 10 else (1 if C <= 100 else 2)] += c
    mass[p] = {'C<=10': m[0], '11..100': m[1], '101..1000': m[2]}
out['Z1938'] = mass
# Z2796: mean |corr| of witness indicators across levels 1..30 (off-diagonal), vs independence baseline (shuffle rows per level)
cc = np.corrcoef(W[:, :30].T); off = np.abs(cc[~np.eye(30, dtype=bool)])
rng = np.random.default_rng(0)
sh = np.column_stack([rng.permutation(W[:, j]) for j in range(30)]); cs = np.corrcoef(sh.T); offs = np.abs(cs[~np.eye(30, dtype=bool)])
out['Z2796'] = {'mean_abs_offdiag_corr_levels1_30': round(float(off.mean()), 4), 'shuffled_baseline': round(float(offs.mean()), 4), 'max_abs_corr': round(float(off.max()), 3)}
# Z2642: I3 minima (im) from minwords: R² of log(im) on residue class mod 840 within windows of 2e5 (n ≡ 1 mod 4)
A = np.loadtxt('/tmp/u00/minwords_12e6.txt', dtype=np.int64)
im = A[:, 3]; n = np.arange(1, len(im) + 1)
ok = (n % 4 == 1) & (im > 0)
r2 = []
for lo in range(0, 12000000, 2000000):
    sel = ok.copy(); sel[:lo] = False; sel[lo + 2000000:] = False
    y = np.log(im[sel].astype(float)); c = n[sel] % 840
    means = {k: y[c == k].mean() for k in np.unique(c) if (c == k).sum() > 5}
    pred = np.array([means.get(k, y.mean()) for k in c])
    r2.append(round(float(1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()), 3))
out['Z2642'] = {'R2_by_mod840_per_2e6_window': r2, 'note': 'in-sample R² with ~96 class means per window'}
# Z3189: Cmin(3·2^s+1) sequence (proved ET-sterile family, s=1..22) and a linear-recurrence test (order ≤ 4, integer-free least squares)
A12 = A[:, 1]
seq = [int(A12[3 * 2 ** s + 1 - 1]) for s in range(1, 23) if 3 * 2 ** s + 1 <= len(A12)]
def fit_rec(seq, k):
    X = np.array([seq[i:i + k] for i in range(len(seq) - k)], float); y = np.array(seq[k:], float)
    if len(y) < k + 3: return None
    c, *_ = np.linalg.lstsq(X, y, rcond=None); res = y - X @ c
    return round(float(np.sqrt((res ** 2).mean())), 3)
out['Z3189'] = {'seq_s1_22_Cmin(3·2^s+1)': seq, 'rms_residual_order_k': {k: fit_rec(seq, k) for k in [1, 2, 3, 4]}}
# Z0351: e-slice failure correlation conditioned on p mod 24 (recomputed from fix3 logic on p < 5e4)
from cypari2 import Pari as _P
def divs_sq(M):
    f = pari.factor(M); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(2 * e + 1)]
    return ds
def ok_e(p, e):
    M = p * ((p + e) // 4)
    return any((d + M) % e == 0 and ((M * M // d) + M) % e == 0 for d in divs_sq(M))
ES = [3, 7, 11, 15, 19]
PP = [q for q in primerange(5, 50000) if q % 4 == 1]
fails = {e: set(p for p in PP if not ok_e(p, e)) for e in ES}
rat = {}
for r in [1, 5, 13, 17]:
    sub = [p for p in PP if p % 24 == r]
    row = {}
    for i, e in enumerate(ES):
        for f in ES[i + 1:]:
            pe = sum(1 for p in sub if p in fails[e]) / len(sub); pf = sum(1 for p in sub if p in fails[f]) / len(sub)
            pj = sum(1 for p in sub if p in fails[e] and p in fails[f]) / len(sub)
            row[f'{e},{f}'] = round(pj / (pe * pf), 2) if pe * pf > 0 else None
    rat[r] = row
out['Z0351_cond_mod24'] = rat
json.dump(out, open('data/z52b/pass1/U00/fix9.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str)[:5000])
