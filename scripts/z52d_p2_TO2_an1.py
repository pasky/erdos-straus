# TO2 analysis part 1 (items Z0472, Z0481, Z0484, Z0534, Z0628/9, Z0648): uses R(n), minC, minW from z52d_p2_TO2_renum (N=1e7)
import sys, math, json
import numpy as np
sys.path.insert(0, 'scripts')
from z52d_p2_TO2_load import load, primes, N
R, mC, mW = load('/tmp/r1e7.txt')
P = primes(N); P = P[P > 5]
P1 = P[P % 4 == 1]
L2 = np.log(P1.astype(float))**2
out = {}
# --- Z0481: odd-square T1 and prime-level analogue
odd = np.arange(3, N+1, 2)
sq = np.array([m*m for m in range(3, int(N**0.5)+1, 2)])
nonsq_zero = [int(n) for n in odd if R[n] == 0 and int(round(math.sqrt(n)))**2 != n]
out['odd_squares_checked'] = int(len(sq)); out['odd_squares_R_positive'] = int((R[sq] > 0).sum())
out['odd_nonsquare_R0_count'] = len(nonsq_zero); out['odd_nonsquare_R0_first'] = nonsq_zero[:25]
out['primes_1mod4_R0'] = [int(p) for p in P1[R[P1] == 0]]
# --- Z0472/Z0484: families
def stats(sel, name):
    p = P1[sel]; r = R[p]
    if len(p) == 0:
        out[name] = None; return
    x = r / np.log(p.astype(float))**2
    out[name] = dict(count=int(len(p)), R0=int((r == 0).sum()), mean_R_over_log2=float(x.mean()),
                     min_R_over_log2=float(x.min()), argmin=int(p[np.argmin(x)]), median=float(np.median(x)))
allsel = np.ones(len(P1), bool)
stats(allsel, 'all_p1mod4')
stats(P1 % 840 == 1, 'p_1mod840')
sq_near = np.array([abs(int(p) - int(round(math.sqrt(int(p))))**2) for p in P1])
stats(np.array([int(round(math.sqrt(int(p))))**2 for p in P1]) > 0 & (sq_near <= 10) if False else (sq_near <= 10), 'near_square_|p-m^2|<=10')
stats(sq_near <= 2, 'near_square_|p-m^2|<=2')
# p = m^2+1 exactly
stats(sq_near == 1, 'p=m^2+1')
# p = 4^k a + 1 for fixed small a (here a odd, p-1 = 4^k a with k>=1 maximal power of 2 >= 4 i.e. v2(p-1)>=2k)
v2 = np.array([int(math.log2((int(p)-1) & -(int(p)-1))) for p in P1])
stats(v2 >= 8, 'v2(p-1)>=8')
stats(v2 == 2, 'v2(p-1)=2 (p=5 mod 8)')
stats(np.isin(P1, [5, 17, 257, 65537]), 'Fermat primes 2^(2^k)+1')
stats(np.array([int(p) % 840 == 1 for p in P1]) & (v2 >= 4), 'p≡1(840) & v2>=4')
out['minC_over_log2_max'] = None
x = mC[P1] / L2
out['minC_over_log2_max'] = float(x.max()); out['minC_over_log2_argmax'] = int(P1[np.argmax(x)])
out['minC_over_log2_p99'] = float(np.percentile(x, 99))
out['minC_histogram_top'] = {int(k): int(v) for k, v in zip(*np.unique(mC[P1], return_counts=True)) if v > 50}
y = np.log(mW[P1].astype(float)) / np.log(P1.astype(float))
out['log_minUBC_over_logp_max'] = float(y.max()); out['log_minUBC_over_logp_argmax'] = int(P1[np.argmax(y)])
out['minUBC_over_log2_max'] = float((mW[P1] / L2).max())
# --- Z0628/Z0629: Poisson-type statistics of R/(log p)^2 in windows
for lo, hi in [(10**5, 10**6), (10**6, 10**7)]:
    m = (P1 >= lo) & (P1 < hi) & (P1 % 24 == 1)
    r = R[P1[m]].astype(float)
    out[f'window_{lo}_{hi}_p1mod24'] = dict(n=int(m.sum()), mean=float(r.mean()), var=float(r.var()),
                                           var_over_mean=float(r.var()/r.mean()), mean_over_log2=float((r/np.log(P1[m].astype(float))**2).mean()),
                                           frac_R0=float((r == 0).mean()))
# --- Z0648: Legendre splits within p ≡ 1 mod 24 (log-normalised R)
m = (P1 % 24 == 1) & (P1 > 10**4)
pp = P1[m]; xx = R[pp] / np.log(pp.astype(float))**2
split = {}
for q in [11, 13, 17, 19]:
    leg = np.array([pow(int(p) % q, (q-1)//2, q) for p in pp]); leg = np.where(leg == q-1, -1, leg)
    split[q] = {'(p/q)=+1': float(xx[leg == 1].mean()), '(p/q)=-1': float(xx[leg == -1].mean()),
                'n+': int((leg == 1).sum()), 'n-': int((leg == -1).sum()),
                'frac_R0_+': float((R[pp][leg == 1] == 0).mean()), 'frac_R0_-': float((R[pp][leg == -1] == 0).mean())}
out['legendre_split_p1mod24_p>1e4'] = split
out['p1mod24_count'] = int(m.sum())
json.dump(out, open('data/z52b/pass2/TO2/an1.json', 'w'), indent=1, default=float)
print(json.dumps(out, indent=1, default=float)[:6000])
