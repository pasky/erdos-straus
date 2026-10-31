"""z52b pass1 U05 final batch: Z0934 (k(p)=min multiplier of a denominator divisible by p, from solution dumps p≤2e4),
Z0768 (W(n) records, n≤3000), Z1411 (worst mod-840 profiles by C_min≤10 fraction, from cmin census p≤1e6),
Z1628 (p=409 residue table for p+u), Z1747 (residue-indicator regression of log(1+R) vs Q), Z1782 (Type II/I
structure of the 409 solutions by enumeration), Z1943 (near-miss gap with strictly positive gap), Z1573 (14 census primes with C≤20000)."""
import math, subprocess, numpy as np
from collections import Counter, defaultdict
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
D = "data/z52b/pass1/U05/2nd/"
# ---- Z0934
sols = defaultdict(list)
for l in open("/tmp/u05/dump_p2e4.txt"):
    _, n, x, y, z = l.split(); sols[int(n)].append((int(x), int(y), int(z)))
kp = {}
for p, S in sols.items():
    if p % 4 != 1: continue
    ks = [w//p for s in S for w in s if w % p == 0]
    if ks: kp[p] = min(ks)
mx = max((k/math.log(p), p) for p, k in kp.items() if p > 3)
log(f"Z0934 k(p)=min{{denominator/p : p | denominator}} over p≡1(4), 5≤p≤2e4 (solutions with p dividing a denominator): "
    f"max k/log p = {mx[0]:.3f} at p={mx[1]} (k={kp[mx[1]]}); records: " +
    str([(p, kp[p]) for p in sorted(kp) if all(kp[p] > kp[q] for q in kp if q < p)][:10]))
# ---- Z0768: W(n) = #{t,u,v≥1 : tuv-u-v = n}
def W(n):
    c = 0
    for t in range(1, n+2):
        for u in range(1, n+2):
            den = t*u - 1
            if den <= 0: continue
            num = n + u
            if num % den == 0 and num//den >= 1: c += 1
    return c
Wv = {n: W(n) for n in range(1, 801)}
recs = []; best = -1
for n in range(1, 801):
    if Wv[n] > best: best = Wv[n]; recs.append((n, best))
log("Z0768 W(n) records (n≤800): " + str(recs[:14]))
# ---- Z1411: profiles mod 840 with C_min≤10 fraction (from cmin census p≤1e6, p≡1(4))
rows = [tuple(map(int, l.split())) for l in open(D+"cmin_p1e6_C1000.txt")]
prof = defaultdict(list)
for p, c in rows:
    if p > 840: prof[p % 840].append(c)
frac = {r: (sum(1 for c in v if 0 < c <= 10)/len(v), len(v)) for r, v in prof.items() if len(v) >= 30}
worst = sorted(frac.items(), key=lambda t: t[1][0])[:5]
best_ = sorted(frac.items(), key=lambda t: -t[1][0])[:3]
log(f"Z1411 profiles mod 840 (≥30 primes): fraction with C_min≤10: min {worst[0][1][0]:.3f} at r={worst[0][0]} (n={worst[0][1][1]}), "
    f"max {best_[0][1][0]:.3f} at r={best_[0][0]}; lowest-5 classes: {[(r, round(f,3), n) for r,(f,n) in worst]}")
# ---- Z1628: p=409 table, u≤50: factor 409+u, does a divisor ≡ -1 (mod 4u) exist? which odd q have (q/409)
def leg(a, p):
    a %= p; return 1 if pow(a, (p-1)//2, p) == 1 else -1
def fac(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def divs(f):
    ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
p = 409
tab = []
for u in range(1, 51):
    f = fac(p+u); ok = any(d % (4*u) == (4*u-1) for d in divs(f)) if u > 1 else False
    syms = [leg(q, p) for q in f if q != 2]
    tab.append((u, ok, all(s == 1 for s in syms)))
fail_allqr = sum(1 for u, ok, allqr in tab if not ok and allqr)
log(f"Z1628 p=409, u≤50: 'p+u has divisor ≡-1 mod 4u' fails for {sum(1 for t in tab if not t[1])} u; among those, all odd prime factors of p+u are QR mod 409 for {fail_allqr}")
# ---- Z1782: solution structure at p=409 (Type I/II by denominators divisible by 409)
S = sols[409]
typ = Counter("II" if sum(1 for w in s if w % 409 == 0) == 2 else ("I" if sum(1 for w in s if w % 409 == 0) == 1 else "none") for s in S)
log(f"Z1782 p=409: {len(S)} ordered-by-x solutions in dump; type counts {dict(typ)}; min z {min(max(s) for s in S)}; "
    "(Type II solutions exist, so the C-form misses only the Type I route)")
# ---- Z1943 (strictly positive gap)
def near_gap(p, B=8):
    best = None
    for x in range(math.ceil(p/4), B*p + 1):
        r1 = 4*x - p
        if r1 <= 0: continue
        for y in range(x, B*p + 1):
            num = r1*y - p*x
            if num <= 0: continue
            z = -(-p*x*y // num)
            gap = num/(p*x*y) - 1/z
            if gap > 0 and (best is None or gap < best): best = gap
            if y > 4*x: break
    return best
pr = [q for q in range(5, 401) if q % 4 == 1 and all(q % d for d in range(2, int(q**.5)+1))]
gs = {q: near_gap(q, 6) for q in pr}
gs = {q: g for q, g in gs.items() if g is not None}
log(f"Z1943 positive near-miss gap (x,y≤6p, greedy z) for p≡1(4)≤400: {len(gs)} primes; smallest 5 gaps {[(q, round(g,6)) for q,g in sorted(gs.items(), key=lambda t:t[1])[:5]]}; "
    f"gap·p² median {np.median([g*q*q for q,g in gs.items()]):.3f}; for 409: {round(gs[409]*409*409,3) if 409 in gs else None}")
# ---- Z1573: the 14 census primes (C≤1000) : any win for C≤20000?
exc = [p for p, c in rows if c == 0]
got = subprocess.run(["/tmp/cmin", "20000"], input="\n".join(map(str, exc)), capture_output=True, text=True).stdout
log("Z1573 C≤1000 census exceptions ≤1e6 (14) refined to C≤20000: " + "; ".join(l for l in got.strip().split("\n")))
open(D+"final_out.txt", "w").write("\n".join(out)+"\n")
# ---- Z1943 rescale (gap ~ p^-3): report gap·p³ quantiles
g3 = {q: g*q**3 for q, g in gs.items()}
log("Z1943 gap·p³ quantiles over these primes: 10/50/90%% = %s; for 409 (not in range) n/a" % (
    [round(float(np.percentile(list(g3.values()), a)), 4) for a in (10, 50, 90)]))
open(D+"final_out.txt", "a").write("\n".join(out[-1:])+"\n")
