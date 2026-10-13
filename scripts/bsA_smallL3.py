"""bsA_smallL3: for n = 1 (4) non-square, distribution of |L3(n)| (number of length-3 words, letters >= 2) for small
values, and how many -1 words those n have (test whether 'nonempty => some -1 word' is a coin or a structure)."""
import sys
from math import isqrt
from collections import Counter, defaultdict
from sympy import jacobi_symbol
N = int(sys.argv[1])
cnt = [0]*N; negc = [0]*N; words = defaultdict(list)
t = 2
while 4*t - 4 < N:
    u = 2
    while t*u*2 - u - 2 < N:
        v = 2
        while t*u*v - u - v < N:
            n = t*u*v - u - v
            if n % 4 == 1:
                cnt[n] += 1; s = jacobi_symbol(t*u - 1, n); negc[n] += s == -1
                if len(words[n]) < 6: words[n].append((v, t, u, s))
            v += 1
        u += 1
    t += 1
C = Counter(); ex = defaultdict(list)
for n in range(5, N, 4):
    if isqrt(n)**2 == n: continue
    L = cnt[n]
    if L <= 6:
        C[(L, negc[n])] += 1
        if len(ex[(L, negc[n])]) < 5: ex[(L, negc[n])].append(n)
print("(|L3|, #(-1 words)) counts for non-square n=1(4) <", N, "with |L3|<=6:")
for k in sorted(C): print(k, C[k], ex[k])
for n in ex.get((2, 2), [])[:3] + ex.get((4, 2), [])[:2]: print(n, words[n])
# --- comparison N+ vs N- over all non-square n = 1 (4) ---
worse = []; ratio = []
for n in range(5, N, 4):
    if isqrt(n)**2 == n or cnt[n] == 0: continue
    npos = cnt[n] - negc[n]
    if npos > negc[n]: worse.append(n)
    ratio.append((negc[n] / cnt[n], n))
ratio.sort()
print("non-square n=1(4) with N+ > N-:", len(worse), worse[:30])
print("smallest N-/|L3| ratios:", ratio[:8])
