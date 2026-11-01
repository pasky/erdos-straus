# TO2 part 4: U(p)-table analyses (items Z0683-Z0686, Z0689-Z0691, Z0696) from repo count-program outputs
# columns: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm
import numpy as np, json, math
D = 'data/z52b/raw/'
a = np.loadtxt(D + 'f4_all_30000.txt', dtype=np.int64)            # all n <= 30000
b = np.loadtxt(D + 'pr_20001_200000.txt', dtype=np.int64)          # primes 20001..200000
w6 = np.loadtxt(D + 'pr_1e6_window.txt', dtype=np.int64)
w7 = np.loadtxt(D + 'pr_1e7_window.txt', dtype=np.int64)
A = np.vstack([a, b])
def isprime_arr(n):
    s = np.ones(n.max()+1, bool); s[:2] = False
    for i in range(2, int(n.max()**0.5)+1):
        if s[i]: s[i*i::i] = False
    return s[n]
Pm = A[isprime_arr(A[:, 0])]               # primes <= 2e5 (f4 covers all n<=30000)
Pm = Pm[(Pm[:, 0] > 2)]
out = {'n_primes_le_2e5': int(len(Pm)), 'n_windows_1e6': int(len(w6)), 'n_windows_1e7': int(len(w7))}
p = Pm[:, 0]; U = Pm[:, 1]; L2 = np.log(p.astype(float))**2
# Z0683: primes with U <= 4
small = Pm[U <= 4]
out['primes_le_2e5_with_U_le_4'] = [int(x) for x in small[:, 0]]
out['min_U_p_1e6_window'] = int(w6[:, 1].min()); out['min_U_p_1e7_window'] = int(w7[:, 1].min())
out['primes_le_2e5_with_U_eq_5_or_6_first'] = [int(x) for x in Pm[(U == 5) | (U == 6)][:, 0][:8]]
# Z0684: least prime with U=6
m6 = Pm[U == 6]; out['least_prime_U6'] = int(m6[0, 0]) if len(m6) else None
out['least_prime_U_eq_k'] = {int(k): int(Pm[U == k][0, 0]) for k in range(1, 12) if (U == k).any()}
# Z0685: records of U(p)/log^2 p (running minima over p) up to 2e5
ratio = U / L2
order = np.argsort(p); rec = []; best = np.inf
for i in order:
    if ratio[i] < best: best = ratio[i]; rec.append((int(p[i]), int(U[i]), round(float(ratio[i]), 4)))
out['records_low_U_over_log2_le_2e5'] = rec[:25]
out['U_over_log2_min_le_2e5'] = float(ratio.min()), int(p[np.argmin(ratio)])
# window extrema (1e6, 1e7 windows, primes only from pr files)
out['window_min_U_over_log2_1e6'] = float((w6[:, 1]/np.log(w6[:, 0].astype(float))**2).min())
out['window_min_U_over_log2_1e7'] = float((w7[:, 1]/np.log(w7[:, 0].astype(float))**2).min())
# Z0691: complementarity of k1 (exactly one denominator divisible by p) and k2 (exactly two)
k1 = Pm[:, 10]; k2 = Pm[:, 11]; k3 = Pm[:, 12]
out['primes_le_2e5_with_k1_zero'] = int((k1 == 0).sum()); out['primes_le_2e5_with_k2_zero'] = int((k2 == 0).sum())
out['primes_le_2e5_with_both_zero'] = int(((k1 == 0) & (k2 == 0)).sum())
out['primes_1mod4_le_2e5_k1_zero_and_k2_zero'] = [int(x) for x in p[(k1 == 0) & (k2 == 0) & (p % 4 == 1)][:10]]
out['primes_1mod4_le_2e5_k2_zero_count'] = int(((k2 == 0) & (p % 4 == 1)).sum())
out['primes_1mod4_le_2e5_k1_zero_count'] = int(((k1 == 0) & (p % 4 == 1)).sum())
out['primes_le_2e5_k3_nonzero'] = int((k3 > 0).sum())
q1 = k1[p % 4 == 1].astype(float); q2 = k2[p % 4 == 1].astype(float)
out['pearson_k1_k2_p1mod4'] = float(np.corrcoef(q1, q2)[0, 1])
out['spearman_k1_k2_p1mod4'] = float(np.corrcoef(np.argsort(np.argsort(q1)), np.argsort(np.argsort(q2)))[0, 1])
# Z0696: U(p) vs least QNR and #QNR<=log p
def least_qnr(pp):
    for g in range(2, pp):
        if pow(g, (pp-1)//2, pp) == pp-1: return g
ll = np.array([least_qnr(int(x)) for x in p[p % 4 == 1]])
Up = U[p % 4 == 1]; Lp = np.log(p[p % 4 == 1].astype(float))
qn = np.array([sum(1 for q in range(2, int(lp)+1) if pow(q, (int(pp)-1)//2, int(pp)) == int(pp)-1) for pp, lp in zip(p[p % 4 == 1], Lp)])
out['spearman_U_leastQNR_p1mod4'] = float(np.corrcoef(np.argsort(np.argsort(Up)), np.argsort(np.argsort(ll)))[0, 1])
out['spearman_U_numQNR_le_logp_p1mod4'] = float(np.corrcoef(np.argsort(np.argsort(Up)), np.argsort(np.argsort(qn)))[0, 1])
out['spearman_k1_numQNR_le_logp_p1mod4'] = float(np.corrcoef(np.argsort(np.argsort(k1[p % 4 == 1])), np.argsort(np.argsort(qn)))[0, 1])
out['pearson_log_U_vs_numQNR_p1mod4'] = float(np.corrcoef(np.log(Up.astype(float)), qn)[0, 1])
json.dump(out, open('data/z52b/pass2/TO2/an4.json', 'w'), indent=1)
print(json.dumps(out, indent=0)[:5000])
