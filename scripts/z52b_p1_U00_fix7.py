# z52b pass1 U00 fix (7): proxies for underspecified items.
import sys, json, math
import numpy as np
sys.path.insert(0, 'scripts')
from z52b_p1_U00_solver import solutions
from cypari2 import Pari
from sympy import primerange
from collections import Counter
pari = Pari(); pari.allocatemem(10**9)
def divisors_of(N):
    f = pari.factor(N); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
out = {}
# Z1173: optimal transport (1-Wasserstein on Z/8 cyclic? use linear |i-j| on residues 0..7) between the histogram of
# witness divisors a (a ≡ -1 mod 4C, C ≤ 200) and of ALL divisors of 4Cp+1, mod 8, for p in {409, 2521, 10009}.
def w1(h1, h2):
    h1 = h1 / h1.sum(); h2 = h2 / h2.sum(); c = np.cumsum(h1 - h2); return float(np.abs(c).sum())
rows = {}
for p in [409, 2521, 10009]:
    hw = np.zeros(8); ha = np.zeros(8)
    for C in range(1, 201):
        N = 4 * C * p + 1; M = 4 * C; ds = divisors_of(N)
        for a in ds:
            if 1 < a < N:
                ha[a % 8] += 1
                if a % M == M - 1: hw[a % 8] += 1
    rows[p] = {'W1_witness_vs_all_mod8': round(w1(hw + 1e-9, ha + 1e-9), 4), 'witness_hist': hw.astype(int).tolist(), 'all_hist': ha.astype(int).tolist()}
out['Z1173'] = rows
# Z1240: latent structure: PCA (SVD) of the design matrix of Legendre symbols (q/p), q ≤ 79 (prime), for primes p ≡ 1 (4) ≤ 3e4,
# response = centred log(U+1) residual after log p, loglog p. Report variance shares and top loadings (q).
from math import log
F4 = np.loadtxt('/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
Ud = dict(zip(F4[:, 0].tolist(), F4[:, 1].tolist()))
P = [q for q in primerange(5, 30001) if q % 4 == 1]
Qs = [q for q in primerange(3, 80)]
X = np.array([[pari.kronecker(q, p) if True else 0 for q in Qs] for p in P], float)
y = np.log(np.array([Ud[p] for p in P], float) + 1)
Z = np.column_stack([np.ones(len(P)), np.log(P), np.log(np.log(P))])
b = np.linalg.lstsq(Z, y, rcond=None)[0]; res = y - Z @ b
Xc = X - X.mean(axis=0)
Uu, S, Vt = np.linalg.svd(Xc, full_matrices=False)
share = (S ** 2 / (S ** 2).sum())[:5]
loads = {int(i): [(Qs[j], round(float(Vt[i, j]), 2)) for j in np.argsort(-np.abs(Vt[i]))[:4]] for i in range(3)}
corr = [round(float(np.corrcoef(Uu[:, i], res)[0, 1]), 3) for i in range(3)]
out['Z1240'] = {'variance_shares_top5': [round(float(s), 3) for s in share], 'top_loadings_PC1_3': loads, 'corr_PC_with_residual': corr}
# Z1570 / Z1826: multiplicative energy of the witness divisor set mod p, p = 409 (R-zero) vs control 401 and 433:
# E× = #{(a,b,c,d) ∈ D^4 : ab ≡ cd (mod p)} / |D|^3 ; D = witness divisors a (a ≡ -1 mod 4C, C ≤ 300) reduced mod p
def energy(p):
    D = set()
    for C in range(1, 301):
        N = 4 * C * p + 1; M = 4 * C
        for a in divisors_of(N):
            if 1 < a < N and a % M == M - 1: D.add(a % p)
    D = sorted(D)
    if len(D) < 2: return len(D), None
    cnt = Counter((a * b) % p for a in D for b in D)
    E = sum(v * v for v in cnt.values())
    return len(D), round(E / len(D) ** 3, 4)
out['Z1570_energy'] = {str(p): energy(p) for p in [409, 401, 433, 577, 1009]}
# Z1610: exceptional primes (no witness at C ≤ 200) vs residue classes mod 24: frequency vs all primes ≡1 mod 4
exc = []; allp = []
for p in [q for q in primerange(5, 20000) if q % 4 == 1]:
    w = False
    for C in range(1, 201):
        N = 4 * C * p + 1; M = 4 * C
        if any(1 < a < N and a % M == M - 1 for a in divisors_of(N)): w = True; break
    allp.append(p)
    if not w: exc.append(p)
out['Z1610'] = {'n_primes': len(allp), 'n_exceptional_C<=200': len(exc), 'exceptional': exc[:30],
                'mod24_counts_exceptional': dict(Counter(p % 24 for p in exc)), 'mod24_counts_all': dict(Counter(p % 24 for p in allp))}
# Z1960: Hypothesis-H record primes from A400619 (available records): Type I-type stress via U(p)/log^3 p
rec = [73, 1129, 1201, 21169]
out['Z1960'] = {str(p): {'U': len(solutions(p)), 'U/log3p': round(len(solutions(p)) / math.log(p) ** 3, 3)} for p in rec}
out['Z1960']['all_1mod4_mean_U/log3(p<=3e4) (from f4)'] = round(float(np.mean([Ud[p] / math.log(p) ** 3 for p in P])), 3)
# Z2011: σ2-level sets: M = xy+yz+zx for solutions of p: fraction with p | M (identity: 4xyz = p·M)
tot = 0; divM = 0
for p in [q for q in primerange(5, 1000) if q % 4 == 1]:
    for t in solutions(p):
        x, y, z = t; M = x * y + y * z + z * x; tot += 1
        if M % p == 0: divM += 1
out['Z2011'] = {'solutions': tot, 'frac_p_divides_M': round(divM / tot, 4)}
json.dump(out, open('data/z52b/pass1/U00/fix7.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str)[:4000])
