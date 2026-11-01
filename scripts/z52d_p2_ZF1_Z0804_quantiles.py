"""Z0804 (ZF1 finisher): L(1,χ_p) and h(−4p) quantiles at Type-A (b = 1 line) near-failures, p ≤ 1e8.
Input: N1 census data/z52b/pass2/ZF1/Z0804/N1_le1e8.txt.gz (p N1; scripts/z29_census.c countlist mode;
all p ≡ 1 (4) ≤ 1e7, p ≡ 1 (24) in (1e7, 1e8]).
Targets: (a) N1(p) ∈ {0,1,2} (the item's definition) with p > 100; (b) scale-free lower tail: bottom 0.2% of
N1/log²p inside each of 12 log-bins, p ≡ 1 (24), 1e5 ≤ p ≤ 1e8.
Controls: residue-matched (p ≡ 1 mod 24; for (a) also same class mod 24 as the target) random primes from the census,
same log-bin; quantile = fraction of controls with a smaller value.
L(1,χ_p) ∝ h(p)·log ε_p/√p (PARI quadclassunit, GRH-conditional), H = h(−4p)/√p (PARI qfbclassno).
Run: uv run --with numpy --with cypari2 python scripts/z52d_p2_ZF1_Z0804_quantiles.py
"""
import numpy as np, json, os, gzip, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data/z52b/pass2/ZF1/Z0804')
A = np.loadtxt(gzip.open(os.path.join(D, 'N1_le1e8.txt.gz'), 'rt'), dtype=np.int64)
p = A[:, 0]; N1 = A[:, 1]
rng = np.random.default_rng(7)
def L1(q): r = pari.quadclassunit(int(q)); return float(r[0]) * float(r[3]) / math.sqrt(q)
def Hm(q): return int(pari.qfbclassno(-4 * int(q))) / math.sqrt(q)
lp = np.log(p.astype(float)); r = N1 / lp ** 2
bins = np.linspace(math.log(1e5), math.log(1e8), 13)
out = {}
# (a) item definition
ta = [(int(q), int(n)) for q, n in zip(p, N1) if n <= 2 and q > 100]
cache = {}
def ctrl(q, cls, k=400):
    m = (p % 24 == q % 24) if cls == 'mod24' else (p % 24 == 1)
    w = 0.15
    while True:
        mm = m & (np.abs(lp - math.log(q)) < w) & (p != q)
        if mm.sum() >= 40 or w > 3: break
        w *= 1.5
    c = p[mm]
    if len(c) > k: c = rng.choice(c, k, replace=False)
    return c
def val(q):
    if q not in cache: cache[q] = (L1(q), Hm(q))
    return cache[q]
resa = []
for q, n in ta:
    c = ctrl(q, 'mod24', 300)
    Lq, Hq = val(q)
    cv = np.array([val(int(x)) for x in c])
    resa.append(dict(p=q, N1=n, p_mod_840=q % 840, n_ctrl=len(c), L1_q=float((cv[:, 0] < Lq).mean()), h_q=float((cv[:, 1] < Hq).mean())))
out['a_N1_le2'] = resa
La = np.array([x['L1_q'] for x in resa]); Ha = np.array([x['h_q'] for x in resa])
out['a_summary'] = dict(n=len(resa), mean_L1_quantile=float(La.mean()), mean_h_quantile=float(Ha.mean()),
                        frac_L1_q_gt_0_8=float((La > 0.8).mean()), frac_h_q_lt_0_2=float((Ha < 0.2).mean()),
                        frac_either=float(((La > 0.8) | (Ha < 0.2)).mean()))
# (b) scale-free lower tail at p ≡ 1 (24), 1e5..1e8
m24 = (p % 24 == 1) & (p >= 1e5)
tb = []
for i in range(12):
    mb = m24 & (lp >= bins[i]) & (lp < bins[i + 1])
    idx = np.nonzero(mb)[0]
    k = max(3, int(round(0.002 * len(idx))))
    sel = idx[np.argsort(r[idx])[:k]]
    tb += [int(j) for j in sel]
resb = []
refcache = {}
for j in tb:
    q = int(p[j]); b = int(np.searchsorted(bins, lp[j]) - 1)
    if b not in refcache:
        mb = m24 & (lp >= bins[b]) & (lp < bins[b + 1]) & (r > np.quantile(r[m24 & (lp >= bins[b]) & (lp < bins[b + 1])], 0.02))
        c = rng.choice(p[mb], 300, replace=False)
        refcache[b] = np.array([val(int(x)) for x in c])
    cv = refcache[b]; Lq, Hq = val(q)
    resb.append(dict(p=q, N1=int(N1[j]), N1_over_log2=float(r[j]), p_mod_840=q % 840, L1_q=float((cv[:, 0] < Lq).mean()), h_q=float((cv[:, 1] < Hq).mean())))
Lb = np.array([x['L1_q'] for x in resb]); Hb = np.array([x['h_q'] for x in resb])
# random-control baseline: same procedure applied to random p ≡ 1 (24) from the reference bins
base = []
for b, cv in refcache.items():
    mb = m24 & (lp >= bins[b]) & (lp < bins[b + 1])
    for q in rng.choice(p[mb], 20, replace=False):
        Lq, Hq = val(int(q)); base.append(((cv[:, 0] < Lq).mean(), (cv[:, 1] < Hq).mean()))
base = np.array(base)
out['b_tail'] = resb
out['b_summary'] = dict(n=len(resb), mean_L1_quantile=float(Lb.mean()), mean_h_quantile=float(Hb.mean()),
                        frac_L1_q_gt_0_8=float((Lb > 0.8).mean()), frac_h_q_lt_0_2=float((Hb < 0.2).mean()),
                        corr_L1q_hq=float(np.corrcoef(Lb, Hb)[0, 1]),
                        baseline_random_n=len(base), baseline_mean_L1_q=float(base[:, 0].mean()), baseline_mean_h_q=float(base[:, 1].mean()),
                        baseline_frac_L1_q_gt_0_8=float((base[:, 0] > 0.8).mean()), baseline_frac_h_q_lt_0_2=float((base[:, 1] < 0.2).mean()))
json.dump(out, open(os.path.join(D, 'quantiles.json'), 'w'), indent=1)
print(json.dumps(out['a_summary']), json.dumps(out['b_summary']))
for x in resa: print(x)
