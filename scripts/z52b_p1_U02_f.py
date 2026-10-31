"""U02 fix pass part 2: verify the C<=200 slice-failure set, Z1054 sign rule, Z0636 (strict gap), Z0356 (p*D too),
Z0329 (Gaussian numerators), Z0701 (L-regression), Z0968 (h(-2p), h(-8p) vs Tunnell-type counts omitted: see note)."""
import sys, json, math
import numpy as np
from fractions import Fraction as Fr
from collections import Counter
from sympy import primerange, divisors, jacobi_symbol, factorint
from scipy.special import digamma
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
R = {}
def has_slice(p, C):
    m = 4 * C; N = 4 * C * p + 1
    return any(1 < d < N and (d - (m - 1)) % m == 0 for d in divisors(N))
pp = [p for p in primerange(5, 10001) if p % 4 == 1]
fails200 = [p for p in pp if not any(has_slice(p, C) for C in range(1, 201))]
R['Z1568_slice_fail_C<=200_p<=1e4'] = fails200
# check the exceptions list is exactly this set in range
R['Z1568_matches_given_list'] = (fails200 == [409, 577, 5569, 9601])
# how many primes = 1 mod 4 up to 1e5 (sieve-based fast check using C<=60 for speed)
pp2 = [p for p in primerange(10001, 60001) if p % 4 == 1]
f2 = [p for p in pp2 if not any(has_slice(p, C) for C in range(1, 61))]
R['slice_fail_C<=60_p_in_(1e4,6e4]'] = f2[:20]
R['n_checked_(1e4,6e4]'] = len(pp2)
# Z1054: sign rule. one denominator divisible by p vs two
cnt = Counter(); tot = 0; prod = Counter()
for p in primerange(5, 5000):
    if p % 4 != 1: continue
    for s in esols(p):
        r = [v % p == 0 for v in s]
        k = sum(r)
        if k == 1:
            i = r.index(True)
            o = [s[j] for j in range(3) if j != i]
            sy = tuple(jacobi_symbol(v % p, p) for v in o)
            cnt[sy] += 1
            prod[jacobi_symbol((o[0] * o[1]) % p, p)] += 1
        tot += 1
R['Z1054_one_den_div_p'] = {str(k): v for k, v in cnt.items()}
R['Z1054_legendre_of_yz_when_one_den_div_p'] = {str(k): v for k, v in prod.items()}
R['Z1054_solutions'] = tot
# Z0636: strict positive gap 4/p - S, S = sum of three unit fractions with x<=y<=z<=M
M = 120
T = np.array([(x, y, z) for x in range(1, M + 1) for y in range(x, M + 1) for z in range(y, M + 1)], dtype=float)
S = np.sort(1 / T[:, 0] + 1 / T[:, 1] + 1 / T[:, 2])
gaps = []
for p in primerange(5, 200):
    t = 4 / p
    k = np.searchsorted(S, t - 1e-12, side='left')  # strictly below t
    if k - 1 >= 0 and S[k - 1] < t - 1e-12:
        gaps.append((p, float((t - S[k - 1]) * p)))
R['Z0636'] = {'M': M, 'n': len(gaps), 'min_gap_times_p': min(gaps, key=lambda x: x[1]),
              'median_gap_times_p': float(np.median([g for _, g in gaps]))}
# Z0356: denominators a*2^k (a<=15, k<=12) and p times them
def three_in_set(p, Dsorted):
    Ds = set(Dsorted)
    for i, x in enumerate(Dsorted):
        if 4 * x <= p: continue
        for y in Dsorted[i:]:
            num = 4 * x * y - p * (x + y)
            if num <= 0: continue
            z = p * x * y
            if z % num == 0 and (z // num) in Ds and z // num >= y: return True
    return False
base = sorted(set(a * 2 ** k for a in range(1, 16) for k in range(0, 13)))
ok = 0; tested = 0
for p in [q for q in primerange(5, 1000)]:
    D = sorted(set(base) | {p * d for d in base})
    tested += 1; ok += three_in_set(p, D)
R['Z0356'] = {'primes': tested, 'with_solution_with_p_multiples': ok}
# Z0329: (1+i)^k / pi for Gaussian primes pi, norm <= 60; search 4/... replaced by target t = (1+i)^k/pi and
# t = sum of three Z[i] unit fractions, norms <= 25. Exact Gaussian rational arithmetic.
def gmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def gdiv(a, b):
    n = b[0]**2 + b[1]**2
    z = gmul(a, (b[0], -b[1]))
    return (Fr(z[0], n), Fr(z[1], n))
def ginv(a):
    return gdiv((1, 0), a)
els = [(a, b) for a in range(-6, 7) for b in range(-6, 7) if 0 < a*a + b*b <= 25]
inv_els = [ginv(e) for e in els]
gp = [(a, b) for a in range(-8, 9) for b in range(0, 9)
      if (a*a + b*b) in {2, 5, 9, 13, 17, 29, 37, 41, 49, 53, 61} or (a*a+b*b == 2)]
gp = [g for g in gp if g != (0, 0) and all(gmul(g, (1, 0)) for _ in [0])]
res_z329 = {}
for k in (1, 2, 3):
    tot = 0; succ = 0; primes_tested = 0
    for pi in gp:
        if pi[0]*pi[0]+pi[1]*pi[1] < 2: continue
        # keep one representative per associate class and skip non-prime norms
        N = pi[0]**2 + pi[1]**2
        if N not in (2, 5, 13, 17, 29, 37, 41, 53, 61): continue
        if pi[1] < 0 or (pi[1] == 0 and pi[0] < 0): continue
        num = (1, 0)
        for _ in range(k): num = gmul(num, (1, 1))
        t = gdiv(num, pi)
        primes_tested += 1
        found = False
        for i1 in range(len(els)):
            for i2 in range(i1, len(els)):
                w = (t[0] - inv_els[i1][0] - inv_els[i2][0], t[1] - inv_els[i1][1] - inv_els[i2][1])
                if w == (0, 0): continue
                iw = ginv((w[0], w[1])) if False else None
                nw = w[0]**2 + w[1]**2
                if nw == 0: continue
                iw = (Fr(w[0], nw), Fr(-w[1], nw))
                if iw[0].denominator == 1 and iw[1].denominator == 1 and (iw[0] != 0 or iw[1] != 0):
                    found = True; break
            if found: break
        succ += found
    res_z329[k] = {'gaussian_primes_tested': primes_tested, 'with_three_term_repr_norm<=25': succ}
R['Z0329'] = res_z329
json.dump(R, open('data/z52b/pass1/U02/fix_f.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:4000])
