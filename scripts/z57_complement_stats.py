# z57 COMPLEMENT: joint structure of certificate families (output of z57_complement_words.c).
# usage: python z57_complement_stats.py LABEL file1 [file2 ...]   (files may be .gz)
# Reports: means/L^2, zero rates; residual correlations (raw, within p mod 840, OLS on residues mod small prime powers);
# partial correlations given W and given QR; joint-zero / joint-low-tail Mantel–Haenszel odds ratios within p mod 840.
import sys, gzip, math, functools
print = functools.partial(print, flush=True)
import numpy as np

COLS = ['W', 'STAR', 'B1', 'I1', 'QR', 'BND', 'G', 'K', 'H3', 'HC', 'c2', 'c3']
def load(files):
    rows = []
    for f in files:
        op = gzip.open if f.endswith('.gz') else open
        with op(f, 'rt') as fh:
            for line in fh:
                a = line.split()
                if len(a) < 73: continue
                rows.append([int(x) for x in a[:73]])
    A = np.array(rows, dtype=np.int64)
    p = A[:, 0]
    D = {c: A[:, 1 + i].astype(float) for i, c in enumerate(COLS)}
    for k, (name, off) in enumerate([('STARz', 13), ('B1z', 23), ('I1z', 33), ('QRz', 43), ('c2z', 53), ('c3z', 63)]):
        for b in range(10):
            D[f'{name}{b}'] = A[:, off + b].astype(float)
    return p, D

def sidx(s):
    _, inv = np.unique(s, return_inverse=True); return inv

def strata_resid(y, s):
    k = sidx(s); n = np.bincount(k); return y - (np.bincount(k, y) / n)[k]

def onehot_design(p, mods):
    cols = [np.ones(len(p))]
    for q in mods:
        res = p % q
        for v in np.unique(res)[1:]:
            cols.append((res == v).astype(float))
    return np.column_stack(cols)

def ols_resid(y, X):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta

def corr(a, b):
    a = a - a.mean(); b = b - b.mean()
    d = math.sqrt((a * a).sum() * (b * b).sum())
    return (a * b).sum() / d if d > 0 else float('nan')

def partial(a, b, z):
    # correlation of a, b after regressing both on z (with intercept)
    X = np.column_stack([np.ones(len(z)), z])
    return corr(ols_resid(a, X), ols_resid(b, X))

def mh_or(e1, e2, s):
    # Mantel–Haenszel odds ratio for events e1, e2 within strata s
    k = sidx(s); n = np.bincount(k).astype(float); K = len(n)
    a = np.bincount(k, e1 & e2, K); b = np.bincount(k, e1 & ~e2, K); c = np.bincount(k, ~e1 & e2, K); d = n - a - b - c
    num = (a * d / n).sum(); den = (b * c / n).sum()
    return num / den if den > 0 else float('nan')

def joint_ratio(e1, e2, s):
    # observed joint count / within-stratum independence prediction
    k = sidx(s); n = np.bincount(k).astype(float); K = len(n)
    obs = (e1 & e2).sum(); pred = (np.bincount(k, e1, K) * np.bincount(k, e2, K) / n).sum()
    return obs, pred

def low_event(y, s, q):
    # y <= within-stratum q-quantile (ties included)
    e = np.zeros(len(y), bool)
    for v in np.unique(s):
        m = s == v; thr = np.quantile(y[m], q); e[m] = y[m] <= thr
    return e

