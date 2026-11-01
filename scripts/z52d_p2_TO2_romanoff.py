# Z0602: Romanoff-type density: fraction of odd n <= N of the form p + 2^k (k>=0, p prime), and mean number of representations
import numpy as np, json
N = 10**7
s = np.ones(N+1, bool); s[:2] = False
for i in range(2, int(N**0.5)+1):
    if s[i]: s[i*i::i] = False
P = np.nonzero(s)[0]
cnt = np.zeros(N+1, np.int32)
k = 0
while 2**k < N:
    m = P + 2**k
    m = m[m <= N]
    np.add.at(cnt, m, 1)
    k += 1
odd = np.arange(3, N+1, 2)
r = cnt[odd]
out = dict(N=N, odd_n=int(len(odd)), frac_rep_by_p_plus_2k=float((r > 0).mean()),
           mean_reps=float(r.mean()))
for lo, hi in [(10**3, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 10**7)]:
    m = (odd >= lo) & (odd < hi)
    out[f'frac_{lo}_{hi}'] = float((r[m] > 0).mean())
    out[f'mean_reps_{lo}_{hi}'] = float(r[m].mean())
out['fraction_zero_reps_by_residue_mod3'] = {int(c): float((r[odd % 3 == c] == 0).mean()) for c in [1, 2]}
json.dump(out, open('data/z52b/pass2/TO2/romanoff.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
