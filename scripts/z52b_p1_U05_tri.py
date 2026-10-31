"""z52b pass1 U05 Z2652 follow-up: triangle multigraphs (tau = xy+yz+zx = p, pairing class = ((x+y)/p)); test for p<=2e4
whether a non-square triangle always exists and compare with the C-form criterion (wins for C<=5, from cform data)."""
import numpy as np, math
from collections import Counter
D = "data/z52b/pass1/U05/2nd/"
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
M = 20000
isp = np.ones(M+1, bool); isp[:2] = False
for i in range(2, int(M**.5)+1):
    if isp[i]: isp[i*i::i] = False
primes = [p for p in range(5, M+1) if isp[p] and p % 4 == 1]
def leg(a, p):
    a %= p; return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
cf = {}
for l in open(D+"cform_C200_p1e5.txt"):
    t = list(map(int, l.split())); cf[t[0]] = set(t[3:3+t[2]])
has_tri = {}; cnt_tri = Counter()
for p in primes:
    found = None; nsol = 0
    for x in range(1, int(p**.5)+2):
        for y in range(1, p):
            if x*y >= p: break
            r = p - x*y
            if r % (x+y): continue
            z = r//(x+y)
            if z < 1: continue
            nsol += 1
            if leg(x+y, p) == -1: found = (x, y, z); break
        if found: break
    has_tri[p] = found is not None
    cnt_tri[nsol > 0] += 1
tri_any = sum(has_tri.values())
log(f"triangles: p≡1(4), 5≤p≤2e4 ({len(primes)} primes): non-square-pairing triangle exists for {tri_any}; representation p=xy+yz+zx exists for {cnt_tri[True]}")
fails = [p for p in primes if not has_tri[p]]
log("  primes with NO non-square triangle (first 15):", fails[:15], "count", len(fails))
# comparison with C-form (C<=5) on primes <=1e5 that are in both tables
both = [p for p in primes if p in cf]
agree = Counter((has_tri[p], any(c <= 5 for c in cf[p])) for p in both)
log("  2x2 table (triangle criterion, C-form win C≤5) on p≤1e5 ∩ ≤2e4:", dict(agree))
open(D+"tri_out.txt", "w").write("\n".join(out)+"\n")
