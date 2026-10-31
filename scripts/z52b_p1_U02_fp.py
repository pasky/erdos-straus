"""U02 fingerprint-type checks on f4 data (U(p) = #ES solutions, data/z52b/raw/f4_all_30000.txt).
Items: Z0698 (tau(p-1) vs L(1,chi_p) partial), Z0699 (tau((p+3)/4)), Z0712 (U mod 6), Z0782 (cubic/quartic residue
characters of primes q<=50), Z0783 (p mod 16 classes), Z0801 (ord_p(2) partial), Z0811 (Fermat quotient q_p(2) vs residual)."""
import numpy as np, json, math, sys
sys.path.insert(0, 'scripts')
from sympy import primerange, divisor_count, n_order
R = '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
n_all, U = F[:, 0], F[:, 1]
isp = np.ones(n_all.max() + 1, bool); isp[:2] = False
for i in range(2, int(n_all.max() ** .5) + 1):
    if isp[i]: isp[i*i::i] = False
sel = isp[n_all] & (n_all % 4 == 1) & (n_all > 100)
P = n_all[sel]; UU = U[sel].astype(float)
out = {}
lp = np.log(P); lU = np.log(UU)
X = np.column_stack([np.ones_like(lp), lp, np.log(lp)])
beta = np.linalg.lstsq(X, lU, rcond=None)[0]; res = lU - X @ beta
out['n_primes_1mod4'] = int(len(P))

def rank(a): return np.argsort(np.argsort(a)).astype(float)
def pcorr(x, y, Z):
    # Spearman partial correlation of x,y given columns Z (ranks)
    rx, ry = rank(x), rank(y)
    Zr = np.column_stack([np.ones(len(x))] + [rank(z) for z in Z]) if Z else np.ones((len(x), 1))
    ex = rx - Zr @ np.linalg.lstsq(Zr, rx, rcond=None)[0]
    ey = ry - Zr @ np.linalg.lstsq(Zr, ry, rcond=None)[0]
    return float(np.corrcoef(ex, ey)[0, 1])

leg2 = np.array([1 if p % 8 in (1, 7) else -1 for p in P], float)
# Z0699 tau((p+3)/4)
tau = np.array([divisor_count((p + 3) // 4) for p in P], float)
out['Z0699'] = {'spearman_resU_tau': pcorr(res, tau, []), 'spearman_U_tau': pcorr(UU, tau, [])}
# Z0698: tau(p-1) partial controlling L(1,chi_p) (computed via L=-(1/sqrt p) sum chi(a) log|1-zeta^a|) for p<=6000
m = P <= 6000
Lv = []
for p in P[m]:
    a = np.arange(1, p)
    chi = np.where(np.array([pow(int(x), (p - 1) // 2, p) for x in a]) == 1, 1.0, -1.0) if p < 0 else None
    # fast Legendre via squares
    sq = np.zeros(p, bool); sq[(a * a) % p] = True
    chi = np.where(sq[a], 1.0, -1.0)
    L = -(1 / math.sqrt(p)) * np.sum(chi * np.log(np.abs(1 - np.exp(2j * np.pi * a / p))))
    Lv.append(L.real)
Lv = np.array(Lv)
tm = np.array([divisor_count(int(p) - 1) for p in P[m]], float)
out['Z0698'] = {'n': int(m.sum()), 'L1_mean': float(Lv.mean()), 'spearman_resU_tau_p-1': pcorr(res[m], tm, []),
                'partial_given_logL': pcorr(res[m], tm, [np.log(np.abs(Lv))]),
                'spearman_resU_logL': pcorr(res[m], np.log(np.abs(Lv)), [])}
# Z0712: U mod 6 distribution, p=1 mod 4, plus repeated-denominator count (zero for p=1 mod 4 by Z0259 lemma)
r6 = np.bincount((UU.astype(int)) % 6, minlength=6) / len(UU)
out['Z0712'] = {'U_mod6_freq': [round(float(x), 4) for x in r6]}
# Z0783: p mod 16 classes (1 vs 9): mean residual difference in log U
c1 = (P % 16 == 1); c9 = (P % 16 == 9)
d = res[c1].mean() - res[c9].mean()
se = math.sqrt(res[c1].var() / c1.sum() + res[c9].var() / c9.sum())
out['Z0783'] = {'n1': int(c1.sum()), 'n9': int(c9.sum()), 'diff_logU_1_minus_9': float(d), 'se': float(se),
                'ratio_meanU_1_over_9': float((UU[c1] / (np.log(P[c1]) ** 2)).mean() / (UU[c9] / (np.log(P[c9]) ** 2)).mean())}
# Z0782: cubic (order 3) / quartic (order 4) residue classes of primes q<=50, ANOVA on residual of log U,
# AFTER removing the quadratic-character stratum of q (q/p) (otherwise the (2/p)-type effect swamps the test).
rows = []
for q in primerange(2, 51):
    qr = np.array([1 if pow(q, (int(p) - 1) // 2, int(p)) == 1 else -1 for p in P])
    for order in (3, 4):
        ok = (P % order == 1)
        def lab(p):
            v = pow(q, (p - 1) // order, p)
            if v == 1: return 0
            if order == 4 and v == p - 1: return 1
            return 2 if order == 4 else 1
        cls = np.array([lab(int(p)) if okp else -1 for p, okp in zip(P, ok)])
        r2 = res.copy()
        for s_ in (1, -1):
            m = ok & (qr == s_)
            r2[m] = res[m] - res[m].mean()
        groups = {}
        for v in set(cls[ok].tolist()):
            g = (cls == v) & ok
            if g.sum() >= 30: groups[v] = r2[g]
        if len(groups) < 2: continue
        allr = np.concatenate(list(groups.values())); gm = allr.mean()
        ssb = sum(len(g) * (g.mean() - gm) ** 2 for g in groups.values())
        ssw = sum(((g - g.mean()) ** 2).sum() for g in groups.values())
        k = len(groups); N = len(allr)
        F_ = (ssb / (k - 1)) / (ssw / (N - k))
        rows.append((q, order, round(float(F_), 3), len(groups), int(N)))
out['Z0782_F_stats_within_quadratic_strata'] = rows
out['Z0782_max_F'] = max(rows, key=lambda r: r[2]) if rows else None
# Z0801: ord_p(2)/(p-1) partial Spearman with residual U given (2/p) and tau(p-1); also ord_p(3), ord_p(5)
ordp = {b: np.array([n_order(b, int(p)) / (int(p) - 1) for p in P]) for b in (2, 3, 5)}
out['Z0801'] = {'resU_vs_ord2_partial(leg2,tau)': pcorr(res, ordp[2], [leg2, tau]),
                'resU_vs_ord3_partial': pcorr(res, ordp[3], [leg2, tau]),
                'resU_vs_ord5_partial': pcorr(res, ordp[5], [leg2, tau]),
                'raw_spearman_resU_ord2': pcorr(res, ordp[2], [])}
# Z0811: Fermat quotient q_p(2) = (2^{p-1}-1)/p mod p, normalised to [0,1)
qp = np.array([((pow(2, int(p) - 1, int(p) * int(p)) - 1) // int(p)) % int(p) / int(p) for p in P])
out['Z0811'] = {'spearman_resU_qp2': pcorr(res, qp, []), 'partial_given_logp': pcorr(res, qp, [lp])}
json.dump(out, open('data/z52b/pass1/U02/fp_U02.json', 'w'), indent=1, default=float)
for k, v in out.items(): print(k, str(v)[:400])
