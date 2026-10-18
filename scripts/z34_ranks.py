"""O264 goal 2: hardness ranks in both worlds and their correlation, before/after conditioning on the local profile.
Input: output of z34_scores (p N1 fII m0 Mpts S e0 LI), all primes p = 1 (4) <= X.
Hardness orientation: small N1, fII, S, LI and large m0, e0 are hard. Each score is turned into a *size-normalised
hardness percentile* u in [0,1] (1 = hardest): its mid-rank among the W nearest primes (sliding window by index).
Profile cell of p: (chi_p(l) for l in 3,5,7,11,13, p mod 8) -- the B1 data (QR pattern of small primes).
Residual hardness: u minus the mean u of the profile cell within the same size block (blocks of B primes).
usage: z34_ranks.py scores.txt [W] [B]
"""
import sys
import numpy as np

W = int(sys.argv[2]) if len(sys.argv) > 2 else 1001
B = int(sys.argv[3]) if len(sys.argv) > 3 else 5000
A = np.loadtxt(sys.argv[1], dtype=np.int64)
p = A[:, 0]
names = ['N1', 'fII', 'm0', 'S', 'e0', 'LI']
raw = {'N1': -A[:, 1], 'fII': -A[:, 2], 'm0': A[:, 3], 'S': -A[:, 5], 'e0': np.where(A[:, 6] == 0, 10**9, A[:, 6]), 'LI': -A[:, 7]}
n = len(p)


def midrank_pct(x):
    """mid-rank percentile of each entry within a sliding index window of width W (hardness up)."""
    u = np.empty(n)
    h = W // 2
    for i in range(n):
        lo, hi = max(0, i - h), min(n, i + h + 1)
        if hi - lo < W:
            lo, hi = (0, W) if lo == 0 else (n - W, n)
        w = x[lo:hi]
        u[i] = ((w < x[i]).sum() + 0.5 * ((w == x[i]).sum() - 1)) / (len(w) - 1)
    return u


def spearman(a, b):
    ra = a.argsort().argsort().astype(float); rb = b.argsort().argsort().astype(float)
    return np.corrcoef(ra, rb)[0, 1]


U = {k: midrank_pct(raw[k]) for k in names}
P0 = int(sys.argv[4]) if len(sys.argv) > 4 else 50000   # correlations only for p >= P0 (window spans < factor 1.2)


def band_pct(x, i):
    """mid-rank hardness percentile of entry i among primes in [p/2, 2p] (fixtures: no window edge effect)."""
    lo, hi = np.searchsorted(p, p[i] // 2), np.searchsorted(p, 2 * p[i], side='right')
    w = x[lo:hi]
    return ((w < x[i]).sum() + 0.5 * ((w == x[i]).sum() - 1)) / (len(w) - 1), hi - lo


def chi(p, l):
    r = pow(int(p) % l, (l - 1) // 2, l)
    return 1 if r == 1 else -1


cell = np.array([hash((tuple(chi(q, l) for l in (3, 5, 7, 11, 13)), int(q) % 8)) for q in p])
block = np.arange(n) // B
R = {}
for k in names:
    r = U[k].copy()
    for bl in np.unique(block):
        mb = block == bl
        for c in np.unique(cell[mb]):
            m = mb & (cell == c)
            r[m] = U[k][m] - U[k][m].mean()
    R[k] = r
sm = np.zeros(n)
for i, q in enumerate(p):
    m = int(q) - 1; s = 1
    for l in (2, 3, 5, 7, 11, 13):
        while m % l == 0:
            m //= l; s *= l
    sm[i] = np.log(s) / np.log(float(q))
mod24 = (p % 24 == 1)
big = p >= P0
print(f'n = {n} primes p = 1 (4) <= {p[-1]}; window W = {W}, profile blocks B = {B}; correlations over p >= {P0}')
for lab, sel in (('all', big), ('p=1(24)', big & mod24)):
    print(f'\nSpearman of hardness percentiles u ({lab}, n = {sel.sum()}):')
    print('      ' + ''.join(f'{k:>7}' for k in names + ['sm13']))
    for a in names:
        print(f'{a:>6}' + ''.join(f'{spearman(U[a][sel], U[b][sel]):7.2f}' for b in names) + f'{spearman(U[a][sel], sm[sel]):7.2f}')
    print(f'Spearman of profile residuals ({lab}):')
    for a in names:
        print(f'{a:>6}' + ''.join(f'{spearman(R[a][sel], R[b][sel]):7.2f}' for b in names) + f'{spearman(R[a][sel], sm[sel]):7.2f}')
# share of variance of u explained by the profile cells
print('\nfraction of var(u) explained by (block, profile cell), p >= P0:', {k: round(1 - R[k][big].var() / U[k][big].var(), 3) for k in names})
print('\nfixtures: band percentile u in [p/2, 2p] (band size); residual only meaningful for p >= P0; sm13 = log(13-smooth part of p-1)/log p')
idx = {int(q): i for i, q in enumerate(p)}
for q in (97, 193, 2521, 3361, 5209, 66529, 233689):
    if q in idx:
        i = idx[q]
        bp = {k: band_pct(raw[k], i) for k in names}
        print(q, 'raw', A[i, 1:].tolist(), f' band n={bp["N1"][1]} u', ' '.join(f'{k}={bp[k][0]:.3f}' for k in names),
              ' res', ' '.join(f'{R[k][i]:+.2f}' for k in names), f' sm13={sm[i]:.2f}')
# joint extremes: primes in the top 1 % of both a Claude score and an Astra score
for a, b in (('N1', 'S'), ('fII', 'S'), ('m0', 'e0'), ('N1', 'e0'), ('fII', 'e0')):
    both = np.where((U[a] >= 0.99) & (U[b] >= 0.99) & big)[0]
    exp = big.sum() * 0.01 * 0.01
    print(f'top-1% in both {a},{b}: {len(both)} (independence would give {exp:.1f}); first: {p[both][:12].tolist()}')
