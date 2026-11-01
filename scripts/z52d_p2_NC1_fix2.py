# z52d pass2 NC1 fix round 2. Items: Z1223 (bias-corrected entropies), Z1479 (witness d^{(p-1)/k} classes),
# Z1707 (more candidate C rules vs matched base rate), Z1832/Z1833 (candidate certificate rules from sums of squares),
# Z1689 (periodicity of a box-count), Z1889 (blind prediction of witness status on held-out primes),
# Z1908 (projected area of the ES surface), Z1922 (fibration of y=z surface over n), Z1936 (Koszul Euler characteristic),
# Z1485 (Hurwitz-type reduced-form counts along p²+4c²), Z1438 (Type I counts for d=1), Z1409 (energy landscape, p=13..37).
import numpy as np, math, json, random
from collections import defaultdict, Counter
from sympy import primerange, legendre_symbol, symbols, Matrix, factor, solve, discriminant, simplify, jacobi_symbol
out = {}
W0 = defaultdict(list)
for line in open('/tmp/wit_1e6.txt'):
    p, C, d = map(int, line.split()); W0[p].append((C, d))
W = dict(W0)
allp = [p for p in primerange(5, 10**6) if p % 4 == 1]
random.seed(0)
def H(xs):
    c = Counter(xs); n = len(xs); return -sum(v/n*math.log2(v/n) for v in c.values())
def Hcond(xs, ys):
    n = len(xs); cy = defaultdict(list)
    for x, y in zip(xs, ys): cy[y].append(x)
    return sum(len(v)/n*H(v) for v in cy.values())
CMIN = [min(C for C, d in W[p]) if W.get(p) else 0 for p in allp]
cls = [p % 840 for p in allp]
leg = [tuple(legendre_symbol(p, q) if p % q else 0 for q in [11, 13, 17, 19, 23, 29, 31]) for p in allp]
def bias_corr(x, y):
    shuf = list(x); random.shuffle(shuf)
    return Hcond(x, y) - Hcond(shuf, y)   # conditional entropy minus its shuffled-label baseline
out['Z1223_bias_corrected'] = {'H(family|p mod 840) - shuffled baseline': round(bias_corr(CMIN, cls), 4),
    'H(family|p mod 840, legendre 11..31) - shuffled baseline': round(bias_corr(CMIN, list(zip(cls, leg))), 4),
    'H(family)': round(H(CMIN), 4), 'cells_mod840_x_legendre': len(set(zip(cls, leg)))}
# --- Z1479: k-th power classes of witness d mod p: d^{(p-1)/k} as a root of unity; distribution over the k classes
rt = {}
for k in [4, 8]:
    cnt = Counter()
    for p in allp:
        if not W.get(p): continue
        for C, d in W[p][:1]:
            e = (p-1)//math.gcd(k, p-1)
            cnt[pow(d % p, e, p)] += 1
    rt[k] = {'distinct_values_of_d^((p-1)/gcd(k,p-1))': len(cnt), 'values_with_counts(top)': cnt.most_common(4)}
out['Z1479'] = {'note': 'k=2 gives only the non-residue value for every witness (Lemma B, jacobi_a_of_cform); k=4,8 classes below',
                'first_witness_root_of_unity_classes': rt}
# --- Z1707: candidate rules for representations p = x^2 - D y^2 vs matched base rate (base rate = P(witness at C) over all primes)
def witness(p, C):
    N = 4*C*p+1; m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
P4 = [p for p in allp if p < 200000]
rate_cache = {}
def base(C):
    if C not in rate_cache: rate_cache[C] = sum(witness(p, C) for p in P4[:6000])/6000
    return rate_cache[C]
z17 = {}
for D in [5, 8, 12, 13]:
    rows = defaultdict(lambda: [0, 0, 0.0])
    for p in P4[:6000]:
        rep = None
        for y in range(1, 200):
            x2 = p+D*y*y; x = math.isqrt(x2)
            if x*x == x2: rep = (x, y); break
        if rep is None: continue
        x, y = rep
        for name, Cc in [('C=y', y), ('C=x-y', x-y), ('C=x+y', x+y)]:
            if Cc < 1: continue
            rows[name][0] += 1; rows[name][1] += int(witness(p, Cc)); rows[name][2] += base(Cc)
    z17[f'D={D}'] = {k: {'n': v[0], 'witness_rate': round(v[1]/v[0], 3), 'matched_base_rate': round(v[2]/v[0], 3)} for k, v in rows.items() if v[0] > 0}
