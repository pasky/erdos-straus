# Z3004 (concrete reading): smallest set of levels C (menu) such that every Mordell-hard prime p <= P (p mod 840 a square class,
# p ≡ 1 mod 8) has a level-4C word for some C in the menu; levels C <= CMAX.  Level-4C words <-> divisors of 4Cp+1
# (scripts/z52d_p2_NC3_levels.py).  Exact min hitting set via branch and bound on the family {S_p} (S_p = levels that work for p),
# greedy upper bound.  Reports min menu size K as a function of P and CMAX.
import sys
from sympy import factorint
from collections import Counter
P = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
CMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
HARD = {1, 121, 169, 289, 361, 529}
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def divs(N):
    f = factorint(N); ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def levels_ok(p, C):
    t = 4*C; N = t*p + 1
    for A in divs(N):
        if A % t != t-1 or A < 2*t-1: continue
        B = N // A
        if B % t == t-1 and B >= 2*t-1: return True
    return False
hard = [p for p in L.primes_upto(P) if p % 8 == 1 and p % 840 in HARD]
S = {}
for p in hard:
    S[p] = frozenset(C for C in range(1, CMAX+1) if levels_ok(p, C))
no_cover = [p for p in hard if not S[p]]
print("hard primes p <= %d: %d; with no level <= %d: %d %s" % (P, len(hard), CMAX, len(no_cover), no_cover[:10]))
# greedy set cover
rem = {p for p in hard if S[p]}
menu = []
while rem:
    cnt = Counter()
    for p in rem:
        for C in S[p]: cnt[C] += 1
    C, _ = cnt.most_common(1)[0]
    menu.append(C)
    rem = {p for p in rem if C not in S[p]}
print("greedy menu size:", len(menu), "levels:", sorted(menu))
# exact minimum for small menus: check sizes k = 1,2,3 by brute force over level subsets of the greedy support
allC = sorted({C for p in hard for C in S[p]})
best = None
for k in range(1, len(menu)+1):
    from itertools import combinations
    found = None
    for comb in combinations(allC[:CMAX], k):
        cs = set(comb)
        if all(S[p] & cs for p in hard if S[p]):
            found = comb; break
    if found:
        print("exact minimum menu size:", k, "e.g.", found); best = k; break
    if k >= 4: print("no menu of size <= 4 found; greedy gives", len(menu)); break
# exact minimum hitting set by branch and bound (sets S_p, primes with nonempty S_p)
fam = [S[p] for p in hard if S[p]]
def minhit(fam, budget):
    # returns a hitting set of size <= budget or None
    if not fam: return []
    if budget == 0: return None
    # branch on the smallest unhit set
    f = min(fam, key=len)
    for C in sorted(f):
        rest = [g for g in fam if C not in g]
        sub = minhit(rest, budget-1)
        if sub is not None: return [C] + sub
    return None
for b in range(1, len(menu)+1):
    res = minhit(fam, b)
    if res is not None:
        print("exact minimum hitting set size (levels <= %d):" % CMAX, len(res), sorted(res)); break
