# z52d pass2 NC1 fix round 6: Z1358 (which Dedekind three-term form holds), Z1382 (class-frequency classifier), Z1401 (LP over
# the witness library), Z1464 (adaptive prover simulation), Z1548 (ray-class existence by (c,d)), Z1584 (polynomial ansatz search),
# Z1322 (Farkas certificate for the x ≤ 3p/4 linearisation).
import math, json, itertools, random
import numpy as np
from fractions import Fraction as Fr
from collections import defaultdict, Counter
from sympy import primerange, divisors, jacobi_symbol
from scipy.optimize import linprog
out = {}
W0 = defaultdict(list)
for line in open('/tmp/wit_1e6.txt'):
    p, C, d = map(int, line.split()); W0[p].append((C, d))
W = dict(W0)
allp = [p for p in primerange(5, 10**6) if p % 4 == 1]
def ded(h, k):
    if k == 1: return Fr(0)
    s = Fr(0)
    for i in range(1, k):
        u = (h*i) % k
        if u == 0: continue
        s += (Fr(i, k)-Fr(1, 2))*(Fr(u, k)-Fr(1, 2))
    return s
# --- Z1358: test candidate forms of the three-term Dedekind identity over pairwise coprime triples (a,b,c ≤ 25)
trip = [(a, b, c) for a in range(2, 26) for b in range(2, 26) for c in range(2, 26)
        if math.gcd(a, b) == math.gcd(b, c) == math.gcd(a, c) == 1]
lhs = {t: ded(t[1]*t[2], t[0]) + ded(t[2]*t[0], t[1]) + ded(t[0]*t[1], t[2]) for t in trip}
cands = {
  'A: -1/4+(a2+b2+c2)/(12abc)': lambda a, b, c: Fr(-1, 4) + Fr(a*a+b*b+c*c, 12*a*b*c),
  'B: +(a2+b2+c2)/(12abc)-1/4 with abc-parity term (-1/8)*(1-(-1)^(a+b+c+...))': None,
}
res = {}
for name, fn in cands.items():
    if fn is None: continue
    ok = sum(1 for t in trip if lhs[t] == fn(*t))
    res[name] = {'holds_for': ok, 'of': len(trip)}
# residual pattern: lhs - (-1/4 + (a2+b2+c2)/(12abc)) as a function of parity of abc
par = defaultdict(Counter)
for t in trip:
    a, b, c = t
    r = lhs[t] - (Fr(-1, 4) + Fr(a*a+b*b+c*c, 12*a*b*c))
    par[(a % 2, b % 2, c % 2)][str(r)] += 1
res['residual_by_parity_pattern(first 2 values)'] = {str(k): dict(list(v.items())[:2]) for k, v in par.items()}
out['Z1358'] = res
# --- Z1382 classifier: target = witness with C ≤ 2; features = p mod 840 (class frequency with Laplace smoothing), trained on p<5e5
train = [p for p in allp if p < 5*10**5]; test = [p for p in allp if p >= 5*10**5]
y = lambda p: 1 if any(C <= 2 for C, d in W.get(p, [])) else 0
freq = defaultdict(lambda: [0, 0])
for p in train:
    f = freq[p % 840]; f[0] += 1; f[1] += y(p)
base = sum(y(p) for p in train)/len(train)
acc_model = acc_base = 0
for p in test:
    f = freq[p % 840]; q = (f[1]+1)/(f[0]+2)
    acc_model += int((q >= 0.5) == bool(y(p))); acc_base += int((base >= 0.5) == bool(y(p)))
out['Z1382'] = {'classifier': 'class-frequency (p mod 840), Laplace', 'test_accuracy_model': round(acc_model/len(test), 4),
                'test_accuracy_majority': round(acc_base/len(test), 4), 'test_primes': len(test)}
# --- Z1401 LP over the witness library: min sum x_w s.t. sum_{w ∋ p} x_w ≥ 1 (each prime covered by its own witnesses), x ≥ 0
p_sample = [p for p in allp[:300] if W.get(p)]
lp = {}
vals = []
for p in p_sample[:50]:
    ws = W[p]
    res_ = linprog(c=np.ones(len(ws)), A_ub=-np.ones((1, len(ws))), b_ub=[-1.0], bounds=[(0, None)]*len(ws), method='highs')
    vals.append(res_.fun)
out['Z1401'] = {'primes': len(vals), 'LP_value_min_mean_over_primes': round(float(np.mean(vals)), 4),
                'note': 'LP over witnesses of one prime (cover constraint sum x ≥ 1): optimum 1 for every prime; the relaxation carries no information'}
# --- Z1464 adaptive prover: strategies with query cost (number of C-tests) to find a witness
def queries_scan(p):
    cs = sorted(C for C, d in W.get(p, []))
    return cs[0] if cs else None
def queries_adaptive(p):
    # query C=1, then C = each prime factor q of 4p+1 (ascending) and of 4q·p+1? here: C in [1] + prime factors of 4p+1 ; cost = #queries
    from sympy import factorint
    cand = [1] + sorted(q for q in factorint(4*p+1) if q <= 50 and q > 1)
    wset = set(C for C, d in W.get(p, []))
    for i, C in enumerate(cand):
        if C in wset: return i+1
    return None
sc = []; ad = []; fails_a = 0; fails_s = 0
for p in [q for q in allp if q < 200000][:3000]:
    a = queries_adaptive(p); s = queries_scan(p)
    if a is None: fails_a += 1
    else: ad.append(a)
    if s is None: fails_s += 1
    else: sc.append(s)
