# TO2 part 8: Z0616 pairwise correlation of C-slice events E_C(p) = [slice C carries a Type-II (star) triple] over primes p≡1 mod 4, p<=1e6
# Z0543 Type-I residue-class coverage by (a,d) grid (upper bound, ignores b>=a), Z0673 Legendre test (d/p) for Type I (a,d)
import numpy as np, json, math
out = {}
M = np.loadtxt('/tmp/mask1e6.txt', dtype=np.int64)
mask = np.zeros(10**6+1, np.int64); mask[M[:,0]] = M[:,1]
s = np.ones(10**6+1, bool); s[:2] = False
for i in range(2, 1001):
    if s[i]: s[i*i::i] = False
P = np.nonzero(s)[0]; P = P[(P % 4 == 1) & (P > 5)]
E = np.array([(mask[P] >> c) & 1 for c in range(8)]).T.astype(float)   # events E_1..E_8
out['n_primes'] = int(len(P))
out['P(E_C)'] = [float(x) for x in E.mean(0)]
C = np.corrcoef(E.T)
out['pearson_matrix_C1_C4'] = np.round(C[:4, :4], 3).tolist()
out['mean_offdiag_corr_C1_8'] = float((C.sum() - 8) / 56)
out['P(no slice 1..8 hit)'] = float((mask[P] == 0).mean())
# conditional on size of p: correlation within windows
for lo, hi in [(5, 10**4), (10**4, 10**5), (10**5, 10**6)]:
    sel = (P >= lo) & (P < hi)
    Cw = np.corrcoef(E[sel].T)
    out[f'corr_E1_E2_window_{lo}_{hi}'] = float(Cw[0, 1]); out[f'corr_E1_E3_window_{lo}_{hi}'] = float(Cw[0, 2])
# Z0543: residue coverage. Type-I divisor condition: f | 4a^2 d + 1, f ≡ -p (mod 4ad) (gcd(f,4ad)=1 automatic)
pp = np.array([int(x) for x in P if int(x) % 24 == 1][:]); 
def divisors(n):
    ds = [1]; x = n; f = 2
    while f*f <= x:
        if x % f == 0:
            e = 0
            while x % f == 0: x //= f; e += 1
            ds = [d*f**k for d in ds for k in range(e+1)]
        f += 1
    if x > 1: ds = ds + [d*x for d in ds]
    return ds
cover = np.zeros(len(pp), bool)
res_hist = []
for D_ in [5, 10, 20, 50]:
    for a_ in range(1, 51):
        for d_ in range(1, D_+1):
            pass
# incremental: grid a<=A, d<=D
Acap, Dcap = 50, 50
classes_cum = {}
cov_at = {}
tbl = {}
covered = np.zeros(len(pp), bool)
step_marks = {5: None, 10: None, 20: None, 50: None}
for d_ in range(1, Dcap+1):
    for a_ in range(1, Acap+1):
        q = 4*a_*d_; N_ = 4*a_*a_*d_ + 1
        S = set((-f) % q for f in divisors(N_) if math.gcd(f, q) == 1)
        if not S: continue
        r = pp % q
        hit = np.isin(r, list(S))
        covered |= hit
    if d_ in step_marks:
        tbl[d_] = float(covered.mean())
out['fraction_p1mod24_covered_by_typeI_grid_d<=D_a<=50'] = tbl
out['n_p1mod24_le_1e6'] = int(len(pp))
json.dump(out, open('data/z52b/pass2/TO2/an8.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
