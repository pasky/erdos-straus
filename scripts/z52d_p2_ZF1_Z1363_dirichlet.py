"""Z1363 (ZF1 finisher): Dirichlet series F(s) = Σ f(n) n^{-s} of the ES counting function, n <= 3·10^4.
f(n) = U(n) (unordered x<=y<=z) and O(n) (ordered) from scripts/z52b_fingerprint_count.c (m=4, all n; data file
data/z52b/pass2/ZF1/Z1363/fn_3e4.txt.gz: n U O).  Tests of the item's question 'is F/ζ³ or F/(ζ² L(s,χ₋₄)) nice':
 (a) partial sums at s = 2, 3 with an explicit tail estimate from the local mean of f/log³n;
 (b) Euler-product test: g = f * μ*μ*μ (resp. f * μ*μ*(μχ₋₄)) are the coefficients of F/ζ³ (resp. F/(ζ²L));
     F/ζ³ has an Euler product iff g is multiplicative -> test g(mn) = g(m)g(n) on coprime pairs mn <= N;
 (c) growth of g (bounded? sign pattern) and of Σ g(n)/n^2.
Run: uv run --with numpy python scripts/z52d_p2_ZF1_Z1363_dirichlet.py
"""
import numpy as np, json, os, gzip, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data/z52b/pass2/ZF1/Z1363')
A = np.loadtxt(gzip.open(os.path.join(D, 'fn_3e4.txt.gz'), 'rt'), dtype=np.int64)
N = int(A[:, 0].max())
fU = np.zeros(N + 1); fO = np.zeros(N + 1)
fU[A[:, 0]] = A[:, 1]; fO[A[:, 0]] = A[:, 2]
n = np.arange(N + 1, dtype=float)
# Möbius
mu = np.ones(N + 1, dtype=np.int64); isp = np.ones(N + 1, bool); isp[:2] = False
for p in range(2, N + 1):
    if isp[p]:
        isp[2 * p::p] = False
        mu[p::p] *= -1
        mu[p * p::p * p] = 0
mu[0] = 0
chi = np.zeros(N + 1); chi[1::4] = 1; chi[3::4] = -1
def dconv(a, b):
    c = np.zeros(N + 1)
    for d in range(1, N + 1):
        if a[d] == 0: continue
        c[d::d][: (N // d)] += a[d] * b[1: N // d + 1]
    return c
muf = mu.astype(float)
out = {'N': N}
for name, f in (('U', fU), ('O', fO)):
    r = {}
    for s in (2.0, 3.0):
        part = {}
        for M in (3000, 10000, 30000 if N >= 30000 else N):
            S = float((f[1:M + 1] / n[1:M + 1] ** s).sum())
            # tail: local mean c = mean f/log^3 n over (M/2, M]; tail ≈ c ∫_M^∞ log^3 x x^{-s} dx
            w = slice(M // 2 + 1, M + 1); c = float((f[w] / np.log(n[w]) ** 3).mean())
            L = math.log(M)
            if s == 2.0: tail = c * (L ** 3 + 3 * L ** 2 + 6 * L + 6) / M
            else: tail = c * (L ** 3 / 2 + 3 * L ** 2 / 4 + 3 * L / 4 + 3 / 8) / M ** 2
            z = {2.0: math.pi ** 2 / 6, 3.0: 1.2020569031595942}[s]
            part[str(M)] = dict(partial=S, tail_est=tail, F_est=S + tail, F_over_zeta3=(S + tail) / z ** 3, c_local=c)
        r[f's={int(s)}'] = part
    # Euler-product (multiplicativity) tests
    g3 = dconv(dconv(dconv(f, muf), muf), muf)
    g2L = dconv(dconv(dconv(f, muf), muf), muf * chi)
    for gname, g in (('F/zeta^3', g3), ('F/(zeta^2 L)', g2L)):
        tot = 0; eq = 0; rel = []
        M = 3000
        for a in range(2, M + 1):
            for b in range(a + 1, N // a + 1):
                if math.gcd(a, b) != 1: continue
                tot += 1
                lhs = g[a * b]; rhs = g[a] * g[b]
                if abs(lhs - rhs) < 1e-9: eq += 1
                if tot <= 200000: rel.append((lhs, rhs))
        rel = np.array(rel)
        cc = float(np.corrcoef(rel[:, 0], rel[:, 1])[0, 1])
        gp = g[isp]
        r[gname] = dict(coprime_pairs_tested=tot, frac_exact_multiplicative=eq / tot, corr_g_mn_vs_gm_gn=cc,
                        g_first=[int(round(x)) for x in g[1:31]], max_abs_g_le_N=float(np.abs(g[1:]).max()),
                        frac_g_zero=float((np.abs(g[1:]) < 1e-9).mean()),
                        mean_g_prime_over_log2p_by_range={str(lo): float((g[lo:2 * lo][isp[lo:2 * lo]] / np.log(n[lo:2 * lo][isp[lo:2 * lo]]) ** 2).mean()) for lo in (100, 1000, 10000) if 2 * lo <= N + 1},
                        partial_G2={str(M): float((g[1:M + 1] / n[1:M + 1] ** 2).sum()) for M in (1000, 3000, 10000, N)})
    out[name] = r
json.dump(out, open(os.path.join(D, 'dirichlet.json'), 'w'), indent=1)
print(json.dumps(out, indent=1)[:6000])
