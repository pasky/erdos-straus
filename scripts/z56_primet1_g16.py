"""z56 PRIMET1 Amendment 6, test A7: is the residual p ± 1 signal (G16) the u = 1 ticket or larger-modulus local data?
Outcome z' = (Y - tau3(p+1))/s(mu), s = sqrt(mu + mu^2/k); null = 𝓛 design + mu/s + f1, f-1 (53..997) + f1+, f-1+ (1000<q<=20000).
Tests: (a) {omega(p+1), log P+(p+1)/L}; (b) {omega(p-1), log P+(p-1)/L}. Factorisations of p ± 1 by PARI.
Usage: python z56_primet1_g16.py PRED.npy MODEL.npz OUT [--label S3]"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design, primes_upto
from z56_primet1_amend import lstsq_rss
from z56_primet1_tests import holm

def pm1_feats(ps):
    import cypari2
    pari = cypari2.Pari(); out = np.zeros((len(ps), 5))
    for i, p in enumerate(ps):
        p = int(p); fm = pari.factor(p - 1); fp = pari.factor(p + 1)
        tau = 1; s = 1
        for q, e in zip(fp[0], fp[1]):
            q = int(q); e = int(e)
            if q == 2: continue
            tau *= e + 1; s *= (e + 1) if q % 4 == 1 else (1 if e % 2 == 0 else 0)
        out[i] = [(tau - s) // 2, len(fm[0]), math.log(int(fm[0][len(fm[0]) - 1])), len(fp[0]), math.log(int(fp[0][len(fp[0]) - 1]))]
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('pred'); ap.add_argument('model'); ap.add_argument('out'); ap.add_argument('--label', default='S3')
    a = ap.parse_args()
    pred = np.load(a.pred); m = np.load(a.model); K = float(m['k'])
    p = pred['p'].astype(np.uint64); n = len(p); L = np.log(p.astype(float)); mu = pred['mu']; Y = pred['R'] / 2.0
    s = np.sqrt(mu + mu * mu / K)
    pf = pm1_feats(p); t3 = pf[:, 0]
    z = (Y - t3) / s
    mids = [int(q) for q in primes_upto(997) if q >= 53]; bigs = [int(q) for q in primes_upto(20000) if q > 1000]
    def agg(qs, sign):
        f = np.zeros(n)
        for q in qs:
            f += np.where(p % np.uint64(q) == (np.uint64(1) if sign > 0 else np.uint64(q - 1)), math.log(q) / q, 0.0)
        return f
    extra = np.column_stack([mu / s, agg(mids, 1), agg(mids, -1), agg(bigs, 1), agg(bigs, -1)])
    Fp = np.column_stack([pf[:, 3], pf[:, 4] / L]); Fm = np.column_stack([pf[:, 1], pf[:, 2] / L])
    Fp = (Fp - Fp.mean(0)) / Fp.std(0); Fm = (Fm - Fm.mean(0)) / Fm.std(0)
    des = Design(1000); ch = 100000; G = None; c = None
    for st in range(0, n, ch):
        Z = np.column_stack([des.build(p[st:st + ch]), extra[st:st + ch], Fp[st:st + ch], Fm[st:st + ch]])
        if G is None: G = np.zeros((Z.shape[1], Z.shape[1])); c = np.zeros(Z.shape[1])
        G += Z.T @ Z; c += Z.T @ z[st:st + ch]
    k0 = G.shape[0] - 4; null = list(range(k0)); rr = float(z @ z)
    rows = []
    for name, idx in [('p+1 part', [k0, k0 + 1]), ('p-1 part', [k0 + 2, k0 + 3])]:
        r0, kk0, _ = lstsq_rss(G, c, rr, null); r1, kk1, b = lstsq_rss(G, c, rr, null + idx)
        df1 = kk1 - kk0; df2 = n - kk1; Fs = ((r0 - r1) / df1) / (r1 / df2)
        rows.append((name, df1, Fs, stats.f.sf(Fs, df1, df2), b[-2], b[-1]))
    adj = holm([r[3] for r in rows]); sc = float(np.mean(s / mu))
    with open(a.out + '_A7.tsv', 'w') as f:
        f.write(f'# A7 label={a.label} n={n} outcome z\'=(Y - tau3(p+1))/s(mu); coefficients in z-units per SD (x mean s/mu = {sc:.3f} for relative E[Y] effect)\n')
        f.write('test\tdf\tF\tp_raw\tp_holm\tcoef_omega\tcoef_logP+/L\n')
        for r, ad in zip(rows, adj): f.write('%s\t%d\t%.3f\t%.3e\t%.3e\t%+.5f\t%+.5f\n' % (r[0], r[1], r[2], r[3], ad, r[4], r[5]))
    print(open(a.out + '_A7.tsv').read())
