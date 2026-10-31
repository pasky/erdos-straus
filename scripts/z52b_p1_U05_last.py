"""z52b pass1 U05 last computations: Z1642 (max denominator/p² over solutions, dumps p≤2e4), Z1763 (degree of primes in
'share a winning C' graph), Z2606 (log-concavity of a_k=#(p,C) wins with ω(C)=k), Z3017 (extremality score vs U),
Z3018 (class-wide certificate coverage), Z3059 (certificate-free residues mod q), Z0837 (binary digits vs U),
Z1238 (matched pairs by mod 60060 profile), Z1744 (EVT of max Cmin), Z1747 (MaxEnt regression of log(1+R)), Z1613 (Beatty gaps),
Z2308/Z2328 (reciprocal sumsets mod p), Z2840 (largest component of F_p), Z2669 (Sylver Grundy, N≤30, u,v≤30)."""
import math, numpy as np
from collections import Counter, defaultdict
from scipy.stats import spearmanr
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
D = "data/z52b/pass1/U05/2nd/"
sols = defaultdict(list)
for l in open("/tmp/u05/dump_p2e4.txt"):
    _, n, x, y, z = l.split(); sols[int(n)].append((int(x), int(y), int(z)))
cf = {}
for l in open(D+"cform_C200_p1e5.txt"):
    t = list(map(int, l.split())); cf[t[0]] = set(t[3:3+t[2]])
UP = {}
for l in open(D+"U_primes_1e5.txt"):
    p, u, nx = map(int, l.split()); UP[p] = u
