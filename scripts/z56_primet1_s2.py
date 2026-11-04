"""z56 PRIMET1 S2 (Z56_PRIMET1.md §3.5): extreme tail of Bulk2 (p ≡ 1 (24), 10^9 < p <= 10^10).
Stage 'select': with 𝓛 refitted on the hash-sample h64 = 2 (MODEL), compute mu-hat and mid-PIT for every prime of Bulk2,
take the hardest 0.01 % (lowest PIT) and, for each, 3 controls with the same p mod 35 and p mod 16 and nearest mu-hat among
non-hard primes (PIT >= 0.01), each control used once. Writes OUT_sets.npy (set id, role, p, R, mu, pit).
Stage 'test': conditional-logistic LR test per family on the matched sets (needs FEAT and CF for the set primes).
Usage: python z56_primet1_s2.py select MODEL.npz SIEVE.bin OUT
       python z56_primet1_s2.py test OUT FEAT.npy CF4.txt
"""
import sys, math
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit('/', 1)[0])

def select(model, sieve, out):
    from z56_primet1_local import Design
    m = np.load(model); des = Design(int(m['Q0']), int(m['qmax']), bool(m['drop13'])); beta = m['beta']; K = float(m['k'])
    d = np.memmap(sieve, dtype=np.dtype([('p', '<u8'), ('r', '<u2')]), mode='r')
    n = len(d); mu = np.empty(n); ch = 500000
    for s in range(0, n, ch):
        mu[s:s + ch] = np.exp(des.build(np.asarray(d['p'][s:s + ch])) @ beta)
        if (s // ch) % 10 == 0: print(s, n, file=sys.stderr, flush=True)
    y = np.asarray(d['r']).astype(float) / 2; pr = K / (K + mu)
    pit = stats.nbinom.cdf(y - 1, K, pr) + 0.5 * stats.nbinom.pmf(y, K, pr)
    P = np.asarray(d['p']).astype(np.int64)
    nh = int(round(1e-4 * n)); hard = np.argsort(pit, kind='stable')[:nh]
    print('n', n, 'nhard', nh, 'max pit among hard', pit[hard].max(), 'frac pit<0.01', (pit < 0.01).mean(), file=sys.stderr)
    cls = (P % 35) * 16 + (P % 16)
    used = np.zeros(n, bool); used[hard] = True
    rows = []
    elig = (pit >= 0.01)
    byc = {}
    for c in np.unique(cls[hard]):
        idx = np.nonzero((cls == c) & elig)[0]; byc[c] = idx[np.argsort(mu[idx])]
    for sid, i in enumerate(hard):
        rows.append((sid, 1, P[i], d['r'][i], mu[i], pit[i]))
        idx = byc[cls[i]]; pos = np.searchsorted(mu[idx], mu[i]); got = 0; lo, hi = pos - 1, pos
        while got < 3:
            cand = []
            if lo >= 0: cand.append((abs(mu[idx[lo]] - mu[i]), 'l'))
            if hi < len(idx): cand.append((abs(mu[idx[hi]] - mu[i]), 'h'))
            dd, side = min(cand)
            j = idx[lo] if side == 'l' else idx[hi]
            if side == 'l': lo -= 1
            else: hi += 1
            if used[j]: continue
            used[j] = True; got += 1; rows.append((sid, 0, P[j], d['r'][j], mu[j], pit[j]))
    arr = np.array(rows, dtype=[('set', '<i4'), ('case', '<i1'), ('p', '<u8'), ('R', '<i4'), ('mu', '<f8'), ('pit', '<f8')])
    np.save(out + '_sets.npy', arr); np.save(out + '_setp.npy', arr['p']); np.savetxt(out + '_setp.txt', arr['p'], fmt='%d')
    np.save(out + '_pit_hist.npy', np.histogram(pit, bins=np.r_[0, np.logspace(-8, 0, 81)])[0])

def clogit_lr(sets, case, X):
    """1:m conditional logistic; LR test of beta = 0."""
    order = np.argsort(sets, kind='stable'); sets, case, X = sets[order], case[order], X[order]
    bounds = np.r_[0, np.nonzero(np.diff(sets))[0] + 1, len(sets)]
    k = X.shape[1]; b = np.zeros(k)
    def ll_grad_hess(b):
        eta = X @ b; ll = 0.0; g = np.zeros(k); H = np.zeros((k, k))
        for s, e in zip(bounds[:-1], bounds[1:]):
            et = eta[s:e]; mx = et.max(); w = np.exp(et - mx); W = w.sum(); pw = w / W; Xs = X[s:e]
            ci = np.nonzero(case[s:e])[0][0]
            ll += et[ci] - mx - math.log(W)
            xm = pw @ Xs; g += Xs[ci] - xm
            H -= (Xs * pw[:, None]).T @ Xs - np.outer(xm, xm)
        return ll, g, H
    ll0, _, _ = ll_grad_hess(b)
    for it in range(50):
        ll, g, H = ll_grad_hess(b)
        step = np.linalg.lstsq(-H, g, rcond=None)[0]; b = b + step
        if np.max(np.abs(step)) < 1e-8: break
    ll1, _, H = ll_grad_hess(b)
    LR = 2 * (ll1 - ll0); df = np.linalg.matrix_rank(H)
    return LR, stats.chi2.sf(LR, max(df, 1)), df, b

def test(out, featf, cff):
    from z56_primet1_tests import families, holm, FAMS
    arr = np.load(out + '_sets.npy'); feat = np.load(featf)
    fi = {int(x): i for i, x in enumerate(feat['p'])}; feat = feat[np.array([fi[int(x)] for x in arr['p']])]
    cf = np.loadtxt(cff, dtype=np.int64); cfd = {int(r[0]): r[1:] for r in cf}
    cfa = np.array([cfd[int(x)] for x in arr['p']], dtype=float)
    F = families(feat, cfa[:, 0])
    L = np.log(arr['p'].astype(float))
    F['G17'] = (np.column_stack([np.log(np.maximum(cfa[:, 2], 1)) / L, np.log(cfa[:, 1]) / L]), ['Gamma', 'log(a1)/L'])
    rows = []
    for g in FAMS + ['G17']:
        X = F[g][0]; X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
        LR, pv, df, b = clogit_lr(arr['set'], arr['case'], X)
        rows.append((g, df, LR, pv, ' '.join(f'{n}:OR/sd={math.exp(x):.3f}' for n, x in zip(F[g][1], b))))
    adj = holm([r[3] for r in rows[:16]]) .tolist() + [float('nan')]
    with open(out + '_s2.tsv', 'w') as f:
        f.write(f'# S2 matched sets: {int(arr["case"].sum())} hard primes, {int((arr["case"]==0).sum())} controls; G17 post-hoc (not in Holm)\n')
        f.write('family\tdf\tLR\tp_raw\tp_holm(G1-G16)\tORs\n')
        for r, a in zip(rows, adj): f.write('%s\t%d\t%.3f\t%.3e\t%.3e\t%s\n' % (r[0], r[1], r[2], r[3], a, r[4]))
    print(open(out + '_s2.tsv').read())

if __name__ == '__main__':
    if sys.argv[1] == 'select': select(sys.argv[2], sys.argv[3], sys.argv[4])
    else: test(sys.argv[2], sys.argv[3], sys.argv[4])
