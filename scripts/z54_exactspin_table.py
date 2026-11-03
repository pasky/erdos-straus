# z54 EXACTSPIN: compact markdown table for the memo from layers.tsv (dedup on (tag, n)).
import sys, math, collections
import numpy as np
rows = {}; hdr = None
for line in open(sys.argv[1]):
    f = line.rstrip('\n').split('\t')
    if f[0] == 'tag': hdr = f; continue
    rows[(f[0], f[1])] = dict(zip(hdr, f))
by = collections.defaultdict(list)
for (t, n), r in rows.items(): by[t].append(r)
KL = [3,4,5,6,7,8,9,10,11,12,13,16,20,24]
A = lambda rs, k: np.array([float(r[k]) for r in rs])
mz = []
order = ['rand_1e9','rand_1e10','rand_1e11','rand_1e12','rand_1e13','rand_1e14','nearsq_1e10','nearsq_1e12','nearsq_1e14']
print('| sample | N | mean G/log²p | mean R/mean G | P(R=0) | var S₂/var(R−G) | var S_o/var(R−G) | z(S₂) mean, sd | z(S_o) mean, sd | z(R−G) mean, sd | max_k |mean z(Δ_k)|/se | sd z(Δ_k) range | listed orders Σ_k marginal var (model / emp.) |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for t in order:
    rs = by[t]; N = len(rs)
    R, G, S2, So, V2, Vo, VRu = (A(rs, k) for k in ('R','G','S2','Sodd','VG2','VGo','VRu'))
    L2 = np.array([math.log(float(r['n']))**2 for r in rs])
    RG = R - G; v = np.var(RG)
    z2 = S2/np.sqrt(V2); zo = So/np.sqrt(Vo); zr = RG/np.sqrt(V2+Vo)
    mx = 0; sds = []
    for k in KL:
        D, V = A(rs,'D%d'%k), A(rs,'V%d'%k); ok = V > 0   # zero-variance rows (D = 0) excluded, as in the stats script
        z = D[ok]/np.sqrt(V[ok]); se = np.std(z)/math.sqrt(ok.sum())
        mx = max(mx, abs(np.mean(z))/se); sds.append(np.std(z)); mz.append((abs(np.mean(z)), t, k))
    VK = sum(A(rs,'V%d'%k) for k in KL); emp = sum(np.var(A(rs,'D%d'%k)) for k in KL)/v
    mz.append((abs(np.mean(z2)), t, 'S2')); mz.append((abs(np.mean(zo)), t, 'Sodd')); mz.append((abs(np.mean(zr)), t, 'R-G'))
    print(f'| {t} | {N} | {np.mean(G/L2):.4f} | {np.mean(R)/np.mean(G):.3f} | {np.mean(R==0):.3f} | {np.var(S2)/v:.2f} | {np.var(So)/v:.2f} | {np.mean(z2):+.3f}, {np.std(z2):.2f} | {np.mean(zo):+.3f}, {np.std(zo):.2f} | {np.mean(zr):+.3f}, {np.std(zr):.2f} | {mx:.1f} | {min(sds):.2f}–{max(sds):.2f} | {np.mean(VK/VRu):.2f} / {emp:.2f} |')
mz.sort(reverse=True); print('\nlargest |mean z| over all layers and samples:', ', '.join('%.3f (%s, %s)' % m for m in mz[:5]))
# pooled random z(R-G)
zz = []
for t in order[:6]:
    rs = by[t]; zz += list((A(rs,'R')-A(rs,'G'))/np.sqrt(A(rs,'VG2')+A(rs,'VGo')))
zz = np.array(zz); print(f'\npooled random primes: N={len(zz)}, mean z(R-G) = {np.mean(zz):+.4f} (se {np.std(zz)/math.sqrt(len(zz)):.4f})')
for t in ('squares_1e10','squares_1e12','squares_1e14'):
    rs = by[t]
    print(t, 'N=%d' % len(rs), 'max|R|,|G|,|S2|,|So| =', max(abs(A(rs,'R'))), max(abs(A(rs,'G'))), max(abs(A(rs,'S2'))), max(abs(A(rs,'Sodd'))),
          '; mean |D_k| for k=3,5,6,7:', ' '.join('%.3f' % np.mean(abs(A(rs,'D%d'%k))) for k in (3,5,6,7)), '; max |D_k|, 4|k:', max(max(abs(A(rs,'D%d'%k))) for k in (4,8,12,16,20,24)))
