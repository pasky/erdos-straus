"""U02 compliance pass (batch R)."""
import sys, math, json
import numpy as np
from fractions import Fraction as Fr
from collections import Counter
from sympy import divisors, primerange, jacobi_symbol
sys.path.insert(0, 'scripts')
R = {}
pl = [p for p in primerange(5, 20000) if p % 4 == 1]
# Z1471 all winning divisors a (a = -1 mod 4C, a | N, 1<a<N), C<=12, p<=2e4 (first 300 primes)
cc = Counter()
for p in pl[:300]:
    for C in range(1, 13):
        m = 4 * C; N = 4 * C * p + 1
        for a in divisors(N):
            if 1 < a < N and (a + 1) % m == 0:
                cc[jacobi_symbol(a % p, p)] += 1
R['Z1471_all_winning_a_legendre_mod_p'] = {str(k): v for k, v in cc.items()}
# Z0249: r_T(n) = #{(a,b,c) >= 0 : T_a+T_b+T_c = n}, T_a = a(a+1)/2 ; correlate with residual log U (n <= 3000 composite-free? use all n)
import sys as _s
F = np.loadtxt('/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
n_all, U = F[:, 0], F[:, 1].astype(float)
Nm = 3000
rT = np.zeros(Nm + 1)
T = [a * (a + 1) // 2 for a in range(0, 80) if a * (a + 1) // 2 <= Nm]
for a in T:
    for b in T:
        for c in T:
            s = a + b + c
            if s <= Nm: rT[s] += 1
sel = (n_all >= 100) & (n_all <= Nm) & (U > 0)
lu = np.log(U[sel]); ln = np.log(n_all[sel])
X = np.column_stack([np.ones_like(ln), ln, np.log(ln)])
res = lu - X @ np.linalg.lstsq(X, lu, rcond=None)[0]
R['Z0249'] = {'n': int(sel.sum()), 'corr_resU_rT': round(float(np.corrcoef(res, rT[n_all[sel]])[0, 1]), 4),
              'corr_resU_log_rT': round(float(np.corrcoef(res, np.log1p(rT[n_all[sel]]))[0, 1]), 4)}
# Z0889: Markov primes (prime Markov numbers <= 1e5) and least QNR; fail(12) membership from f4-free check: 12/p 3-term? use esols on 12/p
from z52b_p1_U02_lib import esols
mk = set(); stack = [(1, 1, 2), (1, 2, 5), (2, 1, 5)]
# Markov triples x^2+y^2+z^2=3xyz: generate from (1,1,1) by Vieta; collect numbers <= 1e5
trip = [(1, 1, 1)]; seen = set([(1, 1, 1)]); frontier = [(1, 1, 1)]
while frontier:
    x, y, z = frontier.pop()
    for t in [(x, y, 3 * x * y - z), (x, 3 * x * z - y, z), (3 * y * z - x, y, z)]:
        if min(t) >= 1 and max(t) <= 10**5 and tuple(sorted(t)) not in seen:
            seen.add(tuple(sorted(t))); frontier.append(tuple(sorted(t)))
for t in seen:
    for v in t: mk.add(v)
from sympy import isprime
mp = sorted(v for v in mk if isprime(v))
def least_qnr(p):
    if p == 2: return None
    q = 2
    while pow(q, (p - 1) // 2, p) == 1: q += 1
    return q
R['Z0889'] = {'prime_markov_numbers_le_1e5': mp, 'least_qnr': {p: least_qnr(p) for p in mp}}
# Z0890: U(p) at 409, 577 and at primes near Pell numbers 2378..2380? (use nearest primes to 408 and 577 squares)
R['Z0890'] = {'U(409)': int(U[n_all == 409][0]), 'U(577)': int(U[n_all == 577][0]),
              'nearest_primes_1mod4_to_2379_3361_13861_19601': [p for p in [2377, 2381, 3359, 3371, 13859, 13873, 19597, 19609] if p % 4 == 1 and isprime(p)]}
json.dump(R, open('data/z52b/pass1/U02/compl_r.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:3000])
