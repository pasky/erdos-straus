# z54 EXACTSPIN: summary statistics of layers.tsv (dedup on (tag, n)).
import sys, math, collections
import numpy as np
rows = {}
hdr = None
for line in open(sys.argv[1]):
    f = line.rstrip('\n').split('\t')
    if f[0] == 'tag': hdr = f; continue
    rows[(f[0], f[1])] = dict(zip(hdr, f))
by = collections.defaultdict(list)
for (t, n), r in rows.items(): by[t].append(r)
KL = [3,4,5,6,7,8,9,10,11,12,13,16,20,24]
def arr(rs, k): return np.array([float(r[k]) for r in rs])
for t in sorted(by, key=lambda s: (s.split('_')[0], float(s.split('_')[1].replace('1e','1e')) if '_' in s else 0)):
    rs = by[t]; N = len(rs)
    R, G, S2, So = arr(rs,'R'), arr(rs,'G'), arr(rs,'S2'), arr(rs,'Sodd')
    VG2, VGo = arr(rs,'VG2'), arr(rs,'VGo')
    L2 = np.array([math.log(float(r['n']))**2 for r in rs])
    print(f'== {t}  N={N}  mean G/log^2={np.mean(G/L2):.4f}  mean G={np.mean(G):.3f}  mean R={np.mean(R):.3f}  P(R=0)={np.mean(R==0):.3f}  max|R-G-S2-So|={np.max(np.abs(R-G-S2-So)):.2e} badsplit={sum(int(r["badsplit"]) for r in rs)}')
    if np.mean(G) < 1e-12:
        print('   squares/controls: max|R|=%g max|G|=%g max|S2|=%g max|Sodd|=%g' % (np.max(np.abs(R)), np.max(np.abs(G)), np.max(np.abs(S2)), np.max(np.abs(So))))
        print('   odd/even-order layers at controls: ' + ' '.join('D%d:mean|.|=%.3f' % (k, np.mean(np.abs(arr(rs, 'D%d' % k)))) for k in KL))
        continue
    RG = R - G
    vRG = np.var(RG)
    print('   mean S2/G=%.4f  mean Sodd/G=%.4f | var share S2=%.3f Sodd=%.3f cov=%.3f | z(S2): mean %.3f sd %.3f ; z(Sodd): mean %.3f sd %.3f ; z(R-G): mean %.3f sd %.3f' % (
        np.mean(S2)/np.mean(G), np.mean(So)/np.mean(G), np.var(S2)/vRG, np.var(So)/vRG, 2*np.cov(S2,So)[0,1]/vRG,
        np.mean(S2[VG2>0]/np.sqrt(VG2[VG2>0])), np.std(S2[VG2>0]/np.sqrt(VG2[VG2>0])), np.mean(So[VGo>0]/np.sqrt(VGo[VGo>0])), np.std(So[VGo>0]/np.sqrt(VGo[VGo>0])),
        np.mean(RG/np.sqrt(VG2+VGo)), np.std(RG/np.sqrt(VG2+VGo))))
    zs = []
    for k in KL:
        D, V = arr(rs, 'D%d' % k), arr(rs, 'V%d' % k)
        ok = V > 0   # rows with zero model variance (no character of order k on the shell) have D = 0 and are excluded
        z = D[ok]/np.sqrt(V[ok])
        zs.append('k=%d: <D/G>=%+.3f <z>=%+.3f(se %.3f) sd(z)=%.2f nvalid=%d' % (k, np.mean(D)/np.mean(G), np.mean(z), np.std(z)/math.sqrt(ok.sum()), np.std(z), ok.sum()))
    for i in range(0, len(zs), 3): print('   ' + ' | '.join(zs[i:i+3]))
# bounded-order variance share (uniform model and empirical); listed orders only
print('\n== listed-order variance statistic (orders k in KL only; model: mean over n of sum_k V_k / VRu (x uniform on G); empirical: sum_k var(D_k) / var(R-G), marginal variances, no cross-covariances)')
for t in sorted(by):
    rs = by[t]
    VRu = arr(rs, 'VRu')
    if np.mean(VRu) < 1e-12 or t.startswith('squares'): continue
    VK = sum(arr(rs, 'V%d' % k) for k in KL)
    R, G = arr(rs, 'R'), arr(rs, 'G')
    emp = sum(np.var(arr(rs, 'D%d' % k)) for k in KL) / np.var(R - G)
    print('   %-12s model share mean %.3f (min %.3f max %.3f)  empirical sum var(D_k)/var(R-G) = %.3f' % (t, np.mean(VK / VRu), np.min(VK / VRu), np.max(VK / VRu), emp))
