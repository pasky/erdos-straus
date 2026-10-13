"""R180: Prop 7.1 check. Stern s(N) on binary 1 0^{a1-2} 1 ... 0^{ak-2} 1 equals negative continuant; and
{s(N): popcount N = k+1, N < 2^B} vs {K^-(a)} for small values."""
from functools import lru_cache
import itertools, sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def s(n):
    if n < 2: return n
    return s(n // 2) if n % 2 == 0 else s(n // 2) + s(n // 2 + 1)
def K(a):
    p, q = 1, 0
    for x in a: p, q = x * p - q, p
    return p
bad = 0
for k in (1, 2, 3, 4):
    for a in itertools.product(range(2, 12 if k < 4 else 8), repeat=k):
        N = int("1" + "".join("0" * (x - 2) + "1" for x in a), 2)
        if s(N) != K(a): bad += 1
        if k == 3 and s(N) != a[0]*a[1]*a[2] - a[0] - a[2]: bad += 1
print("mismatches:", bad)
# value sets for k=3 below 300: Stern side from all N with popcount 4 up to 2^40 restricted by value (s >= number of bits gives cutoff)
LIM = 300
vals = set()
for B in range(4, 40):
    for ones in itertools.combinations(range(B - 1), 2):  # top bit B-1, bottom bit 0 set (odd N), 2 more ones
        N = (1 << (B - 1)) | 1 | (1 << ones[0]) | (1 << ones[1])
        if ones[1] == 0 or ones[0] == 0: continue
        v = s(N)
        if v < LIM: vals.add(v)
direct = {x*y*z - x - z for x in range(2, LIM) for y in range(2, LIM) for z in range(2, LIM) if x*y*z - x - z < LIM and x*y <= LIM+x+z}
print("Stern popcount-4 values == A3 values below", LIM, ":", vals == direct, sorted(set(range(LIM)) - vals)[:20])