out['Z1464'] = {'primes': 3000, 'adaptive(C=1 then prime factors of 4p+1 ≤50)': {'mean_queries_success': round(float(np.mean(ad)), 3), 'fail': fails_a},
                'scan(C=1,2,…)': {'mean_queries_success': round(float(np.mean(sc)), 3), 'fail': fails_s}}
# --- Z1548 ray-class existence: for d ∈ {2,3,5,6,7} (class number 1 fields), c ≤ 20, p ≤ 3000: fraction of (p,c) with a norm-divisor f ≡ -p (mod 4c)
ray = {}
Ps = [q for q in primerange(5, 3000) if q % 4 == 1][:200]
for dd in [2, 3, 5, 6, 7]:
    ex = Counter(); tot = Counter()
    for p in Ps:
        for c in range(1, 21):
            N = p*p+4*c*c*dd; mod = 4*c*dd
            ok = any(f % mod == (-p) % mod for f in divisors(N))
            tot[c] += 1; ex[c] += int(ok)
    ray[f'd={dd}'] = {'overall': round(sum(ex.values())/sum(tot.values()), 4),
                      'by_c(min,max)': (round(min(ex[c]/tot[c] for c in tot), 3), round(max(ex[c]/tot[c] for c in tot), 3))}
out['Z1548'] = ray
# --- Z1584 polynomial ansatz: x,y,z linear forms in (u,v,1) with integer coefficients in {-2..2}, n = Q(u,v);
#     test 4xyz = n(xy+yz+zx) at random integer points (u,v). Forms: u²+2v², u²+3v², u²-2v², u²+uv+v², u²+6v²
rng = np.random.default_rng(0)
pts = rng.integers(-30, 31, size=(6, 2))
forms = {'u2+2v2': lambda u, v: u*u+2*v*v, 'u2+3v2': lambda u, v: u*u+3*v*v, 'u2-2v2': lambda u, v: u*u-2*v*v,
         'u2+uv+v2': lambda u, v: u*u+u*v+v*v, 'u2+6v2': lambda u, v: u*u+6*v*v}
coef = np.array(list(itertools.product(range(-2, 3), repeat=3)))  # 125 linear forms a*u+b*v+c
found = {}
for name, Q in forms.items():
    hits = 0
    X = coef[:, 0][:, None]*pts[:, 0][None, :] + coef[:, 1][:, None]*pts[:, 1][None, :] + coef[:, 2][:, None]
    # candidate triples over linear forms: 125^3 ~ 2e6, check vectorised per x-form
    nvals = np.array([Q(int(u), int(v)) for u, v in pts])
    cnt = 0
    for ix in range(len(coef)):
        x = X[ix]
        if np.any(x == 0): continue
        for iy in range(len(coef)):
            yv = X[iy]
            if np.any(yv == 0): continue
            xy = x*yv
            # z must satisfy 4xyz = n(xy + z(x+y)) -> z (4xy - n(x+y)) = n xy
            den = 4*xy - nvals*(x+yv)
            num = nvals*xy
            ok_den = den != 0
            with np.errstate(divide='ignore', invalid='ignore'):
                zv = np.where(ok_den, num/np.where(ok_den, den, 1), np.nan)
            # z must be the same linear form at every point: compare with X
            Z = X
            good = np.all(np.isclose(Z, zv[None, :], atol=1e-9), axis=1) if False else None
            # direct: check each z-form
            m = np.all(np.isclose(X*den[None, :] if False else (X*den[None, :]), num[None, :], atol=1e-6), axis=1)
            cnt += int(np.sum(m & np.all(ok_den)))
    found[name] = cnt
out['Z1584_ansatz'] = {'linear_forms_per_variable': len(coef), 'points': 6, 'identities_found(x,y,z linear in u,v)': found,
                      'note': 'x,y,z linear forms with coefficients in {-2..2}; identity checked at 6 integer points'}
# --- Z1322 Farkas: candidates x ∈ [⌈p/4⌉, ⌊3p/4⌋] (all three denominators in this range), weights w ∈ [0,∞), Σw = 3, Σ w/x = 4/p
p = 409
xs = list(range(-(-p//4), (3*p)//4+1))
# dual certificate: α=1, β=-1/x_max:  α/x + β ≥ 0 for all x ∈ S, and 4α/p + 3β < 0
xmax = max(xs)
alpha, beta = 1.0, -1.0/xmax
ok_dual = all(alpha/x + beta >= -1e-15 for x in xs)
val = 4*alpha/p + 3*beta
lp = linprog(c=np.zeros(len(xs)), A_eq=np.array([[1.0/x for x in xs], [1.0]*len(xs)]), b_eq=[4.0/p, 3.0], bounds=[(0, None)]*len(xs), method='highs')
out['Z1322_farkas'] = {'p': p, 'candidate_range': [xs[0], xs[-1]], 'dual_multiplier(alpha,beta)': [alpha, beta],
                       'dual_feasible(alpha/x+beta>=0 for all x)': bool(ok_dual), 'b.y = 4/p - 3/x_max': round(val, 8),
                       'LP_status_with_w>=0_unbounded_upper': int(lp.status),
                       'interpretation': 'Farkas: no nonnegative weights; every ES triple has max denominator ≥ 3p/4'}
print(json.dumps(out, indent=1, default=str))
