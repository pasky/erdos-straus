"""z17_zpairs.py (O242): sibling-pair statistics of r-adic boxes on the r-generic line (EVIDENCE tool).
Reads boxes exactly as scripts/z16_ztree.py (P-data DIR/p{K}.txt, Q/U box files DIR/{Q,U}{k}.txt with inverses),
for every depth n: boxes of level n in cell C_v, parents (classes mod r^(n-1)) holding >= 2 of them (ALL parents, alive
or not), Poisson expectation b(b-1)/2/#parents, and the source labels of each clustered parent's boxes.
usage: python3 scripts/z17_zpairs.py DIR DMAX [v] [r]"""
import sys, os
from collections import defaultdict
D, DMAX = sys.argv[1], int(sys.argv[2]); v = int(sys.argv[3]) if len(sys.argv) > 3 else 5
R = int(sys.argv[4]) if len(sys.argv) > 4 else 17
boxes = defaultdict(dict)
def add(L, r, lab):
    r %= R ** L
    if r % R == v: boxes[L].setdefault(r, []).append(lab)
for K in range(1, 2 * DMAX, 2):
    L, n = (K + 1) // 2, R ** K
    fn = os.path.join(D, f"p{K}.txt")
    if not os.path.exists(fn): continue
    for line in open(fn):
        a, b, c, d = map(int, line.split()); assert 4 * a * b * c * d == a + b + n * c
        add(L, -(4 * a * c * d - 1), ("P", a, b, c, d)); add(L, -(4 * b * c * d - 1), ("P*", a, b, c, d))
for T in "QU":
    for k in range(1, DMAX + 1, 2):
        fn = os.path.join(D, f"{T}{k}.txt")
        if not os.path.exists(fn): continue
        for line in open(fn):
            r = int(line.split()[1]); add(k, r, (T,))
            if r % R: add(k, pow(r, -1, R ** k), (T + "inv",))
for n in range(2, DMAX + 1):
    B = boxes[n]; par = defaultdict(list)
    for x in B: par[x % R ** (n - 1)].append(x)
    npar = R ** (n - 2); b = len(B)
    cl = {p: xs for p, xs in par.items() if len(xs) >= 2}
    hist = defaultdict(int)
    for xs in par.values(): hist[len(xs)] += 1
    print(f"depth {n}: boxes {b}, parents with k boxes {dict(sorted(hist.items()))}, pairs {sum(len(x)*(len(x)-1)//2 for x in par.values())}"
          f", Poisson exp {b*(b-1)/2/npar:.4f}")
    if n >= 4:
        for p, xs in sorted(cl.items()):
            print("   parent", p, "children digits", sorted(x // R ** (n - 1) for x in xs))
            for x in xs: print("      ", x // R ** (n - 1), B[x][:3])
