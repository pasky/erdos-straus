"""R213 from-scratch coverage check of CAP_TWO §3 (k = 1 cap-<=2 shots, least g per odd n <= N, g <= G).
Per modulus g = 4K - 1 (ascending), enumerate Q1 = prod_{l | K, l odd} l^{e_l}, e_l in {0,1,2}; the shot condition
g | n + 4(K Q1)^2 is n = -Q1^2/4 (mod g); gcd(Q, n) = 1 is gcd(n, K Q1) = gcd(n, K) = 1.
Tracks least g overall, least g with Q1 squarefree (cap 1), least g with Q1 = 1 (ES k=1). Then re-verifies the
least shot of every prime exactly (Fractions, Def 1.1)."""
import sys
import numpy as np
from fractions import Fraction
from math import gcd, isqrt
from itertools import product
N = int(sys.argv[1]); G = int(sys.argv[2])
KM = (G + 1)//4 + 1
spf = np.arange(KM + 1)
for i in range(2, isqrt(KM) + 1):
    if spf[i] == i:
        s = spf[i*i::i]; m = s == np.arange(i*i, KM + 1, i); s[m] = i
INF = 1 << 62
least = np.full(N + 1, INF, dtype=np.int64); lq1 = np.zeros(N + 1, dtype=np.int64)
lsqf = np.full(N + 1, INF, dtype=np.int64); les = np.full(N + 1, INF, dtype=np.int64); lb2 = np.full(N + 1, INF, dtype=np.int64)
for g in range(3, G + 1, 4):
    K = (g + 1)//4
    ps = []; k = K
    while k > 1:
        p = int(spf[k]); k //= p
        if p != 2 and (not ps or ps[-1] != p): ps.append(p)
    inv4 = pow(4, -1, g)
    for ex in product((0, 1, 2), repeat=len(ps)):
        Q1 = 1
        for p, e in zip(ps, ex): Q1 *= p**e
        n0 = (-Q1*Q1*inv4) % g
        if n0 > N: continue
        idx = np.arange(n0, N + 1, g)
        idx = idx[(idx & 1) == 1]; idx = idx[idx >= 3]
        idx = idx[np.gcd(idx, K) == 1]
        if idx.size == 0: continue
        new = least[idx] == INF
        least[idx[new]] = g; lq1[idx[new]] = Q1
        if max(ex, default=0) == 2:
            s = lb2[idx] == INF; lb2[idx[s]] = g
        if max(ex, default=0) <= 1:
            s = lsqf[idx] == INF; lsqf[idx[s]] = g
            if Q1 == 1:
                s = les[idx] == INF; les[idx[s]] = g
# primes
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, isqrt(N) + 1):
    if sieve[i]: sieve[i*i::i] = False
pr = np.nonzero(sieve)[0]; pr = pr[pr >= 3]
unc = pr[least[pr] == INF]
print("primes 3..%d: %d, uncovered: %d %s" % (N, pr.size, unc.size, unc[:10]))
cov = pr[least[pr] < INF]
print("max least g over primes: %d at p = %s" % (least[cov].max(), cov[least[cov] == least[cov].max()]))
print("least g of p=379:", least[379] if N >= 379 else None, "Q1:", lq1[379] if N >= 379 else None)
needB = cov[lsqf[cov] > least[cov]]
print("primes whose least shot needs B>1 (no cap-1 shot at least g):", needB.size)
p1 = cov[cov % 4 == 1]
es = (les[p1] == least[p1]).sum(); b1 = ((lsqf[p1] == least[p1]) & (les[p1] > least[p1])).sum()
print("p = 1 mod 4: %d; least shot ES: %d, B=1<c: %d, B>1: %d" % (p1.size, es, b1, p1.size - es - b1))
for lo in range(0, 7):
    sel = cov[(cov >= 10**lo) & (cov < 10**(lo+1))]
    if sel.size: print("  decade 10^%d: max least g %d" % (lo, least[sel].max()))
sq = np.array([m*m for m in range(3, isqrt(N) + 1, 2)])
print("odd squares covered:", int((least[sq] < INF).sum()), "of", sq.size)
odd = np.arange(3, N + 1, 2); ns = odd[~np.isin(odd, sq)]
uc = ns[least[ns] == INF]
print("odd non-squares uncovered:", uc.size, " of which 3|n:", int((uc % 3 == 0).sum()))
# exact re-verification of every prime's least shot
fail = 0
for p in cov.tolist():
    g = int(least[p]); Q1 = int(lq1[p]); K = (g+1)//4; Q = K*Q1
    assert (p + 4*Q*Q) % g == 0 and gcd(Q, p) == 1
    m = (p + 4*Q*Q)//g; x = (p + m)//4; y = p*(g+1)//4; z = Fraction(p*x*(g+1), 4*Q*Q)
    ok = Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1/z
    d = z.denominator; q = isqrt(d)
    r = q
    while gcd(r, y) > 1: r //= gcd(r, y)
    ok = ok and q*q == d and q % 2 == 1 and gcd(q, p) == 1 and r == 1 and all(q % (l**3) for l in range(3, 2000, 2))
    # v_l(q) <= 2: q | Q1 which has exponents <= 2 by construction; check q == Q1 and Q1 | rad(K)^2
    ok = ok and q == Q1 and (K*K) % Q1 == 0
    fail += not ok
print("exact re-verification failures:", fail)
# extra stats (R213)
h = {d: int(((least[cov] >= 10**d) & (least[cov] < 10**(d+1))).sum()) for d in range(0, 7)}
print("least-g decade histogram (primes):", h)
print("primes with NO cap-1 (B = 1) k=1 shot at any g <= G:", int((lsqf[cov] == INF).sum()))
# ties: primes whose least g carries both a B=1 and a B>1 shot
tie = []
tie = cov[(least[cov] == lsqf[cov]) & (least[cov] == lb2[cov])]
print('primes with a B=1 AND a B>1 shot at the least g (tie):', tie.size, tie[:10], least[tie[:10]])
