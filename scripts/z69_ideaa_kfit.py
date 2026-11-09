#!/usr/bin/env python3
"""z69 IDEAA T2 analysis: tail law of the two-small search cost K(p) (output of z69_ideaa_kcost.c).
Fits -ln P(K>Q) against kappa_j * (ln Q)^j, j = 2, 3 (pre-registered comparison, memo §2), prints the
Type I / Type II dependence exponent, and profiles the record setters (least QNR, class mod 840)."""
import math, re, sys, json
D = "data/z69/ideaa/"

def load(fn):
    N = None; S = []; rec = []
    for line in open(D + fn):
        if line.startswith("# X="):
            N = int(re.search(r"primes=(\d+)", line).group(1))
        elif line.startswith("S "):
            w = line.split(); S.append((int(w[1]), int(w[2]), [int(x) for x in w[3:]]))
        elif line.startswith("REC"):
            m = re.match(r"REC K=(\d+) p=(\d+)", line); rec.append((int(m.group(1)), int(m.group(2))))
    return N, S, rec

def lsq1(xs, ys):  # y = k x through origin
    return sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)

out = {}
for fn in ("kcost_1e10_both.txt", "kcost_1e10_typeII.txt", "kcost_1e10_typeI.txt", "kcost_1e9_both.txt"):
    N, S, rec = load(fn)
    pts = [(Q, s) for Q, s, _ in S if 50 <= Q and s >= 20]
    lq = [math.log(Q) for Q, _ in pts]; y = [-math.log(s / N) for _, s in pts]
    res = {}
    for j in (2, 3):
        k = lsq1([l ** j for l in lq], y)
        rms = math.sqrt(sum((yy - k * l ** j) ** 2 for l, yy in zip(lq, y)) / len(y))
        res[j] = (k, rms)
    # free exponent: ln y = ln k + j ln ln Q
    X = [math.log(l) for l in lq]; Y = [math.log(v) for v in y]
    mx = sum(X) / len(X); my = sum(Y) / len(Y)
    jfree = sum((a - mx) * (b - my) for a, b in zip(X, Y)) / sum((a - mx) ** 2 for a in X)
    print(f"{fn}: N={N}  points={len(pts)}  kappa2={res[2][0]:.4f} (rms {res[2][1]:.3f})  "
          f"kappa3={res[3][0]:.5f} (rms {res[3][1]:.3f})  free exponent j={jfree:.2f}  maxK={rec[-1]}")
    out[fn] = {"N": N, "kappa2": res[2], "kappa3": res[3], "jfree": jfree, "maxK": rec[-1],
               "tail": [(Q, s) for Q, s in pts]}
    if fn == "kcost_1e10_both.txt":
        k3 = res[3][0]
        for lX, lab in ((10, "1e10"), (17, "1e17"), (30, "1e30"), (100, "1e100"), (1000, "1e1000")):
            lnX = lX * math.log(10); lnN = lnX - math.log(lnX) - math.log(8)   # primes = 1 (24) up to X
            for j, k in ((3, res[3][0]), (2, res[2][0]), (jfree, math.exp(my - jfree * mx))):
                lnK = (lnN / k) ** (1.0 / j)
                print(f"   model j={j:.2f}: predicted max K for p<= {lab}: exp({lnK:.2f}) = {math.exp(lnK):.3g}")
        # per-decade tails (local in p): columns are decades [1e3,1e4),...,[1e9,1e10]
        print("   per-decade -ln P(K>Q)/ln^3 Q at Q=421, 1031, 2016 (decades 1e7.., 1e8.., 1e9..):")
        tot = S[0][2]
        for Q, s, c in S:
            if Q in (421, 1031, 2016):
                row = []
                for d in (4, 5, 6):
                    row.append(-math.log(c[d] / tot[d]) / math.log(Q) ** 3 if c[d] > 0 else float("nan"))
                print(f"     Q={Q}: " + "  ".join(f"{v:.4f}" for v in row), " counts", [c[d] for d in (4, 5, 6)])

# dependence exponent between Type I and Type II failures
Nb, Sb, _ = load("kcost_1e10_both.txt"); N2, S2, _ = load("kcost_1e10_typeII.txt"); N1, S1, _ = load("kcost_1e10_typeI.txt")
d2 = {Q: s for Q, s, _ in S2}; d1 = {Q: s for Q, s, _ in S1}
print("Q   P(II fails)  P(I fails)  P(both fail)  theta=lnP(both)/lnP(II)   P(both)/(P(I)P(II))")
dep = []
for Q, s, _ in Sb:
    if Q in d2 and Q in d1 and s >= 10 and Q >= 20:
        p2 = d2[Q] / N2; p1 = d1[Q] / N1; pb = s / Nb
        th = math.log(pb) / math.log(p2)
        dep.append((Q, p2, p1, pb, th))
        print(f"{Q:5d} {p2:.3e} {p1:.3e} {pb:.3e}  {th:.3f}  {pb/(p1*p2):.1f}")
out["dependence"] = dep

# record setters profile
def lqnr(p):
    q = 2
    while True:
        if q == 2:
            if p % 8 in (3, 5): return 2
        elif all(q % r for r in range(2, int(q ** 0.5) + 1)):
            if pow(p % q, (q - 1) // 2, q) == q - 1: return q
        q += 1
_, _, rec = load("kcost_1e10_both.txt")
print("record setters (K, p, p mod 840, least QNR n_p, in M?):")
M = {1, 121, 169, 289, 361, 529}
prof = []
for K, p in rec[-14:]:
    prof.append((K, p, p % 840, lqnr(p), (p % 840) in M))
    print("  ", prof[-1])
out["records"] = prof
json.dump(out, open(D + "kfit.json", "w"), indent=1)
