"""z56 PRIMET1 Amendment 1 (Z56_PRIMET1.md §3.9): tests of G1–G17 with the extended known-model null 𝓛⁺, on one split.

Usage: python z56_primet1_amend.py PRED.npy FEAT.npy CF4.txt OUTPREFIX [--label h2] [--blocks A1,A2,A3,A4]
PRED from z56_primet1_local.py predict (D-fitted 𝓛); FEAT from z56_primet1_feat.py; CF4 = cfper output "p len a1 amax".
Null design 𝓛⁺ = 𝓛 design + exact tau (and tau^2) + one-hot p mod 64, 27, 25, 49 (rank deficiency handled by lstsq).
OLS F-tests on the Pearson residual r; logistic score tests on 1[hard] (hard = mid-PIT < 0.01 under 𝓛).
"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design
from z56_primet1_tests import families, holm, FAMS

def tau3_p1(ps):
    """tau_3(p+1) = #{m | p+1 : m ≡ 3 (mod 4)} via PARI factorisation."""
    import cypari2
    pari = cypari2.Pari(); out = np.zeros(len(ps), np.int64)
    for i, p in enumerate(ps):
        f = pari.factor(int(p) + 1); tau = 1; s = 1
        for q, e in zip(f[0], f[1]):
            q = int(q); e = int(e)
            if q == 2: continue
            tau *= e + 1
            s *= (e + 1) if q % 4 == 1 else (1 if e % 2 == 0 else 0)
        out[i] = (tau - s) // 2
    return out

def extra_known(p, feat, des):
    """exact tau, tau^2, and one-hots p mod 64, 27, 25, 49 (all classes; collinearity allowed)."""
    pf = p.astype(np.float64); L = np.log(pf)
    tq, LQ = des.tau(p)
    Lex = 2 * feat['hR'] * feat['reg'] / np.sqrt(pf)
    tex = tq * (Lex / LQ)**2 / L**2
    cols = [tex, tex * tex]
    for q in (64, 27, 25, 49):
        r = (p % np.uint64(q)).astype(np.int64)
        for c in np.unique(r):
            cols.append((r == c).astype(np.float64))
    return np.column_stack(cols)

def lstsq_rss(G, c, rr, idx):
    Gs = G[np.ix_(idx, idx)]; cs = c[idx]
    sc = np.sqrt(np.maximum(np.diag(Gs), 1e-300)); Gn = Gs / np.outer(sc, sc); cn = cs / sc
    w, V = np.linalg.eigh(Gn); keep = w > w.max() * 1e-11
    b = V[:, keep] @ ((V[:, keep].T @ cn) / w[keep])
    return rr - cn @ b, int(keep.sum()), b / sc

def chunkX(X, E, s, ch):
    Xc = X[s:s + ch].astype(np.float64)
    return Xc if E is None else np.column_stack([Xc, E[s:s + ch]])

def logit_fit(X, h, E=None, iters=30):
    """IRLS logistic with rank-deficient [X, E] (X float32 storage, float64 accumulation)."""
    n = X.shape[0]; k = X.shape[1] + (0 if E is None else E.shape[1]); b = np.zeros(k); ch = 50000
    for it in range(iters):
        A = np.zeros((k, k)); g = np.zeros(k)
        for s in range(0, n, ch):
            Xc = chunkX(X, E, s, ch); eta = Xc @ b; pr = 1 / (1 + np.exp(-eta)); w = pr * (1 - pr)
            A += (Xc * w[:, None]).T @ Xc; g += Xc.T @ (h[s:s + ch] - pr)
        sc = np.sqrt(np.maximum(np.diag(A), 1e-300)); An = A / np.outer(sc, sc)
        wv, V = np.linalg.eigh(An); keep = wv > wv.max() * 1e-11
        step = (V[:, keep] @ ((V[:, keep].T @ (g / sc)) / wv[keep])) / sc
        b += step
        if np.max(np.abs(step)) < 1e-8: break
    return b

