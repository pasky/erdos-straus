"""z56 PRIMET1 Amendment 5, battery A6 (null 𝓛⁺⁺⁺ = 𝓛⁺⁺ + exact genus-field L-values); derived from Amendment 2, battery A5 (Z56_PRIMET1.md §3.9): beyond-local tests with the null 𝓛⁺⁺.
Usage: python z56_primet1_amend3.py PRED.npy FEAT.npy FEAT2.npy CF4.txt OUTPREFIX [--label h3p]
Continuous: OLS F-test of r on [𝓛⁺⁺, X_G] vs [𝓛⁺⁺] (Gram accumulated in chunks, rank-deficiency by eigen-pseudo-inverse).
Tail: logistic score test with the compact null 𝓛⁺ + f_{-1} + log L_Q0(1, chi_{-4}chi_p) (+square) + log(a1)/L.
G16 tests add tau3(p+1), log(1+tau3(p+1)) to both nulls.
"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design, primes_upto, legendre_table
from z56_primet1_tests import families, holm
from z56_primet1_amend import tau3_p1, extra_known, lstsq_rss, logit_fit, score_test

MIDQ = [int(q) for q in primes_upto(997) if q >= 53]

def LQ_imag(p, Q0=1000):
    """L_{Q0}(1, chi_{-4} chi_p) truncated Euler product (chi_{-4}chi_p(2) = 0)."""
    lg = np.zeros(len(p))
    for q in primes_upto(Q0):
        q = int(q)
        if q == 2: continue
        t = legendre_table(q); c = t[(p % np.uint64(q)).astype(np.int64)].astype(float) * (1 if q % 4 == 1 else -1)
        lg -= np.log1p(-c / q)
    return lg

def mid_local(p):
    cols = []
    for q in MIDQ:
        t = legendre_table(q); r = (p % np.uint64(q)).astype(np.int64)
        cols += [t[r].astype(float), (r == 1).astype(float), (r == q - 1).astype(float)]
    return np.column_stack(cols)

def fm1(p):
    f = np.zeros(len(p))
    for q in MIDQ: f += np.where(p % np.uint64(q) == np.uint64(q - 1), math.log(q) / q, 0.0)
    return f

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pred'); ap.add_argument('feat'); ap.add_argument('feat2'); ap.add_argument('cf'); ap.add_argument('out')
    ap.add_argument('--label', default='h2'); ap.add_argument('--hard', type=float, default=0.01)
    a = ap.parse_args()
    pred = np.load(a.pred); feat = np.load(a.feat)
    fi = {int(x): i for i, x in enumerate(feat['p'])}; feat = feat[np.array([fi[int(x)] for x in pred['p']])]
    f2 = np.load(a.feat2); fi2 = {int(x): i for i, x in enumerate(f2['p'])}; f2 = f2[np.array([fi2[int(x)] for x in pred['p']])]
    cf = np.loadtxt(a.cf, dtype=np.int64); cfd = {int(r[0]): r[1:] for r in cf}
    cfa = np.array([cfd[int(x)] for x in pred['p']], dtype=np.float64)
    p = pred['p'].astype(np.uint64); n = len(p); pf = p.astype(float); L = np.log(pf)
    r = pred['resid']; hard = (pred['pit'] < a.hard).astype(np.float64); mu = pred['mu']
    F = families(feat, cfa[:, 0])
    lqi = LQ_imag(p)
    lex_i = np.log(math.pi * feat['h4'] / (2 * np.sqrt(pf)))
    F['G1p'] = ((lex_i - lqi)[:, None], ["log L(1,chi_-4p) - log L_Q0"])
    F['G17p'] = ((np.log(np.maximum(cfa[:, 2], 1)) / L)[:, None], ['Gamma'])
    la1 = np.log(cfa[:, 1]) / L
    t3 = tau3_p1(p); TK = np.column_stack([t3.astype(float), np.log1p(t3)])
    sq8 = np.sqrt(8 * pf)
    ell = [np.log(2 * feat['hR'] * feat['reg'] / np.sqrt(pf)), lex_i, np.log(2 * f2['h8'] * f2['reg8'] / sq8),
           np.log(math.pi * f2['hm8'] / sq8)]
    Lc = ell + [x * x for x in ell] + [ell[i] * ell[j] for i in range(4) for j in range(i + 1, 4)]
    comp = np.column_stack([fm1(p), lqi, lqi**2, la1] + Lc)   # compact extras (tail null) incl. the 14 L-value columns
    print('features done', file=sys.stderr, flush=True)
    des = Design(1000)
    fams = ['G2', 'G3', 'G4', 'G6', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17p']
    Xf = []; Gidx = {}; off = 0
    for g in fams:
        X = F[g][0]; X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
        Gidx[g] = list(range(off, off + X.shape[1])); off += X.shape[1]; Xf.append(X)
    Gidx['T3'] = [off, off + 1]; Xf.append(TK); XG = np.column_stack(Xf)
    # continuous: Gram over [L+ (406) | mid_local (477) | comp (4) | XG]
    ch = 50000; G = None; c = None; rr = float(r @ r)
    for s in range(0, n, ch):
        ps = p[s:s + ch]
        Z = np.column_stack([des.build(ps), extra_known(ps, feat[s:s + ch], des), mid_local(ps), comp[s:s + ch], XG[s:s + ch]])
        if G is None: G = np.zeros((Z.shape[1], Z.shape[1])); c = np.zeros(Z.shape[1]); kN0 = Z.shape[1] - XG.shape[1]
        G += Z.T @ Z; c += Z.T @ r[s:s + ch]
    print('gram done, null cols', kN0, file=sys.stderr, flush=True)
    null = list(range(kN0)); rows = []; eff = []
    scale = float(np.mean(np.sqrt(1 / mu + 1 / 58.5)))
    for g in fams:
        nidx = null + ([kN0 + i for i in Gidx['T3']] if g == 'G16' else [])
        gidx = [kN0 + i for i in Gidx[g]]
        r0, k0, _ = lstsq_rss(G, c, rr, nidx); r1, k1, b = lstsq_rss(G, c, rr, nidx + gidx)
        df1 = k1 - k0; df2 = n - k1; Fs = ((r0 - r1) / max(df1, 1)) / (r1 / df2)
        rows.append(('A6', g, 'cont|L+++', df1, Fs, stats.f.sf(Fs, max(df1, 1), df2)))
        for j, nm in enumerate(F[g][1]): eff.append((g, nm, b[len(nidx) + j], b[len(nidx) + j] * scale))
    del G
    print('OLS rows', rows, file=sys.stderr, flush=True)
    with open(a.out + '_A6_effects.tsv', 'w') as f:
        f.write('family\tfeature\tbeta_r_per_sd\tapprox_rel_effect_on_E[Y]_per_sd\n')
        for e in eff: f.write('%s\t%s\t%+.5f\t%+.5f\n' % e)
    # tail: compact null
    XN = None
    for s in range(0, n, 100000):
        ps = p[s:s + 100000]
        blk = np.column_stack([des.build(ps), extra_known(ps, feat[s:s + 100000], des), comp[s:s + 100000]]).astype(np.float32)
        if XN is None: XN = np.empty((n, blk.shape[1]), np.float32)
        XN[s:s + len(ps)] = blk; del blk
    bN = logit_fit(XN, hard)
    for g in fams:
        if g == 'G16': continue
        S, pv, df = score_test(XN, XG[:, Gidx[g]], hard, bN); rows.append(('A6', g, 'tail|L+c', df, S, pv))
    b3 = logit_fit(XN, hard, TK); S, pv, df = score_test(XN, XG[:, Gidx['G16']], hard, b3, TK)
    rows.append(('A6', 'G16', 'tail|L+c,tau3', df, S, pv))
    adj = holm([x[5] for x in rows])
    with open(a.out + '_A6.tsv', 'w') as f:
        f.write(f'# label={a.label} n={n} hard={int(hard.sum())} cont-null cols={kN0}\nblock\tfamily\ttest\tdf\tstat\tp_raw\tp_holm\n')
        for row, pa in zip(rows, adj): f.write('%s\t%s\t%s\t%d\t%.4f\t%.3e\t%.3e\n' % (row + (pa,)))
    with open(a.out + '_A6_effects.tsv', 'w') as f:
        f.write('family\tfeature\tbeta_r_per_sd\tapprox_rel_effect_on_E[Y]_per_sd\n')
        for e in eff: f.write('%s\t%s\t%+.5f\t%+.5f\n' % e)
    print(open(a.out + '_A6.tsv').read())
