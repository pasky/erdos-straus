"""Pass-2 TO3: per-prime Euler-weight regressions (Z0806, Z0823-Z0826), twist fits (Z0921), idoneal/x^2+840y^2 checks (Z0935,
Z0936), h(-8p)/h(-24p) strata (Z0959), and 2-adic nested contrasts (Z0835 follow-up). Uses base table + PARI.
Writes data/z52b/pass2/TO3/regress_results.json"""
import csv, json, math
import numpy as np
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
out = {}
P = np.array([int(r['p']) for r in rows]); M4 = np.array([int(r['mod4']) for r in rows])
U = np.array([float(r['U']) for r in rows]); H4 = np.array([float(r['h4p']) for r in rows])
L1 = np.array([float(r['L1real']) if r['L1real'] != 'NA' else np.nan for r in rows])
k1 = np.array([float(r['k1']) for r in rows]); k2 = np.array([float(r['k2']) for r in rows])
Qs = [q for q in pari.primes(50)] if False else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def resid(y, X):
    X = np.column_stack([np.ones(len(y))] + X)
    return y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
def fit(y, Xcols):
    X = np.column_stack([np.ones(len(y))] + Xcols)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    s2 = res @ res / (len(y) - X.shape[1])
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, np.sqrt(np.diag(cov))
# ---- p = 1 mod 4 ----
m1 = (M4 == 1) & (P > 100) & (U > 0)
p1 = P[m1]; lp = np.log(p1.astype(float)); y = np.log(U[m1]) - resid(np.log(U[m1]), [lp, np.log(lp)]) * 0
yres = resid(np.log(U[m1]), [lp, np.log(lp)])          # residual after log p, loglog p
Lg = {q: np.array([int(pari.kronecker(q, int(p))) for p in p1]) for q in Qs}
Xs = [Lg[q] for q in Qs]
beta, se = fit(yres, Xs)
out['Z0823_chi_p_weights_p1mod4'] = {int(q): dict(beta=round(float(beta[i + 1]), 4), se=round(float(se[i + 1]), 4), q_beta=round(float(q * beta[i + 1]), 3))
                                     for i, q in enumerate(Qs)}
# (q/p)=+/-1 ; q mod 3 split
# ---- shift-divisor indicators: 1[q | p+3] ----
Ind = {q: (((p1 + 3) % q) == 0).astype(float) for q in Qs if q >= 5}
Xs2 = Xs + [Ind[q] for q in Qs if q >= 5]
beta2, se2 = fit(yres, Xs2)
names = Qs + [q for q in Qs if q >= 5]
out['Z0824_with_indicator_q_divides_p_plus_3'] = {f'chi_{q}': dict(beta=round(float(beta2[i + 1]), 4), se=round(float(se2[i + 1]), 4))
                                                    for i, q in enumerate(Qs)}
out['Z0824_indicator_coeffs'] = {f'1[{q}|p+3]': dict(beta=round(float(beta2[len(Qs) + 1 + j]), 4), se=round(float(se2[len(Qs) + 1 + j]), 4))
                                 for j, q in enumerate([q for q in Qs if q >= 5])}
out['Z0825_beta7_before_after'] = dict(before=round(float(beta[Qs.index(7) + 1]), 4), after=round(float(beta2[Qs.index(7) + 1]), 4),
                                       se_after=round(float(se2[Qs.index(7) + 1]), 4))
# mod-3 split with/without controls
mod3 = {}
for q in Qs:
    if q == 2: continue
    mod3[int(q)] = (q % 3, round(float(q * beta[Qs.index(q) + 1]), 3), round(float(q * beta2[Qs.index(q) + 1]), 3))
out['Z0823_Z0824_q_mod3_split'] = mod3
# counts
out['Z0824_n_primes_p1mod4'] = int(m1.sum())
# ---- p = 3 mod 4: chi_{-p}(q) ----
m3 = (M4 == 3) & (P > 100) & (U > 0)
p3 = P[m3]; lp3 = np.log(p3.astype(float))
yres3 = resid(np.log(U[m3]), [lp3, np.log(lp3)])
Lg3 = {q: np.array([int(pari.kronecker(-int(p), q)) for p in p3]) for q in Qs}
beta3, se3 = fit(yres3, [Lg3[q] for q in Qs])
out['Z0826_chi_minus_p_weights_p3mod4'] = {int(q): dict(beta=round(float(beta3[i + 1]), 4), se=round(float(se3[i + 1]), 4), q_beta=round(float(q * beta3[i + 1]), 3))
                                          for i, q in enumerate(Qs)}
# ---- Z0921 / genus twists: L(1, chi_{-m p}) for fundamental disc of -m p ----
def L1_twist(D):
    d = int(pari.coredisc(D))
    h = int(pari.quadclassunit(d)[0]) if d < 0 else None
    w = 6 if d == -3 else (4 if d == -4 else 2)
    return math.pi * h / (w * math.sqrt(-d))
mset = [3, 5, 7, 15, 21, 35, 105]
twist = {m: [] for m in mset}
sel = np.arange(len(p1))
for m in mset:
    vals = []
    for p in p1:
        D = -m * int(p)
        vals.append(L1_twist(D))
    twist[m] = np.array(vals)
