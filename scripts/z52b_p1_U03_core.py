"""z52b Pass-1 U03 core: divisor-form counts R_C(p) = #{d | 4Cp+1 : d = -1 mod 4C} (FRONTIER §2.1 divisor form).
R_K(p) = sum_{C<=K} R_C(p); for p <= PFULL the C-range is the full range C <= p//4+1 (so R(p)=0 there is exact, up to
the C-bound argument: d*e = 4Cp+1 with d,e >= 4C-1 forces C <= ~p/4).
Output: data/z52b/pass1/U03/core_P{P}_K{K}.npz  (primes, Rc matrix [prime x C], Kp per prime).
Usage: uv run --with numpy python scripts/z52b_p1_U03_core.py P K PFULL
"""
import sys, numpy as np, time
P, K, PFULL = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
def kp(p): return p // 4 + 1 if p <= PFULL else K
# primes
s = np.ones(P + 1, bool); s[:2] = False
for i in range(2, int(P ** 0.5) + 1):
    if s[i]: s[i*i::i] = False
primes = [int(x) for x in np.nonzero(s)[0] if x % 4 == 1]
M = max(4 * kp(p) * p + 1 for p in primes) + 1
spf = np.zeros(M + 1, np.int32)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == 0:
        seg = spf[i*i::i]; m = seg == 0; seg[m] = i
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx  # spf[n]=n for primes/1
spf = spf.tolist() if M < 5_000_000 else spf
def factor(n):
    f = {}
    while n > 1:
        q = int(spf[n]); f[q] = f.get(q, 0) + 1; n //= q
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
Kmax = max(kp(p) for p in primes)
Rc = np.zeros((len(primes), Kmax), np.int32)
t0 = time.time()
for i, p in enumerate(primes):
    for C in range(1, kp(p) + 1):
        N = 4 * C * p + 1; m = 4 * C
        Rc[i, C-1] = sum(1 for d in divisors(factor(N)) if d % m == m - 1)
np.savez_compressed(f"data/z52b/pass1/U03/core_P{P}_K{K}_F{PFULL}.npz", primes=np.array(primes), Rc=Rc,
                    kp=np.array([kp(p) for p in primes]))
print("primes", len(primes), "time", round(time.time() - t0, 1))
