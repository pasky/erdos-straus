# z52d pass2 NC1 fix round 4: Z1289 chambers, Z1314 incidences (F_q), Z1325 exponential-polynomial zeros, Z1326 frustration index,
# Z1337 cocycle growth vs witnesses, Z1506 signed sibling, Z1611 formula sizes, Z1720 certificate-size distribution,
# Z1777 exact vs near-miss divisibility, Z1786 (p=409) witness search beyond C=50, Z1814 first-moment of the Type-II count,
# Z1848 hardness of prime values in two families.
import numpy as np, math, json, itertools
from collections import defaultdict, Counter
from sympy import primerange, divisors, factorint, totient, isprime, Poly, symbols
from scipy.ndimage import label as ndlabel
out = {}
W0 = defaultdict(list)
for line in open('/tmp/wit_1e6.txt'):
    p, C, d = map(int, line.split()); W0[p].append((C, d))
W = dict(W0)
allp = [p for p in primerange(5, 10**6) if p % 4 == 1]
def cmin(p):
    return min(C for C, d in W[p]) if W.get(p) else 0
# --- Z1289: sign chambers of (f1,f2,f3,f4) = (Cuv, Cv, Cu, 4Cuv-u-v) with C=1 on the real plane
g = np.linspace(-6, 6, 1201); U_, V_ = np.meshgrid(g, g, indexing='ij')
f = [U_*V_, V_, U_, 4*U_*V_-U_-V_]
sig = np.stack([np.sign(x) for x in f], axis=-1).reshape(-1, 4)
patterns = Counter(map(tuple, sig.tolist()))
pos = (f[0] > 0) & (f[1] > 0) & (f[2] > 0) & (f[3] > 0)
lab, ncomp = ndlabel(pos)
out['Z1289'] = {'grid': '[-6,6]^2 step 0.01, C=1', 'sign_patterns_realised(excluding zero)': sum(1 for k in patterns if 0 not in k),
                'positive_chamber_components(all of f1..f4>0)': int(ncomp), 'positive_cells': int(pos.sum())}
# --- Z1314: F_q incidences: points P = F_q^2, curves Γ_{C,n}: 4Cuv - u - v = n, C in F_q^*, n in QNR (or all n)
inc = {}
for q in [5, 7, 11, 13, 17, 19, 23]:
    qnr = set((x*x) % q for x in range(1, q))
    nonres = [n for n in range(1, q) if n not in qnr]
    I_qnr = 0; I_all = 0; maxc = 0
    for C in range(1, q):
        for n in range(q):
            cnt = sum(1 for u in range(q) for v in range(q) if (4*C*u*v - u - v - n) % q == 0)
            I_all += cnt; maxc = max(maxc, cnt)
            if n in nonres: I_qnr += cnt
    inc[q] = {'I(points, curves with QNR n)': I_qnr, 'I(all)': I_all, 'max_points_on_one_curve': maxc,
              'curves_with_QNR_n': (q-1)*len(nonres), 'expected_I_if_uniform': round(q*q*(q-1)*len(nonres)/(q*q)/1 * 1.0, 1)}
out['Z1314'] = inc
# --- Z1325: Z_p(z) = sum_{e ≡ -p (4), e ≤ 4p} sum_{(a,b): ab | N_e} z^{dist(a b^-1 mod e, -1)}, N_e=(p+e)/4 ;
#     dist(r) = min(r+1 mod e, e - (r+1 mod e)) ; c_0 = number of exact hits
def zpoly(p):
    coef = Counter()
    for e in range(1, 4*p+1):
        if (p+e) % 4: continue
        if e % 2 == 0 and False: pass
        N = (p+e)//4
        if N < 1: continue
        dv = divisors(N)
        for a in dv:
            for b in dv:
                if (a*b) % N and N % (a*b): pass
                if N % (a*b): continue
                if math.gcd(b, e) != 1: continue
                r = (a*pow(b, -1, e) if e > 1 else 0) % e if e > 1 else 0
                t = (r+1) % e if e > 1 else 0
                dist = min(t, e-t) if e > 1 else 0
                coef[dist] += 1
    return coef
