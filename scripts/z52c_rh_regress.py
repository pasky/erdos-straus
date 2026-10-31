"""RESIDUE_HARDNESS §2: does the full-residue factor F (model of §1.3) explain the Pass-1 class-of-one effect (Z0199) and
the 'practical p−1' effect (Z0900)?  Does M_BM·F make the (★)-failure primes / hard primes less surprising?

Inputs (/tmp/rh): t2e5full, t1e6, t2e6 [, t1e7] tuple counts (z52c_rh_types.c) -> U(p) for primes p ≡ 1 (4);
s1e7_R (z52c_rh_star.c) -> R(p); mbm_1e6.txt (z38_mbm.c 3 1e6 0) -> M_BM(p) for p ≤ 1e6; data/z52c/rh/model_tables.json.
Predicted factor: log F(p) = Σ_components ± log(1 + (F_Q(p mod Q) − 1)·L0/log p), F_Q from the model window [1e6, 2e6]
(L0 = its log-centre), 1/L scaling of §1.2 (checked across windows below). Main variant COMP: F_840·(F_16/F_8)·F_11·F_13
(the joint mod-840 table keeps the interactions of the characters mod 3, 5, 7, 8); variant COMP_PRIME: product over the
prime-power components 16, 3, 5, 7, 11, 13 (misses those interactions: rms log-difference 0.10 against the joint 840 table).
Output: data/z52c/rh/regress.json + printed report.
Usage: uv run --with numpy --with sympy python scripts/z52c_rh_regress.py
"""
import numpy as np, json, os
from sympy import primerange, factorint

T = '/tmp/rh/'
MT = json.load(open('data/z52c/rh/model_tables.json'))
REF = '1e6'
COMP_PRIME = [(16, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1)]          # product over prime-power components
COMP = [(840, 1), (16, 1), (8, -1), (11, 1), (13, 1)]                     # joint mod 840 (captures character interactions), 16/8 refinement
out = {}

# ---------- data assembly ----------
HI = 10**7
R7 = np.fromfile(T + 's1e7_R.u16', np.uint16).astype(float)
isp = np.ones(HI + 1, bool); isp[:2] = False
for i in range(2, int(HI**.5) + 1):
    if isp[i]: isp[i*i::i] = False
P, Uv = [], []
for pre, lo, hi in [('t2e5full', 101, 200000), ('t1e6', 200001, 1000000), ('t2e6', 1000001, 2000000), ('t1e7', 5000001, 10000000)]:
    if not os.path.exists(T + pre + '_TI.f32'): print('missing', pre); continue
    TI = np.fromfile(T + pre + '_TI.f32', np.float32); TII = np.fromfile(T + pre + '_TII.f32', np.float32)
    v = np.arange(lo, hi + 1); s = isp[lo:hi+1] & (v % 4 == 1) & (v > 100)
    P.append(v[s]); Uv.append((TI[s] + TII[s])/2)
P = np.concatenate(P); U = np.concatenate(Uv); lp = np.log(P.astype(float))


def model_factor(PP, family='U', ref=REF, comps=COMP):
    L0 = MT[ref]['L']; lf = np.zeros(len(PP)); L = np.log(PP.astype(float))
    for Q, sgn in comps:
        d = MT[ref][str(Q)]; fac = dict(zip(d['classes'], d[family]['model']))
        f = np.array([fac[int(x)] for x in PP % Q])
        lf += sgn*np.log(1 + (f - 1)*L0/L)
    return lf


# ---------- check 1: product approximation on Q = 840, and 1/L scaling across windows ----------
chk = {}
for fam in ['U', 'S']:
    for ref in ['1e5', '1e6', '5e6']:
        if ref not in MT: continue
        d = MT[ref]['840']; cl = np.array(d['classes'])
        f8 = dict(zip(MT[ref]['8']['classes'], MT[ref]['8'][fam]['model']))
        pr = np.array([f8[r % 8]*dict(zip(MT[ref]['3']['classes'], MT[ref]['3'][fam]['model']))[r % 3]
                       * dict(zip(MT[ref]['5']['classes'], MT[ref]['5'][fam]['model']))[r % 5]
                       * dict(zip(MT[ref]['7']['classes'], MT[ref]['7'][fam]['model']))[r % 7] for r in cl])
        m = np.array(d[fam]['model']); se = np.array(d[fam]['model_se'])
        pr = pr/pr.mean()
        chk[f'{fam}_{ref}'] = dict(corr=float(np.corrcoef(np.log(m), np.log(pr))[0, 1]), rms_log_diff=float(np.sqrt(np.mean((np.log(m) - np.log(pr))**2))),
                                   rms_model_se=float(np.sqrt(np.mean(se**2))))
    # 1/L scaling: (F−1)·L across windows for Q = 7, 5
    for Q in (5, 7, 16):
        rows = {}
        for ref in ['1e5', '1e6', '5e6']:
            if ref not in MT: continue
            d = MT[ref][str(Q)]; rows[ref] = [round((f - 1)*MT[ref]['L'], 3) for f in d[fam]['model']]
        chk[f'{fam}_scaling_Q{Q}'] = rows
print('product approximation / scaling checks:'); [print(' ', k, v) for k, v in chk.items()]
out['checks'] = chk

