"""Pass-2 TO3 (Z0918): number of supersingular j-invariants lying in F_p (p >= 5), by brute force (a_p(E_j)=0 test),
compared with class numbers h(-4p), h(-3p), h(-p). Writes data/z52b/pass2/TO3/supersingular_results.json"""
import numpy as np, json, csv, math
from sympy import primerange
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
def ss_count(p):
    x = np.arange(p, dtype=np.int64)
    qr = np.zeros(p, dtype=np.int64)            # Legendre symbol table
    sq = (x * x) % p
    qr[:] = -1; qr[0] = 0; qr[np.unique(sq[1:])] = 1
    ss = []
    for j in range(p):
        if j == 0:
            A, B = 0, 1
        elif j == 1728 % p:
            A, B = 1, 0
        else:
            k = (1728 - j) % p
            A = (3 * j * k) % p; B = (2 * j * k * k) % p
        f = (x * x % p * x + A * x + B) % p
        s = int(qr[f].sum())                     # sum of chi(f(x)) (chi(0)=0 handled: qr[0]=0)
        if s == 0 and (A * A * A * 4 + 27 * B * B) % p != 0:
            ss.append(j)
    return ss
out = {'rows': []}
rows = []
for p in primerange(5, 1200):
    if p % 4 == 3 and False: pass
    S = ss_count(p)
    h4 = int(pari.qfbclassno(-4 * p)) if p % 4 == 1 else None
    h3 = int(pari.quadclassunit(-3 * p)[0]) if (p % 4 == 1) else None
    hm = int(pari.quadclassunit(-p)[0]) if p % 4 == 3 else None
    rows.append((p, len(S), h4, hm, h3))
out['first_rows'] = rows[:20]
# fit: candidates for p=1 mod 4 and p=3 mod 4
c1 = [(p, n, h4, h3) for p, n, h4, hm, h3 in rows if p % 4 == 1]
c3 = [(p, n, hm, h3) for p, n, h4, hm, h3 in rows if p % 4 == 3]
out['p1mod4_match_h4p_over2_plus_stuff'] = {}
# tabulate n - h4/2 and n - (h4+h3)/2 patterns
def tab(sel):
    from collections import Counter
    return Counter(sel)
out['p1mod4_diff_nss_minus_h4p_half'] = dict(tab([round(n - h4 / 2, 1) for p, n, h4, h3 in c1]))
out['p3mod4_diff_nss_minus_hmp_half'] = dict(tab([round(n - hm / 2, 1) for p, n, hm, h3 in c3]))
out['p1mod4_diff_nss_minus_h4p_half_minus_h3p_half'] = dict(tab([round(n - (h4 + (h3 or 0)) / 2, 1) for p, n, h4, h3 in c1]))
json.dump(out, open('data/z52b/pass2/TO3/supersingular_results.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:3000])
