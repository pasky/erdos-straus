# Z0660: fraction of n <= N having a divisor d ≡ -1 (mod m) (d>0), for small m; Erdos–Hall-type statistic
import numpy as np, json
N = 10**5
divs = [[] for _ in range(N+1)]
for d in range(1, N+1):
    for m in range(d, N+1, d): divs[m].append(d)
out = {'N': N}
for m in range(2, 13):
    c = 0
    for n in range(2, N+1):
        if any(d % m == m-1 for d in divs[n]): c += 1
    out[f'frac_n_with_divisor_1mod_m_minus1_m={m}'] = c/(N-1)
json.dump(out, open('data/z52b/pass2/TO2/divm1.json', 'w'), indent=1)
print(out)
