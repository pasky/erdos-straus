"""U02 fix pass part 3: class numbers via L(1,chi_D) = -(1/|D|) sum_{a<=|D|} chi_D(a) psi(a/|D|), h(D) = sqrt|D| L/pi (D<-4).
Items: Z0796 (r3(p)=12h(-4p) check), Z0798 (Hurwitz H(4p),H(8p),H(3p) regression), Z0968 (Tunnell A,B vs h(-4p),h(-8p)),
Z0919 (Tunnell counts A(p)=r_{1,2,8}(p), B(p)=r_{1,2,32}(p) vs residual U, p<=3e4), Z0701 (log L(1,chi_{dp}) regression)."""
import sys, json, math
import numpy as np
from scipy.special import digamma
from sympy import jacobi_symbol, primerange
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
_cache = {}
def L1(D):
    q = abs(D)
    if q in _cache and D in _cache[q]: return _cache[q][D]
    a = np.arange(1, q + 1)
    chi = np.array([kron(D, int(x)) if math.gcd(int(x), q) == 1 else 0 for x in a], float)
    v = -(1.0 / q) * float(np.sum(chi * digamma(a / q)))
    _cache.setdefault(q, {})[D] = v
    return v
def hD(D):  # class number of fundamental disc D<-4 (w=2)
    return math.sqrt(-D) * L1(D) / math.pi
# residual of log U on (1, log p, log log p) for primes 1 mod 4 in (100, 30000]
sel = isp[n_all] & (n_all % 4 == 1) & (n_all > 100)
P = n_all[sel]; lU = np.log(U[sel]); lp = np.log(P)
X = np.column_stack([np.ones_like(lp), lp, np.log(lp)])
res_all = lU - X @ np.linalg.lstsq(X, lU, rcond=None)[0]
# Z0796: r3(p) vs 12 h(-4p) for p<=2000 (p=1 mod 4)
pl = [int(p) for p in P if p <= 2000]
r3 = {}
for p in pl[:60]:
    c = 0
    m = int(math.isqrt(p))
    for x in range(-m, m + 1):
        for y in range(-m, m + 1):
            r = p - x*x - y*y
            if r < 0: continue
            z = math.isqrt(r)
            if z*z == r: c += 2 if z > 0 else 1
    r3[p] = c
R['Z0796_identity_check'] = {str(p): (r3[p], round(12 * hD(-4 * p), 6)) for p in list(r3)[:8]}
R['Z0796_identity_max_err'] = max(abs(r3[p] - 12 * hD(-4 * p)) for p in r3)
# class numbers on p<=2000 (p=1 mod 4)
h4 = {p: hD(-4 * p) for p in pl}
h8 = {p: hD(-8 * p) for p in pl}
h3 = {p: hD(-3 * p) for p in pl if p % 3 != 0}  # -3p fundamental (p=1 mod 4)
idx = np.array([i for i, p in enumerate(P) if p <= 2000])
resU = res_all[idx]; Pl = P[idx]
def pc(x, y, Z=None):
    Zs = [np.ones(len(x))] + (Z or [])
    Zm = np.column_stack(Zs)
    ex = x - Zm @ np.linalg.lstsq(Zm, x, rcond=None)[0]
    ey = y - Zm @ np.linalg.lstsq(Zm, y, rcond=None)[0]
    return float(np.corrcoef(ex, ey)[0, 1])
# Z0798: regression of resU on log H(4p)/sqrtp etc.
H4 = np.array([h4[int(p)] for p in Pl]); H8 = np.array([h8[int(p)] for p in Pl])
H3 = np.array([h3.get(int(p), np.nan) for p in Pl]); ok3 = ~np.isnan(H3)
Z = np.column_stack([np.ones(ok3.sum()), np.log(H4[ok3] / np.sqrt(Pl[ok3])), np.log(H8[ok3] / np.sqrt(Pl[ok3])), np.log(H3[ok3] / np.sqrt(Pl[ok3]))])
coef = np.linalg.lstsq(Z, resU[ok3], rcond=None)[0]
pred = Z @ coef
R['Z0798'] = {'coef_logH4_logH8_logH3': [round(c, 4) for c in coef], 'R2': round(1 - np.sum((resU[ok3] - pred)**2) / np.sum((resU[ok3] - resU[ok3].mean())**2), 4),
              'corr_resU_logH4': round(pc(resU, np.log(H4)), 4), 'corr_resU_logH8': round(pc(resU, np.log(H8)), 4)}
