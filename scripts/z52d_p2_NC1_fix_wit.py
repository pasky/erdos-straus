# z52d pass2 NC1 fix round: witness-based computations (input /tmp/wit_1e6.txt from scripts/z52d_p2_NC1_wit.c, X=1e6, CMAX=50).
# Items: Z1223 family isolation (entropies), Z1228 learned next-C policy, Z1277 C-form degree profiles, Z1281 resultant
# check, Z1287 gcd strata, Z1320 concentration (degree of vanishing polynomial), Z1479 k-th power tower, Z1510 parity proxy,
# Z1359 invariant mutual information, Z1584 T1 at odd squares in the C-form, Z1621 generating-function coefficients.
import numpy as np, math, json, sys
from collections import defaultdict, Counter
from sympy import primerange, legendre_symbol, resultant, symbols, Poly, gcd as sgcd
W0 = defaultdict(list)           # p -> list of (C,d)
for line in open('/tmp/wit_1e6.txt'):
    p, C, d = map(int, line.split()); W0[p].append((C, d))
W = dict(W0)
P = sorted(W.keys()); allp = [p for p in primerange(5, 10**6) if p % 4 == 1]
CMIN = {p: min(C for C, d in W.get(p, [])) if W.get(p) else 0 for p in allp}
out = {}
def H(xs):
    c = Counter(xs); n = len(xs); return -sum(v/n*math.log2(v/n) for v in c.values())
def Hcond(xs, ys):
    n = len(xs); cy = defaultdict(list)
    for x, y in zip(xs, ys): cy[y].append(x)
    return sum(len(v)/n*H(v) for v in cy.values())
# --- Z1223 family isolation: family = C_min (first firing C; 0 = none ≤ 50)
fam = [CMIN[p] for p in allp]; cls = [p % 840 for p in allp]
leg = [tuple(legendre_symbol(p, q) if p % q else 0 for q in [11, 13, 17, 19, 23, 29, 31]) for p in allp]
out['Z1223'] = {'primes': len(allp), 'H(family)': round(H(fam), 4), 'H(family|p mod 840)': round(Hcond(fam, cls), 4),
                'H(family|p mod 840, legendre 11..31)': round(Hcond(fam, list(zip(cls, leg))), 4),
                'frac_primes_with_C_min<=2': round(sum(1 for f in fam if 1 <= f <= 2)/len(fam), 4)}
# --- Z1228 learned order of C per residue class (train p < 5e5, test p ≥ 5e5); cost = #tests to first witness (51 if none)
train = [p for p in allp if p < 5*10**5]; test = [p for p in allp if p >= 5*10**5]
wit_sets = {p: set(C for C, d in W.get(p, [])) for p in allp}
rate = defaultdict(lambda: np.zeros(51)); cnt = defaultdict(float)
for p in train:
    r = p % 840; cnt[r] += 1
    for C in wit_sets[p]: rate[r][C] += 1
glob = np.zeros(51)
for p in train:
    for C in wit_sets[p]: glob[C] += 1
glob /= len(train)
def cost(order, p):
    for i, C in enumerate(order):
        if C in wit_sets[p]: return i+1
    return 51
fixed = list(range(1, 51))
glob_order = list(np.argsort(-glob[1:])+1)
c_fixed = [cost(fixed, p) for p in test]
c_glob = [cost(glob_order, p) for p in test]
c_cls = []
for p in test:
    r = p % 840
    if r in rate and cnt[r] > 20:
        order = list(np.argsort(-rate[r][1:]/cnt[r])+1)
    else:
        order = glob_order
    c_cls.append(cost(order, p))
out['Z1228'] = {'test_primes': len(test), 'mean_tests_fixed_order_1..50': round(float(np.mean(c_fixed)), 3),
                'mean_tests_global_learned_order': round(float(np.mean(c_glob)), 3),
                'mean_tests_class_learned_order(p mod 840)': round(float(np.mean(c_cls)), 3),
                'max_tests_class_learned': int(max(c_cls)), 'unresolved_in_50_fixed': sum(1 for c in c_fixed if c > 50),
                'unresolved_in_50_class': sum(1 for c in c_cls if c > 50)}
