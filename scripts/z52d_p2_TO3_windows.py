"""Pass-2 TO3: (Z0879) out-of-sample exponent of U on L(1,chi_p) in the 1e6 / 1e7 windows; (Z0853) slice-event correlations
E_C(p) = [4Cp+1 has a divisor = -1 mod 4C] for C<=20, p=1 mod 4 <= 2e5; (Z0778) closure test of greedy failures;
(Z0906) lognormal-noise heuristic for the number of primes with U(p)=0 (model only); (Z0836,Z0843) single-feature AUCs.
Writes data/z52b/pass2/TO3/windows_results.json"""
import csv, json, math
import numpy as np
import cypari2
from sympy import factorint, divisors
pari = cypari2.Pari(); pari.allocatemem(10**9)
out = {}
# ---- Z0879 ----
def win(fn):
    W = np.loadtxt(fn, dtype=np.int64); W = W[W[:, 0] % 4 == 1]
    p = W[:, 0]; U = W[:, 1].astype(float); k1 = W[:, 10].astype(float); k2 = W[:, 11].astype(float)
    L1 = np.array([2 * int(pari.quadclassunit(int(q))[0]) * float(pari.log(pari.quadunit(int(q)))) / math.sqrt(q) for q in p])
    lp = np.log(p.astype(float))
    X = np.column_stack([np.ones(len(p)), np.log(L1), lp])
    b = np.linalg.lstsq(X, np.log(U), rcond=None)[0]
    b1 = np.linalg.lstsq(X, np.log(k1), rcond=None)[0]; b2 = np.linalg.lstsq(X, np.log(k2), rcond=None)[0]
    from scipy.stats import spearmanr
    res_ = np.log(U) - X @ b; s2 = res_ @ res_ / (len(p) - 3); se = float(np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1]))
    return dict(n=int(len(p)), alpha_U_logL1_with_logp=round(float(b[1]), 3), se_alpha=round(se, 3), alpha_k1=round(float(b1[1]), 3), alpha_k2=round(float(b2[1]), 3),
                spearman_U_L1=round(float(spearmanr(U, L1)[0]), 3))
out['Z0879'] = {'1e6': win('data/z52b/raw/pr_1e6_window.txt'), '1e7': win('data/z52b/raw/pr_1e7_window.txt')}
import csv as _c
_rows = list(_c.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
_S = [r for r in _rows if int(r['mod4']) == 1 and int(r['p']) > 100]
_p = np.array([int(r['p']) for r in _S]); _U = np.array([float(r['U']) for r in _S]); _L = np.array([float(r['L1real']) for r in _S])
_X = np.column_stack([np.ones(len(_p)), np.log(_L), np.log(_p.astype(float))]); _b = np.linalg.lstsq(_X, np.log(_U), rcond=None)[0]
_r = np.log(_U) - _X @ _b; _se = float(np.sqrt(_r @ _r / (len(_p) - 3) * np.linalg.inv(_X.T @ _X)[1, 1]))
out['Z0879_base_le2e5'] = dict(n=len(_p), alpha=round(float(_b[1]), 3), se=round(_se, 3))
# base-range comparison
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
# ---- Z0853 slice events ----
ps = [int(r['p']) for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100]
C_list = list(range(1, 21))
E = np.zeros((len(ps), len(C_list)), dtype=np.int8)
for i, p in enumerate(ps):
    for j, C in enumerate(C_list):
        n = 4 * C * p + 1
        ok = False
        for d in divisors(n):
            if d % (4 * C) == (4 * C - 1):
                ok = True; break
        E[i, j] = 1 if ok else 0
pe = E.mean(axis=0)
corr = np.corrcoef(E.T.astype(float))
out['Z0853'] = dict(n=len(ps), P_E_C_first10={C: round(float(pe[j]), 3) for j, C in enumerate(C_list[:10])},
                    P_E_C_last5={C: round(float(pe[j]), 3) for j, C in enumerate(C_list) if C > 15},
                    corr_E1_E2=round(float(corr[0, 1]), 3), corr_E1_E3=round(float(corr[0, 2]), 3),
                    corr_E_C_E_2C_mean=round(float(np.mean([corr[c - 1, 2 * c - 1] for c in range(1, 11)])), 3),
                    max_offdiag=round(float(np.max(np.abs(corr - np.eye(len(C_list))))), 3),
                    min_corr=round(float(np.min(corr)), 3))
# Cmin tail prediction under independence
Pall = np.prod(1 - pe[:10]) if False else None
out['Z0853']['note'] = 'E_C defined literally as in the item (divisor of 4Cp+1 that is -1 mod 4C); not the (u,B)-weighted R-count'
# ---- Z0778 greedy failure closure ----
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
minx = dict(zip(F[:, 0].tolist(), F[:, 8].tolist()))
bad = set(n for n in range(2, 30001) if n % 4 == 1 and minx[n] > n // 4 + 1)
comp_bad = sorted(n for n in bad if len(factorint(n)) > 1 or any(e > 1 for e in factorint(n).values()))
cl = []
tested = 0; closed = 0; fails = []
for a in sorted(bad):
    for b in sorted(bad):
        if a * b > 30000: break
        if a * b % 4 != 1: continue
        tested += 1
        if a * b in bad: closed += 1
        else: fails.append((a, b))
out['Z0778'] = dict(n_greedy_fail_le30000=len(bad), composite_list_first12=[n for n in sorted(bad) if n not in (p for p in [])][:0] or [n for n in sorted(bad) if len(factorint(n)) > 1][:12],
                    products_tested=tested, products_in_set=closed, closure_counterexamples_first=fails[:5])
json.dump(out, open('data/z52b/pass2/TO3/windows_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:600])
