"""z52b pass1 U05 Z1596: for C-form failures with omega(N)≥6 (list from z52b_p1_U05_omega6.c, p≤1e5, C≤200):
D = {d mod 4C : d | N} (all divisors); periodic iff the stabiliser {h ∈ (Z/4C)^×: hD = D} is nontrivial.
Report counts: periodic (stab≠1), and periodic with -1 ∉ stab (the Kneser-type case of the item)."""
import math
from collections import Counter
rows = [l.split() for l in open("data/z52b/pass1/U05/2nd/omega6_fail_p1e5_C200.txt")]
cnt = Counter(); examples = []
for r in rows:
    p, C, N, k = int(r[0]), int(r[1]), int(r[2]), int(r[3])
    m = 4*C
    fac = [(int(a.split('^')[0]), int(a.split('^')[1])) for a in r[4:]]
    D = {1 % m}
    for q, e in fac:
        D = {(d*pow(q, j, m)) % m for d in D for j in range(e+1)}
    assert (m-1) % m not in D
    units = [h for h in range(1, m) if math.gcd(h, m) == 1]
    stab = [h for h in units if {(h*d) % m for d in D} == D]
    nontriv = len(stab) > 1
    cnt['omega≥6 failures'] += 1
    cnt[f'stab size {len(stab)}'] += 1 if len(stab) <= 4 else 0
    cnt['periodic (stab≠1)'] += nontriv
    cnt['periodic & -1∉stab'] += nontriv and (m-1) not in stab
    if nontriv and len(examples) < 3: examples.append((p, C, len(stab), len(D), m))
print(dict(cnt)); print("examples (p,C,|stab|,|D|,4C):", examples)
