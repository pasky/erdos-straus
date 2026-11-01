"""Pass-2 TO3: greedy shift s(p)=min(4x-p) (A400619-type), Vmin(p) (U-word certificate, minwords), Cmin(p) (star-words)
Inputs: data/z52b/raw/mink_pr_2e5.txt (col 4 = min 4x-p), /tmp/z52/minwords3e6.txt (from scripts/z52b_fingerprint_minwords.c 3000000)
Outputs data/z52b/pass2/TO3/shifts_results.json"""
import numpy as np, json, sys
from scipy.stats import spearmanr
M = np.loadtxt('data/z52b/raw/mink_pr_2e5.txt', dtype=np.int64)
MW = np.loadtxt(sys.argv[1] if len(sys.argv) > 1 else '/tmp/z52/minwords3e6.txt', dtype=np.int64)
out = {}
p = M[:, 0]; s = M[:, 4]
pr = p[p > 2]; sr = s[p > 2]
# records of 4x-p (strict) over primes in order
rec = []; best = None
for pp, ss in zip(pr, sr):
    if best is None or ss > best:
        best = ss; rec.append((int(pp), int(ss)))
out['records_4x_minus_p'] = rec
out['A400619_first7_check'] = rec[:7]
vm = MW[p[p > 2] - 1, 2]   # Vmin at prime p (col 2 = vm)
m1 = (pr % 4 == 1)
out['Z0943'] = dict(n_p1mod4=int(m1.sum()), spearman_shift_vmin_p1mod4=float(spearmanr(sr[m1], vm[m1])[0]),
                    shift_ge_vmin_frac=float(np.mean(sr[m1] >= vm[m1])),
                    vmin_minus_shift_range=[int((vm[m1] - sr[m1]).min()), int((vm[m1] - sr[m1]).max())],
                    most_common_pairs=[[int(a), int(b), int(c)] for (a, b), c in
                                       sorted({(a, b): c for a, b, c in zip(*np.unique(np.column_stack([sr[m1], vm[m1]]), axis=0).T, [0]*0)}.items())[:0]])
pairs, counts = np.unique(np.column_stack([sr[m1], vm[m1]]), axis=0, return_counts=True)
order = np.argsort(-counts)[:6]
out['Z0943']['most_common_pairs'] = [[int(pairs[i][0]), int(pairs[i][1]), int(counts[i])] for i in order]
out['Z0943']['vmin_max_p1mod4_le2e5'] = int(vm[m1].max())
out['Z0943']['shift_max_p1mod4_le2e5'] = int(sr[m1].max())
out['Z0942'] = dict(max_shift_le2e5=int(sr.max()), prime_with_max_shift=int(pr[np.argmax(sr)]),
                    n_primes_shift_ge112=int((sr >= 112).sum()), note='A400619 bound (no prime in (1.2e11,4e11) with shift>=112) is an OEIS claim, not checked here')
# Vmin vs shift for U-hard primes
out['Z0943']['spearman_vmin_with_loglog'] = None
# ---- Z0775: Cmin distribution at primes (R(p)>0 ; Cmin = min t/4) ----
Pm = MW[:, 0]; cm = MW[:, 1]
isp = np.ones(len(Pm) + 1, bool); isp[:2] = False
for i in range(2, int(len(Pm) ** .5) + 1):
    if isp[i]: isp[i * i::i] = False
pr_mask = isp[Pm]
pr_mask_1 = pr_mask & (Pm % 4 == 1)
c = cm[pr_mask_1]
out['Z0775'] = dict(n_primes_1mod4=int(pr_mask_1.sum()), n_cm0=int((c == 0).sum()),
                    cmin_hist_head={int(k): int(v) for k, v in zip(*np.unique(c[c > 0], return_counts=True)) if k <= 20},
                    max_cmin_by_X={int(X): int(cm[pr_mask_1 & (Pm <= X)].max()) for X in [10**3, 10**4, 10**5, 10**6, 3 * 10**6]},
                    argmax_cmin_le3e6=int(Pm[pr_mask_1][np.argmax(c)]), max_cmin=int(c.max()))
# Z0775 for all n
out['Z0775']['n_all_cm0_le3e6'] = int((cm == 0).sum())
# ---- Z0781: R-zeros by dyadic window (Poisson comparison) ----
json.dump(out, open('data/z52b/pass2/TO3/shifts_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:500])
