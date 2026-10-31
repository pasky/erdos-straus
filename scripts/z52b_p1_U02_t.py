"""U02 compliance pass (batch T): Z1835 (fail rate vs 2-rank of (Z/4C)^*), Z1686 (residual U vs class number / L(1,chi_p)),
Z1022 (solutions with a denominator sharing a factor with 4C), Z0536 control (random N of same size)."""
import sys, math, json, random
import numpy as np
from sympy import divisors, primerange, factorint
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
R = {}
def two_rank(m):
    # number of x with x^2 = 1 in (Z/m)^* is 2^rank
    cnt = sum(1 for x in range(1, m) if math.gcd(x, m) == 1 and (x * x) % m == 1)
    return int(round(math.log2(cnt)))
def fail(p, C):
    m = 4 * C; N = 4 * C * p + 1
    return not any(1 < d < N and (d + 1) % m == 0 for d in divisors(N))
pl = [p for p in primerange(5, 3000) if p % 4 == 1]
rows = []
for C in range(1, 61):
    r = two_rank(4 * C)
    f = np.mean([fail(p, C) for p in pl[:150]])
    rows.append((C, r, float(f)))
by = {}
for C, r, f in rows:
    by.setdefault(r, []).append(f)
R['Z1835'] = {'mean_fail_by_2rank': {r: round(float(np.mean(v)), 4) for r, v in sorted(by.items())}, 'n_C': len(rows)}
# Z1022: ES solutions for p=1 mod 4 (p<1200): fraction with some denominator sharing a factor with 4C, C in {1,2,3,5,15}
R['Z1022'] = {}
for C in (1, 2, 3, 5, 15):
    tot = 0; shared = 0
    for p in [q for q in primerange(5, 1200) if q % 4 == 1]:
        for s in esols(p):
            tot += 1
            shared += any(math.gcd(v, 4 * C) > 1 for v in s)
    R['Z1022'][f'C={C}'] = {'solutions': tot, 'frac_some_denominator_shares_factor_with_4C': round(shared / tot, 4)}
# Z0536 control: fraction of random N = 4Cp+1-sized odd N=1 mod 4 that divide some Lucas term (same search)
def lucas_terms(P, Q, K):
    u0, u1 = 0, 1; out = [u0, u1]
    for _ in range(K):
        u0, u1 = u1, P * u1 - Q * u0; out.append(u1)
    return out
terms = [lucas_terms(P, Q, 60) for P in range(-3, 4) for Q in range(-3, 4) if Q != 0 and P * P - 4 * Q != 0]
def divides_some(N):
    return any(any(t % N == 0 for t in seq[1:]) for seq in terms)
rng = random.Random(1)
ctrl = []
for _ in range(400):
    N = rng.randrange(10**4, 6 * 10**5)
    N = N if N % 4 == 1 else N + (1 - N % 4) % 4
    ctrl.append(divides_some(N))
R['Z0536_control'] = {'random_N_1mod4_in_[1e4,6e5]': round(float(np.mean(ctrl)), 4), 'n': len(ctrl)}
json.dump(R, open('data/z52b/pass1/U02/compl_t.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:3000])