def score_test(XN, XG, h, b, E=None):
    n = len(h); ch = 50000; kN = XN.shape[1] + (0 if E is None else E.shape[1]); kG = XG.shape[1]
    ANN = np.zeros((kN, kN)); ANG = np.zeros((kN, kG)); AGG = np.zeros((kG, kG)); U = np.zeros(kG)
    for s in range(0, n, ch):
        Xn = chunkX(XN, E, s, ch); Xg = XG[s:s + ch]
        pr = 1 / (1 + np.exp(-(Xn @ b))); w = pr * (1 - pr)
        ANN += (Xn * w[:, None]).T @ Xn; ANG += (Xn * w[:, None]).T @ Xg; AGG += (Xg * w[:, None]).T @ Xg
        U += Xg.T @ (h[s:s + ch] - pr)
    sc = np.sqrt(np.maximum(np.diag(ANN), 1e-300)); An = ANN / np.outer(sc, sc)
    wv, V = np.linalg.eigh(An); keep = wv > wv.max() * 1e-11
    Ainv = (V[:, keep] / wv[keep]) @ V[:, keep].T / np.outer(sc, sc)
    I = AGG - ANG.T @ Ainv @ ANG
    wi, Vi = np.linalg.eigh(I); kk = wi > wi.max() * 1e-10
    S = float(((Vi[:, kk].T @ U)**2 / wi[kk]).sum())
    return S, stats.chi2.sf(S, int(kk.sum())), int(kk.sum())

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pred'); ap.add_argument('feat'); ap.add_argument('cf'); ap.add_argument('out')
    ap.add_argument('--label', default='h2'); ap.add_argument('--hard', type=float, default=0.01)
    a = ap.parse_args()
    pred = np.load(a.pred); feat = np.load(a.feat)
    fi = {int(x): i for i, x in enumerate(feat['p'])}; feat = feat[np.array([fi[int(x)] for x in pred['p']])]
    cf = np.loadtxt(a.cf, dtype=np.int64); cfd = {int(r[0]): r[1:] for r in cf}
    cfa = np.array([cfd[int(x)] for x in pred['p']], dtype=np.float64)
    p = pred['p'].astype(np.uint64); n = len(p); L = np.log(p.astype(np.float64))
    r = pred['resid']; hard = (pred['pit'] < a.hard).astype(np.float64); mu = pred['mu']
    print('n', n, 'hard', int(hard.sum()), file=sys.stderr, flush=True)
    F = families(feat, cfa[:, 0])
    F['G17'] = (np.column_stack([np.log(np.maximum(cfa[:, 2], 1)) / L, np.log(cfa[:, 1]) / L]), ['Gamma', 'log(a1)/L'])
    t3 = tau3_p1(p); TK = np.column_stack([t3.astype(float), np.log1p(t3)])
    print('t3 done', file=sys.stderr, flush=True)
    des = Design(1000)
    # null design (float32), built in chunks
    blocks = []
    for s in range(0, n, 200000):
        blocks.append(np.column_stack([des.build(p[s:s + 200000]), extra_known(p[s:s + 200000], feat[s:s + 200000], des)]).astype(np.float32))
    XN = np.concatenate(blocks); del blocks
    kN = XN.shape[1]; print('null cols', kN, file=sys.stderr, flush=True)
    fams = FAMS + ['G17']
    Gcols = []; Gidx = {}
    for g in fams:
        X = F[g][0]; X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
        Gidx[g] = list(range(kN + sum(c.shape[1] for c in Gcols), kN + sum(c.shape[1] for c in Gcols) + X.shape[1])); Gcols.append(X)
    T0 = kN + sum(c.shape[1] for c in Gcols); Gidx['T3'] = [T0, T0 + 1]; Gcols.append(TK)
    XG = np.column_stack(Gcols)
    # Gram for OLS
    k = kN + XG.shape[1]; G = np.zeros((k, k)); c = np.zeros(k); rr = float(r @ r)
    for s in range(0, n, 200000):
        Z = np.column_stack([XN[s:s + 200000].astype(np.float64), XG[s:s + 200000]])
        G += Z.T @ Z; c += Z.T @ r[s:s + 200000]
    nullidx = list(range(kN))
    rows = []; eff = []
    scale = float(np.mean(np.sqrt(1 / mu + 1 / 58.5)))
    def ols(name, nidx, gidx):
        r0, k0, _ = lstsq_rss(G, c, rr, nidx); r1, k1, b = lstsq_rss(G, c, rr, nidx + gidx)
        df1 = k1 - k0; df2 = n - k1; Fs = ((r0 - r1) / max(df1, 1)) / (r1 / df2)
        return Fs, stats.f.sf(Fs, max(df1, 1), df2), df1, b[len(nidx):]
    for g in fams:
        Fs, pv, df, b = ols(g, nullidx, Gidx[g]); rows.append(('A1' if g != 'G17' else 'A3', g, 'cont|L+', df, Fs, pv))
        for j, nm in enumerate(F[g][1]): eff.append((g, nm, b[j], b[j] * scale))
    Fs, pv, df, _ = ols('G6|G17', nullidx + Gidx['G17'], Gidx['G6']); rows.append(('A3', 'G6', 'cont|L+,G17', df, Fs, pv))
    Fs, pv, df, _ = ols('G16|T3', nullidx + Gidx['T3'], Gidx['G16']); rows.append(('A4', 'G16', 'cont|L+,tau3', df, Fs, pv))
    del G
    print('OLS rows', rows, file=sys.stderr, flush=True)
    # logistic: null fits
    print('logit null', file=sys.stderr, flush=True)
    bN = logit_fit(XN, hard)
    for g in fams:
        S, pv, df = score_test(XN, XG[:, [i - kN for i in Gidx[g]]], hard, bN)
        rows.append(('A2' if g != 'G17' else 'A3', g, 'tail|L+', df, S, pv))
    E2 = XG[:, [i - kN for i in Gidx['G17']]]
    b2 = logit_fit(XN, hard, E2); S, pv, df = score_test(XN, XG[:, [i - kN for i in Gidx['G6']]], hard, b2, E2)
    rows.append(('A3', 'G6', 'tail|L+,G17', df, S, pv))
    b3 = logit_fit(XN, hard, TK); S, pv, df = score_test(XN, XG[:, [i - kN for i in Gidx['G16']]], hard, b3, TK)
    rows.append(('A4', 'G16', 'tail|L+,tau3', df, S, pv))
    adj = holm([x[5] for x in rows])
    with open(a.out + '_amend.tsv', 'w') as f:
        f.write(f'# label={a.label} n={n} hard={int(hard.sum())} nullcols={kN}\nblock\tfamily\ttest\tdf\tstat\tp_raw\tp_holm\n')
        for row, pa in zip(rows, adj): f.write('%s\t%s\t%s\t%d\t%.4f\t%.3e\t%.3e\n' % (row + (pa,)))
    with open(a.out + '_amend_effects.tsv', 'w') as f:
        f.write('family\tfeature\tbeta_r_per_sd\tapprox_rel_effect_on_E[Y]_per_sd\n')
        for e in eff: f.write('%s\t%s\t%+.5f\t%+.5f\n' % e)
    print(open(a.out + '_amend.tsv').read())
