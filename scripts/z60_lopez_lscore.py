"""z60 LOPEZ: is the tail co-failure of the two branches explained by the quadratic character chi_p?
Score s(p) = sum_{l <= Y prime odd} chi_p(l) log(l)/l   (chi_p(l) = (p/l) = (l/p) for p ≡ 1 mod 4),
a weighted character score (first-prime-term approximation to -L'/L(1,chi_p); NOT an estimate of log L(1,chi_p)).  Strata: quantile bins of s(p) (optionally x exact p mod 5,7).
Prints pooled observed/expected co-failure ratios and the marginal tail rates per score bin.
Usage: python z60_lopez_lscore.py file Y nbins [inM]"""
import sys, numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64)
if len(sys.argv) > 4 and sys.argv[4] == '1':
    d = d[np.isin(d[:, 0] % 840, [1, 121, 169, 289, 361, 529])]
Y = int(sys.argv[2]); nb = int(sys.argv[3])
INF = 10**12; X = d.copy(); X[X == 0] = INF; p = X[:, 0]
ps = [l for l in range(3, Y + 1) if all(l % q for q in range(2, int(l ** .5) + 1))]
s = np.zeros(len(p))
for l in ps:
    r = p % l
    tab = np.array([0] + [1 if pow(x, (l - 1) // 2, l) == 1 else -1 for x in range(1, l)])
    s += tab[r] * np.log(l) / l
edges = np.quantile(s, np.linspace(0, 1, nb + 1)); edges[-1] += 1
bins = np.digitize(s, edges[1:-1])
print("N", len(p), "Y", Y, "bins", nb, "bin edges", np.round(edges, 4).tolist())
for col, nm in ((1, 'a'), (3, 'f'), (5, 'T')):
    B = X[:, col]; A = X[:, col + 1]
    xs = sorted(set(int(np.quantile(B, q)) for q in (0.9, 0.99, 0.999)))
    for strat_name, key in (("score", bins), ("score x p mod 35", bins * 100 + (p % 35))):
        keys, inv = np.unique(key, return_inverse=True)
        out = []
        for x in xs:
            a = (A > x).astype(float); b = (B > x).astype(float)
            Ns = np.bincount(inv); Sa = np.bincount(inv, a); Sb = np.bincount(inv, b); Sab = np.bincount(inv, a * b)
            exp = (Sa * Sb / Ns).sum(); obs = Sab.sum()
            out.append(f"X={x}: obs {int(obs)} exp {exp:.1f} r {obs/exp:.2f}")
        print(f"[{nm}; {strat_name}] " + " | ".join(out))
    x = xs[1]
    print(f"  per-bin (coord {nm}, X={x}): bin: P(B>X) P(A>X) P(both>X) ratio")
    for k in range(nb):
        m = bins == k; pb = (B[m] > x).mean(); pa = (A[m] > x).mean(); pab = ((A[m] > x) & (B[m] > x)).mean()
        print(f"   {k} s~{np.median(s[m]):+.2f}: {pb:.2e} {pa:.2e} {pab:.2e} {pab/(pa*pb) if pa*pb else float('nan'):.2f}")
