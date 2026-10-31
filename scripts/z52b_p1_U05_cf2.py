"""z52b pass1 U05: (Z1497) explain class-wide C-form wins by small primes {3,5,7};
(Z1029) certificate divisors are all QNR mod p?  (Z1036) local win-densities mod 8,9,5,7 for C=1..3;
(Z1403) Fourier spectrum of win indicator mod lcm(4C,840) for C<=20; (Z1229) depth-3 tree for win_{C<=5}."""
import math, numpy as np
from collections import Counter
D = "data/z52b/pass1/U05/2nd/"
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
N = 200000
spf = list(range(N+1))
for i in range(2, int(N**.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = Counter()
    while n > 1:
        q = spf[n]; f[q] += 1; n //= q
    return f
def facbig(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
rows = {}
for l in open(D+"cform_C200_p1e5.txt"):
    t = list(map(int, l.split())); rows[t[0]] = set(t[3:3+t[2]])
P1 = [p for p in rows if p % 4 == 1 and p > 4]
# ---- Z1497: for full (class mod 840, C) pairs, does the win come from {3,5,7}-divisors ≡ -1 (mod 4C)?
cls = {}
for p in P1: cls.setdefault(p % 840, []).append(p)
full = []
for r, ps in cls.items():
    if len(ps) < 5: continue
    for C in range(1, 51):
        if all(C in rows[p] for p in ps): full.append((r, C))
def small_explains(r, C):
    m = 4*C
    N_ = m*r + 1  # class representative: divisibility by 3,5,7 is class-determined
    qs = [q for q in (3, 5, 7) if N_ % q == 0 and q % 2 == 1]
    # subsets of {3,5,7} (exponent 1 suffices for a subset product; use all prime powers dividing N)
    fs = fac(N_)
    small = {q: fs[q] for q in (3, 5, 7) if q in fs}
    ds = divisors(small)
    return any(d % m == m-1 for d in ds)
expl = sum(1 for r, C in full if small_explains(r, C))
log(f"Z1497 class-wide wins (class mod 840 with ≥5 primes, C≤50): {len(full)} pairs; explained by a divisor of 4Cr+1 supported on {{3,5,7}} ≡ -1 (mod 4C): {expl}")
# ---- Z1029: are all certificate divisors QNR mod p? sample primes, C<=30
def leg(a, p):
    a %= p; return 1 if pow(a, (p-1)//2, p) == 1 else -1
bad = 0; tot = 0
for p in P1[:600]:
    for C in range(1, 31):
        m = 4*C; N_ = m*p+1; fs = facbig(N_)
        for d in divisors(fs):
            if d % m == m-1:
                tot += 1
                if leg(d, p) != -1: bad += 1
log(f"Z1029 certificate divisors d (p≡1(4) first 600 primes, C≤30): {tot} total; with (d/p)=+1: {bad} (signed sums cannot cancel iff 0)")
# ---- Z1036: win densities by class mod 8, 9, 5, 7 for C=1,2,3 (all primes p≡1(4), p<=1e5)
for mod in (8, 9, 5, 7):
    res = []
    for C in (1, 2, 3):
        rates = {}
        for c in range(mod):
            ps = [p for p in P1 if p % mod == c]
            if ps: rates[c] = round(sum(1 for p in ps if C in rows[p]) / len(ps), 3)
        res.append((C, min(rates.values()), max(rates.values())))
    log(f"Z1036 mod {mod}: win-rate range (min,max) over classes for C=1,2,3: {[(c,a,b) for c,a,b in res]}")
# ---- Z1403: Fourier energy of class-average win indicator mod M = lcm(4C, 840)
for C in (1, 2, 3, 5, 10, 20):
    M = math.lcm(4*C, 840)
    cl = {}
    for p in P1:
        cl.setdefault(p % M, []).append(1.0 if C in rows[p] else 0.0)
    f = np.zeros(M)
    for r, v in cl.items(): f[r] = np.mean(v)
    fh = np.fft.fft(f - f.mean())
    en = np.abs(fh)**2; en[0] = 0
    s = en.sum()
    top = np.sort(en)[::-1]
    # energy in frequencies that are multiples of M/(4C)  (dependence on p mod 4C only)
    lowfreq = sum(en[k] for k in range(M) if k % (M//math.gcd(M, 4*C)) == 0) / s if s > 0 else 0
    log(f"Z1403 C={C}: M={M}, top-5 frequency energy share = {top[:5].sum()/s:.3f}, share on frequencies with period dividing 4C: {lowfreq:.3f}")
# ---- Z1229: depth-3 tree for target win_{C<=5}
feat_names = []; F = []; Y = []
qs = [q for q in range(3, 32) if spf[q] == q]
for p in P1:
    row = [1.0 if leg(q, p) == 1 else 0.0 for q in qs]
    row += [float(p % m == c) for m, c in [(8,1),(8,5),(9,1),(9,4),(5,1),(5,4),(7,1),(7,2),(3,1)]]
    F.append(row); Y.append(1 if any(C in rows[p] for C in range(1, 6)) else 0)
F = np.array(F); Y = np.array(Y)
names = [f"(q{q}/p)=+1" for q in qs] + ["p≡1(8)", "p≡5(8)", "p≡1(9)", "p≡4(9)", "p≡1(5)", "p≡4(5)", "p≡1(7)", "p≡2(7)", "p≡1(3)"]
half = len(Y)//2
def best_split(X, y):
    best = (1e9, None, None)
    for j in range(X.shape[1]):
        for v in (0.5,):
            L = X[:, j] < v
            if L.sum() < 20 or (~L).sum() < 20: continue
            g = 0
            for m in (L, ~L):
                pm = y[m].mean() if m.any() else 0
                g += m.sum()*2*pm*(1-pm)
            if g < best[0]: best = (g, j, v)
    return best
def grow(X, y, depth, prefix=""):
    if depth == 0 or len(y) < 40 or y.mean() in (0.0, 1.0):
        return ("leaf", y.mean(), len(y), prefix)
    g, j, v = best_split(X, y)
    if j is None: return ("leaf", y.mean(), len(y), prefix)
    L = X[:, j] < v
    return ("node", j, grow(X[L], y[L], depth-1, prefix+f"{names[j]}=0 & "), grow(X[~L], y[~L], depth-1, prefix+f"{names[j]}=1 & "))
tree = grow(F[:half], Y[:half], 3)
def leaves(t, acc):
    if t[0] == "leaf": acc.append(t); return acc
    leaves(t[2], acc); leaves(t[3], acc); return acc
def predict(t, x):
    while t[0] == "node": t = t[2] if x[t[1]] < 0.5 else t[3]
    return t[1]
pred = np.array([predict(tree, x) for x in F[half:]]) > 0.5
log(f"Z1229 depth-3 tree for 'some C≤5 wins' trained on p≤5e4 ({half} primes): test accuracy on p>5e4 = {(pred == Y[half:].astype(bool)).mean():.3f} (base {max(Y[half:].mean(),1-Y[half:].mean()):.3f})")
for lf in leaves(tree, []):
    log(f"  leaf: P(win)={lf[1]:.3f} n={lf[2]}  rule: {lf[3][:-3]}")
open(D+"cf2_out.txt", "w").write("\n".join(out)+"\n")
