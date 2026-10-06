"""O53 (EXCEPTIONAL_SPW2 §6): heuristic test of the dual certificate.
psi0 = min-norm element of V_D (span of classes mod d <= D on Z/L0) with
psi0 = 1 on W = [1,N] and psi0 = 0 on the near zone Z = [N-CN, 0] u [N+1, CN+1].
Kernel: psi0(x) = sum_{y in I} beta_y S_D(x - y), S_D(m) = sum_{d<=D} c_d(m)
(Ramanujan sums) = sum_{k | m, k <= D} k M(D/k).
A dual certificate refuting RSPW at N needs psi <= cov_w everywhere off W,
cov_w(x) = sum_e w(e) 1[x mod e in W mod e] (full-line cover, e > CN).
We sample random x in Z/L0 (random big integers) and report the distribution
of psi0(x) and of cov(x) (w uniform on e in (CN, 2CN]).
Usage: python spw2_psi0_test.py N C samples seed"""
import sys, random
import numpy as np

N, C, S, seed = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
random.seed(seed)
D = N // 2
# Mertens function
mu = np.ones(D + 1, dtype=np.int64); mu[0] = 0
isp = np.ones(D + 1, bool); isp[:2] = False
for p in range(2, D + 1):
    if isp[p]:
        isp[2 * p::p] = False
        mu[p::p] *= -1
        mu[p * p::p * p] = 0
M = np.cumsum(mu)
wk = np.array([0] + [k * M[D // k] for k in range(1, D + 1)], dtype=float)  # k*M(D/k)


def SD(m):
    m = abs(int(m))
    if m == 0:
        return float(sum(wk[1:]))  # = Phi(D)
    return float(sum(wk[k] for k in range(1, D + 1) if m % k == 0))


lo, hi = int(N - C * N), int(C * N + 1)
I = np.arange(lo, hi + 1)
A = np.array([[SD(a - b) for b in I] for a in I])
tgt = ((I >= 1) & (I <= N)).astype(float)
beta = np.linalg.solve(A, tgt)
print(f"N={N} D={D} |I|={len(I)} Phi(D)={SD(0):.0f} cond(A)={np.linalg.cond(A):.1f} max|beta|={abs(beta).max():.2e}")
E = [e for e in range(int(C * N) + 1, int(2 * C * N) + 1)]
ks = np.arange(1, D + 1)


def psi(x):
    r = np.array([x % k for k in range(1, D + 1)])  # x mod k
    tot = 0.0
    for b, y in zip(beta, I):
        # k | x - y  <=> r_k == y mod k
        tot += b * wk[1:][(r - (y % ks)) % ks == 0].sum()
    return tot


def cov(x):
    return np.mean([1 <= (x % e) <= N for e in E])


L0bits = int(sum(np.log2(np.arange(2, D + 1)))) + 64
vals = []
for _ in range(S):
    x = random.getrandbits(L0bits)
    vals.append((psi(x), cov(x)))
v = np.array(vals)
print(f"random x: psi mean={v[:,0].mean():.4f} rms={np.sqrt((v[:,0]**2).mean()):.4f} max={v[:,0].max():.4f} "
      f"| cov mean={v[:,1].mean():.4f} min={v[:,1].min():.4f} | frac psi>cov = {(v[:,0] > v[:,1]).mean():.4f} "
      f"| max(psi-cov)={(v[:,0]-v[:,1]).max():.4f}")
# structured: integers x at moderate distance
st = []
for x in list(range(hi + 1, hi + 2000)) + list(range(lo - 2000, lo)):
    st.append((psi(x), cov(x)))
s = np.array(st)
print(f"integers near I: psi max={s[:,0].max():.4f} rms={np.sqrt((s[:,0]**2).mean()):.4f} | frac psi>cov={(s[:,0]>s[:,1]).mean():.4f} "
      f"max(psi-cov)={(s[:,0]-s[:,1]).max():.4f}")