# --- Z1277 C-form degree profiles from the first (minimal-C) witness: u=(d+1)/(4C), v=(e+1)/(4C), e=N/d,
# denominators x=Cuv, y=pCv, z=pCu (Lean cform: x=Cuv, y=nCv, z=nCu), checked: p = 4Cuv-u-v and 1/x+1/y+1/z = 4/p.
prof = Counter(); ok = 0; tot = 0
from fractions import Fraction as Fr
for p in allp[:20000]:
    if not W.get(p): continue
    C, d = min(W[p]); N = 4*C*p+1; e = N//d; u = (d+1)//(4*C); v = (e+1)//(4*C)
    tot += 1
    x, y, z = C*u*v, p*C*v, p*C*u
    ok += int(4*C*u*v - u - v == p and Fr(1, x)+Fr(1, y)+Fr(1, z) == Fr(4, p))
    lp = math.log(p)
    key = tuple(round(math.log(t)/lp*4)/4 for t in (x, y, z))   # exponents in units of 1/4 of log p
    prof[key] += 1
out['Z1277'] = {'witnesses_checked': tot, 'identity_ok': ok, 'top_profiles(exponents of x,y,z in log p)': [(list(k), c) for k, c in prof.most_common(8)],
                'n_distinct_profiles': len(prof)}
# --- Z1281 resultant in C of the two divisor factors d = 4Cu-1, e = 4Cv-1 (linear in C) is 4(v-u); check gcd(d,e) | 4(v-u)
Cs = symbols('C'); u_, v_ = symbols('u v')
res_expr = resultant(4*Cs*u_-1, 4*Cs*v_-1, Cs)
viol = 0; nontriv = 0; tot = 0
for p in allp[:5000]:
    for C in range(1, 51):
        ds = [d for CC, d in W.get(p, []) if CC == C]
        if len(ds) < 2: continue
        for i in range(len(ds)):
            for j in range(i+1, len(ds)):
                d, e = ds[i], ds[j]
                uu = (d+1)//(4*C); vv = (e+1)//(4*C); tot += 1
                g = math.gcd(d, e)
                if g > 1: nontriv += 1
                if (4*(vv-uu)) % g: viol += 1