X_tw = [np.log(twist[m]) for m in mset]
b_single = {}
for m, xv in zip(mset, X_tw):
    b, s = fit(yres, [xv]); b_single[m] = dict(coef=round(float(b[1]), 4), se=round(float(s[1]), 4))
b_joint, s_joint = fit(yres, X_tw)
out['Z0921_single_coef'] = b_single
out['Z0921_joint_coef'] = {m: dict(coef=round(float(b_joint[i + 1]), 4), se=round(float(s_joint[i + 1]), 4)) for i, m in enumerate(mset)}
out['Z0921_base_coef_logL1real'] = dict(zip(['logL1real'], [round(float(fit(yres, [np.log(L1[m1])])[0][1]), 4)]))
# ---- Z0959 : h(-8p), h(-24p) strata mod 16 (p = 1 mod 8) ----
m8 = m1 & (P % 8 == 1)
p8 = P[m8]; lp8 = np.log(p8.astype(float))
y8 = resid(np.log(U[m8]), [lp8, np.log(lp8)])
h8 = np.array([int(pari.qfbclassno(-8 * int(p))) for p in p8])
h24 = np.array([int(pari.qfbclassno(-24 * int(p))) for p in p8])
out['Z0959'] = dict(n=int(len(p8)),
                    U_resid_by_h8p_mod16={int(c): round(float(y8[(h8 % 16) == c].mean()), 4) for c in (0, 4, 8, 12) if ((h8 % 16) == c).any()},
                    U_resid_by_h24p_mod16={int(c): round(float(y8[(h24 % 16) == c].mean()), 4) for c in (0, 4, 8, 12) if ((h24 % 16) == c).any()},
                    count_h8p_mod16={int(c): int(((h8 % 16) == c).sum()) for c in (0, 4, 8, 12)},
                    count_h24p_mod16={int(c): int(((h24 % 16) == c).sum()) for c in (0, 4, 8, 12)})
# ---- Z0935: primes x^2 + 840 y^2 vs classes mod 840 ----
N = 10**6
rep = set()
for y_ in range(1, int(math.isqrt(N // 840)) + 1):
    for x_ in range(0, int(math.isqrt(N - 840 * y_ * y_)) + 1):
        v = x_ * x_ + 840 * y_ * y_
        if v <= N and pari.isprime(v): rep.add(int(v))
classes = {1, 121, 169, 289, 361, 529}
allp = [int(p) for p in P if p <= N]
allp = [p for p in pari.primes(N) if True] if False else allp
cls_primes = set(p for p in [int(x) for x in np.array(list(pari.primes(78498)))] ) if False else None
pr_list = [int(x) for x in pari.primes(78498)] if False else None
import sympy
pr_list = [int(x) for x in sympy.primerange(3, N)]
ok_cls = [p for p in pr_list if (p % 840) in classes]
out['Z0935'] = dict(primes_le1e6_represented_x2_840y2=len(rep), primes_in_six_classes=len(ok_cls),
                    represented_not_in_classes=sorted(rep - set(ok_cls))[:5], in_classes_not_represented=sorted(set(ok_cls) - rep)[:5],
                    n_rep_in_classes=len(rep & set(ok_cls)))
# ---- Z0936 : class group of disc -4D elementary 2-group for idoneal D? ----
res936 = {}
for D in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 21, 22, 24, 25, 28, 30, 33, 37, 40, 42, 45, 48, 57, 58, 60, 70, 72, 78, 85, 88, 93, 102, 105, 112, 120, 130, 133, 165, 168, 177, 190, 210, 232, 240, 253, 273, 280, 312, 330, 345, 357, 385, 408, 462, 520, 760, 840, 1320, 1365, 1848):
    d = -4 * D
    cl = pari.quadclassunit(d)
    cyc = [int(c) for c in cl[1]] if len(cl[1]) else []
    elem2 = all(c <= 2 for c in cyc)
    res936[D] = dict(h=int(cl[0]), elem2=elem2)
out['Z0936_idoneal_check'] = {D: v for D, v in res936.items() if D in (840, 1320, 1365, 1848, 210, 1155 if False else 210, 280, 312, 330, 1)}
# idoneal list from sequence A000926 (Euler's 65 known numbers, first 30 for reference)
IDON = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 21, 22, 24, 25, 28, 30, 33, 37, 40, 42, 45, 48, 57, 58, 60, 70, 72, 78, 85, 88, 93, 102, 105, 112, 120, 130, 133, 165, 168, 177, 190, 210, 232, 240, 253, 273, 280, 312, 330, 345, 357, 385, 408, 462, 520, 760, 840, 1320, 1365, 1848]
nonidon_check = {}
for D in [x for x in range(1, 400) if x not in IDON][:0]:
    pass
ex = {}
for D in [1155, 1365, 1848, 2310, 1320, 255, 330, 390]:
    cl = pari.quadclassunit(-4 * D)
    ex[D] = dict(h=int(cl[0]), cyc=[int(c) for c in cl[1]])
out['Z0936_nonidoneal_examples'] = ex
json.dump(out, open('data/z52b/pass2/TO3/regress_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:700])
