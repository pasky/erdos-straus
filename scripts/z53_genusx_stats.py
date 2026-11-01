# z53 GENUSX statistics over the TSV outputs of z53_genusx_run.py
# Usage: uv run --with numpy python scripts/z53_genusx_stats.py data/z53/genusx/random_small.tsv data/z53/genusx/random.tsv ...
import sys, math
import numpy as np
rows = []
for fn in sys.argv[1:]:
    for line in open(fn):
        if line.startswith('tag'): continue
        t = line.rstrip('\n').split('\t')
        rows.append(t)
by = {}
for t in rows: by.setdefault(t[0], []).append(t)
print('tag N mean(L) mean(M/L2) mean(R/M) mean(G/M) | sd(R-M)/M sd(G-M)/M sd(R-G)/M | var(R-M)=var(G-M)+var(R-G)+2cov [shares] | var(R-G)/(2*mean G) | P(R=0) mean exp(-M/2) | corr(G-M,R-M)')
for tag, T in by.items():
    a = np.array([[float(x) for x in t[2:11]] for t in T])
    L, R, G, E1, C4, CU0, CBM, REST, M = a.T
    if np.isnan(M).all(): continue
    ok = M > 0
    L, R, G, M = L[ok], R[ok], G[ok], M[ok]
    dRM, dGM, dRG = R - M, G - M, R - G
    vRM, vGM, vRG = dRM.var(), dGM.var(), dRG.var(); cov = np.mean((dGM - dGM.mean()) * (dRG - dRG.mean()))
    print('%s %d %.2f %.4f %.3f %.3f | %.3f %.3f %.3f | %.2f = %.2f + %.2f + 2*%.2f [%.2f %.2f %.2f] | %.2f | %.3f %.3f | %.3f' % (
        tag, len(R), L.mean(), (M / L ** 2).mean(), (R / M).mean(), (G / M).mean(),
        (dRM / M).std(), (dGM / M).std(), (dRG / M).std(), vRM, vGM, vRG, cov, vGM / vRM, vRG / vRM, 2 * cov / vRM,
        vRG / (2 * G.mean()), (R == 0).mean(), np.exp(-M / 2).mean(), np.corrcoef(dGM, dRM)[0, 1]))
# components of G relative to M (means) per tag
print('\ncomponent means / M:  E1 C4 CU0 CBM REST ; sd/M of E1-M and of G-M ; corr(E1-M, G-M)')
for tag, T in by.items():
    a = np.array([[float(x) for x in t[2:11]] for t in T])
    L, R, G, E1, C4, CU0, CBM, REST, M = a.T
    ok = (M > 0) & ~np.isnan(M)
    if ok.sum() < 3: continue
    E1, C4, CU0, CBM, REST, G, M = E1[ok], C4[ok], CU0[ok], CBM[ok], REST[ok], G[ok], M[ok]
    print('%s %.3f %.3f %.3f %.3f %.3f ; %.3f %.3f ; %.3f' % (tag, (E1 / M).mean(), (C4 / M).mean(), (CU0 / M).mean(), (CBM / M).mean(), (REST / M).mean(),
          ((E1 - M) / M).std(), ((G - M) / M).std(), np.corrcoef(E1 - M, G - M)[0, 1]))
