#!/usr/bin/env python3
"""z51 forcing: summary and fits of the reach data (EXSET_CHAR_FORCING §6).
Reads data/z51_forcing/reach/p*_*.txt (z51_forcing_reach.c output). Per p: q* (first unreached QNR class),
S_e = mean over primes q in [11,300] of q*(mean distinct productive (type,e) per QNR class)  [supply],
Rmaj(eta) = largest R<=QMAX with reach at >= (1/2+eta) of the odd primes q<=R, fraction of reached q<=(log p)^2.
Then least-squares fits of log S_e and log q* against log log p, and ratios to (log p)^2, (log p)^3/log log p."""
import glob, math, re, statistics as st
rows = []
for fn in sorted(glob.glob("data/z51_forcing/reach/p*_*.txt")):
    if fn.endswith(".wit"): continue
    p = int(re.search(r"/p(\d+)_", fn).group(1)); tag = fn.split("_")[-1][:-4]
    Q = []
    for line in open(fn):
        if line.startswith("#"): continue
        a = line.split(); Q.append((int(a[0]), int(a[3]), float(a[7])))
    qstar = next((q for q, un, _ in Q if un > 0), None)
    Se = st.mean(q * me for q, un, me in Q if 11 <= q <= 300)
    L = math.log(p)
    def rmaj(eta):
        best = None; n = r = 0
        for q, un, _ in Q:
            n += 1; r += (un == 0)
            if r / n >= 0.5 + eta: best = q
        return best
    n2 = [un == 0 for q, un, _ in Q if q <= L * L]
    rows.append((p, tag, qstar, Se, rmaj(0.1), rmaj(0.25), sum(n2) / len(n2), L))
print(f"{'p':>12} {'tag':>10} {'q*':>4} {'S_e':>7} {'Rmaj.6':>6} {'Rmaj.75':>7} {'frac<=L^2':>9} {'q*/L^2':>7} {'q*/(L^3/lnL)':>12} {'S_e/L^3':>8}")
for p, tag, qs, Se, r1, r2, f2, L in rows:
    print(f"{p:>12} {tag:>10} {qs:>4} {Se:7.1f} {str(r1):>6} {str(r2):>7} {f2:9.3f} {qs/L**2:7.3f} {qs/(L**3/math.log(L)):12.4f} {Se/L**3:8.4f}")
# fits on per-scale medians
scales = {}
for p, tag, qs, Se, r1, r2, f2, L in rows:
    k = round(math.log10(p)); scales.setdefault(k, []).append((qs, Se, r1, L))
xs, ys, zs = [], [], []
print("\nscale  n  median q*  median S_e  median Rmaj(0.6)  log p")
for k in sorted(scales):
    v = scales[k]; mq = st.median(a[0] for a in v); ms = st.median(a[1] for a in v); mr = st.median(a[2] for a in v); L = st.mean(a[3] for a in v)
    print(f"1e{k:<3} {len(v):2d} {mq:9.1f} {ms:10.1f} {mr:12.1f}  {L:6.2f}")
    xs.append(math.log(L)); ys.append(math.log(ms)); zs.append(math.log(mq))
def slope(x, y):
    mx, my = st.mean(x), st.mean(y); return sum((a-mx)*(b-my) for a, b in zip(x, y)) / sum((a-mx)**2 for a in x)
print(f"\nfit: S_e ~ (log p)^{slope(xs, ys):.2f};  q* ~ (log p)^{slope(xs, zs):.2f}")
