"""Fix round TO3 (Z0758): test divisor-class characterisations of the even ESC zeros.
Candidate: ESC(n)=0 <=> [exists d | n+1 with d mod 8 in S] or [exists d | 2n+1 with d mod 8 in T]  (S,T subsets of odd classes),
searched over all 256 pairs (S,T) on all even n <= NMAX from the word census (ESC column).
Non-square even n only (squares are T1-type zeros, all ESC-zero). Writes data/z52b/pass2/TO3/esc_char_results.json"""
import sys, json, numpy as np
from sympy import divisors
NMAX = 30000
W = np.loadtxt('/tmp/z52/words3e6.txt', dtype=np.int64)[:NMAX]
ESC0 = {int(n) for n, e in zip(W[:, 0], W[:, 5]) if e == 0}
import math
ns = [n for n in range(2, NMAX + 1, 2) if math.isqrt(n) ** 2 != n]   # squares excluded (T1-type zeros)
def classes(m):
    return frozenset(d % 8 for d in divisors(m) if d % 2 == 1)
C1 = {n: classes(n + 1) for n in ns}
C2 = {n: classes(2 * n + 1) for n in ns}
truth = {n: (n in ESC0) for n in ns}
best = []
odd = [1, 3, 5, 7]
for sm in range(1, 16):
    S = {odd[i] for i in range(4) if sm >> i & 1}
    for tm in range(0, 16):
        T = {odd[i] for i in range(4) if tm >> i & 1}
        ok = sum(1 for n in ns if (not (C1[n] & S) and not (C2[n] & T)) == truth[n])
        best.append((ok, sorted(S), sorted(T)))
best.sort(reverse=True)
out = {'n_even_checked': len(ns), 'n_ESC_zero_even': len(ESC0), 'best_matches': best[:5],
       'zero_list_even_nonsquare_le_NMAX': sorted(x for x in ESC0 if math.isqrt(x) ** 2 != x)}
json.dump(out, open('data/z52b/pass2/TO3/esc_char_results.json', 'w'), indent=1)
print(json.dumps(out)[:1500])
