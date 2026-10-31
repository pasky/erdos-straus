"""z52b pass1 U05: solution-level analyses. Needs dumps made by:
   seq 3 3000 | UDUMP=1 scripts-built /tmp/ucount | grep ^S > /tmp/u05/dump_n3000.txt   (all n≤3000)
   awk '$1>=5 && $1<=20000' primes | UDUMP=1 /tmp/ucount | grep ^S > /tmp/u05/dump_p2e4.txt
Items: Z0939 (A257843 membership), Z0279 (min-max solution type), Z0955 (y/x, z/y spectra), Z0818 (Gini of x-profile),
Z0819 (residue patterns mod 3,5,7), Z0982 (smallest z-y), Z0233 (product collisions)."""
import math, numpy as np
from collections import Counter, defaultdict
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
sols_n = defaultdict(list)
for l in open("/tmp/u05/dump_n3000.txt"):
    _, n, x, y, z = l.split(); sols_n[int(n)].append((int(x), int(y), int(z)))
sols_p = defaultdict(list)
for l in open("/tmp/u05/dump_p2e4.txt"):
    _, n, x, y, z = l.split(); sols_p[int(n)].append((int(x), int(y), int(z)))
# ---- Z0939: A257843: n where lexicographically-first solution != max-z solution
def is_A(n, src=None):
    S = (src or sols_n).get(n, [])
    if not S: return None
    lex = min(S)                      # lexicographically first (x,y,z) with x≤y≤z
    mz = max(S, key=lambda t: (t[2], t[1], t[0]))
    return lex != mz
A = [n for n in range(3, 3001) if is_A(n)]
log("Z0939 A257843 terms reproduced (n≤3000, first 13):", A[:13])
log("  claimed: 89,113,161,233,281,329,353,401,409,449,473,521,593 — all present:", all(n in A for n in [89,113,161,233,281,329,353,401,409,449,473,521,593]))
pr = [p for p in sols_p if p % 4 == 1 and p > 4]
mem = [p for p in pr if is_A(p, sols_p)]
log(f"  primes p≡1(4) in A257843: {len(mem)} of {len(pr)} ({len(mem)/len(pr):.3f}); by p mod 24: " +
    str({c: round(np.mean([is_A(p, sols_p) for p in pr if p % 24 == c]), 3) for c in (1, 5, 13, 17)}))
# ---- Z0279: type of the min-max solution (smallest largest denominator)
typ = Counter()
for p in pr:
    S = sols_p[p]
    best = min(S, key=lambda t: (t[2], t[0], t[1]))
    x, y, z = best
    typ["II (p|y,z)" if (y % p == 0 and z % p == 0) else ("I (p|x)" if x % p == 0 else "other")] += 1
log("Z0279 type of minmax-z solution (primes p≡1(4), ≤2e4):", dict(typ))
x_min = Counter()
for p in pr:
    S = sols_p[p]; best = min(S, key=lambda t: (t[2], t[0], t[1]))
    x_min["x|z" if best[2] % best[0] == 0 else "x∤z"] += 1
log("  minmax-z solution: x | z ?", dict(x_min))
# ---- Z0955: spectrum of log(y/x) and log(z/y) for p≡1(4) ≤ 2e4, by class mod 840 (summary)
ly = []; lz = []
for p in pr:
    for x, y, z in sols_p[p]:
        ly.append(math.log(y/x)); lz.append(math.log(z/y))
h, edges = np.histogram(ly, bins=40, range=(0, 8))
top = np.argsort(h)[::-1][:5]
log("Z0955 peaks of log(y/x) histogram (40 bins on [0,8]): top bins at", [round(edges[i],2) for i in top], "counts", h[top].tolist(), f"; total {len(ly)} solutions")
# integer ratios: fraction of solutions with y/x or z/y an integer, and the most common integer ratio
ri = Counter()
for p in pr:
    for x, y, z in sols_p[p]:
        if y % x == 0: ri[("y/x", y//x)] += 1
        if z % y == 0: ri[("z/y", z//y)] += 1
log("  most common integer ratios:", ri.most_common(6))
# ---- Z0818: Gini of x-profile per prime (number of solutions per distinct x), p≡1(4), ≤2e4
def gini(v):
    v = np.sort(np.array(v, float)); n = len(v)
    if n == 0 or v.sum() == 0: return float('nan')
    return (2*np.arange(1, n+1) - n - 1).dot(v) / (n * v.sum())
G = []
for p in pr:
    cnt = Counter(x for x, _, _ in sols_p[p]); G.append(gini(list(cnt.values())))
log(f"Z0818 Gini of solutions-per-x over p≡1(4)≤2e4: median {np.nanmedian(G):.3f}, 10%/90% {np.nanpercentile(G,10):.3f}/{np.nanpercentile(G,90):.3f}")
# ---- Z0819: residue patterns mod 3,5,7 of solutions (distinct patterns per prime)
pat = {}
for p in pr:
    S = sols_p[p]
    pt = set((x % 105, y % 105, z % 105) for x, y, z in S)
    pat[p] = (len(S), len(pt))
hard = sorted(pr, key=lambda p: len(sols_p[p]) / math.log(p)**2)[:200]
easy = sorted(pr, key=lambda p: -len(sols_p[p]) / math.log(p)**2)[:200]
log("Z0819 distinct (x,y,z) mod 105 patterns per prime: hard-200 median %.1f of median %.1f solutions; easy-200 median %.1f of %.1f" % (
    np.median([pat[p][1] for p in hard]), np.median([pat[p][0] for p in hard]),
    np.median([pat[p][1] for p in easy]), np.median([pat[p][0] for p in easy])))
# ---- Z0982: smallest z-y over solutions (primes <1000), and all n≤3000 of U(n)
zy = {}
for p in pr:
    if p < 1000: zy[p] = min(z - y for x, y, z in sols_p[p])
log("Z0982 smallest z−y over solutions, primes p≡1(4)<1000 (first 12):", [(p, zy[p]) for p in list(zy)[:12]])
log("  overall min z−y among those:", min(zy.values()), "at", min(zy, key=zy.get))
# ---- Z0233: collisions of products x*y among solutions at fixed p (sample of hard/easy primes)
col = []
for p in hard[:100] + easy[:100]:
    S = sols_p[p]; prods = Counter(x*y for x, y, z in S)
    col.append(sum(c for c in prods.values() if c > 1) / len(S))
log(f"Z0233 share of solutions whose product x·y collides with another solution's product: hard-100 median {np.median(col[:100]):.3f}, easy-100 median {np.median(col[100:]):.3f}")
open("data/z52b/pass1/U05/2nd/sol_out.txt", "w").write("\n".join(out)+"\n")