zs = {}
for p in [13, 37, 101, 409]:
    coef = zpoly(p)
    deg = max(coef)
    cvec = [coef.get(j, 0) for j in range(deg+1)]
    roots = np.roots(cvec[::-1]) if deg > 0 else np.array([])
    mods = np.abs(roots) if len(roots) else np.array([])
    zs[p] = {'c_0 (exact hits)': cvec[0], 'degree': deg, 'roots_on_unit_circle(|z|-1|<1e-6)': int(np.sum(np.abs(mods-1) < 1e-6)) if len(mods) else 0,
             'min_|root|': round(float(mods.min()), 4) if len(mods) else None, 'max_|root|': round(float(mods.max()), 4) if len(mods) else None}
out['Z1325'] = zs
# --- Z1326: frustration index of the signed divisor graph for e-slices: vertices divisors of N_e; edge (a,b) iff a*b^-1 ≡ -1 (mod e);
#     spin sigma; edge satisfied iff sigma_a = -sigma_b. Frustration = min unsatisfied edges (brute force, ≤ 12 divisors)
def frust(p, e):
    N = (p+e)//4
    dv = divisors(N)
    if len(dv) > 12 or e < 2: return None
    E = []
    for i, a in enumerate(dv):
        for j, b in enumerate(dv):
            if j <= i or math.gcd(b, e) != 1 or math.gcd(a, e) != 1: continue
            if (a*pow(b, -1, e) + 1) % e == 0: E.append((i, j))
    if not E: return 0
    best = len(E)
    for mask in range(1 << len(dv)):
        bad = sum(1 for i, j in E if ((mask >> i) & 1) == ((mask >> j) & 1))
        best = min(best, bad)
        if best == 0: break
    return best
fr = {}
for p in [q for q in primerange(5, 200) if q % 4 == 1]:
    vals = []
    for e in range(1, 4*p+1):
        if (p+e) % 4: continue
        f_ = frust(p, e)
        if f_ is not None: vals.append(f_)
    fr[p] = {'slices_tested': len(vals), 'min_frustration': min(vals) if vals else None, 'frac_slices_with_0': round(sum(1 for v in vals if v == 0)/len(vals), 3) if vals else None}
out['Z1326'] = {'per_prime(first 8)': dict(list(fr.items())[:8]), 'primes': len(fr),
                'primes_with_some_slice_frustration_0': sum(1 for v in fr.values() if v['min_frustration'] == 0)}
# --- Z1337: cocycle A_q = [[q,-1],[1,0]] over the prime factors of 4cp+1 ; lambda_c = log ||prod||/#factors ; correlate with witness (C=c)
def lam(p, c):
    N = 4*c*p+1; fs = []
    for q, e in factorint(N).items(): fs += [q]*e
    M = np.eye(2); lg = 0.0
    for q in fs:
        M = M @ np.array([[q, -1.0], [1.0, 0.0]]); nrm = np.linalg.norm(M)
        lg += math.log(nrm); M = M/nrm
    return lg/len(fs) if fs else 0.0
lamw = []; lamn = []
for p in [q for q in allp[:400]]:
    for c in [1, 2, 3, 5]:
        has = any(C == c for C, d in W.get(p, []))
        (lamw if has else lamn).append(lam(p, c))
out['Z1337'] = {'mean_lambda_with_witness': round(float(np.mean(lamw)), 4), 'mean_lambda_without': round(float(np.mean(lamn)), 4),
                'n_with': len(lamw), 'n_without': len(lamn), 'cocycle': 'A_q=[[q,-1],[1,0]] over prime factors (with multiplicity) of 4cp+1, normalised product'}
# --- Z1506 signed sibling 4/p = 1/x + 1/y - 1/z: exists z ≤ 60 with (4z+p)/(pz) = 1/x+1/y (two-term) ?
def two_term(a, b):
    for d in divisors(b*b):
        if (d+b) % a == 0:
            dp = b*b//d
            if (dp+b) % a == 0: return True
    return False
