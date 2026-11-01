# z52d pass2 NC1 misc3: Z1351 lemma check (witness (C,d) for p propagates to p+24k iff d | k when gcd(d,3)=1, d/3 | k otherwise);
# Z1464 C_min distribution (from list file); Z1707 Pell-representation witness rate at C=y vs base rate at the same C over all primes.
import math, random, sys
import numpy as np
from sympy import primerange
def wits(p, C):
    N = 4*C*p+1; m = 4*C; out = []; d = m-1
    while d*d <= N:
        if N % d == 0: out.append(d)
        d += m
    return out
random.seed(2); tot = viol = 0
P = [p for p in primerange(5, 200000) if p % 24 == 1]
for p in random.sample(P, 300):
    for C in range(1, 6):
        for d in wits(p, C)[:1]:
            for k in range(1, 400):
                q = p+24*k; has = d in wits(q, C)
                pred = (k % (d if d % 3 else d//3) == 0)
                tot += 1; viol += int(has != pred)
print('Z1351 lemma checks', tot, 'violations', viol)
d = np.loadtxt('/tmp/list_c50_1e7.txt', dtype=np.int64); c = d[:, 1]
print('Z1464 frac Cmin=1', round(float((c == 1).mean()), 4), 'Cmin=2', round(float((c == 2).mean()), 4), 'Cmin<=2', round(float(((c == 1) | (c == 2)).mean()), 4))
P4 = [p for p in primerange(5, 20000) if p % 4 == 1]
def witness(p, C): return len(wits(p, C)) > 0
base = {}
def rate(C): return sum(witness(p, C) for p in P4)/len(P4)
res = {}
for D in [5, 8, 12, 13]:
    hits = []; bases = []
    for p in P4:
        rep = None
        for y in range(1, 200):
            x2 = p+D*y*y; x = math.isqrt(x2)
            if x*x == x2: rep = (x, y); break
        if rep is None: continue
        y = rep[1]; hits.append(witness(p, y))
        if y not in base: base[y] = rate(y)
        bases.append(base[y])
    res[f'D={D}'] = {'reps': len(hits), 'witness_at_C=y': round(sum(hits)/len(hits), 3), 'base_rate_same_C_all_primes': round(sum(bases)/len(bases), 3)}
print('Z1707', res)
