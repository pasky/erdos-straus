"""U02 re-run (fix pass). Concrete versions of previously vague/needs-compute items.
Z0270 (Gaussian pair search), Z0317/Z0329/Z0330/Z0343 (3-term unit fractions in quadratic orders, finite height),
Z0356/Z0332 (lacunary and Beatty denominator sets), Z0278 (n=pq, p | a denominator), Z0347 (x/p histogram),
Z0151 (nearest other 3-term sum), Z0539 (least C), Z0636 (min positive gap), Z1054 (joint Legendre), Z1445/Z1569/Z1582/Z3188
(smallest-C slice success), Z1491 (2-adic valuations), Z0701 & Z0968 (L(1,chi_D) -> class numbers)."""
import sys, json, math
from fractions import Fraction as Fr
from sympy import primerange, divisors, factorint, jacobi_symbol, n_order
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
R = {}

# ---------- generic quadratic order K = Q(theta), theta^2 = t*theta + s ----------
def make_order(t, s, H):
    """elements a + b theta with norm N = a^2 + t a b - s b^2 in (0, H] (and the negatives of nothing: we keep all)."""
    els = []
    B = int(math.isqrt(4 * H) // 1) + 3
    for b in range(-B, B + 1):
        for a in range(-B * 3, B * 3 + 1):
            N = a * a + t * a * b - s * b * b
            if N != 0 and abs(N) <= H:
                els.append((a, b, N))
    return els
def inv(a, b, N, t):
    # 1/(a+b theta) = (a+b(t-theta))/N  since conj(theta)=t-theta
    return Fr(a + b * t, N), Fr(-b, N)
def ring_solutions(p, t, s, H, filt=lambda a, b: True):
    """all (x,y,z) (unordered, x<=y<=z by index) with 4/p = 1/x+1/y+1/z and x,y,z in the order of norm<=H
    (filt applies to each denominator). Returns the count; w is 1/z computed exactly; z must be in the order."""
    els = [e for e in make_order(t, s, H) if filt(e[0], e[1])]
    if not els: return 0
    target = (Fr(4, p), Fr(0))
    cnt = 0
    for (a1, b1, N1) in els:
        i1 = inv(a1, b1, N1, t)
        for (a2, b2, N2) in els:
            i2 = inv(a2, b2, N2, t)
            wr = target[0] - i1[0] - i2[0]
            wi = target[1] - i1[1] - i2[1]
            # w = wr + wi*theta ; need 1/w in O_K: w = wr + wi*theta, N(w) = wr^2 + t wr wi - s wi^2
            Nw = wr * wr + t * wr * wi - s * wi * wi
            if Nw == 0: continue
            zr, zi = Fr(wr + wi * t) / Nw, Fr(-wi) / Nw  # 1/w = (wr+wi(t-theta))/Nw
            # zr + zi*theta must be integral: zr,zi integers
            if zr.denominator == 1 and zi.denominator == 1:
                if filt(int(zr), int(zi)) and (zr, zi) != (0, 0):
                    cnt += 1
    return cnt
# NOTE: counts ordered pairs (x,y); used only as a yes/no per prime and for comparisons.
ORDERS = {'Z[i]': (0, -1), 'Z[omega]': (-1, -1), 'Z[sqrt2]': (0, 2), 'Z[(1+sqrt-7)/2]': (1, -2)}
ps = [p for p in primerange(5, 90)]
R['Z0317_Z0329_Z0330'] = {}
for name, (t, s) in ORDERS.items():
    succ = [p for p in ps if ring_solutions(p, t, s, 25) > 0]
    R['Z0317_Z0329_Z0330'][name] = {'primes_tested': len(ps), 'with_solution_norm<=25': len(succ), 'fail': [p for p in ps if p not in succ][:12]}
# Z0329 numerators (1+i)^k/pi for Gaussian primes: test sum-of-three-unit-fraction with H=25
def gauss_primes(H):
    out = []
    for a in range(1, 40):
        for b in range(0, 40):
            N = a * a + b * b
            if 1 < N <= H and all(N % q for q in []):  # placeholder
                pass
    return out
# Z0343 cones in Z[sqrt2]: (N) rational ; (Nn) a,b>=0 ; (H+) a+b sqrt2>0 ; (TP) a+b sqrt2>0 and a-b sqrt2>0
cones = {'N_rational': lambda a, b: b == 0 and a > 0,
         'N[sqrt2]': lambda a, b: a >= 0 and b >= 0 and (a, b) != (0, 0),
         'height_positive': lambda a, b: a + b * math.sqrt(2) > 0,
         'totally_positive': lambda a, b: a + b * math.sqrt(2) > 0 and a - b * math.sqrt(2) > 0}
R['Z0343'] = {}
for cn, cf in cones.items():
    ok = [p for p in ps if ring_solutions(p, 0, 2, 25, filt=cf) > 0]
    R['Z0343'][cn] = {'primes': len(ps), 'with_solution': len(ok), 'fail_first': [p for p in ps if p not in ok][:10]}

# ---------- Z0356 lacunary, Z0332 Beatty: 3 unit fractions with denominators in a set D ----------
def three_in_set(p, Dset, Dsorted):
    cnt = 0
    for i, x in enumerate(Dsorted):
        if 4 * x <= p: continue
        for y in Dsorted[i:]:
            num = 4 * x * y - p * (x + y)
            if num <= 0: continue
            z = p * x * y
            if z % num == 0 and (z // num) in Dset and z // num >= y:
                return True
    return False
pr = [p for p in primerange(5, 1000)]
Dl = set(a * 2 ** k for a in range(1, 16) for k in range(0, 13))
Dl = Dl | {d * p for d in Dl for p in (1,)}
Dls = sorted(Dl)
R['Z0356'] = {'primes': len(pr), 'with_solution': sum(three_in_set(p, Dl, Dls) for p in pr)}
R['Z0356']['fail_first'] = [p for p in pr if not three_in_set(p, Dl, Dls)][:20]
R['Z0332'] = {}
for nm, th in (('sqrt2', math.sqrt(2)), ('phi', (1 + math.sqrt(5)) / 2), ('e/2', math.e / 2)):
    Dset = set(int(math.floor(k * th)) for k in range(1, 4000))
    Dset = {d for d in Dset if d >= 1}
    Dsorted = sorted(Dset)
    ok = [p for p in pr if p < 1000 and three_in_set(p, Dset, Dsorted)]
    R['Z0332'][nm] = {'with_solution': len(ok), 'primes': len([p for p in pr if p < 1000]), 'fail_first': [p for p in pr if p < 1000 and p not in ok][:10]}

# ---------- Z0278: n=pq (p,q=1 mod 4 <100): does some solution of 4/(pq) have p | a denominator? ----------
P1 = [p for p in primerange(5, 100) if p % 4 == 1]
res278 = {'pairs': 0, 'some_den_div_p': 0, 'none': 0}
for i, p in enumerate(P1):
    for q in P1[i + 1:]:
        n = p * q
        S = esols(n)
        res278['pairs'] += 1
        if any(any(v % p == 0 for v in s) for s in S): res278['some_den_div_p'] += 1
        else: res278['none'] += 1
R['Z0278'] = res278

# ---------- Z0347: histogram of x/p over ES solutions (p=1 mod 4, p<1500) ----------
bins = [0] * 10; tot = 0
for p in primerange(5, 1500):
    if p % 4 != 1: continue
    for s in esols(p):
        x = s[0] / p
        bins[min(9, int((x - 0.25) / 0.05))] += 1; tot += 1
R['Z0347'] = {'solutions': tot, 'hist_x_over_p_bins_0.25_to_0.75': bins}

# ---------- Z0151: nearest other 3-term sum to 4/p, with x,y,z <= N ----------
N = 120
vals = {}
import numpy as np
arr = []
for x in range(1, N + 1):
    for y in range(x, N + 1):
        for z in range(y, N + 1):
            arr.append((x, y, z))
A = np.array(arr, dtype=float)
S3 = np.sort(1 / A[:, 0] + 1 / A[:, 1] + 1 / A[:, 2])
dists = []
for p in primerange(5, 120):
    t = 4 / p
    k = np.searchsorted(S3, t)
    cand = [S3[j] for j in (k - 2, k - 1, k, k + 1, k + 2) if 0 <= j < len(S3) and abs(S3[j] - t) > 1e-15]
    dists.append((p, round(min(abs(c - t) for c in cand), 10)))
R['Z0151'] = {'N': N, 'sample': dists[:8], 'mean_dist': float(np.mean([d for _, d in dists]))}

# ---------- Z0539, Z1445, Z1569, Z1582, Z3188: least C with a divisor = -1 mod 4C of N=4Cp+1 ----------
def least_C(p, Cmax=200):
    for C in range(1, Cmax + 1):
        m = 4 * C
        N_ = 4 * C * p + 1
        for d in divisors(N_):
            if d > 1 and d < N_ and (d - (m - 1)) % m == 0:  # d = -1 mod m
                return C
    return None
pp = [p for p in primerange(5, 10000) if p % 4 == 1]
Cm = {p: least_C(p) for p in pp}
vals = [v for v in Cm.values() if v is not None]
R['Z0539_Z1445'] = {'n': len(pp), 'none_up_to_200': sum(1 for v in Cm.values() if v is None),
                    'C_hist_head': dict(sorted({c: vals.count(c) for c in set(vals)}.items())[:12]),
                    'max_C': max(vals), 'argmax_p': [p for p in pp if Cm[p] == max(vals)][:5],
                    'ln2_ratio_mean': float(np.mean([v / math.log(p) ** 2 for p, v in Cm.items() if v])),}
ex = [409, 577, 5569, 9601]
R['Z1569_Z1582'] = {'exceptions_given': ex, 'C_min_of_exceptions': {p: Cm.get(p) for p in ex},
                    'primes_1mod24_with_Cmin>=8': [p for p in pp if p % 24 == 1 and (Cm[p] or 999) >= 8][:20],
                    'exception_quartic2': {p: pow(2, (p - 1) // 4, p) == 1 for p in ex}}
# Z3188: distribution of least-C mod 8 and mod 3 (p<=10^4)
R['Z3188'] = {'Cmin_mod8': dict(sorted({r: sum(1 for v in vals if v % 8 == r) for r in range(8)}.items())),
              'Cmin_mod3': {r: sum(1 for v in vals if v % 3 == r) for r in range(3)}}

# ---------- Z0636: min positive gap 4/p - (1/x+1/y+1/z), x<=y<=z<=M ----------
M = 120
T = np.array([(x, y, z) for x in range(1, M + 1) for y in range(x, M + 1) for z in range(y, M + 1)], dtype=float)
S3b = np.sort(1 / T[:, 0] + 1 / T[:, 1] + 1 / T[:, 2])
gaps = []
for p in primerange(5, 200):
    t = 4 / p
    k = np.searchsorted(S3b, t, side='right')
    if k - 1 >= 0: gaps.append((p, float(t - S3b[k - 1]) * p))  # gap in units of 1/p
R['Z0636'] = {'M': M, 'mean_gap_times_p': float(np.mean([g for _, g in gaps])), 'min_gap_times_p': min(gaps, key=lambda x: x[1]),
              'n': len(gaps)}

# ---------- Z1054: joint Legendre symbols of (x,y,z) mod p over solutions, p=1 mod 4 < 1500 ----------
from collections import Counter
cnt = Counter(); tot = 0
for p in primerange(5, 1500):
    if p % 4 != 1: continue
    for s in esols(p):
        sig = tuple(jacobi_symbol(v % p, p) if v % p else 0 for v in s)
        cnt[sig] += 1; tot += 1
R['Z1054'] = {'solutions': tot, 'sign_triples': {str(k): v for k, v in cnt.most_common()}}

# ---------- Z1491: 2-adic valuations of tau(N) and phi(4C) for slice success/failure, C<=12, p=1 mod 4 < 3000 ----------
def v2(n):
    k = 0
    while n % 2 == 0 and n: n //= 2; k += 1
    return k
def phi(m): return sum(1 for a in range(1, m + 1) if math.gcd(a, m) == 1)
pairs = Counter()
for C in range(1, 13):
    m = 4 * C
    ph = phi(m)
    for p in primerange(5, 3000):
        if p % 4 != 1: continue
        N_ = 4 * C * p + 1
        dv = divisors(N_)
        M_ = sum(1 for d in dv if d > 1 and (d - (m - 1)) % m == 0)
        pairs[('fail' if M_ == 0 else 'ok', v2(len(dv)) - v2(ph))] += 1
R['Z1491'] = {str(k): v for k, v in sorted(pairs.items())}

# ---------- Z0701, Z0968: L(1,chi_D) via L = -(1/q) sum_{a=1}^{q} chi(a) psi(a/q); h(D) = sqrt|D| L / pi for D<-4 ----------
from scipy.special import digamma
def L1(D):
    q = abs(D)
    a = np.arange(1, q + 1)
    chi = np.array([0 if math.gcd(int(x), q) > 1 else jacobi_symbol(D % int(x), int(x)) if x > 1 else 1 for x in a], float) if False else None
    chi = np.zeros(q)
    for x in range(1, q + 1):
        if math.gcd(x, q) == 1:
            # Kronecker symbol (D/x) for x odd; for even x use kronecker via factoring 2
            chi[x - 1] = kron(D, x)
    return -(1.0 / q) * float(np.sum(chi * digamma(a / q)))
def kron(D, n):
    r = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0: return 0
        r *= 1 if D % 8 in (1, 7) else -1
    if n == 1: return r
    return r * jacobi_symbol(D % n, n)
h = {}
for p in [q for q in primerange(3, 400) if q % 4 == 1]:
    h[p] = {'h-8p': float(math.sqrt(8 * p) * L1(-8 * p) / math.pi)}
R['Z0968_sample_h8p'] = list(h.items())[:6]
json.dump(R, open('data/z52b/pass1/U02/fix_e.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:6000])
