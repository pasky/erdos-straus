"""z56 PRIMET1: invariant families G1–G16 (Z56_PRIMET1.md §3.3) and the primary tests P-cont / P-tail (§3.4).

Library: families(feat, cf, p) -> dict name -> (feature matrix, column names)
CLI:     python z56_primet1_tests.py PRED.npy FEAT.npy CFPER.txt OUTPREFIX [--hard 0.01] [--label C]
PRED: output of z56_primet1_local.py predict; FEAT: z56_primet1_feat.py; CFPER: "p len" lines (any order).
Writes OUTPREFIX_tests.tsv (one line per test) and OUTPREFIX_effects.tsv (per-column effect sizes).
"""
import sys, math, argparse
import numpy as np
from scipy import stats

FAMS = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16']

def v_adic(x, q):
    x = np.asarray(x, dtype=np.int64).copy(); v = np.zeros(len(x), np.int64)
    m = (x != 0)
    while True:
        d = m & (x % q == 0)
        if not d.any(): break
        v[d] += 1; x[d] //= q
    return v

def onehot(v, cats):
    # cats: list of (name, mask-function); the reference category is omitted by the caller
    return np.column_stack([c(v).astype(float) for _, c in cats]), [n for n, _ in cats]

def legendre_Q0_L(p, Q0=1000):
    from z56_primet1_local import Design
    des = Design(Q0=Q0)
    _, L1 = des.tau(np.asarray(p, dtype=np.uint64))
    return L1

def families(feat, cflen, Q0=1000):
    p = feat['p'].astype(np.uint64); pf = p.astype(np.float64); L = np.log(pf); sq = np.sqrt(pf)
    F = {}
    h4 = feat['h4'].astype(np.int64)
    F['G1'] = (np.log(h4 / sq)[:, None], ['log(h4/sqrt p)'])
    v2h = v_adic(h4, 2)
    F['G2'] = (np.column_stack([(v2h == 3), (v2h >= 4)]).astype(float), ['v2(h4)=3', 'v2(h4)>=4'])
    F['G3'] = (np.column_stack([(h4 % 3 == 0), (h4 % 5 == 0)]).astype(float), ['3|h4', '5|h4'])
    F['G4'] = ((feat['hR'] > 1).astype(float)[:, None], ['h(p)>1'])
    Lex = 2 * feat['hR'] * feat['reg'] / sq
    LQ = legendre_Q0_L(p, Q0)
    F['G5'] = ((np.log(Lex) - np.log(LQ))[:, None], ['logL1-logL1_Q0'])
    F['G6'] = (np.column_stack([np.log(feat['reg'] / sq), np.log(cflen / sq)]), ['log(reg/sqrt p)', 'log(cflen/sqrt p)'])
    F['G7'] = (np.log(feat['nqr'].astype(float))[:, None], ['log n(p)'])
    for g, col in (('G8', 'i2'), ('G9', 'i3')):
        i = feat[col].astype(np.int64); v = v_adic(i, 2)
        F[g] = (np.column_stack([(v == 2), (v >= 3), (i % 3 == 0), np.log(i.astype(float))]).astype(float),
                [f'v2({col})=2', f'v2({col})>=3', f'3|{col}', f'log {col}'])
    r3 = feat['r3']; F['G10'] = (np.column_stack([(r3 == 1), (r3 == 3)]).astype(float), ['r3=1', 'r3=3'])
    r4 = feat['r4']; F['G11'] = (np.column_stack([(r4 == 1), (r4 == 2), (r4 == 4)]).astype(float), ['r4=1', 'r4=2', 'r4=4'])
    th = np.arctan2(feat['gb'].astype(float), feat['ga'].astype(float))
    ps = np.arctan2(math.sqrt(3) * feat['ey'].astype(float), feat['ex'].astype(float))
    F['G12'] = (np.column_stack([np.cos(4 * th), np.cos(8 * th), np.cos(6 * ps), np.cos(12 * ps)]),
                ['cos4theta', 'cos8theta', 'cos6psi', 'cos12psi'])
    t = feat['ap11'] / (2 * sq)
    F['G13'] = (np.column_stack([t, 4 * t * t - 1]), ['t', '4t^2-1'])
    pm1 = (p - np.uint64(1))
    v2 = v_adic((pm1 // np.uint64(8)).astype(np.int64), 2) + 3
    F['G14'] = (np.column_stack([(v2 == 5), (v2 >= 6), (pm1 % np.uint64(27) == 0), (pm1 % np.uint64(25) == 0),
                                 (pm1 % np.uint64(49) == 0)]).astype(float),
                ['v2(p-1)=5', 'v2(p-1)>=6', '27|p-1', '25|p-1', '49|p-1'])
    m = feat['legmask']
    F['G15'] = (np.column_stack([np.where((m >> j) & 1, 1.0, -1.0) for j in range(10)]),
                [f'leg{q}' for q in [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]])
    F['G16'] = (np.column_stack([np.log(feat['Pm'].astype(float)) / L, feat['wm'].astype(float),
                                 np.log(feat['Pp'].astype(float)) / L, feat['wp'].astype(float)]),
                ['logP+(p-1)/L', 'omega(p-1)', 'logP+(p+1)/L', 'omega(p+1)'])
    return F

def scalar_summary(F):
    """Pre-registered per-family scalar for S3 (§3.5)."""
    s = {}
    s['G1'] = F['G1'][0][:, 0]
    s['G2'] = None  # v2(h4) itself, filled by caller from h4
    return s

def ols_F(y, X0, X1):
    def rss(X):
        b = np.linalg.solve(X.T @ X, X.T @ y); e = y - X @ b; return e @ e
    r0, r1 = rss(X0), rss(np.column_stack([X0, X1]))
    df1 = X1.shape[1]; df2 = len(y) - X0.shape[1] - df1
    Fst = ((r0 - r1) / df1) / (r1 / df2)
    return Fst, stats.f.sf(Fst, df1, df2), df1

def logit_LR(h, X1):
    import statsmodels.api as sm
    X = sm.add_constant(X1, has_constant='add')
    m1 = sm.Logit(h, X).fit(disp=0, method='newton', maxiter=100)
    p0 = h.mean(); ll0 = np.sum(h * np.log(p0) + (1 - h) * np.log(1 - p0))
    LR = 2 * (m1.llf - ll0)
    return LR, stats.chi2.sf(LR, X1.shape[1]), m1

def effects_poisson(y, mu, L, X1, iters=30):
    """Quasi-Poisson GLM, log link, offset log mu; returns coefficients of X1 and quasi-SEs (Pearson scale)."""
    X = np.column_stack([np.ones(len(y)), np.log(L), X1]); off = np.log(mu)
    b = np.zeros(X.shape[1])
    for _ in range(iters):
        eta = off + X @ b; m = np.exp(eta)
        A = (X * m[:, None]).T @ X; g = X.T @ (y - m)
        step = np.linalg.solve(A, g); b = b + step
        if np.max(np.abs(step)) < 1e-10: break
    m = np.exp(off + X @ b); A = (X * m[:, None]).T @ X
    phi = np.sum((y - m)**2 / m) / (len(y) - X.shape[1])
    se = np.sqrt(np.diag(np.linalg.inv(A)) * phi)
    return b[2:], se[2:]

def holm(pvals):
    pv = np.asarray(pvals); order = np.argsort(pv); m = len(pv); adj = np.empty(m)
    run = 0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (m - rank) * pv[i])); adj[i] = run
    return adj

