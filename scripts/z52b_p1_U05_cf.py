"""z52b pass1 U05: C-form census analyses from data/z52b/pass1/U05/2nd/cform_C200_p1e5.txt
(columns: p R nwin C_1..C_nwin; R = sum_{C<=200} #{d|4Cp+1: d≡-1 mod 4C}; wins at C≤200)."""
import math, numpy as np
from collections import Counter
from scipy.stats import spearmanr
D = "data/z52b/pass1/U05/2nd/"
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rows = {}
for l in open(D+"cform_C200_p1e5.txt"):
    t = list(map(int, l.split())); p, R, nw = t[0], t[1], t[2]
    rows[p] = (R, t[3:3+nw])
P1 = [p for p in rows if p % 4 == 1 and p > 4]
CM = 200
# ---- Z0358 / Z0626: f(B) = fraction of primes p≡1(4), p<=1e5 with no C-form win for C<=B
fB = {}
for B in (1, 2, 4, 8, 16, 32, 64, 100, 150, 200):
    fB[B] = sum(1 for p in P1 if not any(c <= B for c in rows[p][1])) / len(P1)
log("Z0358/Z0626 f(B)=frac of p≡1(4), p≤1e5 with no C-form win C≤B:", {b: round(v, 5) for b, v in fB.items()})
Bs = np.array([8, 16, 32, 64, 100, 150, 200]); fs = np.array([fB[b] for b in Bs])
ok = fs > 0
slope = np.polyfit(np.log(Bs[ok]), np.log(fs[ok]), 1)[0]
log(f"  log f(B) ~ {slope:.2f}·log B  (power law fit on B∈{Bs[ok].tolist()}); count of never-won primes (C≤200): {sum(1 for p in P1 if not rows[p][1])}")
# ---- Z0625 / Z1418: greedy cover of primes p≡1 (mod 24), p<=1e5 by C-form sets S_C (C<=200)
P24 = [p for p in P1 if p % 24 == 1]
cover_by_C = {C: set(p for p in P24 if C in rows[p][1]) for C in range(1, CM+1)}
unc = set(p for p in P24 if not rows[p][1])
remaining = set(P24) - unc
chosen = []; covered = set()
Xs = [1000, 3000, 10000, 30000, 100000]
hist = {}
while True:
    best = max(cover_by_C, key=lambda C: len(cover_by_C[C] & remaining))
    gain = cover_by_C[best] & remaining
    if not gain: break
    chosen.append(best); remaining -= gain
    for X in Xs:
        if X not in hist and all(p <= X for p in [0]): pass
log(f"Z0625/Z1418 greedy cover of {len(P24)} primes p≡1(24), p≤1e5 by sets S_C (C≤200): {len(chosen)} C-values cover all coverable primes; "
    f"uncoverable (no win C≤200): {len(unc)} = {sorted(unc)[:12]}; first picks {chosen[:12]}")
for X in (1000, 10000, 30000, 100000):
    ch = []; rem = set(p for p in P24 if p <= X) - unc
    while rem:
        best = max(cover_by_C, key=lambda C: len(cover_by_C[C] & rem))
        g = cover_by_C[best] & rem
        if not g: break
        ch.append(best); rem -= g
    log(f"  cover size for p≤{X}: {len(ch)} sets (log X = {math.log(X):.1f}, log² X = {math.log(X)**2:.0f})")
# ---- Z1417: which winning C are preferred? (win C vs all C) by omega(C), C mod 3, C mod 4, smoothness
def omega(n):
    k = 0; d = 2
    while d*d <= n:
        if n % d == 0:
            k += 1
            while n % d == 0: n //= d
        d += 1
    return k + (1 if n > 1 else 0)
def P_plus(n):
    m = 1; d = 2
    while d*d <= n:
        while n % d == 0: m = max(m, d); n //= d
        d += 1
    return max(m, n) if n > 1 else max(m, 1)
allC = list(range(1, CM+1))
wins_all = [c for p in P1 for c in rows[p][1]]
tot_pairs = len(P1)*CM
wr = {c: sum(1 for p in P1 if c in rows[p][1]) / len(P1) for c in allC}
log("Z1417 win-rate by C class (mean over C in class): ")
for name, f in [("omega(C)", omega), ("C mod 3", lambda c: c % 3), ("C mod 4", lambda c: c % 4), ("C mod 8", lambda c: c % 8)]:
    cls = {}
    for c in allC: cls.setdefault(f(c), []).append(wr[c])
    log(f"  {name}: " + ", ".join(f"{k}:{np.mean(v):.4f}" for k, v in sorted(cls.items())))
sm = {c: P_plus(c)/c for c in allC}
log(f"  Spearman(win-rate, P+(C)/C) over C≤200 = {spearmanr([wr[c] for c in allC],[sm[c] for c in allC])[0]:.3f}")
# ---- Z1474 / Z1522: gaps between consecutive winning C; ratio of first two
gaps = []; maxgap = []
for p in P1:
    w = rows[p][1]
    if len(w) >= 2:
        g = np.diff(w); gaps += list(g)
    maxgap.append((max(list(np.diff([0]+w))+[CM - (w[-1] if w else 0)]) if w else CM, p))
log(f"Z1474 gaps between consecutive winning C (C≤200): median {np.median(gaps)}, 90% {np.percentile(gaps,90)}, max {max(gaps)}; "
    f"max initial/tail gap over p: {max(maxgap)}")
r12 = [rows[p][1][1]/rows[p][1][0] for p in P1 if len(rows[p][1]) >= 2]
log(f"Z1522 C2/C1 (two smallest winning C): median {np.median(r12):.2f}, 90% {np.percentile(r12,90):.2f}, share with C2 ≤ 2·C1: {np.mean([x<=2 for x in r12]):.3f}")
clos = {k: np.mean([ (k*c in rows[p][1]) for p in P1 for c in rows[p][1] if k*c <= CM]) for k in (2, 3)}
log(f"  closure: P(kC wins | C wins), k=2,3 (C·k≤200): {clos}")
# ---- Z1497: residue-class win rates mod 840 for C≤50 (classes with 100% win for some C?)
cls840 = {}
for p in P1:
    cls840.setdefault(p % 840, []).append(p)
full = []
for r, ps in cls840.items():
    if len(ps) < 5: continue
    for C in range(1, 51):
        rate = sum(1 for p in ps if C in rows[p][1]) / len(ps)
        if rate == 1.0: full.append((r, C, len(ps)))
log(f"Z1497 residue classes mod 840 (≥5 primes) where some C≤50 wins for EVERY prime: {len(full)} (examples {full[:5]})")
# ---- Z1948: correlation of log(1+R) between p and p+840k (and class-mean residual)
lr = {p: math.log(1 + rows[p][0]) for p in P1}
mu = {}
for c, ps in cls840.items(): mu[c] = np.mean([lr[p] for p in ps])
for k in (1, 2, 5, 10):
    pr = [(p, p+840*k) for p in P1 if p+840*k in lr]
    a = np.array([lr[p] for p, _ in pr]); b = np.array([lr[q] for _, q in pr])
    ra = np.array([lr[p]-mu[p % 840] for p, _ in pr]); rb = np.array([lr[q]-mu[q % 840] for _, q in pr])
    log(f"Z1948 lag 840·{k}: corr log(1+R) = {np.corrcoef(a,b)[0,1]:.3f}; after class-mean removal = {np.corrcoef(ra,rb)[0,1]:.3f} (n={len(pr)})")
open(D+"cf_out.txt", "w").write("\n".join(out)+"\n")