# Z0968/Z0919: Tunnell counts A(n)=r_{1,2,8}(n), B(n)=r_{1,2,32}(n) (congruent-number Tunnell forms), n<=30000
Nm = 30000
def rq(coeffs):
    r = np.zeros(Nm + 1, np.int64)
    lim = [int(math.isqrt(Nm // c)) for c in coeffs]
    for x in range(-lim[0], lim[0] + 1):
        for y in range(-lim[1], lim[1] + 1):
            base = x*x*coeffs[0] + y*y*coeffs[1]
            if base > Nm: continue
            for z in range(-lim[2], lim[2] + 1):
                v = base + z*z*coeffs[2]
                if v <= Nm: r[v] += 1
    return r
A = rq((1, 2, 8)); B = rq((1, 2, 32))
Pa = np.array([int(p) for p in P if p <= 30000])
ia = np.array([np.where(P == p)[0][0] for p in Pa])
rU = res_all[ia]
R['Z0919_spearman_like'] = {'corr_resU_A': round(float(np.corrcoef(rU, np.log1p(A[Pa]))[0, 1]), 4),
                            'corr_resU_B': round(float(np.corrcoef(rU, np.log1p(B[Pa]))[0, 1]), 4),
                            'corr_resU_A-2B': round(float(np.corrcoef(rU, (A[Pa] - 2*B[Pa]).astype(float))[0, 1]), 4),
                            'n': int(len(Pa)), 'A_zero_frac': round(float(np.mean(A[Pa] == 0)), 3)}
# Z0968: Tunnell counts vs class numbers (p<=2000)
Ap = A[Pl].astype(float); Bp = B[Pl].astype(float)
R['Z0968'] = {'corr_A_resU': round(pc(Ap, resU), 4), 'corr_B_resU': round(pc(Bp, resU), 4),
              'partial_A_resU_given_logh8_logh4': round(pc(Ap, resU, [np.log(H8), np.log(H4)]), 4),
              'partial_B_resU_given_logh8_logh4': round(pc(Bp, resU, [np.log(H8), np.log(H4)]), 4),
              'corr_A-2B_resU': round(pc(Ap - 2*Bp, resU), 4)}
# Z0701: L(1,chi_{dp}) for dp fundamental, p<=1000 (p=1 mod 4); d in {1,-4,-8,-3,5,-7}: D = d*p (d=1 -> D=p)
p1k = [int(p) for p in P if p <= 1000]
ids = np.array([i for i, p in enumerate(P) if p <= 1000])
rr = res_all[ids]
Ls = {}
for d in (1, -4, -8, -3, 5, -7):
    Ls[d] = np.array([math.log(abs(L1(d * p if d != 1 else p))) for p in p1k])
Zall = np.column_stack([np.ones(len(rr))] + [Ls[d] for d in Ls])
coefs = np.linalg.lstsq(Zall, rr, rcond=None)[0]
R2_all = 1 - np.sum((rr - Zall @ coefs)**2) / np.sum((rr - rr.mean())**2)
drop = {}
for d in Ls:
    cols = [np.ones(len(rr))] + [Ls[e] for e in Ls if e != d]
    Zd = np.column_stack(cols); cd = np.linalg.lstsq(Zd, rr, rcond=None)[0]
    drop[d] = round(float(R2_all - (1 - np.sum((rr - Zd @ cd)**2) / np.sum((rr - rr.mean())**2))), 4)
R['Z0701'] = {'n': len(rr), 'R2_all': round(float(R2_all), 4), 'coef': {str(d): round(float(c), 3) for d, c in zip(Ls, coefs[1:])},
              'R2_drop_each': {str(k): v for k, v in drop.items()}}
json.dump(R, open('data/z52b/pass1/U02/fix_g.json', 'w'), indent=1, default=str)
print(json.dumps(R, default=str)[:3500])
