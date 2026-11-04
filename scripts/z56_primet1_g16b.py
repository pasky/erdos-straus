"""z56 PRIMET1 Amendment 7 (test A8): the p ± 1 signal split into its <= 1000 part (local interactions) and > 1000 part.
Outcome z' = (Y - tau3(p+1))/s(mu) (u = 1 slice removed exactly). Null: 𝓛 design + mid_local (53 <= q <= 997: (q/p),
1[p ≡ ±1 (q)]) + mu/s + f1+, f-1+ (1000 < q <= 20000). Feature groups (each tested against the null, Holm over 4):
  (a) small-p-1: omega_{<=1000}(p-1) [interaction beyond additive one-hots]
  (b) large-p-1: omega_{>1000}(p-1), log(1000-rough part of p-1)/L
  (c) small-p+1: omega_{<=1000}(p+1)
  (d) large-p+1: omega_{>1000}(p+1), log(1000-rough part of p+1)/L
Usage: python z56_primet1_g16b.py PRED.npy MODEL.npz OUT [--label X]"""
import sys, math, argparse
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z56_primet1_local import Design, primes_upto
from z56_primet1_amend import lstsq_rss
from z56_primet1_amend2 import mid_local
from z56_primet1_tests import holm

def feats(ps):
    import cypari2
    pari = cypari2.Pari(); out = np.zeros((len(ps), 7))
    for i, p in enumerate(ps):
        p = int(p); fm = pari.factor(p - 1); fp = pari.factor(p + 1)
        tau = 1; s = 1
        for q, e in zip(fp[0], fp[1]):
            q = int(q); e = int(e)
            if q == 2: continue
            tau *= e + 1; s *= (e + 1) if q % 4 == 1 else (1 if e % 2 == 0 else 0)
        def split(f):
            ws = wl = 0; rough = 0.0
            for q, e in zip(f[0], f[1]):
                q = int(q); e = int(e)
                if q <= 1000: ws += 1
                else: wl += 1; rough += e * math.log(q)
            return ws, wl, rough
        a = split(fm); b = split(fp)
        out[i] = [(tau - s) // 2, a[0], a[1], a[2], b[0], b[1], b[2]]
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('pred'); ap.add_argument('model'); ap.add_argument('out'); ap.add_argument('--label', default='X')
    a = ap.parse_args()
    pred = np.load(a.pred); m = np.load(a.model); K = float(m['k'])
    p = pred['p'].astype(np.uint64); n = len(p); L = np.log(p.astype(float)); mu = pred['mu']; Y = pred['R'] / 2.0
    s = np.sqrt(mu + mu * mu / K)
    f = feats(p); z = (Y - f[:, 0]) / s
    bigs = [int(q) for q in primes_upto(20000) if q > 1000]
    def agg(sign):
        g = np.zeros(n)
        for q in bigs: g += np.where(p % np.uint64(q) == (np.uint64(1) if sign > 0 else np.uint64(q - 1)), math.log(q) / q, 0.0)
        return g
    extra = np.column_stack([mu / s, agg(1), agg(-1)])
    groups = {'(a) omega<=1000(p-1)': f[:, [1]], '(b) >1000 part of p-1': np.column_stack([f[:, 2], f[:, 3] / L]),
              '(c) omega<=1000(p+1)': f[:, [4]], '(d) >1000 part of p+1': np.column_stack([f[:, 5], f[:, 6] / L])}
    GX = np.column_stack([(g - g.mean(0)) / g.std(0) for g in groups.values()])
    des = Design(1000); ch = 100000; G = None; c = None
    for st in range(0, n, ch):
        ps = p[st:st + ch]
        Z = np.column_stack([des.build(ps), mid_local(ps), extra[st:st + ch], GX[st:st + ch]])
        if G is None: G = np.zeros((Z.shape[1], Z.shape[1])); c = np.zeros(Z.shape[1])
        G += Z.T @ Z; c += Z.T @ z[st:st + ch]
    k0 = G.shape[0] - GX.shape[1]; null = list(range(k0)); rr = float(z @ z)
    rows = []; off = k0
    for name, g in groups.items():
        idx = list(range(off, off + g.shape[1])); off += g.shape[1]
        r0, kk0, _ = lstsq_rss(G, c, rr, null); r1, kk1, b = lstsq_rss(G, c, rr, null + idx)
        df1 = kk1 - kk0; df2 = n - kk1; Fs = ((r0 - r1) / df1) / (r1 / df2)
        rows.append((name, df1, Fs, stats.f.sf(Fs, df1, df2), ' '.join(f'{x:+.5f}' for x in b[-g.shape[1]:])))
    adj = holm([r[3] for r in rows]); sc = float(np.mean(s / mu))
    with open(a.out + '_A8.tsv', 'w') as fo:
        fo.write(f"# A8 label={a.label} n={n}; z-units per SD (x {sc:.3f} = relative effect on E[Y]); mean omega<=1000(p-1)={f[:,1].mean():.3f}, omega>1000(p-1)={f[:,2].mean():.3f}\n")
        fo.write('group\tdf\tF\tp_raw\tp_holm\tcoefs\n')
        for r, ad in zip(rows, adj): fo.write('%s\t%d\t%.3f\t%.3e\t%.3e\t%s\n' % (r[0], r[1], r[2], r[3], ad, r[4]))
    print(open(a.out + '_A8.tsv').read())
