"""s9_thinning.py (O271): is the union count U a binomial thinning of the 4-blind word count W?
From s9_words output (p W A B U A1), p == 1 (mod 4). Reports W/log^2 p, the per-class pi = U/W, dispersion index
Var(U|W)/(W pi (1-pi)) in W-bins, and P(U=0) predicted by E[(1-pi)^W] vs observed.  usage: python s9_thinning.py FILE"""
import sys
import numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64); d = d[d[:, 0] % 4 == 1]
p, W, A, B, U = (d[:, i] for i in range(5)); L2 = np.log(p) ** 2
for lo, hi in ((1e5, 3e5), (3e5, 1e6), (1e6, 3e6), (3e6, 1e7)):
    m = (p >= lo) & (p < hi)
    if m.sum() == 0: continue
    print(f"p in [{lo:.0e},{hi:.0e}): n={m.sum()}, mean W/L^2={np.mean(W[m]/L2[m]):.3f}, min W={W[m].min()}, "
          f"q01 W/L^2={np.quantile(W[m]/L2[m],0.01):.3f}, mean U/W={np.mean(U[m]/W[m]):.3f}")
for mod in (8, 3, 5, 7):
    s = ", ".join(f"{r}:{np.mean(U[p % mod == r] / W[p % mod == r]):.3f}" for r in range(mod) if (p % mod == r).sum() > 100)
    print(f"mean U/W by p mod {mod}: {s}")
# dispersion of U given W, within p mod 24 cells and W bins
m = p > 1e5
pi_c = {}
for r in np.unique(p % 24):
    mm = m & (p % 24 == r); pi_c[r] = U[mm].sum() / W[mm].sum()
pi = np.array([pi_c.get(r, np.nan) for r in p % 24])
for wl, wh in ((40, 80), (80, 120), (120, 200), (200, 1000)):
    mm = m & (W >= wl) & (W < wh)
    if mm.sum() < 50: continue
    exp_var = (W[mm] * pi[mm] * (1 - pi[mm])).mean()
    resid = U[mm] - W[mm] * pi[mm]
    print(f"W in [{wl},{wh}): n={mm.sum()}, Var(U - W pi)/E[W pi(1-pi)] = {resid.var()/exp_var:.2f}")
# words come in mirror pairs (t,u,v),(t,v,u) with the same 2-adic type -> effective trials W/2
pred = np.mean((1 - pi[m]) ** (W[m] / 2)); pred_full = np.mean((1 - pi[m]) ** W[m])
print(f"p > 1e5: n={m.sum()}, observed U=0: {(U[m]==0).sum()}, binomial-thinning prediction (W/2 trials) {pred*m.sum():.3g}, (W trials) {pred_full*m.sum():.3g}")
