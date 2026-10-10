"""R131: compare brute-force solution sets (review_r131_brute.c) with the author's engine + expand_T1,
and check Lemma 1.1 structurally on brute-force data (own code; exf_load only used to read the author's dump)."""
import sys, numpy as np
from math import gcd
from collections import defaultdict
N = int(sys.argv[1]); sol = sys.argv[2]; auth = sys.argv[3]
S = defaultdict(set)
for line in open(sol):
    f, n, a, b, c, d = map(int, line.split()); S[f].add((n, a, b, c, d))
print({k: len(v) for k, v in sorted(S.items())})
sys.path.insert(0, 'scripts'); import exf_load
for sgn, pre, f1, f2 in [(1, 'p', 0, 2), (-1, 'm', 1, 3)]:
    T1, T2 = exf_load.load_full(auth + '/' + pre, N)
    A1 = {(int(r['n']), int(r['a']), int(r['b']), int(r['c']), int(r['d'])) for r in T1}
    A2 = {(int(r['n']), int(r['a']), int(r['b']), int(r['c']), int(r['d'])) for r in T2}
    print('sign', sgn, 'T1 equal:', A1 == S[f1], len(A1), len(S[f1]), ' T2 equal:', A2 == S[f2], len(A2), len(S[f2]))
# Lemma 1.1 structural check on brute data
bad = 0; prim = {0: set(), 1: set()}
for fam, s in [(0, 1), (1, -1)]:
    for (n, a, b, c, d) in S[fam]:
        f = 4*a*c*d - n; h = gcd(f, 4*a*a*d + s); k = f // h
        assert f > 0
        if c % k or n % k: bad += 1; continue
        m, c1 = n // k, c // k
        if not (4*a*b*c1*d == m*(a+b) + s*c1 and (4*a*c1*d - m) == h and (4*a*a*d + s) % h == 0): bad += 1
        if k == 1: prim[fam].add((n, a, b, c, d))
    # converse: every scaling of a k=1 solution is a solution
    for (n, a, b, c, d) in prim[fam]:
        for k in range(2, N // n + 1):
            if (k*n, a, b, k*c, d) not in S[fam]: bad += 1
print('Lemma 1.1 failures:', bad)
for fam in range(4):
    cnt = defaultdict(int)
    for t in S[fam]: cnt[t[0]] += 1
    print('fam', fam, 'zeros n<=%d:' % N, [n for n in range(1, N+1) if cnt[n] == 0][:40])