out['Z1281'] = {'resultant_symbolic': str(res_expr), 'pairs_same_C': tot, 'gcd_gt_1': nontriv, 'violations_gcd_not_dividing_4(v-u)': viol}
# --- Z1287 gcd strata of same-C witness pairs (d,e) with d·e = N: g = gcd(d,e), g² | N, reconstruction (g, d/g, e/g)
strata = Counter(); recon_bad = 0; tot = 0
for p in allp[:20000]:
    for C in range(1, 51):
        ds = [d for CC, d in W.get(p, []) if CC == C]
        for d in ds:
            e = (4*C*p+1)//d; g = math.gcd(d, e); tot += 1
            if (4*C*p+1) % (g*g): recon_bad += 1
            if d*e != 4*C*p+1 or (d//g)*(e//g)*g*g != 4*C*p+1 or math.gcd(d//g, e//g) != 1: recon_bad += 1
            strata[g] += 1
out['Z1287'] = {'witness_pairs': tot, 'reconstruction_failures': recon_bad, 'strata_counts_g(top)': strata.most_common(6)}
# --- Z1320 concentration: monomial rank of witness points (u,v) for C ≤ 2, p ≤ 3000 (all points from different p)
pts = []
for p in allp:
    if p > 3000: break
    for C, d in W.get(p, []):
        if C <= 2:
            e = (4*C*p+1)//d; pts.append(((d+1)//(4*C), (e+1)//(4*C)))
PR = 2147483629
def rank_mod(M):
    M = [list(r) for r in M]; r = 0; cols = len(M[0]) if M else 0
    for c in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][c] % PR), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], PR-2, PR)
        M[r] = [(a*inv) % PR for a in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % PR:
                f = M[i][c]; M[i] = [(a-f*b) % PR for a, b in zip(M[i], M[r])]
        r += 1
    return r
deg_info = {}
for D in range(1, 7):
    mons = [(a, b) for a in range(D+1) for b in range(D+1-a)]
    M = [[pow(u, a, PR)*pow(v, b, PR) % PR for a, b in mons] for u, v in pts[:4000]]
    rk = rank_mod(M); deg_info[D] = {'monomials': len(mons), 'rank': rk, 'vanishing_poly_exists': rk < len(mons)}
out['Z1320'] = {'points': len(pts), 'by_degree': deg_info}
# --- Z1479 k-th power residue tower: among primes with a witness, fraction with some witness d a k-th power residue mod p
tower = {}
for k in [2, 4, 8]:
    have = hk = 0
    for p in allp:
        if not W.get(p): continue
        have += 1
        ex = False
        for C, d in W[p]:
            if pow(d % p, (p-1)//math.gcd(k, p-1), p) == 1: ex = True; break
        hk += int(ex)
    tower[k] = round(hk/have, 4)
out['Z1479'] = {'primes_with_witness': have, 'frac_with_some_kth_power_residue_witness': tower}
# --- Z1510 parity proxy: W(p)=#witnesses (C≤50); parity vs p mod 8, (3/p)... Hilbert-type symbols (2,p)_2, (3,p)_3~(p/3), (5/p)
par = defaultdict(Counter)
for p in allp:
    Wp = len(W.get(p, []))
    key = (p % 8, legendre_symbol(p, 3) if p % 3 else 0, legendre_symbol(p, 5) if p % 5 else 0)
    par[key][Wp % 2] += 1
out['Z1510'] = {'proxy': 'parity of #witnesses (C≤50) vs (2,p)_2 = p mod 8 and Legendre (p/3),(p/5)',
                'table': {str(k): dict(v) for k, v in sorted(par.items())}}
# --- Z1359 invariants: MI between 'witness with C≤2' and Jacobi-type invariants (p/m), m odd, 3..99
from sympy import jacobi_symbol
wit2 = [1 if any(C <= 2 for C, d in W.get(p, [])) else 0 for p in allp]
mis = {}
for m in range(3, 100, 2):
    if m % 4 == 1 and m > 1 and False: pass
    inv = [jacobi_symbol(p, m) for p in allp]
    # mutual information I(X;Y) = H(X) - H(X|Y)
    mis[m] = round(H(wit2) - Hcond(wit2, inv), 5)
out['Z1359'] = {'H(X)': round(H(wit2), 5), 'top_MI_jacobi_invariants': sorted(mis.items(), key=lambda t: -t[1])[:5],
                'note': 'X = witness with C<=2; invariants (p/m) for odd m<100 (Jacobi).'}
# --- Z1584 T1 check inside the C-form: odd squares m^2 have no C-form witness for C ≤ 50
t1 = {}
bad = 0; tested = 0
for m in range(3, 1000, 2):
    N0 = m*m
    for C in range(1, 51):
        N = 4*C*N0+1; mm = 4*C; d = mm-1; hit = False
        while d*d <= N:
            if N % d == 0: hit = True; break
            d += mm
        tested += 1; bad += int(hit)
out['Z1584'] = {'odd_squares_m^2_m<1000_C<=50_pairs_tested': tested, 'witnesses_found_at_odd_squares': bad}
# --- Z1621 generating function coefficients c_C(p) = #witnesses with that C (C ≤ 50), mean over primes, and a multiplicative test
cC = np.zeros(51); nP = 0
for p in allp[:20000]:
    nP += 1
    for C, d in W.get(p, []): cC[C] += 1
out['Z1621'] = {'primes': nP, 'mean_c_C_for_C=1..8': [round(float(cC[c]/nP), 3) for c in range(1, 9)],
                'mean_c_C_for_C=40..50': round(float(cC[40:51].sum()/nP/11), 4)}
print(json.dumps(out, indent=1, default=str))
