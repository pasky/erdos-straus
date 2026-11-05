# z57 COMPLEMENT: joint zero census over all n ≡ 1 (mod 4), 5 <= n <= 4*10^6 (columns of z57_complement_words.c, first 13).
# Prints, for primes / non-square composites / squares: zero counts of each family, joint zeros of each pair, and the
# independence prediction from per-decade marginal rates (sum over decades of N_dec * r_A * r_B).
import sys, gzip, math, itertools
import numpy as np
f = sys.argv[1]
A = np.loadtxt(gzip.open(f, 'rt'), dtype=np.int64)
n = A[:, 0]
cols = ['W', 'STAR', 'B1', 'I1', 'QR', 'BND', 'G', 'K', 'H3', 'HC', 'c2', 'c3']
D = {c: A[:, 1 + i] for i, c in enumerate(cols)}
M = int(n.max()); sv = np.ones(M + 1, bool); sv[:2] = False
for i in range(2, math.isqrt(M) + 1):
    if sv[i]: sv[i * i::i] = False
isp = sv[n]; r = np.array([math.isqrt(int(x)) for x in n]); issq = r * r == n
kinds = {'prime': isp, 'composite non-square': ~isp & ~issq, 'odd square': issq}
fams = ['STAR', 'B1', 'I1', 'c2', 'c3', 'G', 'K']
dec = np.floor(np.log10(n)).astype(int)
for kname, km in kinds.items():
    print(f'## {kname}: {km.sum()} values of n ≡ 1 (4) in [5, {M}]')
    Z = {c: (D[c] == 0) & km for c in fams}
    print('  zeros: ' + ', '.join(f'{c} {Z[c].sum()}' for c in fams))
    for c in ['STAR', 'B1', 'I1']:
        if 0 < Z[c].sum() <= 40: print(f'  {c} zeros: {list(n[Z[c]])}')
    for a, b in itertools.combinations(fams, 2):
        if {a, b} == {'STAR', 'G'} or {a, b} == {'STAR', 'K'}: continue
        j = Z[a] & Z[b]; pred = 0.0
        for d in np.unique(dec[km]):
            m = km & (dec == d); N = m.sum()
            pred += Z[a][m].sum() * Z[b][m].sum() / N
        lst = list(n[j]) if 0 < j.sum() <= 12 else ''
        print(f'  joint {a}&{b}: {j.sum()}  (per-decade independence {pred:.1f}) {lst}')
    j3 = Z['STAR'] & Z['B1'] & Z['I1']
    print(f'  five-slice union zero (STAR=B1=I1=0): {j3.sum()} {list(n[j3])[:20]}')
