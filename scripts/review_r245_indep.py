"""R245: test the 'independent lotteries' heuristic (s6_window_independence) at small windows.
For primes p = 1 (4) < P and windows m = 3 (4), m <= W, gcd(m,p)=1: cap0(p,m) <=> -1 in Sigma_m(K), K=(p+m)/4
(CAP_DOWN Lemma 1.1 / Lemma 3.1 delta_p = 0 slice). Compare observed #p with no cap-0 window to the independence prediction."""
import sys
from sympy import primerange, factorint
P, W = int(sys.argv[1]), int(sys.argv[2])
wins = [m for m in range(3, W + 1, 4)]
def cap0(K, m):
    S = {1}
    for s, b in factorint(K).items():
        pw = [pow(s, e, m) for e in range(b + 1)]
        S = {x * y % m for x in S for y in pw}
        if len(S) == 0: break
    return any((-x) % m in S for x in S)
rows = []
for p in primerange(5, P):
    if p % 4 != 1: continue
    rows.append({m: cap0((p + m) // 4, m) for m in wins if p % m and __import__('math').gcd(m, p) == 1})
rate = {m: sum(r[m] for r in rows if m in r) / sum(1 for r in rows if m in r) for m in wins}
print('per-window cap-0 rates:', {m: round(v, 3) for m, v in rate.items()})
import math
pred = sum(math.prod(1 - rate[m] for m in r) for r in rows)
obs = sum(1 for r in rows if not any(r.values()))
print(f'{len(rows)} primes; observed with no cap-0 window <= {W}: {obs}; independence prediction: {pred:.1f}')
# conditional on failing at m = 3 (p = 1 mod 3), same comparison
sub = [r for r in rows if not r.get(3, False)]
pred2 = sum(math.prod(1 - rate[m] for m in r if m != 3) for r in sub)
print(f'p with m=3 dead: {len(sub)}; observed none: {obs}; pred (marginal rates, m != 3): {pred2:.1f}')
