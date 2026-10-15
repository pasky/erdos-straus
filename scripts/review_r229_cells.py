# R229 from-scratch cell check of FOUR_ADIC_INPUT Prop 1.4 (2^k bit law), cells mod 2^K.
import sys
from fractions import Fraction as F
from collections import defaultdict

K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
N = 2 ** K

def v2m(x):  # 2-adic valuation of a residue mod N, capped at K
    x %= N
    if x == 0: return K
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def fk(k):
    s = F(1, 2 ** (k - 1))
    return F(4, 3) * (2 * s - s * s)

tot = 0; neg = 0; one = 0; two = 0
hit = defaultdict(int); hit1 = defaultdict(int); hit2 = defaultdict(int)
bycls = defaultdict(lambda: defaultdict(int))  # n mod 16 -> counts
for t in range(N):
    for u in range(N):
        A = (t * u - 1) % N
        for v in range(N):
            n = (A * v - u) % N
            if n % 2 == 0: continue
            tot += 1
            P = [t, u, v, A, (t * v - 1) % N]
            vals = [v2m(x) for x in P]
            m = sum(1 for x in vals if x >= 2)
            if m == 0: continue
            neg += 1
            if m == 1: one += 1
            elif m == 2: two += 1
            else: raise SystemExit("more than two entries div by 4")
            mx = max(vals)
            c = n % 16
            bycls[c]['neg'] += 1
            for k in range(2, K + 1):
                if mx >= k:
                    hit[k] += 1; bycls[c][k] += 1
                    if m == 1: hit1[k] += 1
                    else: hit2[k] += 1
print(f"K={K}: odd-n cells {tot} (= {F(tot, N**3)} of all), chi=-1 cells {neg} ({F(neg, tot)}), one-iso {F(one, neg)}, two-iso {F(two, neg)}")
for k in range(2, K + 1):
    print(f" k={k}: share {F(hit[k], neg)} formula {fk(k)} ok={F(hit[k], neg) == fk(k)}; one-iso {F(hit1[k], one)} two-iso {F(hit2[k], two)}")
bad = [(c, k) for c in bycls for k in range(2, K + 1) if F(bycls[c][k], bycls[c]['neg']) != fk(k)]
print("n mod 16 classes:", sorted(bycls), "classes deviating from f_k:", bad[:20], len(bad))
for c in sorted(bycls):
    print(c, bycls[c]['neg'], [str(F(bycls[c][k], bycls[c]['neg'])) for k in range(2, K + 1)])