out['Z1707_candidates'] = z17
# --- Z1832/Z1833: candidate certificate rules from representations of p as sums of 3 or 4 squares
def reps(n, k):
    r = math.isqrt(n); res = []
    if k == 3:
        for a in range(0, r+1):
            for b in range(a, r+1):
                c2 = n-a*a-b*b
                if c2 < b*b: break
                c = math.isqrt(c2)
                if c*c == c2 and c >= b: res.append((a, b, c))
    else:
        for a in range(0, r+1):
            for b in range(a, r+1):
                for c in range(b, r+1):
                    d2 = n-a*a-b*b-c*c
                    if d2 < c*c: break
                    d = math.isqrt(d2)
                    if d*d == d2 and d >= c: res.append((a, b, c, d))
    return res
def cform_ok(p, C):
    return C >= 1 and witness(p, C)
res3 = {}; res4 = {}
P3 = [p for p in primerange(5, 2000) if p % 4 == 1]
cov3 = 0; cov4 = 0; tot = 0
for p in P3:
    tot += 1
    ok = False
    for rep in reps(p, 3):
        for C in set(x for x in rep if x >= 1):
            if cform_ok(p, C): ok = True; break
        if ok: break
    cov3 += ok
    ok4 = False
    for rep in reps(p, 4):
        for C in set(x for x in rep if x >= 1):
            if cform_ok(p, C): ok4 = True; break
        if ok4: break
    cov4 += ok4
out['Z1832_1833_rule_C_in_representation'] = {'primes_p<2000_p≡1(4)': tot,
    'covered_by_some_3-square rep with C=entry': cov3, 'covered_by_some_4-square rep with C=entry': cov4}
# --- Z1689: periodicity of Φ(p) = #{(u,B): u≤U, B≤V, 4uB | p+u+B} (Type-II-type divisibility), U=V=30
U = V = 30
def Phi(p):
    return sum(1 for u in range(1, U+1) for B in range(1, V+1) if (p+u+B) % (4*u*B) == 0)
vals = [Phi(p) for p in range(1, 20001)]
per = None
for T in range(1, 20001):
    if all(vals[i] == vals[i+T] for i in range(0, len(vals)-T)):
        per = T; break
out['Z1689'] = {'window_p<=20000': len(vals), 'U=V=30': True, 'smallest_period_in_window': per,
                'distinct_values': len(set(vals)), 'max_value': max(vals)}
# --- Z1889 blind prediction: train on witness status (C≤2) for p<5e5 via residue-class frequencies (mod 840·24?), test on p≥5e5
train = [p for p in allp if p < 5*10**5]; test = [p for p in allp if p >= 5*10**5]
def y2(p): return 1 if any(C <= 2 for C, d in W.get(p, [])) else 0
freq = defaultdict(lambda: [0, 0])
for p in train:
    f = freq[p % 840]; f[0] += 1; f[1] += y2(p)
g = sum(y2(p) for p in train)/len(train)
brier_model = brier_base = 0.0
for p in test:
    f = freq[p % 840]; q = (f[1]+1)/(f[0]+2) if f[0] > 0 else g
    y = y2(p); brier_model += (q-y)**2; brier_base += (g-y)**2
out['Z1889_blind'] = {'train_primes': len(train), 'test_primes': len(test), 'base_rate_C<=2': round(g, 4),
                      'brier_model(p mod 840)': round(brier_model/len(test), 5), 'brier_base': round(brier_base/len(test), 5)}
# --- Z1908 projected area: A(p) = ∫∫ over (log x, log y) in [log(p/4), 2 log p]^2 of 1[z=1/(4/p-1/x-1/y) in [p/4,p^2], z>0] dlogx dlogy, / log^2 p
def A(p, M=600):
    lo, hi = math.log(p/4), 2*math.log(p)
    g = np.linspace(lo, hi, M); X = np.exp(g)[:, None]; Y = np.exp(g)[None, :]
    den = 4.0/p - 1.0/X - 1.0/Y
    with np.errstate(divide='ignore', invalid='ignore'):
        Z = np.where(den > 0, 1.0/den, np.nan)
    ok = (den > 0) & (Z >= p/4) & (Z <= p*p) & (Y >= X) & (Z >= Y)
    dA = (hi-lo)/(M-1)
    return float(ok.sum()*dA*dA)
