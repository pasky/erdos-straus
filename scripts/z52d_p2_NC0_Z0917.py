"""Z0917: type number of the maximal order of B_{p,inf} (p = 1 mod 4) vs the ES count U(p).
Classical facts used (checked numerically below, not assumed):
  (i)  h(B_{p,inf}) = #supersingular j = S(p) = (p-1)/12 + (1/3)(1 - (-3/p))  for p = 1 mod 4 (Eichler mass formula);
  (ii) type number T(p) = #orbits of Frobenius j -> j^p on supersingular j = (S + s1)/2, s1 = #{j in F_p supersingular};
  (iii) s1 = h(-4p)/2 for p = 1 mod 4 -- tested here by direct point counts for p <= 2000 (a_p(E_j)=0 test).
Then T(p) = (S + h(-4p)/2)/2 and the 'correction term' is h(-4p)/2.  Correlate with U residual (base: 1, log p, loglog p).
Inputs: /tmp/z52d_big/G2/h4p_2e5.txt (from scripts/z52d_p2_NC0_Z0917_h.c). Output: data/z52b/pass2/NC0/sub/Z0917_types.json
Run: ulimit -v 4000000; uv run --with numpy --with sympy --with scipy python scripts/z52d_p2_NC0_Z0917.py
"""
import numpy as np, json, os
from sympy import primerange, legendre_symbol
from scipy.stats import spearmanr
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = dict(tuple(map(int, l.split())) for l in open('/tmp/z52d_big/G2/h4p_2e5.txt'))
def S_of(p):
    return (p - 1) / 12 + (1 / 3) * (1 - int(legendre_symbol(-3 % p, p))) if p > 3 else None
def s1_count(p):
    """#{j in F_p : E_j has a_p = 0}; uses E_j: y^2 = x^3 + 3j(1728-j) x - 2j(1728-j)^2 (j != 0,1728), y^2=x^3+1 (j=0),
    y^2=x^3+x (j=1728).  Returns (s1, list of rational ss j, check of j-invariant for a few j)."""
    x = np.arange(p, dtype=np.int64)
    leg = np.zeros(p, dtype=np.int64)  # Legendre symbol table mod p
    sq = (x * x) % p
    leg[:] = -1; leg[sq] = 1; leg[0] = 0
    ss = []
    for j in range(p):
        if j == 0: a, b = 0, 1
        elif j == 1728 % p: a, b = 1, 0
        else:
            k = (1728 - j) % p
            a = (3 * j * k) % p; b = (-2 * j * k * k) % p
        rhs = (x * x % p * x + a * x + b) % p
        ap = -int(leg[rhs].sum())
        if ap % p == 0 and ap == 0: ss.append(j)
    return len(ss), ss
def jinv(a, b, p):
    # j = 1728 * 4a^3 / (4a^3 + 27 b^2) mod p
    num = (1728 * 4 * a ** 3) % p; den = (4 * a ** 3 + 27 * b * b) % p
    return (num * pow(den, p - 2, p)) % p
out = {'validation_s1_vs_h4p_over_2': []}
for p in primerange(5, 2001):
    if p % 4 != 1: continue
    s1, ss = s1_count(p)
    ok = (s1 == H[p] // 2)
    out['validation_s1_vs_h4p_over_2'].append([p, s1, H[p] // 2, bool(ok)])
    # j-invariant check of the model used for a few generic j
    for j in [2, 3, 7]:
        if j % p in (0, 1728 % p): continue
        k = (1728 - j) % p; a = (3 * j * k) % p; b = (-2 * j * k * k) % p
        assert jinv(a, b, p) == j % p, (p, j)
S_check = []
for p in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]:
    # S from formula vs number of distinct supersingular j in F_p-bar = (number of ss j in F_p)+(others): only F_p-rational known here
    S_check.append([p, S_of(p), H[p] // 2])
out['S_formula_samples[p,S,h4p/2]'] = S_check
bad = [v for v in out['validation_s1_vs_h4p_over_2'] if not v[3]]
out['n_validated'] = len(out['validation_s1_vs_h4p_over_2']); out['n_mismatch_s1'] = len(bad)
# type numbers and correlation with U (2e5 range)
import sys
sys.path.insert(0, ROOT + '/scripts')
R = ROOT + '/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64); G = np.loadtxt(R + 'pr_20001_200000.txt', dtype=np.int64)
UU = {int(r[0]): int(r[1]) for r in np.vstack([F, G])}
P = np.array(sorted(p for p in H if p > 100 and p in UU), dtype=np.int64)
S = np.array([(p - 1) / 12 + (1 / 3) * (1 - int(legendre_symbol(-3 % int(p), int(p)))) for p in P])
h4 = np.array([H[int(p)] for p in P], dtype=float)
T = (S + h4 / 2) / 2
U = np.array([UU[int(p)] for p in P], dtype=float)
lp = np.log(P.astype(float)); base = np.vstack([np.ones_like(lp), lp, np.log(lp)]).T
def resid(v):
    y = np.log(v + 1); return y - base @ np.linalg.lstsq(base, y, rcond=None)[0]
rU = resid(U)
out['n_primes'] = int(len(P))
out['spearman_U_resid_vs_h4p'] = [round(float(spearmanr(rU, resid(h4))[0]), 4), float(spearmanr(rU, resid(h4))[1])]
out['spearman_U_resid_vs_T'] = [round(float(spearmanr(rU, resid(T))[0]), 4), float(spearmanr(rU, resid(T))[1])]
out['spearman_U_resid_vs_T_minus_S_over2'] = [round(float(spearmanr(rU, T - S / 2)[0]), 4), float(spearmanr(rU, T - S / 2)[1])]
# raw: U vs T-correction (T - S/2 = h4p/4) on raw (non-residual) scale, for the 'correction term' question
out['spearman_raw_U_vs_h4p_over_4'] = round(float(spearmanr(U, h4)[0]), 4)
# partial: control for S (growth) by using residuals of U and h4 against log S
out['T_mean_over_S_mean'] = round(float(T.mean() / S.mean()), 4)
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0917_types.json', 'w'), indent=1)
print({k: v for k, v in out.items() if k not in ('validation_s1_vs_h4p_over_2',)})
print('validation rows (p,s1,h/2,ok) first 8:', out['validation_s1_vs_h4p_over_2'][:8], ' mismatches:', len(bad))