# ---------- regression (Pass-1 design) ----------
qs = list(primerange(2, 80))
def leg(a, p): return np.where(pow_mod(a, p) == 1, 1.0, -1.0)
def pow_mod(a, PP): return np.array([pow(a, (int(p) - 1)//2, int(p)) for p in PP])
Xc = np.column_stack([leg(q, P) for q in qs])
div = [5, 7, 11, 13, 16]
Xd = np.column_stack([((P - 1) % d == 0).astype(float) for d in div])
y = np.log(U + 1.0)
lF = model_factor(P, 'U')
lF_prime = model_factor(P, 'U', comps=COMP_PRIME)


def fit(X, yy):
    b, *_ = np.linalg.lstsq(X, yy, rcond=None); r = yy - X @ b; s2 = r @ r/(len(yy) - X.shape[1])
    return b, np.sqrt(np.diag(np.linalg.inv(X.T @ X))*s2), r


def report(sel, tag, lF=lF):
    o = {'n': int(sel.sum())}
    yy = y[sel]; base = np.column_stack([np.ones(sel.sum()), lp[sel], np.log(lp[sel]), Xc[sel]])
    k = base.shape[1]; tss = ((yy - yy.mean())**2).sum()
    b0, se0, r0 = fit(base, yy)
    b1, se1, r1 = fit(np.column_stack([base, Xd[sel]]), yy)
    b2, se2, r2 = fit(np.column_stack([base, Xd[sel]]), yy - lF[sel])          # offset log F
    b3, se3, r3 = fit(np.column_stack([base, lF[sel]]), yy)                     # free coefficient on log F
    b4, se4, r4 = fit(base, yy - lF[sel])
    o['coef_indicators_raw'] = {str(d): [round(b1[k+i], 4), round(se1[k+i], 4)] for i, d in enumerate(div)}
    o['coef_indicators_after_offset'] = {str(d): [round(b2[k+i], 4), round(se2[k+i], 4)] for i, d in enumerate(div)}
    o['coef_logF_free'] = [round(b3[k], 3), round(se3[k], 3)]
    o['R2_gain_indicators_raw'] = float(((r0**2).sum() - (r1**2).sum())/tss)
    o['R2_gain_logF'] = float(((r0**2).sum() - (r3**2).sum())/tss)
    o['R2_gain_indicators_after_offset'] = float(((r4**2).sum() - (r2**2).sum())/tss)
    o['resid_sd_chars'] = float(r0.std()); o['resid_sd_chars_logF'] = float(r3.std())
    PP = P[sel]
    def classmeans(res, Q, cls):
        return {int(c): [round(float(res[PP % Q == c].mean()), 4), int((PP % Q == c).sum())] for c in cls}
    sq840 = [r for r in range(1, 840) if r % 8 == 1 and all(pow(r % m, (m-1)//2, m) == 1 for m in (3, 5, 7))]
    o['resid_by_class_mod7_before'] = classmeans(r0, 7, [1, 2, 4]); o['resid_by_class_mod7_after'] = classmeans(r4, 7, [1, 2, 4])
    o['resid_by_class_mod840_before'] = classmeans(r0, 840, sq840); o['resid_by_class_mod840_after'] = classmeans(r4, 840, sq840)
    nd = Xd[sel][:, :4].sum(1) + ((PP - 1) % 3 == 0)
    o['resid_by_ndiv_before'] = {int(j): [round(float(r0[nd == j].mean()), 4), int((nd == j).sum())] for j in range(6) if (nd == j).any()}
    o['resid_by_ndiv_after'] = {int(j): [round(float(r4[nd == j].mean()), 4), int((nd == j).sum())] for j in range(6) if (nd == j).any()}
    # Z0900: practical p − 1
    prac = np.array([is_practical(int(p) - 1) for p in PP])
    o['practical_frac'] = float(prac.mean())
    o['practical_resid_before'] = [round(float(r0[prac].mean()), 4), round(float(r0[~prac].mean()), 4)]
    o['practical_resid_after'] = [round(float(r4[prac].mean()), 4), round(float(r4[~prac].mean()), 4)]
    bp, sep, _ = fit(np.column_stack([base, prac.astype(float)]), yy)
    bq, seq, _ = fit(np.column_stack([base, prac.astype(float)]), yy - lF[sel])
    o['practical_coef_before_after'] = [[round(bp[k], 4), round(sep[k], 4)], [round(bq[k], 4), round(seq[k], 4)]]
    # hardest primes: how many of the 30 lowest residuals (chars model) remain in the 30 lowest after the offset
    h0 = set(np.argsort(r0)[:30]); h4 = set(np.argsort(r4)[:30])
    o['hard30_overlap'] = len(h0 & h4); o['hard30_mean_logF'] = round(float(lF[sel][list(h0)].mean()), 4)
    o['all_mean_logF'] = round(float(lF[sel].mean()), 4)
    o['hard30_practical_before_after'] = [int(prac[list(h0)].sum()), int(prac[list(h4)].sum())]
    out[tag] = o
    print(f'== {tag}:', json.dumps(o, indent=None)[:4000])


def is_practical(n):
    if n == 1: return True
    if n % 2: return False
    f = sorted(factorint(n).items()); s = 1
    for p, e in f:
        if p > s + 1: return False
        s *= (p**(e+1) - 1)//(p - 1)
    return True


report((P > 100) & (P <= 200000), 'pass1_range_le2e5')
report((P > 100) & (P <= 30000), 'Z0900_range_le3e4')
report((P > 200000) & (P <= 2000000), 'out_of_sample_2e5_2e6')
if (P > 5e6).any(): report(P > 5e6, 'out_of_sample_5e6_1e7')
report((P > 100) & (P <= 200000), 'pass1_range_le2e5_PRIMEPRODUCT_variant', lF=lF_prime)
json.dump(out, open('data/z52c/rh/regress.json', 'w'), indent=1)