areas = {p: A(p) for p in [101, 1009, 10007, 100003]}
out['Z1908_projected_area_over_log2p'] = {p: round(a/math.log(p)**2, 4) for p, a in areas.items()}
# --- Z1922: fibration of the y=z slice 4/n = 1/x + 2/y: solve for n; fibre over n in x,y; singular fibres
xs_, ys_, ns = symbols("x y n")
Eq = 4*ys_*xs_ - ns*(ys_+2*xs_)  # clear denominators of 4/n = (y+2x)/(xy)
disc = factor(discriminant(Eq, ys_)) if Eq.has(ys_) else None
sol_n = solve(Eq, ns)
out['Z1922'] = {'surface': 'y=z: 4/n = 1/x + 2/y  <=>  4xy - n(y+2x) = 0', 'n_as_function': str(sol_n),
                'fibre_over_n_is_conic_in_(x,y)': True, 'degenerate_fibres': 'n=0 (x or y=0), n=infinity'}
# --- Z1936 Koszul Euler characteristic of f = 4Cuv - u - v - p on R = F_q[u,v]/(u^{K+1}, v^{K+1}) (truncation, C fixed=1, p=13)
def koszul_chi(p, K=8, Cc=1, q=2147483629):
    # basis: monomials u^i v^j, i,j<=K; multiplication by f (mod truncation) as matrix
    idx = {(i, j): k for k, (i, j) in enumerate([(i, j) for i in range(K+1) for j in range(K+1)])}
    n = len(idx); M = np.zeros((n, n), dtype=object)
    for (i, j), k in idx.items():
        for (a, b, c) in [(i+1, j+1, 4*Cc), (i+1, j, -1), (i, j+1, -1), (i, j, -p)]:
            if a <= K and b <= K: M[idx[(a, b)], k] += c
    # rank over Q via sympy
    rk = Matrix(M.tolist()).rank()
    return {'dim': n, 'rank': rk, 'dim_ker': n-rk, 'dim_coker': n-rk, 'chi = dim ker - dim coker': 0}
out['Z1936'] = {'p=13,K=8': koszul_chi(13, 8), 'p=101,K=6': koszul_chi(101, 6)}
# --- Z1485 reduced-form counts T(N) for disc -4N, N = p^2+4c^2, c ≤ 60, p = 1009 and 10007 (all forms, incl. imprimitive)
def T_forms(N):
    D = -4*N; cnt = 0; a = 1
    while 3*a*a <= -D:
        for b in range(-a+1, a+1):
            if (b*b - D) % (4*a) == 0:
                c = (b*b - D)//(4*a)
                if c >= a and not (c == a and b < 0): cnt += 1
        a += 1
    return cnt
hur = {}
for p in [1009, 10007]:
    S = 0; Sn = 0.0; Ts = []
    for c in range(1, 61):
        N = p*p+4*c*c; t = T_forms(N); Ts.append(t); S += t; Sn += math.sqrt(N)
    hur[p] = {'sum_T': S, 'mean_T/sqrt(N)': round(S/Sn, 5), 'max_T': max(Ts)}
out['Z1485'] = hur
# --- Z1438 Type I (d=1) counts: divisors f of p^2+4c^2 with f ≡ -p (mod 4c); fraction of primes with ≥1 solution for c≤20
def divisors_of(n):
    from sympy import divisors
    return divisors(n)
frac = []
for p in [q for q in P4[:300]]:
    ok = False
    for c in range(1, 21):
        N = p*p+4*c*c
        if any(f % (4*c) == (-p) % (4*c) for f in divisors_of(N)):
            ok = True; break
    frac.append(ok)
out['Z1438_d1'] = {'primes_tested': len(frac), 'fraction_with_type_I_d1_solution_c<=20': round(sum(frac)/len(frac), 3)}
# --- Z1409 energy landscape: E(x,y,z) = (4xyz - p(xy+yz+zx))^2 over 1..B^3; zero set = solutions; gap to next level
land = {}
for p in [13, 17, 29, 37]:
    B = 64
    r = np.arange(1, B+1)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    E = (4*X*Y*Z - p*(X*Y+Y*Z+Z*X))**2
    vals_ = np.unique(E)
    zeros = int((E == 0).sum())
    nz = vals_[vals_ > 0]
    land[p] = {'B': B, 'states': int(E.size), 'zero_energy_states(solutions with x,y,z<=64)': zeros,
               'gap_first_nonzero_energy': int(nz[0]) if len(nz) else None, 'distinct_levels': int(len(vals_))}
out['Z1409'] = {'energy': '(4xyz - p(xy+yz+zx))^2 on {1..64}^3 (bit-blast-equivalent objective; NOT the QUBO matrix)', 'results': land}
print(json.dumps(out, indent=1, default=str))
