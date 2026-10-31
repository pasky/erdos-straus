"""z52d audit A3, Z1445: 'prime-divisor certificate' = C such that 4Cp+1 has a PRIME factor q = -1 (mod 4C)
(<=> a (★) triple (u,B,C) with 4uC-1 prime).  Sieve over m = 4uC-1 = 3 (4), u | (m+1)/4: hits p = k m - u (k>=1).
Compare min C over prime-m hits (Cp) with min C over all hits (C*) for primes p = 1 (4) <= X."""
import sys, numpy as np
X = int(sys.argv[1])
M = (4 * X + 1) // 3 + 2
isp = np.ones(M + 1, bool); isp[:2] = False
for i in range(2, int(M ** 0.5) + 1):
    if isp[i]: isp[i * i::i] = False
BIG = np.int32(2**31 - 1)
call = np.full(X + 1, BIG, np.int32); cpr = np.full(X + 1, BIG, np.int32)
cnt_all = np.zeros(X + 1, np.int32); cnt_pr = np.zeros(X + 1, np.int32)
# divisors of K=(m+1)/4 via smallest-prime-factor table
Kmax = (M + 1) // 4 + 1
spf = np.zeros(Kmax + 1, np.int64)
for i in range(2, Kmax + 1):
    if spf[i] == 0:
        spf[i::i][spf[i::i] == 0] = i
def divs(K):
    ds = [1]
    while K > 1:
        q = int(spf[K]); e = 0
        while K % q == 0: K //= q; e += 1
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds
for m in range(3, M + 1, 4):
    K = (m + 1) // 4
    pm = isp[m]
    for u in divs(K):
        start = m - u
        if start > X: continue
        C = K // u
        sl = slice(start, X + 1, m)
        np.minimum(call[sl], C, out=call[sl]); cnt_all[sl] += 1
        if pm:
            np.minimum(cpr[sl], C, out=cpr[sl]); cnt_pr[sl] += 1
P = np.nonzero(isp[:X + 1])[0]; P = P[P % 4 == 1]
nostar = P[call[P] == BIG]; nopr = P[cpr[P] == BIG]
print(f"X={X}: primes p=1(4): {len(P)}; (★) fails at {len(nostar)}: {nostar.tolist()}")
print(f"no prime-divisor certificate at {len(nopr)} primes; first 40: {nopr[:40].tolist()}; last 10: {nopr[-10:].tolist()}")
ok = P[cpr[P] != BIG]
print("among certified: Cp == C* share", float(np.mean(cpr[ok] == call[ok])), " mean C*", float(call[ok].mean()), "mean Cp", float(cpr[ok].mean()), "max Cp", int(cpr[ok].max()), "at p", int(ok[np.argmax(cpr[ok])]))
print("mean R(p) (ordered triples)", float(cnt_all[P].mean()), " mean prime-m hits", float(cnt_pr[P].mean()), " share prime", float(cnt_pr[P].sum() / cnt_all[P].sum()))
for lo, hi in [(1, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 10**7)]:
    sel = (P >= lo) & (P < hi)
    if sel.sum(): print(f"  [{lo},{hi}): primes {sel.sum()}, no-prime-cert {int((cpr[P[sel]] == BIG).sum())}, (★)-fail {int((call[P[sel]] == BIG).sum())}")
np.save(f"data/z52d/audit/A3/z1445_noprime_{X}.npy", nopr)
