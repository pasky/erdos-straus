"""z52b Pass-1 U03: per-(p,C) features for primes p=1 mod 4, p<=P, C<=K.
N=4Cp+1; R = #{d|N : d=-1 (4C)}; Omega(N), omega(N), largest prime factor P+(N), flag hasm1 = some prime q|N with q=-1 (4C).
Output data/z52b/pass1/U03/feat_P{P}_K{K}.npz. Usage: uv run --with numpy python scripts/z52b_p1_U03_feat.py P K
"""
import sys, numpy as np, time
P, K = int(sys.argv[1]), int(sys.argv[2])
s = np.ones(P + 1, bool); s[:2] = False
for i in range(2, int(P ** 0.5) + 1):
    if s[i]: s[i*i::i] = False
primes = [int(x) for x in np.nonzero(s)[0] if x % 4 == 1]
M = 4 * K * P + 2
spf = np.zeros(M + 1, np.int32)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == 0:
        seg = spf[i*i::i]; seg[seg == 0] = i
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx
spf = spf.tolist()
def factor(n):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
NP, t0 = len(primes), time.time()
R = np.zeros((NP, K), np.int32); Om = np.zeros((NP, K), np.int16); om = np.zeros((NP, K), np.int16)
Pplus = np.zeros((NP, K), np.int64); hm1 = np.zeros((NP, K), bool)
for i, p in enumerate(primes):
    for C in range(1, K + 1):
        N = 4 * C * p + 1; m = 4 * C
        f = factor(N)
        R[i, C-1] = sum(1 for d in divisors(f) if d % m == m - 1)
        Om[i, C-1] = sum(f.values()); om[i, C-1] = len(f); Pplus[i, C-1] = max(f)
        hm1[i, C-1] = any(q % m == m - 1 for q in f)
np.savez_compressed(f"data/z52b/pass1/U03/feat_P{P}_K{K}.npz", primes=np.array(primes), R=R, Om=Om, om=om,
                    Pplus=Pplus, hm1=hm1)
print("done", NP, round(time.time() - t0, 1))
