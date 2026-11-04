"""z56 PRIMET1 post-review robustness (§6): heteroskedasticity-robust LM (score) tests of invariant families against the
complete known-model null, with exact residualisation (Frisch–Waugh) in two passes; saves the null residual for the
S4b-style nonlinear omnibus (z56_primet1_s4r.py).

Null (always): 𝓛 design (325) + exact tau, tau^2 + one-hots p mod 64, 27, 25, 49 + per-q (q/p), 1[p ≡ ±1 (q)] for
53 <= q <= 997 + f_{-1}, log L_Q0(1, chi_{-4}chi_p) (+square), log(a1)/L + the 14 exact genus-field L-value columns
(ell_d, d in {1,-4,8,-8}; squares; pairwise products) [= 𝓛⁺⁺⁺ of Amendment 5]
  --a9: additionally mu/s, f1+, f-1+ (1000 < q <= 20000), log of the 1000-smooth parts of p ∓ 1 over L [A9 null].
Outcome: Pearson residual r (default) or, with --tau3, z' = (Y - tau3(p+1))/s(mu).
Tests per family J: classical F (from the Gram) and robust LM = (Σ x̃ ẽ)' (Σ ẽ² x̃ x̃')^{-1} (Σ x̃ ẽ) ~ chi2(rank),
x̃, ẽ = residuals of X_J and of the outcome on the null. Rank via eigenvalues relative to the PARENT information
(tolerance 1e-9 of max diag of the residualised block, absolute floor 1e-6·n), so null-contained features give df 0.
Usage: python z56_primet1_robust.py PRED FEAT FEAT2 CF4 MODEL OUT [--tau3] [--a9] [--exclude P.npy] [--fams ...]
"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design, primes_upto
from z56_primet1_tests import families, holm
from z56_primet1_amend import extra_known
from z56_primet1_amend2 import mid_local, LQ_imag, fm1
from z56_primet1_g16c import feats as pm1feats

def pinv_sym(A, rel=1e-11):
    sc = np.sqrt(np.maximum(np.diag(A), 1e-300)); An = A / np.outer(sc, sc)
    w, V = np.linalg.eigh(An); keep = w > w.max() * rel
    return (V[:, keep] / w[keep]) @ V[:, keep].T / np.outer(sc, sc)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    for x in ('pred', 'feat', 'feat2', 'cf', 'model', 'out'): ap.add_argument(x)
    ap.add_argument('--tau3', action='store_true'); ap.add_argument('--a9', action='store_true')
    ap.add_argument('--exclude'); ap.add_argument('--fams', default='G2,G3,G4,G6,G8,G9,G10,G11,G12,G13,G15,G16,G17p,PM1,PP1')
    ap.add_argument('--label', default='')
    a = ap.parse_args()
    pred = np.load(a.pred)
    if a.exclude:
        ex = set(np.load(a.exclude).tolist()); keep = np.array([int(x) not in ex for x in pred['p']]); pred = pred[keep]
        print('excluded', int((~keep).sum()), file=sys.stderr)
    def align(arr):
        fi = {int(x): i for i, x in enumerate(arr['p'])}; return arr[np.array([fi[int(x)] for x in pred['p']])]
    feat = align(np.load(a.feat)); f2 = align(np.load(a.feat2))
    cf = np.loadtxt(a.cf, dtype=np.int64); cfd = {int(r[0]): r[1:] for r in cf}
    cfa = np.array([cfd[int(x)] for x in pred['p']], dtype=np.float64)
    K = float(np.load(a.model)['k'])
    p = pred['p'].astype(np.uint64); n = len(p); pf = p.astype(float); L = np.log(pf); mu = pred['mu']; Y = pred['R'] / 2.0
    s = np.sqrt(mu + mu * mu / K)
    pm = pm1feats(p)   # tau3(p+1), om<=1000(p-1), om>1000(p-1), log rough(p-1), om<=(p+1), om>(p+1), log rough(p+1), logP+(p-1), logP+(p+1)
    y = (Y - pm[:, 0]) / s if a.tau3 else pred['resid']
    F = families(feat, cfa[:, 0])
    F['G17p'] = ((np.log(np.maximum(cfa[:, 2], 1)) / L)[:, None], ['Gamma'])
    F['PM1'] = (np.column_stack([pm[:, 2], pm[:, 7] / L]), ['omega>1000(p-1)', 'logP+(p-1)/L'])
    F['PP1'] = (np.column_stack([pm[:, 5], pm[:, 8] / L]), ['omega>1000(p+1)', 'logP+(p+1)/L'])
    lqi = LQ_imag(p); sq = np.sqrt(pf); sq8 = np.sqrt(8 * pf)
    ell = [np.log(2 * feat['hR'] * feat['reg'] / sq), np.log(math.pi * feat['h4'] / (2 * sq)),
           np.log(2 * f2['h8'] * f2['reg8'] / sq8), np.log(math.pi * f2['hm8'] / sq8)]
    Lc = ell + [x * x for x in ell] + [ell[i] * ell[j] for i in range(4) for j in range(i + 1, 4)]
    comp = [fm1(p), lqi, lqi**2, np.log(cfa[:, 1]) / L] + Lc
    if a.a9:
        bigs = [int(q) for q in primes_upto(20000) if q > 1000]
        def agg(sign):
            g = np.zeros(n)
            for q in bigs: g += np.where(p % np.uint64(q) == (np.uint64(1) if sign > 0 else np.uint64(q - 1)), math.log(q) / q, 0.0)
            return g
        comp += [mu / s, agg(1), agg(-1), (np.log(pf - 1) - pm[:, 3]) / L, (np.log(pf + 1) - pm[:, 6]) / L]
    comp = np.column_stack(comp)
    fams = a.fams.split(',')
    Xl = []; J = {}; off = 0
    for g in fams:
        X = F[g][0]; X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
        J[g] = list(range(off, off + X.shape[1])); off += X.shape[1]; Xl.append(X)
    XG = np.column_stack(Xl); kX = XG.shape[1]
    des = Design(1000); ch = 50000
    def null_chunk(st):
        ps = p[st:st + ch]
        return np.column_stack([des.build(ps), extra_known(ps, feat[st:st + ch], des), mid_local(ps), comp[st:st + ch]])
    # pass 1: Gram
    GNN = GNX = cN = None; GXX = XG.T @ XG; cX = XG.T @ y
    for st in range(0, n, ch):
        N = null_chunk(st)
        if GNN is None: kN = N.shape[1]; GNN = np.zeros((kN, kN)); GNX = np.zeros((kN, kX)); cN = np.zeros(kN)
        GNN += N.T @ N; GNX += N.T @ XG[st:st + ch]; cN += N.T @ y[st:st + ch]
    Pinv = pinv_sym(GNN); B = Pinv @ GNX; b = Pinv @ cN
    print('pass1 done kN', kN, file=sys.stderr, flush=True)
    # pass 2: residualised x̃, ẽ; robust meat
    Sxe = np.zeros(kX); Meat = np.zeros((kX, kX)); Sxx = np.zeros((kX, kX)); E = np.empty(n, np.float32); ee = 0.0
    for st in range(0, n, ch):
        N = null_chunk(st); xt = XG[st:st + ch] - N @ B; et = y[st:st + ch] - N @ b
        E[st:st + ch] = et; ee += et @ et
        Sxe += xt.T @ et; Sxx += xt.T @ xt; Meat += (xt * (et * et)[:, None]).T @ xt
    np.save(a.out + '_nullresid.npy', np.rec.fromarrays([pred['p'], E], names='p,e'))
    rows = []
    sig2 = ee / (n - kN)
    for g in fams:
        j = J[g]; A = Sxx[np.ix_(j, j)]; d = np.diag(A)
        tol = max(1e-9 * max(d.max(), 1e-300), 1e-6 * n)
        w, V = np.linalg.eigh(A); kk = w > tol; df = int(kk.sum())
        if df == 0:
            rows.append((g, 0, float('nan'), float('nan'), float('nan'), float('nan'), 'not estimable (in null)')); continue
        Vk = V[:, kk]; u = Vk.T @ Sxe[j]; Ak = np.diag(w[kk]); Mk = Vk.T @ Meat[np.ix_(j, j)] @ Vk
        Fc = float(u @ np.linalg.solve(Ak, u)) / df / sig2
        LM = float(u @ np.linalg.solve(Mk, u))
        beta = Vk @ (u / w[kk])
        rows.append((g, df, Fc, stats.f.sf(Fc, df, n - kN - df), LM, stats.chi2.sf(LM, df), ' '.join(f'{x:+.5f}' for x in beta)))
    pc = holm([r[3] if r[1] else 1.0 for r in rows]); pr = holm([r[5] if r[1] else 1.0 for r in rows])
    with open(a.out + '_robust.tsv', 'w') as f:
        f.write(f"# {a.label} n={n} null cols={kN} outcome={'z_prime(tau3 removed)' if a.tau3 else 'Pearson r'} a9null={a.a9} mean(s/mu)={np.mean(s/mu):.3f}\n")
        f.write('family\tdf\tF_classical\tp_classical\tp_holm_cl\tLM_robust\tp_robust\tp_holm_rob\tcoef_z_per_sd\n')
        for r, h1, h2 in zip(rows, pc, pr):
            f.write('%s\t%d\t%.4f\t%.3e\t%.3e\t%.4f\t%.3e\t%.3e\t%s\n' % (r[0], r[1], r[2], r[3], h1, r[4], r[5], h2, r[6]))
    print(open(a.out + '_robust.tsv').read())
