"""U02 pass-1 completion (64 items), numerical part. Helpers: esols (z52b_p1_U02_lib), L(1,chi_D) class numbers.
Items: Z2365/Z2930/Z2731 (class-number regressions of residual log U), Z2739 (h(-4p) mod 8 classes), Z0541 (divisor
equidistribution over C), Z0232 (Hooley Delta on 4Cp+1), Z3075 (failure rate at squares vs primes), Z2752 (F2 rank
of slice-success bits), Z2562 (primitive-root-type prime factor vs divisor -1), Z2491 (small split primes vs classes of
disc -16d), Z2964 (multiplicativity of F_p(C,a)), Z2967 (rational linear relations among indicators), Z2968 (log mass of
'incapable' primes), Z3130 (divisor-pairing parity), Z3030 (divisors of p^2+4c^2 in classes -p mod 4c), Z0475 (class
numbers of sporadic small-U n), Z0339 (mean U/log^2 p), Z0483 (signal of log L(1,chi_p))."""
import sys, json, math
import numpy as np
from fractions import Fraction
from scipy.special import digamma
from sympy import jacobi_symbol, divisors, primerange, factorint
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
R = {}
F = np.loadtxt('/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
n_all, U = F[:, 0], F[:, 1].astype(float)
isp = np.ones(30001, bool); isp[:2] = False
for i in range(2, 174):
    if isp[i]: isp[i*i::i] = False
def kron(D, n):
    r = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0: return 0
        r *= 1 if D % 8 in (1, 7) else -1
    if n == 1: return r
    return r * jacobi_symbol(D % n, n)
def L1(D):
    q = abs(D); a = np.arange(1, q + 1)
    chi = np.array([kron(D, int(x)) if math.gcd(int(x), q) == 1 else 0 for x in a], float)
    return -(1.0 / q) * float(np.sum(chi * digamma(a / q)))
def hD(D): return math.sqrt(-D) * L1(D) / math.pi
sel = isp[n_all] & (n_all % 4 == 1) & (n_all > 100)
P = n_all[sel]; lU = np.log(U[sel]); lp = np.log(P)
X = np.column_stack([np.ones_like(lp), lp, np.log(lp)])
res_all = lU - X @ np.linalg.lstsq(X, lU, rcond=None)[0]
pl = [int(p) for p in P if p <= 1500]
idx = np.array([i for i, p in enumerate(P) if p <= 1500]); rU = res_all[idx]
def r2(cols):
    Z = np.column_stack([np.ones(len(rU))] + cols); c = np.linalg.lstsq(Z, rU, rcond=None)[0]
    return float(1 - np.sum((rU - Z @ c)**2) / np.sum((rU - rU.mean())**2))
Hd = {D: np.array([hD(-D * p) for p in pl]) for D in (3, 4, 7, 8)}
sq = np.array([np.sqrt(p) for p in pl])
R['Z2365_Z2930'] = {'R2_sum_h_over_sqrtp(D=3,4,7,8)': r2([sum(Hd[D] for D in Hd) / sq]),
                    'R2_each_logh_D4': r2([np.log(Hd[4])]), 'R2_each_logh_D8': r2([np.log(Hd[8])]),
                    'R2_each_logh_D3': r2([np.log(Hd[3])]), 'R2_each_logh_D7': r2([np.log(Hd[7])]),
                    'R2_legendre(2,-3,5,-7)': r2([np.array([kron(2, p) for p in pl], float), np.array([kron(-3, p) for p in pl], float),
                                                   np.array([kron(5, p) for p in pl], float), np.array([kron(-7, p) for p in pl], float)])}
# Z2731: fit residual on level-combination of h(-Dp) with D in {3,4,7,8}, positive combination test
Zc = np.column_stack([np.ones(len(rU))] + [np.log(Hd[D]) for D in (3, 4, 7, 8)])
c = np.linalg.lstsq(Zc, rU, rcond=None)[0]
R['Z2731'] = {'coef_logh_D3_D4_D7_D8': [round(float(v), 3) for v in c[1:]], 'R2': round(r2([np.log(Hd[D]) for D in (3, 4, 7, 8)]), 3)}
# Z2739: genus / 4-rank proxy: h(-4p) mod 8 classes vs residual
h4 = np.round(Hd[4]).astype(int)
R['Z2739'] = {str(m): {'n': int(np.sum(h4 % 8 == m)), 'mean_res': round(float(rU[h4 % 8 == m].mean()), 4)} for m in (2, 4, 6, 0)
              if np.sum(h4 % 8 == m) > 3}
# Z0541: divisor equidistribution: D_C(p) = #{d | N : d = -1 mod 4C, 1<d<N}, N = 4Cp+1, vs tau(N)/phi(4C)
def phi(m): return sum(1 for a in range(1, m + 1) if math.gcd(a, m) == 1)
ratios = []; tot_bad = 0; tot = 0
for C in range(1, 51):
    m = 4 * C; ph = phi(m)
    for p in [q for q in primerange(5, 3000) if q % 4 == 1]:
        N = 4 * C * p + 1
        dv = divisors(N)
        cnt = sum(1 for d in dv if 1 < d < N and (d - (m - 1)) % m == 0)
        exp = len(dv) / ph
        ratios.append(cnt / exp if exp else np.nan); tot += 1
        tot_bad += (cnt == 0)
R['Z0541'] = {'mean_ratio_count_over_expected': round(float(np.nanmean(ratios)), 4), 'median': round(float(np.nanmedian(ratios)), 4),
              'frac_zero_count': round(tot_bad / tot, 4), 'n_pairs': tot}
# Z3130 (parity pairing): d and N/d both = -1 mod 4C when d = -1 and N = 1 mod 4C; so M(N,C) even unless N is a square
viol = 0; tested = 0
for C in range(1, 13):
    m = 4 * C
    for p in [q for q in primerange(5, 2000) if q % 4 == 1]:
        N = 4 * C * p + 1; dv = divisors(N)
        M = sum(1 for d in dv if 1 < d < N and (d - (m - 1)) % m == 0)
        sqN = math.isqrt(N) ** 2 == N
        if (M % 2 == 1) and not sqN: viol += 1
        tested += 1
R['Z3130_pairing'] = {'tested': tested, 'odd_M_without_square_N': viol}
# Z0232: Hooley Delta(N) = max_u #{d | N : e^u < d <= e^{u+1}} on N=4Cp+1 (C<=50, p<=2000) vs random N of same size
def hooley(N):
    dv = np.log(np.array(divisors(N), float))
    best = 0
    for u0 in np.arange(0, math.log(N) + 1, 0.25):
        best = max(best, int(np.sum((dv > u0) & (dv <= u0 + 1))))
    return best
fam = []
for C in range(1, 51, 5):
    for p in [q for q in primerange(5, 2000) if q % 4 == 1][:60]:
        fam.append(hooley(4 * C * p + 1))
rnd = [hooley(int(x)) for x in np.random.default_rng(1).integers(10**5, 10**6, 300)]
R['Z0232'] = {'family_mean_Delta': round(float(np.mean(fam)), 3), 'random_mean_Delta': round(float(np.mean(rnd)), 3)}
# Z3075: failure rate (no proper divisor = -1 mod 4C) at N = 4C m^2 + 1 (squares m odd) vs N = 4C p + 1 (primes)
def fail(N, m):
    return not any(1 < d < N and (d - (m - 1)) % m == 0 for d in divisors(N))
sq_f = []; pr_f = []
for C in range(1, 26):
    for mm in range(3, 80, 2):
        sq_f.append(fail(4 * C * mm * mm + 1, 4 * C))
    for p in [q for q in primerange(5, 2000) if q % 4 == 1][:80]:
        pr_f.append(fail(4 * C * p + 1, 4 * C))
R['Z3075'] = {'fail_rate_squares_m2': round(float(np.mean(sq_f)), 4), 'fail_rate_primes': round(float(np.mean(pr_f)), 4), 'n_sq': len(sq_f)}
# Z2752: F2 rank of success bits across slices C=1..20 for primes p=1 mod 4 (p<3000): columns = C, rows = p
rows = []
for p in [q for q in primerange(5, 3000) if q % 4 == 1]:
    bits = []
    for C in range(1, 21):
        N = 4 * C * p + 1; m = 4 * C
        bits.append(int(any(1 < d < N and (d - (m - 1)) % m == 0 for d in divisors(N))))
    rows.append(bits)
A = np.array(rows, dtype=np.uint8)
def f2rank(M):
    M = M.copy() % 2; r = 0
    for col in range(M.shape[1]):
        piv = np.where(M[r:, col] == 1)[0]
        if len(piv) == 0: continue
        pr = piv[0] + r
        M[[r, pr]] = M[[pr, r]]
        for i in range(M.shape[0]):
            if i != r and M[i, col]: M[i] ^= M[r]
        r += 1
        if r == M.shape[0]: break
    return r
R['Z2752'] = {'rows': len(rows), 'F2_rank_success_bits_C1_20': f2rank(A), 'n_all_ones_rows': int(np.sum(A.sum(1) == 20))}
# Z2562: prime factor q of N with order of q mod 4C equal to the Carmichael lambda(4C) ("maximal order"); then is -1 a divisor residue?
def carm(m):
    from sympy import totient
    # exponent of (Z/m)^*: lcm of orders of units
    from math import lcm
    e = 1
    for a in range(1, m):
        if math.gcd(a, m) == 1:
            o = 1; x = a % m
            while x != 1 % m:
                x = (x * a) % m; o += 1
            e = lcm(e, o)
    return e
withq = 0; withq_minus1 = 0; tot2 = 0; withoutq = 0; withoutq_minus1 = 0
for C in range(1, 21):
    m = 4 * C; lam = carm(m)
    for p in [q for q in primerange(5, 1500) if q % 4 == 1]:
        N = 4 * C * p + 1
        qs = list(factorint(N).keys())
        has = any(pow(q % m, lam, m) == 1 and all(pow(q % m, lam // r, m) != 1 for r in factorint(lam) if lam % r == 0) for q in qs) if lam > 1 else True
        mi = any(1 < d < N and (d - (m - 1)) % m == 0 for d in divisors(N))
        tot2 += 1
        if has: withq += 1; withq_minus1 += mi
        else: withoutq += 1; withoutq_minus1 += mi
R['Z2562'] = {'slices': tot2, 'with_max_order_prime_factor': withq, 'P(-1 divisor|max-order factor)': round(withq_minus1 / max(1, withq), 4),
              'without': withoutq, 'P(-1 divisor|no max-order factor)': round(withoutq_minus1 / max(1, withoutq), 4)}
# Z2491: small split primes in disc -16d (d<=100): classes hit by primes q<=100 via forms x^2+d y^2-type enumeration (small reps)
def reduced_forms(D):
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a: continue
            if c == a and b < 0: continue
            if math.gcd(math.gcd(a, abs(b)), c) != 1: continue
            out.append((a, b, c))
        a += 1
    return out
cls_hit = []
for d in range(1, 101, 1):
    D = -16 * d
    if D % 4: continue
    fs = reduced_forms(D)
    if not fs: continue
    hit = set()
    for q in primerange(3, 101):
        if kron(D, q) != 1: continue
        found = None
        for i, (a, b, c) in enumerate(fs):
            for x in range(-10, 11):
                for y in range(-10, 11):
                    if a * x * x + b * x * y + c * y * y == q: found = i; break
                if found is not None: break
            if found is not None: break
        if found is not None: hit.add(found)
    cls_hit.append((d, len(fs), len(hit)))
R['Z2491'] = {'d_tested': len(cls_hit), 'full_coverage_count': sum(1 for d, h, k in cls_hit if k == h),
              'mean_frac_classes_hit': round(float(np.mean([k / h for d, h, k in cls_hit])), 3)}
# Z2964: multiplicativity of F_p(C,a)=1[a mod 4C contains a divisor of N]; test F(a)F(b)=F(ab) over unit classes mod 4C (C<=12)
mult_ok = 0; mult_tot = 0
for C in range(1, 13):
    m = 4 * C
    units = [a for a in range(1, m) if math.gcd(a, m) == 1]
    for p in [q for q in primerange(5, 2000) if q % 4 == 1][:120]:
        N = 4 * C * p + 1
        cls = set(d % m for d in divisors(N))
        F = {a: int(a in cls) for a in units}
        for a in units:
            for b in units:
                mult_tot += 1
                mult_ok += (F[a] * F[b] == F[(a * b) % m])
R['Z2964'] = {'agreement_F(a)F(b)=F(ab)': round(mult_ok / mult_tot, 4), 'pairs': mult_tot}
# Z2967: rational linear relations among indicators I_p(C,a)=1[a in divisor classes mod 4C] over rows p; count columns and rank
cols = []; M = []
for C in range(1, 13):
    m = 4 * C
    units = [a for a in range(1, m) if math.gcd(a, m) == 1]
    cols += [(C, a) for a in units]
for p in [q for q in primerange(5, 2000) if q % 4 == 1][:300]:
    row = []
    for C in range(1, 13):
        m = 4 * C; N = 4 * C * p + 1
        cls = set(d % m for d in divisors(N))
        row += [int(a in cls) for a in range(1, m) if math.gcd(a, m) == 1]
    M.append(row)
Mm = np.array(M, float)
R['Z2967'] = {'columns': len(cols), 'rank': int(np.linalg.matrix_rank(Mm)), 'rows': len(M)}
# Z2968: log-mass of 'incapable' primes (q with q != +-1 mod 4C) in N vs log N
frac = []
for C in range(1, 13):
    m = 4 * C
    for p in [q for q in primerange(5, 2000) if q % 4 == 1][:100]:
        N = 4 * C * p + 1
        mass_in = sum(math.log(q) * e for q, e in factorint(N).items() if q % m not in (1 % m, (m - 1) % m))
        frac.append(mass_in / math.log(N))
R['Z2968'] = {'mean_frac_log_mass_q_not_pm1_mod4C': round(float(np.mean(frac)), 4)}
# Z3030: divisors f of p^2+4c^2 (d=1) in class -p mod 4c (f ≡ -p mod 4c)?
hits = 0; tot3 = 0
for c in range(1, 21):
    for p in [q for q in primerange(5, 1000) if q % 4 == 1][:80]:
        Nn = p * p + 4 * c * c; m = 4 * c
        ok = any(1 < f < Nn and (f + p) % m == 0 for f in divisors(Nn))
        hits += ok; tot3 += 1
R['Z3030'] = {'frac_with_divisor_minus_p_mod_4c': round(hits / tot3, 4), 'pairs': tot3}
# Z0475: class numbers of Q(sqrt(-n)) for the smallest-U composite-free n: take n<=3000 with U(n)==min, and h(-4n) (n squarefree part)
Us = {int(n): int(u) for n, u in zip(n_all, U) if n <= 3000}
minU = min(Us.values())
low = [n for n, u in Us.items() if u == minU and n >= 2][:10]
R['Z0475'] = {'minU_over_n<=3000': minU, 'n_with_minU': low[:10], 'h(-4n)': {n: round(hD(-4 * n), 2) for n in low[:6] if n % 4 == 1}}
# Z0339: mean U/log^2 p over p=1 mod 4 (f4 primes 100..30000) and its spread
ratio = U[sel] / (np.log(P) ** 2)
R['Z0339'] = {'mean_U_over_log2p': round(float(ratio.mean()), 3), 'median': round(float(np.median(ratio)), 3), 'sd': round(float(ratio.std()), 3)}
# Z0483: coefficient of log L(1,chi_p) (Z0701 regression) on residual, p<=1000
pl2 = [int(p) for p in P if p <= 1000]; ids = np.array([i for i, p in enumerate(P) if p <= 1000]); rr = res_all[ids]
Lp = np.array([math.log(abs(L1(p))) for p in pl2])
Z = np.column_stack([np.ones(len(rr)), Lp]); cc = np.linalg.lstsq(Z, rr, rcond=None)[0]
R['Z0483'] = {'coef_log_L1chi_p': round(float(cc[1]), 3), 'corr': round(float(np.corrcoef(Lp, rr)[0, 1]), 3), 'n': len(rr)}
json.dump(R, open('data/z52b/pass1/U02/completion_m.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:5000])
