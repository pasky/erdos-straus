# Z0051 analysis: does N_II(P) (FF Type II count, q=3) depend on class-number data h(P) = L(1,chi_P),
# or on the BM-type pair sum T(P)?  Within-class (P mod A) correlations; comparison with residue model.
import numpy as np, sys, glob, os
D = 'data/z52b/pass2/ZF1/Z0051'
for fn in sorted(glob.glob(D + '/q3_A*_n*.txt')):
    a = np.loadtxt(fn)
    nii, h, T, key = a[:, 1], a[:, 2], a[:, 3], a[:, 4].astype(int)
    n = int(fn.split('_n')[1].split('.')[0]); g = (n - 1) // 2
    L1 = h / 3**g                     # L(1/q... normalised): h/q^g = L(q^{-1/2}) scale ~ L(1,chi)
    # remove class means (residue class of P mod A)
    def dm(x):
        y = x.copy()
        for k in np.unique(key):
            m = key == k; y[m] -= x[m].mean()
        return y
    r_res = 1 - dm(nii).var() / nii.var()
    c_h = np.corrcoef(dm(nii), dm(L1))[0, 1]
    c_T = np.corrcoef(dm(nii), dm(T))[0, 1]
    c_L2 = np.corrcoef(dm(nii), dm(L1**2))[0, 1]
    c_hT = np.corrcoef(dm(T), dm(L1**2))[0, 1]
    # linear regression of nii on class dummies + T
    print(f"{os.path.basename(fn)}: #P={len(nii)} meanNII={nii.mean():.2f} sd={nii.std():.2f} NII0={int((nii==0).sum())} "
          f"R2(class P mod A)={r_res:.3f} | within-class corr(NII,h/q^g)={c_h:+.3f} corr(NII,(h/q^g)^2)={c_L2:+.3f} "
          f"corr(NII,T)={c_T:+.3f} corr(T,(h/q^g)^2)={c_hT:+.3f} | h range {int(h.min())}..{int(h.max())}")
    # exact-identity test: is NII a function of (class, h)?  count groups with same (key,h) but different NII
    from collections import defaultdict
    grp = defaultdict(set)
    for k, hh, v in zip(key, h, nii): grp[(k, hh)].add(v)
    multi = sum(1 for s in grp.values() if len(s) > 1)
    print(f"   (class,h) groups={len(grp)}, groups with >1 distinct N_II value={multi}")

# --- control: is the h-dependence just the small-prime Legendre data (P mod deg-1 primes)?  Demean by
# (P mod A, chi_P(T+c) for c = 0,1,2, chi_P at the 3 monic irreducible quadratics) and recompute corr(NII, h).
print("--- refined control: classes = (P mod A, Legendre symbols of P at all monic irreducibles of degree <= 2)")
def leg_val(v):  # Legendre on F_3
    return 0 if v % 3 == 0 else (1 if v % 3 == 1 else -1)
quad = [(1, 0, 1), (1, 1, 2), (1, 2, 2)]  # T^2+1, T^2+T+2, T^2+2T+2 (monic irreducible over F_3)
def polymod(P, M):  # coeffs low->high
    r = P[:]; m = len(M) - 1
    for i in range(len(r) - 1, m - 1, -1):
        c = r[i]
        if c:
            for j in range(m + 1): r[i - m + j] = (r[i - m + j] - c * M[j]) % 3
    return r[:m]
for fn in sorted(glob.glob(D + '/q3_A*_n*.txt')):
    a = np.loadtxt(fn); n = int(fn.split('_n')[1].split('.')[0]); g = (n - 1) // 2
    nii, h, key = a[:, 1], a[:, 2] / 3**g, a[:, 4].astype(int)
    keys = []
    for idx, k in zip(a[:, 0].astype(int), key):
        P = [(idx // 3**i) % 3 for i in range(n)] + [1]
        l1 = tuple(leg_val(sum(P[i] * c**i for i in range(n + 1))) for c in range(3))
        # quadratic residue of P mod irreducible quadratic Q: (P mod Q)^{(9-1)/2} in F_9 -> use brute norm test
        l2 = []
        for Qp in quad:
            Ml = [Qp[2], Qp[1], Qp[0]]
            r = polymod(P, Ml)
            sq = set()
            for x0 in range(3):
                for x1 in range(3):
                    s = polymod([0, 0, 0] if False else [(x0 * x0) % 3, (2 * x0 * x1) % 3, (x1 * x1) % 3], Ml)
                    sq.add(tuple(s))
            l2.append(0 if r == [0, 0] else (1 if tuple(r) in sq else -1))
        keys.append((k,) + l1 + tuple(l2))
    keys = np.array([hash(t) for t in keys])
    def dm2(x):
        y = x.copy()
        for k in np.unique(keys):
            m = keys == k; y[m] -= x[m].mean()
        return y
    ncls = len(np.unique(keys))
    print(f"{os.path.basename(fn)}: classes={ncls} R2(classes)={1 - dm2(nii).var() / nii.var():.3f} "
          f"within-class corr(NII,h/q^g)={np.corrcoef(dm2(nii), dm2(h))[0, 1]:+.3f}; residual sd of h/q^g within class "
          f"{dm2(h).std():.3f} vs total {h.std():.3f}")
