"""z38_hx.py [file] [col] [mod4class or 0]: H_BM numerics on z38_mbm output: per range, min (M - |R - M|) (H holds iff > 0), max |R-M|/M, max |R-M|/L^2, sd of (R-M)/sqrt(2M); M = MBM (col 5) or MBM8 (col 6)."""
import sys, math
col = int(sys.argv[2]) if len(sys.argv) > 2 else 4
edges = [5, 10**3, 10**4, 3*10**4, 10**5, 3*10**5, 10**6, 10**7, 10**8]
acc = {}
for l in open(sys.argv[1]):
    f = l.split(); n = int(f[0])
    if f[1] != '1': continue
    if len(sys.argv) > 3 and sys.argv[3] != '0' and n % 4 != int(sys.argv[3]): continue
    R = int(f[2]); M = float(f[col]); L2 = math.log(n) ** 2
    if M <= 0: continue
    i = max(j for j in range(len(edges)) if edges[j] <= n)
    a = acc.setdefault(i, dict(N=0, fail=0, mingap=(1e9, 0), maxrel=0, maxL=0, s=0.0, s2=0.0, zero=0, half=0, minz=(9, 0), minr=(9, 0)))
    a['N'] += 1; d = R - M
    gap = M - abs(d)
    if gap <= 0: a['fail'] += 1
    if gap < a['mingap'][0]: a['mingap'] = (round(gap, 2), n)
    a['maxrel'] = max(a['maxrel'], abs(d) / M); a['maxL'] = max(a['maxL'], abs(d) / L2)
    z = d / math.sqrt(2 * M); a['s'] += z; a['s2'] += z * z
    a['zero'] += (R == 0); a['half'] += (R < M / 2)
    if z < a['minz'][0]: a['minz'] = (round(z, 2), n)
    if R / M < a['minr'][0]: a['minr'] = (round(R / M, 3), n)
for i in sorted(acc):
    a = acc[i]; N = a['N']; mu = a['s'] / N; sd = math.sqrt(a['s2'] / N - mu * mu)
    print(f"[{edges[i]:.0e},{edges[i+1]:.0e}): N={N} H-fail={a['fail']} min(M-|X|)={a['mingap']} max|X|/M={a['maxrel']:.3f} max|X|/L²={a['maxL']:.3f} mean,sd of X/√(2M)={mu:.2f},{sd:.2f} | one-sided: R=0 {a['zero']}, R<M/2 {a['half']}, min R/M {a['minr']}, min X/√(2M) {a['minz']}")
