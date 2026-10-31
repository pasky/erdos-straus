"""U01 statistics on the all-solutions enumeration (data/z52b/pass1/U01/allsols_5000.txt.gz) and two extra checks:
Z1655 (prime denominator y or z), Z1941/Z3154 (min max-denominator scaling), Z2232 (U vs D), Z2372 (3-fold reciprocal sums mod hash),
Z3114 (numerator sets A_p ∩ [1,48]), Z1944 (4-term rescue, p<=300)."""
import sys, os, gzip, math, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto, load_m, load_counts, RAW, REPO
rows = [l.split() for l in gzip.open(os.path.join(REPO, "data/z52b/pass1/U01/allsols_5000.txt.gz"), "rt") if not l.startswith("#")]
R = [dict(p=int(r[0]), U=int(r[1]), mm=float(r[2])*int(r[0]), nprime=int(r[4]), niso=int(r[5])) for r in rows]
print("== Z1655 prime y or z denominator (p<=5000)")
none = [d["p"] for d in R if d["U"] > 0 and d["nprime"] == 0]
print("primes with no solution having a prime y or z:", len(none), "of", len(R), "; smallest:", none[:12])
print("== Z1941/Z3154 min over sols of max(x,y,z): dyadic maxima of min-max/p and /p^2")
for lo in (100, 300, 1000, 3000):
    sub = [d for d in R if lo <= d["p"] < lo*3 if d["U"] > 0]
    if sub:
        a = max(d["mm"]/d["p"] for d in sub); b = max(d["mm"]/d["p"]**2 for d in sub)
        print(f"p in [{lo},{3*lo}): n={len(sub)} max minmax/p={a:.1f} (p={max(sub,key=lambda d:d['mm']/d['p'])['p']}), max minmax/p^2={b:.3f}")
x = np.array([math.log(d["p"]) for d in R if d["U"] > 0]); y = np.array([math.log(d["mm"]/d["p"]) for d in R if d["U"] > 0])
print("log(minmax/p) ~ slope", round(np.polyfit(x, y, 1)[0], 3), "in log p")
print("== Z2232 unordered U (x<=y<=z, increasing convention) median", sorted(d["U"] for d in R)[len(R)//2], "; iso fraction", round(sum(1 for d in R if d["niso"]>0)/len(R), 3))
# Z2372: 3-fold reciprocal sums of {1/x: x<=N} mod a 61-bit prime; membership of 4/n (n<=N) denominators-bounded test
P = (1 << 61) - 1
def inv(v): return pow(v, P-2, P)
N = 300
I = [0] + [inv(x) for x in range(1, N+1)]
S = set()
ar = I[1:]
for i in range(N):
    for j in range(i, N):
        s2 = (ar[i] + ar[j]) % P
        for k in range(j, N):
            S.add((s2 + ar[k]) % P)
hits = [n for n in range(2, N+1) if (4*inv(n)) % P in S]
print(f"== Z2372 N={N}: distinct 3-fold sums (mod P) = {len(S)}; 4/n in set for {len(hits)} of {N-1} n (n<=N); misses among primes: {[n for n in primes_upto(N) if n not in hits][:10]}")
# Z3114: numerator sets A_p ∩ [1,48] for primes; union-closure test on the family
U = {m: load_m(m) for m in range(5, 49)}
ps = [p for p in U[5] if p > 5]
Ap = {p: frozenset(m for m in range(5, 49) if U[m][p] > 0) for p in ps}
fam = set(Ap.values())
cnt = 0; tot = 0
flist = list(fam)
for i in range(0, min(len(flist), 400)):
    for j in range(i+1, min(len(flist), 400)):
        tot += 1
        if (flist[i] | flist[j]) in fam: cnt += 1
print(f"== Z3114 numerator sets A_p∩[5,48] for {len(ps)} primes: {len(fam)} distinct; unions of random pairs (first 400) in family: {cnt}/{tot}")
print("   most common A_p sizes:", collections.Counter(len(s) for s in Ap.values()).most_common(3))
