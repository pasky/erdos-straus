"""z52b Pass-1 U03 analyses on feat_P100000_K100.npz (R_C(p)=#{d|4Cp+1, d=-1 (4C)}; S_C(p)= [R_C(p)=0])."""
import numpy as np, math, json
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64); Om = d["Om"]; om = d["om"]; Pp = d["Pplus"]; hm1 = d["hm1"]
NP, K = R.shape
S = (R == 0)
print("primes", NP, "max p", pr[-1])
# A. marginal failure densities
print("A dens S_C:", {C: round(float(S[:, C-1].mean()), 4) for C in [1, 2, 3, 4, 6, 8, 10, 20, 30, 100]})
# B. Z1562 joint failure C=1,2 and C=1..6 pairs
for a, b in [(1, 2), (1, 4), (2, 4), (1, 3), (2, 3)]:
    j = (S[:, a-1] & S[:, b-1]).mean(); print(f"B joint S{a}&S{b}: {j:.4f} vs product {S[:,a-1].mean()*S[:,b-1].mean():.4f}")
# C. Z1816 correlation of S_C, C<=30
X = S[:, :30].astype(float); Cm = np.corrcoef(X.T); off = Cm[~np.eye(30, dtype=bool)]
print("C corr S_C C<=30: max off", round(float(off.max()), 3), "min", round(float(off.min()), 3), "mean|.|", round(float(np.abs(off).mean()), 4))
# D. Z1578 count of S1&S2 vs X
for Xl in [10**3, 10**4, 3*10**4, 10**5]:
    m = pr <= Xl
    print("D X", Xl, "#S1&S2", int((S[m, 0] & S[m, 1]).sum()), "#S1", int(S[m, 0].sum()), "#all-C<=10 fail", int(S[m, :10].all(1).sum()))
# E. Z3168 primes failing all C<=K
for Kk in [1, 2, 3, 5, 10, 20, 50, 100]:
    cnt = [int(S[pr <= Xl, :Kk].all(1).sum()) for Xl in [10**3, 10**4, 10**5]]
    print("E K", Kk, "counts <=1e3,1e4,1e5:", cnt)
# F. Z3072/Z1996 rates of R_C>0 by Omega(N), lambda
ok = R > 0
for k in range(1, 9):
    m = Om == k
    if m.sum(): print(f"F Omega={k}: n={int(m.sum())} P(R_C>0)={ok[m].mean():.4f}")
lam = np.where(Om % 2 == 0, 1, -1)
print("F lambda=+1 P", round(float(ok[lam == 1].mean()), 4), " lambda=-1 P", round(float(ok[lam == -1].mean()), 4))
# G. Z3197/Z3087 least C with R_C>0
Cmin = np.array([next((C for C in range(1, K+1) if ok[i, C-1]), 0) for i in range(NP)])
for lo, hi in [(5, 10**3), (10**3, 10**4), (10**4, 10**5)]:
    m = (pr >= lo) & (pr < hi)
    print(f"G p in [{lo},{hi}): median Cmin {np.median(Cmin[m])}, 90% {np.percentile(Cmin[m],90)}, max {Cmin[m].max()}, #Cmin=0 {int((Cmin[m]==0).sum())}")
print("G max Cmin over p<=X:", [(X_, int(Cmin[pr <= X_].max())) for X_ in [10**3, 10**4, 10**5]])
# Z1452: C_min vs sum_{C<=10} omega(4Cp+1)
w10 = om[:, :10].sum(1); ok_m = Cmin > 0
print("Z1452 spearman(Cmin, sum_{C<=10} omega):", round(float(np.corrcoef(np.argsort(np.argsort(Cmin[ok_m])), np.argsort(np.argsort(w10[ok_m])))[0, 1]), 4))
# H. Z3096/Z1447: prime factor in class -1 mod 4C
for C in [1, 2, 3, 5, 10, 25, 50, 100]:
    m = slice(None)
    phi = 2 * (1 if False else 1)
    mC = 4 * C
    # number of units mod 4C
    ph = sum(1 for a in range(1, mC) if math.gcd(a, mC) == 1)
    print(f"H C={C}: P(has prime q=-1 mod 4C)={hm1[:, C-1].mean():.4f}  P(P+(N)=-1 mod 4C)={float(np.mean([ (int(Pp[i,C-1]) % mC)==mC-1 for i in range(NP)])):.4f}  1/phi(4C)={1/ph:.4f}")
# I. Z2907: Omega=2 fraction
print("I Omega=2 frac over (p,C):", round(float((Om == 2).mean()), 4), " Omega=2 & R>0:", round(float((ok & (Om == 2)).sum() / max(1, (Om == 2).sum())), 4))
# K. Z2362 second moment proxy
RK = R.sum(1).astype(float)
for Xl in [10**3, 10**4, 10**5]:
    m = pr <= Xl; X_ = Xl
    print(f"K X={Xl}: sum R_K/(X log^2 X)={RK[m].sum()/(X_*math.log(X_)**2):.4f}  sum R_K^2/(X log^4 X)={(RK[m]**2).sum()/(X_*math.log(X_)**4):.4f}  mean R_K/log^2={RK[m].mean()/math.log(X_)**2:.4f}")
# Z2584: Var/mean^2 over C of R_C for hard primes (R_K small)
v = R.var(1) / np.maximum(R.mean(1), 1e-9) ** 2
hard = RK <= np.percentile(RK, 5); print("Z2584 Var/mean^2 over C: hard(bottom 5%) median", round(float(np.median(v[hard])), 3), " all median", round(float(np.median(v)), 3))
np.savez_compressed("data/z52b/pass1/U03/cmin.npz", primes=pr, Cmin=Cmin, RK=RK)