def main():
    label = sys.argv[1]; p, D = load(sys.argv[2:])
    N = len(p); L2 = np.log(p.astype(float)) ** 2
    s840 = p % 840
    print(f'# {label}: N = {N} primes p ≡ 1 (4), p in [{p.min()}, {p.max()}]; mean L^2 = {L2.mean():.1f}')
    print('## means/L^2 and zero counts')
    D['INT'] = D['W'] - D['BND']
    for c in COLS + ['INT']:
        y = D[c]; print(f'{c:5s} mean/L2 {np.mean(y / L2):.4f}  var/mean {y.var() / max(y.mean(), 1e-9):.2f}  zeros {int((y == 0).sum())}')
    mods = [8, 3, 9, 5, 25, 7, 49, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    X = onehot_design(p, mods)
    # transform: normalised count y / E[y | stratum] is scale-free; use raw counts residualised (Pearson) and log1p.
    fams = ['STAR', 'B1', 'I1', 'QR', 'c2', 'c3', 'G', 'K']
    pairs = [(a, b) for i, a in enumerate(fams) for b in fams[i + 1:]]
    print('## residual correlations (count scale): raw | within 840 (z) | OLS residues mod', mods[:6], '... (z) | log1p OLS | partial|INT=W-BND (840) | partial|QR (840)')
    R840 = {c: strata_resid(D[c], s840) for c in fams + ['W', 'INT']}
    ROLS = {c: ols_resid(D[c], X) for c in fams + ['W']}
    RLOG = {c: ols_resid(np.log1p(D[c]), X) for c in fams}
    sq = math.sqrt(N)
    for a, b in pairs:
        r0 = corr(D[a], D[b]); r1 = corr(R840[a], R840[b]); r2 = corr(ROLS[a], ROLS[b]); r3 = corr(RLOG[a], RLOG[b])
        pw = partial(R840[a], R840[b], R840['INT']); pq = partial(R840[a], R840[b], R840['QR']) if 'QR' not in (a, b) else float('nan')
        print(f'{a:4s}-{b:4s} {r0:+.3f} | {r1:+.3f} ({r1 * sq:+.1f}) | {r2:+.3f} ({r2 * sq:+.1f}) | {r3:+.3f} | {pw:+.3f} | {pq:+.3f}')
    # joint low tails
    print('## joint low tails within p mod 840: event = count <= within-stratum q-quantile; obs/pred (MH OR)')
    for q in (0.05, 0.10, 0.25):
        E = {c: low_event(D[c], s840, q) for c in fams}
        line = []
        for a, b in pairs:
            o, pr = joint_ratio(E[a], E[b], s840); line.append(f'{a}-{b} {o / pr:.2f}({mh_or(E[a], E[b], s840):.2f})')
        print(f'q={q}: ' + '  '.join(line))
    # joint zeros of level-band sub-families across slices (zero rates in [2%, 98%])
    print('## level-band sub-families: joint-zero ratio obs/pred within 840 and MH OR, for cross-slice pairs with both zero rates in [0.02, 0.98]')
    bands = [k for k in D if k[-1].isdigit() and k[:-1] in ('STARz', 'B1z', 'I1z', 'QRz', 'c2z', 'c3z')]
    Z = {k: D[k] == 0 for k in bands}
    ok = [k for k in bands if 0.02 <= Z[k].mean() <= 0.98]
    RBX = {k: ols_resid(D[k], X) for k in ok}
    res = []
    for i, a in enumerate(ok):
        for b in ok[i + 1:]:
            if a[:-1] == b[:-1]: continue
            o, pr = joint_ratio(Z[a], Z[b], s840)
            if pr < 5: continue
            r = corr(RBX[a], RBX[b])
            res.append((o / pr, a, b, o, pr, mh_or(Z[a], Z[b], s840), r))
    res.sort()
    for t in res[:12] + [None] + res[-6:]:
        if t is None: print('  ...'); continue
        print(f'  {t[1]:7s} {t[2]:7s} zero-rates {Z[t[1]].mean():.3f} {Z[t[2]].mean():.3f}  obs {t[3]} pred {t[4]:.1f} ratio {t[0]:.3f} MH-OR {t[5]:.3f}  OLS-corr {t[6]:+.3f} (z {t[6] * sq:+.1f})')
    rs = np.array([t[0] for t in res]); ors = np.array([t[5] for t in res])
    print(f'  {len(res)} pairs: ratio median {np.median(rs):.3f}, fraction < 1: {np.mean(rs < 1):.2f}; MH-OR median {np.nanmedian(ors):.3f}')
    # most negative OLS-residual correlations among all band pairs (incl. within-slice)
    print('## most negative OLS residual correlations among all band pairs (count scale), nominal z')
    allb = [k for k in bands if D[k].mean() > 0.05]
    RB = {k: ols_resid(D[k], X) for k in allb}
    cc = []
    for i, a in enumerate(allb):
        for b in allb[i + 1:]:
            cc.append((corr(RB[a], RB[b]), a, b))
    cc.sort()
    for r, a, b in cc[:10]: print(f'  {a:7s} {b:7s} {r:+.3f} (z {r * sq:+.1f})')
    rr = np.array([c[0] for c in cc])
    print(f'  {len(cc)} pairs: median {np.median(rr):+.3f}; below -4/sqrt(N): {(rr < -4 / sq).sum()}; above +4/sqrt(N): {(rr > 4 / sq).sum()}')

if __name__ == '__main__':
    main()