sg = []
for p in [q for q in allp[:300]]:
    ok = False
    for z in range(1, 61):
        a = 4*z+p; b = p*z; gg = math.gcd(a, b)
        if two_term(a//gg, b//gg): ok = True; break
    sg.append(ok)
out['Z1506'] = {'primes': len(sg), 'frac_with_signed_solution_z<=60': round(sum(sg)/len(sg), 3)}
# --- Z1611 formula sizes for N = 4Cp+1, C ≤ 50: average number of divisors vs 2^ω (inclusion-exclusion) vs φ(4C) (character sum)
tau = []; w2 = []
for p in allp[:3000]:
    for C in range(1, 51):
        N = 4*C*p+1; f_ = factorint(N)
        tau.append(int(np.prod([e+1 for e in f_.values()]))); w2.append(2**len(f_))
out['Z1611'] = {'pairs': len(tau), 'mean_divisors(N)': round(float(np.mean(tau)), 2), 'mean_2^omega(N)': round(float(np.mean(w2)), 2),
                'mean_phi(4C)_char_terms': round(float(np.mean([int(totient(4*C)) for C in range(1, 51)])), 2),
                'note': 'inclusion–exclusion over witnesses needs 2^(#witnesses) terms; #witnesses per prime (C≤50) is ~8 on average'}
# --- Z1720 certificate-size distribution: minimal height H(p)=min over witnesses of max(C,u,v) for p up to 1e6 (exact)
Hs = []
for p in allp[:20000]:
    best = None
    for C, d in W.get(p, []):
        e = (4*C*p+1)//d; u = (d+1)//(4*C); v = (e+1)//(4*C)
        h = max(C, u, v)
        best = h if best is None else min(best, h)
    if best is not None: Hs.append(best)
Hs = np.array(Hs)
out['Z1720'] = {'primes_with_witness': len(Hs), 'median_H': float(np.median(Hs)), 'mean_log_H/log_p': None,
                'quantiles_H(50,90,99)': [float(np.percentile(Hs, q)) for q in (50, 90, 99)],
                'note': 'no Hermitian ℤ-lattice: the relation 4Cuv-u-v=p is bilinear in (u,v)'}
# --- Z1777 exact vs near-miss divisibility: for C ≤ 10, d ≡ -1 mod 4C, d ≤ sqrt(4Cp+1): exact (d | N) vs residue r = N mod d with |r|≤ 4C
ex = 0; near = 0; tot = 0
for p in allp[:5000]:
    for C in range(1, 11):
        N = 4*C*p+1; m = 4*C; d = m-1
        while d*d <= N:
            r = N % d; tot += 1
            if r == 0: ex += 1
            elif min(r, d-r) <= 4*C: near += 1
            d += m
out['Z1777'] = {'candidates': tot, 'exact_divisors': ex, 'near_misses(|r|<=4C)': near, 'fraction_exact': round(ex/tot, 5)}
# --- Z1786 p=409: witness search for C ≤ 5000 (is there any C-form witness at all?)
p = 409; first = None; cnt = 0
for C in range(1, 5001):
    N = 4*C*p+1; m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0:
            cnt += 1
            if first is None: first = C
            break
        d += m
out['Z1786'] = {'p': 409, 'C_min_for_C<=5000': first, 'C_with_witness_count_<=5000': cnt}
# --- Z1814 first moment: average over primes p≡1 (4), p<2e5, of #(u,B) ≤ X with 4uB | p+u+B (Type-II count with C integer), vs Σ 1/(4uB)
X = 300
mom = sum(1.0/(4*u*B) for u in range(1, X+1) for B in range(1, X+1))
cnts = []
for p in [q for q in primerange(5, 200000) if q % 4 == 1][:4000]:
    c = 0
    for u in range(1, X+1):
        for B in range(1, X+1):
            if (p+u+B) % (4*u*B) == 0: c += 1
    cnts.append(c)
out['Z1814'] = {'X': X, 'mean_count_over_primes': round(float(np.mean(cnts)), 4), 'naive_density_sum': round(mom, 4),
                'primes': len(cnts)}
# --- Z1848 hardness of prime values: families 840m+1 and 4m^2+1 (values < 10^6 to stay inside the witness table)
fam = {}
for name, fn, M in [('840m+1', lambda m: 840*m+1, 1190), ('4m^2+1', lambda m: 4*m*m+1, 499)]:
    vals_ = [fn(m) for m in range(1, M+1) if isprime(fn(m))]
    cm = [cmin(v) for v in vals_]
    fam[name] = {'prime_values': len(vals_), 'frac_C_min<=2': round(sum(1 for c in cm if 1 <= c <= 2)/len(cm), 3),
                 'frac_C_min>=10': round(sum(1 for c in cm if c >= 10)/len(cm), 3), 'max_C_min': max(cm), 'max_at_value': vals_[cm.index(max(cm))]}
out['Z1848'] = fam
print(json.dumps(out, indent=1, default=str))
