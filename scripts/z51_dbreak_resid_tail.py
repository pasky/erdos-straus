# z51 dbreak round 4: negative tail of the residual R. (1) Exact independent-model law of R by convolution on a grid,
# compared with the empirical histogram of an exact run. (2) Structure of the most negative n (NEG lines): squarefree
# kernel, quadratic profile on the band, number of hits; compared with random n from the same range.
# Usage: uv run --with numpy --with sympy python scripts/z51_dbreak_resid_tail.py data/z51_dbreak/resid_exact_bX_NY.txt
import sys, re, math, random
import numpy as np
from sympy import factorint, primerange, divisor_count, legendre_symbol

path = sys.argv[1]
lines = open(path).read().splitlines()
hdr = lines[0]
N = int(re.search(r'N=(\d+)', hdr).group(1)); y = float(re.search(r'y=([0-9.]+)', hdr).group(1)); z = float(re.search(r'z=([0-9.]+)', hdr).group(1))
B = [l for l in primerange(int(y) + 1, int(z) + 1) if l % 4 == 3]
cs = {l: int(divisor_count((l + 1) // 4)) / (l - 1) for l in B}
mu = sum(cs.values())
# (1) model law: R = H - D, H = number of hits (integer), D = 2*sum of c over non-residue primes. Exact DP for
# P(H=k), E[D; H=k], E[D^2; H=k]; given H = k, D is treated as Gaussian with those conditional moments
# (its spread is sqrt(sum c^2), small). (A grid DP would round the tiny drifts -2c to 0.)
KM = 200
Pk = np.zeros(KM); Mk = np.zeros(KM); Sk = np.zeros(KM); Pk[0] = 1.0
for l in B:
    c = cs[l]; w = round(c * (l - 1)); pnr = (l - 1) / (2 * l); ph = w / l; p0 = 1 - pnr; p1 = pnr - ph; p2 = ph
    sP = np.roll(Pk, 1); sP[0] = 0; sM = np.roll(Mk, 1); sM[0] = 0; sS = np.roll(Sk, 1); sS[0] = 0
    nP = (p0 + p1) * Pk + p2 * sP
    nM = p0 * Mk + p1 * (Mk + 2 * c * Pk) + p2 * (sM + 2 * c * sP)
    nS = p0 * Sk + p1 * (Sk + 4 * c * Mk + 4 * c * c * Pk) + p2 * (sS + 4 * c * sM + 4 * c * c * sP)
    Pk, Mk, Sk = nP, nM, nS
def model_cdf(x):
    tot = 0.0
    for k in range(KM):
        if Pk[k] < 1e-300: continue
        m = Mk[k] / Pk[k]; v = max(Sk[k] / Pk[k] - m * m, 1e-18); s = math.sqrt(v)
        # R <= x  <=>  D >= k - x
        tot += Pk[k] * 0.5 * math.erfc((k - x - m) / (s * math.sqrt(2)))
    return tot
hist = {}
for l in lines:
    if l.startswith('HIST '):
        _, v, c = l.split(); hist[float(v)] = int(c)
tot = sum(hist.values())
print(hdr); print(f"mu={mu:.4f}")
print("threshold  P_emp(R<=x)  P_model(R<=x)  ratio")
for x in [-0.25 * mu, -0.5 * mu, -0.75 * mu, -mu, -1.25 * mu]:
    pe = sum(c for v, c in hist.items() if v + 0.02 <= x) / tot
    pm = model_cdf(x)
    print(f"{x:8.3f}  {pe:.3e}  {pm:.3e}  {pe/pm if pm>0 else float('nan'):.3f}")
# (2) structure of the most negative n
neg = [(int(l.split()[1]), float(l.split()[2])) for l in lines if l.startswith('NEG ')]
def kernel(n):
    k = 1
    for p, e in factorint(n).items():
        if e % 2: k *= p
    return k
def profile(n):
    nr = sum(1 for l in B if n % l and legendre_symbol(n % l, l) == -1)
    return nr / len(B)
rnd = random.Random(1); base = []
while len(base) < len(neg):
    n = 8 * rnd.randrange(1, (N - 1) // 8) + 1
    if math.isqrt(n) ** 2 != n: base.append(n)
for name, ns in (("most negative", [n for n, _ in neg]), ("random", base)):
    ks = [kernel(n) for n in ns]; pr = [profile(n) for n in ns]
    small = sum(1 for k in ks if k <= 10 ** 4) / len(ks)
    print(f"{name}: count {len(ns)}  frac kernel<=1e4 {small:.3f}  median kernel {sorted(ks)[len(ks)//2]}  mean nonres-fraction on band {sum(pr)/len(pr):.3f}")
print("most negative examples:", sorted(neg, key=lambda t: t[1])[:8])
