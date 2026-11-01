"""Z52D_HYPERBOLA.md §5 — falsifier statistics for cluster C1 (FRONTIER §7.1).
Inputs: TSVs from scripts/z52d_hyperbola_falsifier.c (columns p Nbal T MQ Nint Su SC R), the block / interior class-blind
densities M0 (scripts/z52d_hyperbola_m0.c, z52d_hyperbola_m0int.c), RESIDUE_HARDNESS model tables (data/z52c/rh/model_tables.json).
Output: data/z52d/hyperbola/falsifier_stats.json (+ printed summary).
Usage: uv run --with numpy --with scipy python scripts/z52d_hyperbola_analyze.py [dir]   (default data/z52d/hyperbola, reads out_<w>.tsv[.gz])"""
import sys, json, numpy as np
from scipy.stats import poisson, chi2
D = sys.argv[1] if len(sys.argv) > 1 else 'data/z52d/hyperbola'
MT = json.load(open('data/z52c/rh/model_tables.json')); REF = '1e6'
COMP = [(840, 1), (16, 1), (8, -1), (11, 1), (13, 1)]


def logF(P, fam='S'):
    """RESIDUE_HARDNESS log F_fam(p) (raw model factor, 1/L-rescaled; same construction as scripts/z52c_rh_hard.py lfac).
    Defined for p = 1 (mod 4) only."""
    P = np.asarray(P, dtype=np.int64); L0 = MT[REF]['L']; L = np.log(P.astype(float)); lf = np.zeros(len(P))
    for Q, sgn in COMP:
        d = MT[REF][str(Q)]; fac = dict(zip(d['classes'], d[fam]['model']))
        lf += sgn*np.log(1 + (np.array([fac[int(x)] for x in P % Q]) - 1)*L0/L)
    return lf


def load(fn):
    import gzip, os
    op = (lambda f: gzip.open(f, 'rt')) if not os.path.exists(fn) and os.path.exists(fn + '.gz') else open
    if op is not open: fn = fn + '.gz'
    rows = [l.split() for l in op(fn) if len(l.split()) == 8 and len(l.split()[0]) <= 19]  # complete lines only
    d = {k: np.array([float(r[i]) for r in rows]) for i, k in enumerate(['p', 'Nbal', 'T', 'MQ', 'Nint', 'Su', 'SC', 'R']) if i}
    d['p'] = np.array([int(r[0]) for r in rows], dtype=np.int64)           # exact (p up to 1e18 > 2^53)
    return d


def gof_swap(N, M):
    """chi^2 of N/2 against Poisson(M/2) (swap-Poisson) and of N against Poisson(M), bins 0,1,2,>=3 (in units of the variable)."""
    out = {}
    for name, X, lam in [('swapPoisson(N/2~Poi(M/2))', N/2, M/2), ('Poisson(N~Poi(M))', N, M)]:
        obs = np.array([(X == 0).sum(), (X == 1).sum(), (X == 2).sum(), (X >= 3).sum()], float)
        pr = np.array([poisson.pmf(0, lam), poisson.pmf(1, lam), poisson.pmf(2, lam), poisson.sf(2, lam)])
        exp = pr*len(X); m = exp > 1e-9
        c2 = float((((obs - exp)**2)/np.where(m, exp, 1))[m].sum()); df = int(m.sum()) - 1
        out[name] = dict(obs=obs.tolist(), exp=[round(float(e), 2) for e in exp], chi2=round(c2, 2), df=df, pval=float(chi2.sf(c2, df)))
    return out


def corr_t(x, y):
    r = float(np.corrcoef(x, y)[0, 1]); n = len(x); t = r*np.sqrt((n - 2)/(1 - r*r)); return dict(r=round(r, 4), t=round(float(t), 2), n=n)


def class_means(P, Y, M, qs=(3, 5, 7, 8, 16)):
    """mean of Y/M over p in each unit class mod q (p = 1 mod 4 only), with z-score of the deviation from the overall mean."""
    out = {}
    sel = (P % 4 == 1); P, Y = P[sel], Y[sel]; mu = Y.mean(); sd = Y.std()
    for q in qs:
        rows = []
        for r in range(q):
            s = (P % q == r)
            if s.sum() < 30: continue
            m = Y[s].mean(); rows.append((r, int(s.sum()), round(float(m/mu), 4), round(float((m - mu)/(sd/np.sqrt(s.sum()))), 2)))
        chi = sum(z*z for *_, z in rows); out[str(q)] = dict(rows=rows, chi2_flat=round(chi, 2), df=len(rows) - 1, pval=float(chi2.sf(chi, len(rows) - 1)))
    # Mordell squares mod 840 (class 1 and the six squares) vs the other classes
    s1 = (P % 840 == 1); sq = np.isin(P % 840, [1, 121, 169, 289, 361, 529])
    out['840'] = dict(class1=(int(s1.sum()), round(float(Y[s1].mean()/mu), 4), round(float((Y[s1].mean() - mu)/(sd/np.sqrt(s1.sum()))), 2)),
                      mordell_sq=(int(sq.sum()), round(float(Y[sq].mean()/mu), 4), round(float((Y[sq].mean() - mu)/(sd/np.sqrt(sq.sum()))), 2)))
    return out