P1 = [p for p in cf if p % 4 == 1 and p > 4]
def fac(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def omega(n): return len(fac(n))
# Z1642
mx = [(max(max(s) for s in sols[p])/p**2, p) for p in sols if p % 4 == 1 and p > 4 and sols[p]]
log(f"Z1642 max denominator/p² over all solutions (p≡1(4), ≤2e4): max {max(mx)[0]:.3f} at p={max(mx)[1]}, median {np.median([a for a,_ in mx]):.3f}")
# Z1763: degree in 'share a winning C' graph (primes ≤1e5, p≡1 mod 4, sample 600)
S = P1[:600]
deg = []
for p in S:
    deg.append(sum(1 for q in S if q != p and cf[p] & cf[q]))
log(f"Z1763 'share a winning C' graph on 600 primes ≡1(4): degree median {int(np.median(deg))} of {len(S)-1}; density {np.mean(deg)/(len(S)-1):.3f}")
# Z2606: a_k = #{(p,C): C wins, omega(C)=k}; log-concavity
a = Counter()
for p in P1:
    for C in cf[p]: a[omega(C)] += 1
seq = [a[k] for k in range(0, max(a)+1)]
lc = [seq[k]**2 >= seq[k-1]*seq[k+1] for k in range(1, len(seq)-1)]
log(f"Z2606 a_k (k=ω(C)) = {seq}; log-concave at {sum(lc)} of {len(lc)} interior points: {lc}")
# Z3017: extremality E(p)=#{ℓ≤100: (ℓ/p)=1} vs U/log²p
def leg(a_, p): a_ %= p; return 1 if pow(a_, (p-1)//2, p) == 1 else -1
pr100 = [q for q in range(3, 101) if all(q % d for d in range(2, int(q**.5)+1))]
E = [sum(1 for q in pr100 if leg(q, p) == 1) for p in P1]
Y = [UP[p]/math.log(p)**2 for p in P1]
log(f"Z3017 Spearman(E(p), U/log²p) = {spearmanr(E, Y)[0]:.3f} over p≡1(4)≤1e5")
# Z3018: fraction of primes (≡1 mod 840 classes) lying in classes where some C≤50 wins for all primes in class
cls = defaultdict(list)
for p in P1: cls[p % 840].append(p)
full = {r for r, ps in cls.items() if len(ps) >= 5 and any(all(C in cf[p] for p in ps) for C in range(1, 51))}
cov = sum(len(cls[r]) for r in full)/len(P1)
log(f"Z3018 primes lying in mod-840 classes certified for all members by some C≤50: {cov:.3f} of primes p≡1(4) ≤1e5 ({len(full)} classes)")
# Z3059: residues r mod q (prime q≤200) certificate-free (no prime p≡r in the sample wins C≤20); counts
for q in (7, 11, 13, 31, 101, 199):
    free = []
    for r in range(q):
        ps = [p for p in P1 if p % q == r]
        if len(ps) >= 20 and all(not (cf[p] & set(range(1, 21))) for p in ps): free.append(r)
    log(f"Z3059 q={q}: residues with ≥20 primes and no C≤20 win: {free}")
# Z0837: binary digits vs U (Spearman), p≡1 mod 24 and conditioned on v2(p-1)
rows = []
for p in P1:
    if p % 24 != 1: continue
    h = bin(p).count('1'); t1 = 0; q = p
    while q & 1: t1 += 1; q >>= 1
    rows.append((p, h, t1, UP[p]/math.log(p)**2, (p-1) & -(p-1)))
r1 = spearmanr([x[1] for x in rows], [x[3] for x in rows])[0]
log(f"Z0837 Spearman(hamming weight of p, U/log²p) over p≡1(24): {r1:.3f}; by v2(p−1) (mean U/log² of hamming groups within v2 classes): " +
    str({v: round(spearmanr([x[1] for x in rows if (x[4]) == v], [x[3] for x in rows if x[4] == v])[0], 2) for v in sorted({x[4] for x in rows}) if sum(1 for x in rows if x[4]==v) > 40}))
# Z1238: matched pairs (same residue mod 60060 = 4·3·5·7·11·13), contrast in Cmin (least winning C)
cmin = {}
for l in open(D+"cmin_p1e6_C1000.txt"):
    p, c = map(int, l.split()); cmin[p] = c
prof = defaultdict(list)
for p in cmin:
    if p > 60060 and cmin[p] > 0: prof[p % 60060].append(p)
pairs = [(a_, b_) for v in prof.values() if len(v) >= 2 for a_, b_ in [(v[0], v[1])]]
big = sum(1 for a_, b_ in pairs if max(cmin[a_], cmin[b_]) >= 10*min(cmin[a_], cmin[b_]))
rnd = sum(1 for i in range(len(pairs)) if max(cmin[pairs[i][0]], cmin[pairs[(i+7) % len(pairs)][1]]) >= 10*min(cmin[pairs[i][0]], cmin[pairs[(i+7) % len(pairs)][1]]))
log(f"Z1238 matched pairs (same class mod 60060): {len(pairs)} pairs; Cmin ratio ≥10 in {big} ({big/len(pairs):.3f}); random pairs: {rnd/len(pairs):.3f}")
# Z1744: EVT: max Cmin over p ≤ X
mxc = 0; recs = []
for p in sorted(cmin):
    if cmin[p] > mxc: mxc = cmin[p]; recs.append((p, mxc))
log("Z1744 record Cmin (C≤1000, p≤1e6) : " + str(recs[-6:]) + f"; log p at last record {math.log(recs[-1][0]):.2f}")
# Z1747: MaxEnt-style regression of log(1+R) on residue indicators mod q ≤Q (5-fold CV)
Rv = {}
for l in open(D+"cform_C200_p1e5.txt"):
    t = list(map(int, l.split())); Rv[t[0]] = t[1]
PP = [p for p in Rv if p % 4 == 1 and p > 4]
y_ = np.array([math.log(1+Rv[p]) for p in PP])
rng = np.random.default_rng(2); idx = np.arange(len(PP)); rng.shuffle(idx); folds = np.array_split(idx, 5)
for Q in (5, 10, 20, 50):
    qs = [q for q in range(3, Q+1) if all(q % d for d in range(2, int(q**.5)+1))]
    X = np.array([[1.0] + [1.0 if p % q == r else 0.0 for q in qs for r in range(1, q)] for p in PP])
    pred = np.zeros(len(PP))
    for f_ in folds:
        tr = np.setdiff1d(idx, f_)
        b = np.linalg.lstsq(X[tr] + 0, y_[tr], rcond=None)[0]; pred[f_] = X[f_] @ b
    r2 = 1 - ((y_-pred)**2).sum()/((y_-y_.mean())**2).sum()
    log(f"Z1747 residue-indicator regression of log(1+R(p)) for primes≡1(4)≤1e5, moduli ≤{Q}: 5-fold CV R2 = {r2:.3f}")
# Z1613: gaps between consecutive 'marked' x in (p/4, 3p/4] (two-term remainder), p=409 vs 401
def two_term(a, b):
    g = math.gcd(a, b); a //= g; b //= g
    f = fac(b*b)
    ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return any((s % a == (-b) % a) and ((b + b*b//s) % a == 0) and ((b + b*b//s)//a > 0) for s in ds)
for p in (409, 401):
    marked = [x for x in range(p//4+1, 3*p//4+1) if (4*x-p) > 0 and two_term(4*x-p, p*x)]
    gaps = Counter(np.diff(marked)) if len(marked) > 1 else Counter()
    log(f"Z1613 p={p}: {len(marked)} marked x in (p/4,3p/4]; distinct gaps {len(gaps)}: {sorted(gaps.items())[:6]}")
# Z2308/Z2328: reciprocal sumsets in F_p: A={1/a: a≤N}, |A+A| vs p and vs |A|²
for p in (1009, 2521):
    for N_ in (30, 60):
        A = {pow(a, p-2, p) for a in range(1, N_+1) if a % p}
        AA = {(x+y) % p for x in A for y in A}
        log(f"Z2308/Z2328 p={p}, N={N_}: |A|={len(A)}, |A+A|={len(AA)} (|A|²={len(A)**2}, p={p}); |A+A|/|A|={len(AA)/len(A):.2f}")
open(D+"last_out.txt", "w").write("\n".join(out)+"\n")
