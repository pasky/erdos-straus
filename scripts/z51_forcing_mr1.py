#!/usr/bin/env python3
"""z51 forcing: the scale-log majority-reach hypothesis MR_1(C, eta) on the sampled primes (EXSET_CHAR_FORCING §5.3).
For each p in data/z51_forcing/reach/ and C in a list, P = C log p: weighted reach fraction
  w = sum_{P<q<=2P, Reach(p,q)} 1/q  /  sum_{P<q<=2P} 1/q   (odd primes q), and the unweighted fraction.
MR_1(C, eta) at p means w >= (1+eta)/2."""
import glob, math, re
res = {}
for fn in sorted(glob.glob("data/z51_forcing/reach/p*_*.txt")):
    if fn.endswith(".wit"): continue
    p = int(re.search(r"/p(\d+)_", fn).group(1)); L = math.log(p)
    reach = {}
    for line in open(fn):
        if line.startswith("#"): continue
        a = line.split(); reach[int(a[0])] = (int(a[3]) == 0)
    for C in (0.5, 1, 2, 3, 4):
        P = C * L; qs = [q for q in reach if P < q <= 2 * P]
        if not qs: continue
        w = sum(1 / q for q in qs if reach[q]) / sum(1 / q for q in qs)
        res.setdefault(C, []).append((p, w, len(qs)))
for C in sorted(res):
    ws = [w for _, w, _ in res[C]]
    bad = [(p, round(w, 2)) for p, w, _ in res[C] if w < 0.6]
    print(f"C={C}: {len(ws)} primes, min weighted reach fraction {min(ws):.3f}, mean {sum(ws)/len(ws):.3f}, "
          f"#(w<0.6) = {len(bad)} {bad[:8]}")