M0BLK = {100: 0.14513321, 1000: 0.14594093, 10000: 0.14603095, 31622: 0.14603641}
M0INT = {'1e8': 1.58707715, '1e12': 4.63513751}   # at window midpoints (p = 100184000, T0 = 100; p = 1000001380000, T0 = 1000)
WIN = [('1e8', 'out_1e8.tsv', 100), ('1e12', 'out_1e12.tsv', 1000), ('1e16', 'out_1e16.tsv', 10000), ('1e18', 'out_1e18.tsv', 31622)]
res = {}
for w, fn, U in WIN:
    try: X = load(f'{D}/{fn}')
    except OSError: continue
    x0 = float(w.replace('1e', '1e')); ok = (X['p'] >= x0) & (X['p'] <= 1.01*x0)        # drop malformed lines
    X = {k: v[ok] for k, v in X.items()}
    P = X['p'].astype(np.int64); N = X['Nbal']; M0 = M0BLK[U]; r = {}
    r['n_primes'] = int(len(P)); r['p_range'] = [int(P.min()), int(P.max())]; r['U'] = U
    se = N.std()/np.sqrt(len(N))
    r['balanced'] = dict(mean_N=round(float(N.mean()), 5), M0=M0, z_mean=round(float((N.mean() - M0)/se), 2), var=round(float(N.var()), 5),
                         var_over_mean=round(float(N.var()/N.mean()), 4), var_over_2M0=round(float(N.var()/(2*M0)), 4),
                         max_N=int(N.max()), hist={int(k): int((N == k).sum()) for k in np.unique(N)}, gof=gof_swap(N, M0),
                         gof_fitted_mean=gof_swap(N, float(N.mean())),
                         odd_N=int((N % 2 == 1).sum()))
    sel1 = (P % 4 == 1)
    if (X['MQ'] != 0).any():
        E = N - M0; MQ = X['MQ']; T = X['T']
        r['balanced']['MQ'] = dict(mean=round(float(MQ.mean()), 5), sd=round(float(MQ.std()), 5), corr_E_MQminusM0=corr_t(E, MQ - M0),
                                   mse_M0=round(float(((N - M0)**2).mean()), 5), mse_MQ=round(float(((N - MQ)**2).mean()), 5),
                                   loglik_swap_M0=round(float(poisson.logpmf(N/2, M0/2).sum()), 2),
                                   loglik_swap_MQ=round(float(poisson.logpmf(N/2, np.maximum(MQ, 1e-9)/2).sum()), 2))
        r['balanced']['BM'] = dict(T_mean=round(float(T.mean()), 6), T_sd=round(float(T.std()), 6), T_maxabs=round(float(np.abs(T).max()), 6),
                                   corr_E_minusT=corr_t(E, -T))
        lf = logF(P[sel1])
        r['balanced']['logF'] = dict(sd_logF=round(float(lf.std()), 4), corr_E_logF=corr_t(E[sel1], lf))
        r['balanced']['class_means'] = class_means(P, N, M0)
    if (X['Nint'] >= 0).any():
        Ni = X['Nint']; Mi = M0INT[w]; sei = Ni.std()/np.sqrt(len(Ni)); lf = logF(P[sel1])
        r['interior'] = dict(T0=U, mean=round(float(Ni.mean()), 4), M0_int=Mi, z_mean=round(float((Ni.mean() - Mi)/sei), 2),
                             var_over_mean=round(float(Ni.var()/Ni.mean()), 4), var_over_2M0=round(float(Ni.var()/(2*Mi)), 4),
                             odd=int((Ni % 2 == 1).sum()), corr_logF=corr_t(Ni[sel1], lf), class_means=class_means(P, Ni, Mi))
        for nm in ['Su', 'SC', 'R']:
            Y = X[nm]
            if (Y < 0).any(): continue
            r[nm] = dict(mean=round(float(Y.mean()), 4), var_over_mean=round(float(Y.var()/Y.mean()), 4), corr_logF=corr_t(Y[sel1], lf),
                         class_means=class_means(P, Y, Y.mean()))
        if (X['R'] >= 0).all():
            Bd = X['R'] - Ni
            r['boundary_R_minus_Nint'] = dict(mean=round(float(Bd.mean()), 4), corr_logF=corr_t(Bd[sel1], lf), class_means=class_means(P, Bd, Bd.mean()))
            # log-scale regression of RESIDUE_HARDNESS type: log(Y+1) ~ a + c log F
            for nm, Y in [('R', X['R']), ('Nint', Ni), ('boundary', Bd)]:
                A = np.column_stack([np.ones(sel1.sum()), lf]); y = np.log(Y[sel1] + 1)
                beta, *_ = np.linalg.lstsq(A, y, rcond=None); res_ = y - A@beta; s2 = res_.var()*len(y)/(len(y) - 2)
                cov = s2*np.linalg.inv(A.T@A)
                r.setdefault('loglin_fit_logY1_on_logF', {})[nm] = dict(c=round(float(beta[1]), 3), se=round(float(np.sqrt(cov[1, 1])), 3))
    res[w] = r
json.dump(res, open('data/z52d/hyperbola/falsifier_stats.json', 'w'), indent=1)
print(json.dumps(res, indent=1)[:20000])