def load_aligned(pred, feat, cfpath):
    cf = np.loadtxt(cfpath, dtype=np.int64)
    cfd = dict(zip(cf[:, 0].tolist(), cf[:, 1].tolist())) if cf.ndim == 2 else {}
    fi = {int(x): i for i, x in enumerate(feat['p'])}
    idx = np.array([fi[int(x)] for x in pred['p']])
    feat = feat[idx]
    cflen = np.array([cfd[int(x)] for x in pred['p']], dtype=float)
    return pred, feat, cflen

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pred'); ap.add_argument('feat'); ap.add_argument('cf'); ap.add_argument('out')
    ap.add_argument('--hard', type=float, default=0.01); ap.add_argument('--label', default='C')
    ap.add_argument('--fams', default=','.join(FAMS)); ap.add_argument('--notail', action='store_true')
    ap.add_argument('--nulllogmu', action='store_true', help='S1: add log mu to the OLS null (recalibration)')
    a = ap.parse_args()
    sys.path.insert(0, __file__.rsplit('/', 1)[0])
    pred = np.load(a.pred); feat = np.load(a.feat)
    pred, feat, cflen = load_aligned(pred, feat, a.cf)
    F = families(feat, cflen)
    y = pred['R'] / 2.0; mu = pred['mu']; r = pred['resid']; L = np.log(pred['p'].astype(float))
    hard = (pred['pit'] < a.hard).astype(float)
    X0 = np.column_stack([np.ones(len(r)), np.log(L)] + ([np.log(mu)] if a.nulllogmu else []))
    rows = []; effrows = []
    for g in a.fams.split(','):
        X, names = F[g]
        ok = np.all(np.isfinite(X), axis=1)
        Xs = (X - X[ok].mean(0)) / np.where(X[ok].std(0) > 0, X[ok].std(0), 1)
        Fst, pc, df = ols_F(r[ok], X0[ok], Xs[ok])
        rows.append((g, 'P-cont', df, Fst, pc, int(ok.sum())))
        if not a.notail:
            LR, pt, m1 = logit_LR(hard[ok], Xs[ok])
            rows.append((g, 'P-tail', df, LR, pt, int(hard[ok].sum())))
            ors = np.exp(m1.params[1:])
        else:
            ors = [np.nan] * len(names)
        b, se = effects_poisson(y[ok], mu[ok], L[ok], Xs[ok])
        for j, nm in enumerate(names):
            effrows.append((g, nm, X[ok][:, j].mean(), X[ok][:, j].std(), b[j], se[j], ors[j]))
    adj = holm([x[4] for x in rows])
    with open(a.out + '_tests.tsv', 'w') as f:
        f.write(f'# label={a.label} n={len(r)} hard(pit<{a.hard})={int(hard.sum())}\n')
        f.write('family\ttest\tdf\tstat\tp_raw\tp_holm\tn_or_nhard\n')
        for (g, t, df, st, pv, nn), pa in zip(rows, adj):
            f.write(f'{g}\t{t}\t{df}\t{st:.4f}\t{pv:.3e}\t{pa:.3e}\t{nn}\n')
    with open(a.out + '_effects.tsv', 'w') as f:
        f.write('family\tfeature\tmean\tsd\tbeta_per_sd(logE[Y])\tse\ttail_OR_per_sd\n')
        for row in effrows:
            f.write('%s\t%s\t%.4g\t%.4g\t%+.5f\t%.5f\t%.4f\n' % row)
    print(open(a.out + '_tests.tsv').read())
