"""R128b: statistics of f_II(p) from review_r128b_count dump ("p f" lines) — checks §10 claims."""
import sys, numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64)
p, f = d[:, 0], d[:, 1].astype(float)
L3 = np.log(p) ** 3
m = p >= 10**5
idx = np.argsort(f[m] / L3[m])[:20]
pp = p[m][idx]
print("20 smallest f/log^3 (p>=1e5): p mod 24 =", sorted(set((pp % 24).tolist())),
      "exceptions:", [int(x) for x in pp if x % 24 != 1])
for k in range(23, 27):
    b = (p >= 2**k) & (p < 2**(k + 1))
    pb, fb = p[b], f[b]
    cls = pb % 840
    R = np.empty_like(fb); keep = np.zeros(len(fb), bool); means = {}
    for r in np.unique(cls):
        s = cls == r
        means[int(r)] = fb[s].mean() / np.mean(L3[b][s])
        if s.sum() >= 30:
            R[s] = fb[s] / fb[s].mean(); keep[s] = True
    six = sorted(means, key=means.get)[:6]
    Rk = R[keep]
    print(f"2^{k}: n={b.sum()} filtered-out={int((~keep).sum())} minR={Rk.min():.3f} "
          f"q0.1%={np.quantile(Rk,0.001):.3f} q1%={np.quantile(Rk,0.01):.3f} sd={Rk.std():.3f} six smallest classes={sorted(six)}")
